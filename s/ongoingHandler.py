from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests, os
load_dotenv()


def OngoingAnimeDat(page: int):
 if page == 1:
  req = requests.get(os.getenv("URL_ONGOING"))
  scrp = BeautifulSoup(req.content, "html.parser")
  items = []
  titles = scrp.find_all(class_="jdlflm")
  sub_titles = scrp.find_all(class_="thumb")
  rates = scrp.find_all(class_="epztipe")
  episodes = scrp.find_all(class_="epz")
  new_episodes = scrp.find_all(class_="newnime")
  thumbs = scrp.find_all(class_="thumbz")
  for title, thumb, sub_title, eps, rate, new_eps in zip(titles, thumbs, sub_titles, episodes, rates, new_episodes):
   items.append({
    "title": title.text,
    "sub-title": sub_title.find("a").get("href").split("/")[4],
    "episode": eps.text.split(" ")[0],
    "rating": rate.text.split(" ")[1],
    "new_episode_released": new_eps.text,
    "thumb": thumb.find("img").get("src")
   })
  
  return items
  
 else:
  req = requests.get(f"{os.getenv('URL_ONGOING')}/page/{page}/")
  scrp = BeautifulSoup(req.content, "html.parser")
  items = []
  titles = scrp.find_all(class_="jdlflm")
  sub_titles = scrp.find_all(class_="thumb")
  episodes = scrp.find_all(class_="epz")
  thumbs = scrp.find_all(class_="thumbz")
  for title, thumb, sub_title, eps in zip(titles, thumbs, sub_titles, episodes):
   items.append({
    "title": title.text,
    "sub-title": sub_title.find("a").get("href").split("/")[4],
    "episode": eps.text.split(" ")[0],
    "thumb": thumb.find("img").get("src")
   })
  
  return items
  
  
 