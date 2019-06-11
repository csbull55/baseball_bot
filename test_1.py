import datetime
import statsapi

# testing some of the features of the statsapi baseball stats lib

today_date = datetime.date.today()


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
    for i in game_scores:
        if team.title() in i:
            line = i
        else:
            line = 'no'
    return line


team_score = get_score('nationals')

print(team_score)

