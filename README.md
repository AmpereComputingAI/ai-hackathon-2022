# Ampere AI use cases
This is PyTorch based RoBERTa pre-trained model trained on tweeteval dataset which contains ~12,000 tweets for the sentiment classification tasks with three classes being positive, negative, neutral sentiments. TweetEval Dataset consists of seven heterogenous tasks in twitter, all framed as multi-class tweet classification.One of the used for this demo is Sentiment Analysis. The model can be downloaded from hugging face: https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest?text=Covid+cases+are+increasing+fast%21

In this Interactive demo, the user can input text and submit to get the corresponding sentiment class probabilities. This web app is developed using Gradio Python library.

# Steps to run the demo on the cloud instace

### SSH to cloud instance
> $ ssh -i \<ssh.key> ubuntu@\<public-ip>

### Launch the container
> $ wget https://raw.githubusercontent.com/AmpereComputingAI/ai-hackathon-2022/master/nlp/sentiment-analysis/start-docker-cloud-hackathon.sh

> $ bash start-docker-cloud-hackathon.sh  
Starting sentiment-analysis-pt-aio-demo container  
Docker container ID:173e054cd5a9  

### Start the demo
> \# ./start-webapp.sh  
>
> Getting Webapp URL ...........................  
Webapp URL: http://\<public-ip>:7860/


### Open ports on the server
> Install *firewalld* package
\$ sudo apt purge ufw -y  
\$ sudo apt install firewalld -y  
\$ sudo firewall-cmd --permanent --zone=public --add-port=\<7860-7864>/tcp  
\$ sudo firewall-cmd --reload  
\$ sudo firewall-cmd --zone=public --list-ports

### View on the Browser
> Copy the URL and paste on the browser
