from atproto import Client
from openai import OpenAI
from openai.types.chat.chat_completion import ChatCompletion
from pynytimes import NYTAPI
import time
import json

# pip install openai
# pip install atproto
# pip install pynytimes

# get NYT api https://developer.nytimes.com/?it=a

with open("creds_danzeeeman.json", "r") as f:
    creds = json.load(f)
    client = Client()
    handle = 'danzeeeman.bsky.social'
    client.login(handle, creds['bluesky'])
    nyt = NYTAPI(creds["nyt"], parse_dates=True)
    oai_client = OpenAI(api_key = creds['openai'])
    
    def get_articles():
        print("===== get_articles")
        top_stories = nyt.top_stories()
        data = []
        for article in top_stories:
            data.append({
                "title":article['title'],
                "abstract":article['abstract']
            })
            print(f"title {article['title']}")
            
        return data
        

    def write_haiku_from_headline(headline):
        print("===== write_haiku_from_headline")
        llm_model = "gpt-4o-mini"
        temp = 0.8
        top_p = 0.9
        message=[
                {
                    "role":"system",
                    "content":f"you are a twitter bot writing haikus about the current state of the world using headlines from the New York Time\nheadline:{headline} ",
                },
                {
                    "role":"user",
                    "content":f"Write a short haiku"
                }
            ]
        completion = oai_client.chat.completions.create(
            model=llm_model,
            messages=message,
            temperature=temp,                
            top_p=top_p,
            max_tokens=128,
            stream=False
        )
        message = None
        if isinstance(completion, ChatCompletion):    
            for choice in completion.choices:                
                message = choice.message.content 
        return message
    
    def write_haiku_from_article(headline, abstract):
        print("===== write_haiku_from_article")
        llm_model = "gpt-4o-mini"
        temp = 0.8
        top_p = 0.9
        message=[
                {
                    "role":"system",
                    "content":f"you are a twitter bot writing haikus about the current state of the world from articles from the new york times\nheadline: {headline}n\article:{abstract}",
                },
                {
                    "role":"user",
                    "content":f"Write a haiku"
                }
            ]
        completion = oai_client.chat.completions.create(
            model=llm_model,
            messages=message,
            temperature=temp,                
            top_p=top_p,
            max_tokens=128,
            stream=False
        )
        message = None
        if isinstance(completion, ChatCompletion):    
            for choice2 in completion.choices:                
                message = choice2.message.content 
        return message
    
    
    def post_poem(poem):
        print("post_poem")
        post = client.create_post(poem)
        print("post made")
        print(post)
    
    
    def main():
        articles = get_articles()
        
        poems = []
        for article in articles:
            poems.append(write_haiku_from_headline(article['title']))
            print(poems[-1])
            time.sleep(15)
            
        for poem in poems:
            print(poem)
            post_poem(poem)
            time.sleep(300)
            
    main()

