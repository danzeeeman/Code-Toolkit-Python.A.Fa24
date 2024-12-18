from atproto import Client, client_utils
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
    
    def get_articles(articles):
        print("===== get_articles")
        top_stories = nyt.top_stories()
        for article in top_stories:
            articles[article['uri']] = {
                "title":article['title'],
                "link":article['url'],
                "byline":article['byline'],
                "abstract":article['abstract']
            }
            print(f"title {article['title']}")
            
        return articles
        

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
        temp = 1.0
        top_p = 0.7
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
        print(completion)
        if isinstance(completion, ChatCompletion):    
            for choice2 in completion.choices:                
                message = choice2.message.content 
        return message
    
    
    def post_poem(poem):
        print("post_poem")
        text_builder = client_utils.TextBuilder()
        text_builder.text(f"From the New York Time:\n")
        text_builder.link(f"{poem['title']} ", poem['link'])
        text_builder.text(f"{poem['byline']}\n\n")
        text_builder.text(f"{poem['poem']}")
        post = client.send_post(text_builder)
        print("post made")
        print(post)
    
    
    def main():
        articles = {}
        posted_articles = []
        while True:
            articles = get_articles(articles)
            
            poems = []
            for key in articles:
                if key not in posted_articles:
                    print("create poem")
                    poem_text = write_haiku_from_headline(articles[key]['title'])
                    if poem_text is not None:
                        poems.append({
                            "title":articles[key]['title'],
                            "byline":articles[key]['byline'],
                            "link":articles[key]['link'],
                            "poem":poem_text
                            })
                        print("poem object:")
                        print(poems[-1])
                        posted_articles.append(key)
                    time.sleep(5)
                
            for poem in poems:
                print(poem)
                post_poem(poem)
                time.sleep(300)
            
            time.sleep(300)
            
    main()

