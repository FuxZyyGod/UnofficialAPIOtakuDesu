from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests, os
load_dotenv()



def SearchAnimeDat(keyword):
 req = requests.get(f"{os.getenv('URL_SEARCH')}?s={keyword}&post_type=anime")
 scrp = BeautifulSoup(req.content, "html.parser")
 items = []
 animes = scrp.find(class_="chivsrc")
 
 for i in range(14):
  genres = [genre.text for genre in animes.contents[i].find_next("div", class_="set").find_all("a")]
  status = animes.contents[i].find('div', class_='set').find_next('div').text.split(": ")[1]
  rating = animes.contents[i].find('div', class_='set').find_next('div').find_next('div').text.split(": ")[1]
  items.append({
   "thumb":animes.contents[i].find_next("img").get("src"),
   "title": animes.contents[i].find_next("h2").text,
   "genres": [genre.text for genre in animes.contents[i].find_next("div", class_="set").find_all("a")],
   "status":animes.contents[i].find('div', class_='set').find_next('div').text.split(": ")[1],
   "rating": animes.contents[i].find('div', class_='set').find_next('div').find_next('div').text.split(": ")[1]
  })
 
 return items

 