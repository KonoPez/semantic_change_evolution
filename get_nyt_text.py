import json, requests
from nltk import tokenize
import time

url = "https://api.nytimes.com/svc/archive/v1"
key = "nR3tUPKNqlHSRnloD4GsUDADDLQiqSpb"
suffix = ".json?api-key=" + key


for year in range(2010,2021):
    sents = []
    for month in range(1,13):
        query = f"/{year}/{month}"
        text = requests.get(url+query+suffix).text
        results = json.loads(text)["response"]["docs"]
        for res in results:
            para = res["lead_paragraph"]
            sents += tokenize.sent_tokenize(para)
        time.sleep(3)
    data = open(f"./nyt_text/{year}data.txt", "w")
    for line in sents:
        data.write(line+"\n")
    data.close()
