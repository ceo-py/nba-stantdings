import requests
from bs4 import BeautifulSoup

list_numbers_wins, list_numbers_losses = [n for n in range(0, 361, 12)], [n for n in range(1, 361, 12)]
list_numbers_last, list_numbers_streak = [n for n in range(7, 361, 12)], [n for n in range(10, 361, 12)]

# wins start from position 0 [n for n in range(0, 361, 12)]
# losses start from position 1 [n for n in range(1, 361, 12)]
# Pct start from position 2 [n for n in range(2, 361, 12)]
# CGB start from position 3 [n for n in range(3, 361, 12)]
# Home start from position 4 [n for n in range(4, 361, 12)]
# Div start from position 5 [n for n in range(5, 361, 12)]
# Conf start from position 6 [n for n in range(6, 361, 12)]
# Last 10 games start from position 7 [n for n in range(7, 361, 12)]
# PF start from position 8 [n for n in range(8, 361, 12)]
# PA start from position 9 [n for n in range(9, 361, 12)]
# Diff start from position 10 [n for n in range(10, 361, 12)]
# Streak start from position 11 [n for n in range(11, 361, 12)]
# Win Championship start from position 12 [n for n in range(12, 361, 12)]
# and below in get_team_information check for the index and add the value if you want more detail info


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
    print("\nEastern Conference\n")
    for position, (team_name, show) in enumerate(
            zip(soup.find_all(class_="Ta(start) Fw(400) Fz(12px) H(40px) W(25%)"), team_info)):
        if position < 15:
            print(
                f"{position + 1}. {team_name.get_text()} : W {show[w]}, L {show[l]}, Last 10 {show[last_games_p]}, Streak {show[streak_p]}")
        else:
            if position == 15:
                print("\nWestern Conference\n")
            print(
                f"{(position + 1) - 15}. {team_name.get_text()} : W {show[w]}, L {show[l]}, Last 10 {show[last_games_p]}, Streak {show[streak_p]}")


get_team_information()
show_result()
