import requests
from bs4 import BeautifulSoup

url = "https://www.seedandspark.com/fund/soiled-doves#updates"
reqStory = requests.get(url)
data = BeautifulSoup(reqStory.content, "html.parser")
is_complete = bool(data.find_all("h2", {"class" : "greenlight"}))

def get_name():
    name = data.find_all("h2", {"class": "project-title"})[0].text
    print(name)

def get_genre():
    genre = data.find_all("h5", {"class" : "genre"})[0].text
    genre = genre.split();
    len_first = len(genre[0])
    genre[0] = genre[0][0:len_first-1]          # get rid of comma after first element
    print(genre)

def get_length():
    length = data.find_all("h5", {"class" : "length"})[0].text
    print(length)

def get_location():
    location = data.find_all("h5", {"class" : "location"})[0].text
    print(location)

def get_story():
    story = data.find_all("div", {"class": "story-body"})[0].text
    print(story)

def get_amounts(is_complete):
    money = data.find_all("h3", {"class" : "financial"})[0].text
    money = money.split();

    if is_complete:
        amount_target = "N/A";          # green light campaigns don't have target amount
        amount_raised = money[1];
    else:
        amount_target = money[2];
        amount_raised = money[0];

    print(amount_raised)
    print(amount_target)

def get_num_supporters():
    num_supporters = data.find_all("h3", {"class" : "supporters"})[0].text
    # num_supporters = num_supporters.split()[0];
    print(num_supporters)

def get_num_followers():
    num_followers = data.find_all("h3", {"class" : "supporters"})[1].text
    # num_followers = num_followers.split()[0];
    print(num_followers)

def get_rewards(is_complete):
    reward_amounts = []
    reward_categories = []

    incentive_items = data.find_all("div", {"class" : "incentive-item"})
    size = int(len(incentive_items) / 2)            # getting rid of duplicate entries
    incentive_items = incentive_items[0:size]

    general = data.find_all("h3")
    start = 7
    if is_complete:         # offset index for green light campaigns
        start = 9

    for item in incentive_items:
        amount = item.find_all("h2")[1].text
        reward_amounts.append(amount)

    for counter in range(start, (start + size)):        # grab headers within a certain range
        award = general[counter].getText();
        reward_categories.append(award)

    print(reward_amounts)
    print(reward_categories)

def convert_money(money):
    money = money[1:len(money)]
    parts = money.split(",")
    size = len(parts)

    money_string = "";                  # convert 123,456 to 123456
    for counter in range(0, size):
        money_string = money_string + parts[counter]

    money_int = int(money_string)
    return money_int

def get_wishlist():
    wishlist_items = []
    wishlist_progress = []
    wishlist = data.find_all("div", {"class" : "card-module wishlist-card"})

    for item in wishlist:
        name = item.find_all("p", {"class" : "item-title"})[0].text
        wishlist_items.append(name)

        progress = item.find_all("div", {"class", "card-panel progress"})[0].text
        progress = progress.split()
        remaining_cost = progress[0]

        if remaining_cost == "FULFILLED":
            wishlist_progress.append(100.0)
        else:
            total_cost = convert_money(progress[4])
            remaining_cost = convert_money(remaining_cost)
            difference = total_cost - remaining_cost
            percent = round(difference / total_cost * 100, 1)
            wishlist_progress.append(percent)

    print(wishlist_items)
    print(wishlist_progress)

get_name()
get_genre()
get_length()
get_location()
get_amounts(is_complete)
get_num_supporters()
get_num_followers()
get_rewards(is_complete)
get_wishlist()







