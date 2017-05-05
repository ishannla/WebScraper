import requests
from bs4 import BeautifulSoup

url = "https://www.seedandspark.com/fund/pay-to-stay"

# data on story page

reqStory = requests.get(url + "#story")
story = BeautifulSoup(reqStory.content, "html.parser")

is_complete = bool(story.find_all("h2", {"class" : "greenlight"}))

name = story.find_all("h2", {"class" : "project-title"})[0].text
print(name)

money = story.find_all("h3", {"class" : "financial"})[0].text
money = money.split();

if is_complete:
    amount_target = "NA";
    amount_raised = money[1];
else:
    amount_target = money[2];
    amount_raised = money[0];

print(amount_raised)
print(amount_target)
print()

num_supporters = story.find_all("h3", {"class" : "supporters"})[0].text
num_supporters = num_supporters.split()[0];
print(num_supporters)

num_followers = story.find_all("h3", {"class" : "supporters"})[1].text
num_followers = num_followers.split()[0];
print(num_followers)
print('');

donation_amounts = []
incentive_items = story.find_all("div", {"class" : "incentive-item"})
size = int(len(incentive_items) / 2)
incentive_items = incentive_items[0:size]
for item in incentive_items:
    donation = item.find_all("h2")[1].text
    donation_amounts.append(donation)

donation_awards = []
general = story.find_all("h3")
start = 7
if is_complete:
    start = 9
for counter in range(start, (start + size)):
    award = general[counter].getText();
    donation_awards.append(award)

for counter in range(0, len(donation_amounts)):
    print(donation_amounts[counter] + " - " + donation_awards[counter])

print()
print(donation_amounts)
print(donation_awards)
print()

urlupdate = "https://www.seedandspark.com/fund/tolifemovie#updates"
update = requests.get(urlupdate)
u = BeautifulSoup(update.content, "html.parser")
data = u.find_all("div", {"class" : "social-links"})
print(data)