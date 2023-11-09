import requests,os
from dotenv import load_dotenv
f = open("rec.txt","r")
mes = f.read()
class request:
    def get(message, apikey, bid, id):
        r = requests.get(
            url=f"http://api.brainshop.ai/get?bid={bid}&key={apikey}&uid={id}&msg={message}"
        )
        return r.json()["cnt"]
print(request.get(mes,'cU25Ss1SZg7yVZdd',169657,123145))