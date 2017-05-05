import requests
from bs4 import BeautifulSoup

url = "https://www.seedandspark.com/fund/soiled-doves"


reqStory = requests.get(url + "#team")
story = BeautifulSoup(reqStory.content, "html.parser")

print(story)
