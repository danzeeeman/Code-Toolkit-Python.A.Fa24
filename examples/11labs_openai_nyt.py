from openai import OpenAI
from openai.types.chat.chat_completion import ChatCompletion
from pynytimes import NYTAPI
import time
import json
from elevenlabs import play, save
from elevenlabs.client import ElevenLabs, VoiceSettings

# pip install openai
# pip install atproto
# pip install pynytimes

# get NYT api https://developer.nytimes.com/?it=a

with open("creds_danzeeeman.json", "r") as f:
    creds = json.load(f)

    client = ElevenLabs(
        api_key=creds['11'], # Defaults to ELEVEN_API_KEY
        )

    nyt = NYTAPI(creds["nyt"], parse_dates=True)
    oai_client = OpenAI(api_key = creds['openai'])
    
    def get_articles(articles):
        print("===== get_articles")
        top_stories = nyt.top_stories()
        for article in top_stories:
            articles[article['uri']] = {
                "title":article['title'].lower(),
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
    
    def main():
        articles = {}
        posted_articles = []
        while True:
            articles = get_articles(articles)
            
            for key in articles:
                if key not in posted_articles:
                    print("create poem")
                    poem_text = write_haiku_from_article(articles[key]['title'], articles[key]['abstract'])
                    if poem_text is not None:
                        poem = {
                            "title":articles[key]['title'],
                            "byline":articles[key]['byline'],
                            "link":articles[key]['link'],
                            "poem":poem_text
                            }
                        print("poem object:")
                        print(poem)
                        print("poem generate audio:")
                        audio = client.generate(
                            text=f"{poem['title']}\n\n{poem['byline']} \n\n {poem['poem']}",
                            voice="Oliver Haddington",
                            model="eleven_multilingual_v2",
                            voice_settings=VoiceSettings(
                                stability=0.51, similarity_boost=0.6, style=0.3, use_speaker_boost=True
                            ),
                        )
                        save(audio, f"{poem['title']}\n\n{poem['byline']}.wav")
                        print("poem generate audio save:")
                        posted_articles.append(key)
                        time.sleep(60)
                    time.sleep(15)
            time.sleep(120)    

            
    main()

