from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://sports.yahoo.com/nba/standings/')
info = {"Eastern": {}, "Western": {}}
conf = {1: "Eastern", 2: "Western"}


def get_teams_information():
    for x in range(1, 16):
        for f in range(1, 3):
            team_name = r.html.xpath(
                f'//*[@id="Col1-0-LeagueStandings-Proxy"]/div/div[2]/table[{f}]/tbody/tr[{x}]/th/div/div/a/span[2]/text()',
                first=True)
            stats_teams = []
            for i in range(1, 14):
                stats_teams.append((r.html.xpath(
                    f'//*[@id="Col1-0-LeagueStandings-Proxy"]/div/div[2]/table[{f}]/tbody/tr[{x}]/td[{i}]',
                    first=True)).text)
            info[conf[f]][team_name] = [
                {"pos": x, "W": stats_teams[0], "L": stats_teams[1], "Last 10": stats_teams[8],
                 "Streak": stats_teams[12]}]


def show_result():
    for conference in info:
        print(f"Conference - {conference}\n")
        for team, stats in info[conference].items():
            print(
                f"{stats[0]['pos']}.{team} W - {stats[0]['W']}, L - {stats[0]['L']}, Last - 10 {stats[0]['Last 10']}, "
                f"Streak {stats[0]['Streak']}")
        print()


get_teams_information()
show_result()



# # you can access additional information
# "stats_teams[0] - W"
# "stats_teams[1] - L"
# "stats_teams[2] - Ptc"
# "stats_teams[3] - CGB"
# "stats_teams[5] - Home"
# "stats_teams[6] - Div"
# "stats_teams[7] - Conf"
# "stats_teams[8] - Last 10"
# "stats_teams[9] - PF"
# "stats_teams[10] - PA"
# "stats_teams[11] - Diff"
# "stats_teams[12] - Streak"
# "stats_teams[12] - Win Championship"





# code with bs4----------
# import requests
# from bs4 import BeautifulSoup

# list_numbers_wins, list_numbers_losses = [n for n in range(0, 361, 12)], [n for n in range(1, 361, 12)]
# list_numbers_last, list_numbers_streak = [n for n in range(7, 361, 12)], [n for n in range(10, 361, 12)]

# # wins start from position 0 [n for n in range(0, 361, 12)]
# # losses start from position 1 [n for n in range(1, 361, 12)]
# # Pct start from position 2 [n for n in range(2, 361, 12)]
# # CGB start from position 3 [n for n in range(3, 361, 12)]
# # Home start from position 4 [n for n in range(4, 361, 12)]
# # Div start from position 5 [n for n in range(5, 361, 12)]
# # Conf start from position 6 [n for n in range(6, 361, 12)]
# # Last 10 games start from position 7 [n for n in range(7, 361, 12)]
# # PF start from position 8 [n for n in range(8, 361, 12)]
# # PA start from position 9 [n for n in range(9, 361, 12)]
# # Streak start from position 10 [n for n in range(10, 361, 12)]
# # Win Championship start from position 11 [n for n in range(11, 361, 12)]
# # and below in get_team_information check for the index and add the value if you want more detail info


# team_info = []
# w, l, last_games_p, streak_p = "W", "L", "Last 10", "Streak"


# def get_data(url):
#     r = requests.get(url)
#     return r.text


# soup = BeautifulSoup(get_data("https://sports.yahoo.com/nba/standings/"), 'html.parser')


# def get_team_information():
#     got_w, got_l, got_last_ten, got_streak = False, False, False, False
#     for index, numbers in enumerate(soup.find_all(class_="Bdb(primary-border) Ta(end) Px(cell-padding-x)")):
#         if index in list_numbers_wins:
#             wins_d = numbers.get_text()
#             got_w = True
#         elif index in list_numbers_losses:
#             loses_d = numbers.get_text()
#             got_l = True
#         elif index in list_numbers_last:
#             last_ten = numbers.get_text()
#             got_last_ten = True
#         elif index in list_numbers_streak:
#             streak_d = numbers.get_text()
#             got_streak = True
#         if all([got_w, got_l, got_last_ten, got_streak]):
#             team_info.append({w: wins_d, l: loses_d, last_games_p: last_ten, streak_p: streak_d})
#             got_w, got_l, got_last_ten, got_streak = False, False, False, False


# def show_result():
#     print("\nEastern Conference\n")
#     i = 1
#     for position, (team_name, show) in enumerate(
#             zip(soup.find_all(class_="Ta(start) Fw(400) Fz(12px) H(40px) W(25%)"), team_info)):
#         if position == 15:
#             print("\nWestern Conference\n")
#             i = -14
#         print(
#             f"{position + i}. {team_name.get_text()} : W {show[w]}, L {show[l]}, Last 10 {show[last_games_p]}, Streak {show[streak_p]}")


# get_team_information()
# show_result()
