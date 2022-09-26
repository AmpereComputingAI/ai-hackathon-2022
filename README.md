# Ampere AI use cases
This is PyTorch based RoBERTa pre-trained model trained on tweeteval dataset which contains ~12,000 tweets for the sentiment classification tasks with three classes being positive, negative, neutral sentiments. TweetEval Dataset consists of seven heterogenous tasks in twitter, all framed as multi-class tweet classification.One of the used for this demo is Sentiment Analysis. The model can be downloaded from hugging face: https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest?text=Covid+cases+are+increasing+fast%21

In this Interactive demo, the user can input text and submit to get the corresponding sentiment class probabilities. This web app is developed using Gradio Python library.

<h1> Running the Demo </h1>

- Pull the docker image: $docker pull ghcr.io/amperecomputingai/sentiment-analysis-pt-aio-demo:hackathon-1.0.
- Once you have the docker image(sentiment-analysis-pt-aio-demo:hackathon-1.0), start the docker by running:
    $ ./start-docker-cloud-hackathon.sh
- Then you will be in container and need to start the webapp by doing:
    $ ./start-webapp.sh
  This will get the webapp URL like this: Webapp URL: http://<ipaddr>:7860 then open any browser, copy and paste this URL to view the webapp.
  
