import requests
from bs4 import BeautifulSoup

list_numbers_wins, list_numbers_losses = [n for n in range(0, 361, 12)], [n for n in range(1, 361, 12)]
list_numbers_last, list_numbers_streak = [n for n in range(7, 361, 12)], [n for n in range(10, 361, 12)]
team_info = []
w, l, last_games_p, streak_p = "W", "L", "Last 10", "Streak"


def get_data(url):
    r = requests.get(url)
    return r.text


soup = BeautifulSoup(get_data("https://sports.yahoo.com/nba/standings/"), 'html.parser')


def get_team_information():
    got_w, got_l, got_last_ten, got_streak = False, False, False, False
    for index, numbers in enumerate(soup.find_all(class_="Bdb(primary-border) Ta(end) Px(cell-padding-x)")):
        if index in list_numbers_wins:
            wins_d = numbers.get_text()
            got_w = True
        elif index in list_numbers_losses:
            loses_d = numbers.get_text()
            got_l = True
        elif index in list_numbers_last:
            last_ten = numbers.get_text()
            got_last_ten = True
        elif index in list_numbers_streak:
            streak_d = numbers.get_text()
            got_streak = True
        if all([got_w, got_l, got_last_ten, got_streak]):
            team_info.append({w: wins_d, l: loses_d, last_games_p: last_ten, streak_p: streak_d})
            got_w, got_l, got_last_ten, got_streak = False, False, False, False


def show_result():
    position, west_p = 1, False
    print("\nEastern Conference\n")
    for team_name, show in zip(soup.find_all(class_="Ta(start) Fw(400) Fz(12px) H(40px) W(25%)"), team_info):
        print(
            f"{position}. {team_name.get_text()} : W {show[w]}, L {show[l]}, Last 10 {show[last_games_p]}, Streak {show[streak_p]}")
        if position < 15:
            position += 1
        else:
            position = 1
            if not west_p:
                print("\nWestern Conference\n")
                west_p = True


get_team_information()
show_result()
