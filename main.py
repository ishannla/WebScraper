import time
start = time.time()
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.seedandspark.com/fund/letting-go"
reqStory = requests.get(url + "#story")
data = BeautifulSoup(reqStory.content, "html.parser")
is_complete = bool(data.find_all("h2", {"class" : "greenlight"}))

driver = webdriver.Chrome("/Users/ishannarula/phantomjs/bin/chromedriver")  # need to pass in path to exec
# driver = webdriver.PhantomJS("/Users/ishannarula/phantomjs/bin/phantomjs")
driver.get(url + "#updates")

end = time.time()
print(end - start)
print()

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

def get_num_updates():
    updates = driver.find_elements_by_class_name("update-item")
    print(len(updates))

def get_team():
    team_button = driver.find_element_by_xpath("""//*[@id="tab_team"]""")
    team_button.click()

    time.sleep(0.5)         # need to sleep each time you switch the page

    member_data = driver.find_elements_by_css_selector(".card-module.team-card")

    members = []
    roles = []

    for member in member_data:
        lines = member.text.splitlines()
        members.append(lines[0]);
        roles.append(lines[1:(len(lines))])

    print(members)
    print(roles)

def get_supporters_and_dates():
    community_button = driver.find_element_by_xpath("""//*[@id="tab_community"]""")
    community_button.click()
    time.sleep(0.5)

    page_nums = driver.find_element_by_class_name("pagination").text
    str_length = len(page_nums)
    tabs = ""       # algorithm only works for 1 and 2-digit numbers, so domain 1 < x < 99

    if str_length <= 9:
        tabs = str_length
    else:
        page_nums = page_nums[9:(str_length + 1)]
        str_length = len(page_nums)
        tabs = page_nums[str_length - 2:str_length]

    tabs = int(tabs);

    supporter_names = [];
    supporter_dates = [];
    supporter_times = [];

    for counter in range(1, tabs + 1):
        entries = driver.find_elements_by_class_name("supporter-item")

        for entry in entries:
            lines = entry.text.splitlines()
            supporter_names.append(lines[0])
            full_date = lines[2].split()
            date = full_date[1] + " " + full_date[2]
            clock = full_date[4] + " " + full_date[5]
            supporter_dates.append(date)
            supporter_times.append(clock)

        next_button = driver.find_element_by_class_name("pageNext")
        next_button.click();
        time.sleep(0.5)

    print(supporter_names)
    print(supporter_dates)
    print(supporter_times)

    size = len(supporter_dates)
    start_date = supporter_dates[size - 1] + " " + supporter_times[size - 1]
    end_date = supporter_dates[0] + " " + supporter_times[0]

    print(start_date)
    print(end_date)


start = time.time()

get_name()
get_genre()
get_length()
get_location()
get_amounts(is_complete)
get_num_supporters()
get_num_followers()
get_rewards(is_complete)
get_wishlist()

get_num_updates()
get_team()
get_supporters_and_dates()

end = time.time()
print()
print(end - start)



