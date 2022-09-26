import gradio as gr
import numpy as np
import os, psutil
import torch
from emoji import emojize
from scipy.special import softmax
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig

nthreads = str(psutil.cpu_count())
os.environ['AIO_NUM_THREADS'] = nthreads
os.environ['OMP_NUM_THREADS'] = nthreads

# Preprocess text (username and link placeholders)
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
config = AutoConfig.from_pretrained(MODEL)

# Generate torchscript model
model = AutoModelForSequenceClassification.from_pretrained(MODEL)
model=torch.jit.trace(model,(torch.zeros(1,40,dtype=torch.int),torch.zeros(1,40,dtype=torch.int)),strict=False)
model=torch.jit.freeze(model)


myDict={}

def classify(text):
    text=preprocess(text)
    encoded_input = tokenizer(text, return_tensors='pt',padding='max_length', max_length=40,truncation=True)
    output = model(**encoded_input)
    scores=output["logits"].detach().numpy()
    scores=scores.ravel()
    scores=softmax(scores)
    ranking=np.argsort(scores)
    ranking=ranking[::-1]
    for i in range(scores.shape[0]):
        l=config.id2label[ranking[i]]
        if l=="Positive":
            l=config.id2label[ranking[i]]+"  "+emojize(":beaming_face_with_smiling_eyes:")

        elif l=="Negative":
            l=config.id2label[ranking[i]]+"  "+emojize(":sad_but_relieved_face:")
        else:
            l=config.id2label[ranking[i]]+"  "+emojize(":neutral_face:")
        s=scores[ranking[i]]
        myDict[l]=np.round(float(s), 4)
    myDict_2=sorted(myDict.items(), key=lambda x:-x[1])
    result={k:v for k,v in myDict_2}
    return result

# Warmup
for i in range(2):
    classify('hello')

with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown('<img src="https://i.ibb.co/48fKLh9/Microsoft-Teams-image-3.png" style="margin:auto">')
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown('<div style="transform: translateY(50%);"><h1 style="font-family:kievit;font-size:30px;">Text Sentiment Analysis with NLP(RoBERTa)</h1></div>')
        with gr.Column(scale=1):
            gr.Markdown('<img src="https://i.ibb.co/QfSL73K/amperelogo1.jpg" alt="images" border="0" style="float:right">')
    with gr.Row():
        with gr.Column(scale=1):
            text = gr.Textbox()
        with gr.Column(scale=1):
            label = gr.Label(num_top_classes=3)
    text.change(fn=lambda value: classify(value), inputs=text, outputs=label)

demo.launch(share=False, debug=True)
