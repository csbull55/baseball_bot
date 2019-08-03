import datetime
import statsapi

# testing some of the features of the statsapi baseball stats lib

today_date = datetime.date.today()
menu_items = [
    '\t1: Score',
    '\t2: Hello',
    '\tq: Quit\n',
    ]


def title_bar():
    print('\t***********************')
    print('\t****Baseball Scores****')
    print('\t***********************\n')


def menu():
    print('Please select an option')
    print('\n'.join(menu_items))


# defines the og lookup, returns games for a date, or today if none given
def game_list(games_date=today_date):
    lookup = statsapi.schedule(date=games_date)
    games = [game['game_id'] for game in lookup]
    return games


# returns line-score for inputted team
def get_score(team):
    games_today = game_list()

    # returns list of linescores from todays games
    game_scores = [statsapi.linescore(game) for game in games_today]

    # returns todays linescore, prints message if no score
    line = "The {} did not play today".format(team.title())
    for i in game_scores:
        if team.title() in i:
            line = i
    return line


# main app #
title_bar()
menu()

option = ''
option = input('Option: ')

while option != 'q':
    if option == '1':
        # prompts for team and returns score
        team = input('Please select a team:')
        team_score = get_score(team)
        print('\n' + team_score)
        menu()

    elif option == 2:
        print('Hello')
