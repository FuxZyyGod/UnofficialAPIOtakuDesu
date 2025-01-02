from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests, os
load_dotenv()



def SubtitleAnimeDat(sub_title):
 req = requests.get(f"{os.getenv('URL_SUBTITLE')}/{sub_title}")
 scrp = BeautifulSoup(req.content, "html.parser")
 datas = scrp.find(class_="infozingle")
 print(datas.contents[0])
 title = datas.contents[0]
 print(title.text.split(": ")[1])
 items = {
  "title": datas.contents[0].text.split(": ")[1],
  "japanese-title":datas.contents[1].text.split(": ")[1],
  "rating":datas.contents[2].text.split(": ")[1],
  "produsers":datas.contents[3].text.split(": ")[1],
  "type":datas.contents[4].text.split(": ")[1],
  "status":datas.contents[5].text.split(": ")[1],
  "current-episodes":datas.contents[6].text.split(": ")[1],
  "duration":datas.contents[7].text.split(": ")[1],
  "release-date":datas.contents[8].text.split(": ")[1],
  "studios":datas.contents[9].text.split(": ")[1],
  "genre":datas.contents[10].text.split(": ")[1]
 }
 return items