from Team import Team

ranking=[]
points_draw=1
points_win=3

def add_team(team:Team):
    ranking.append(team)

def find_team(team_name):
    for i in range(len(ranking)):
        if ranking[i].get_name() == team_name:
            return ranking[i]
    return None

def add_draw(first_team_name, second_team_name):
    for i in range(len(ranking)):
        if ranking[i].get_name() == first_team_name:
            ranking[i].add_points(points_draw)
        if ranking[i].get_name() == second_team_name:
            ranking[i].add_points(points_draw)

def add_victory(team_name):
    for i in range(len(ranking)):
        if ranking[i].get_name() == team_name:
            ranking[i].add_points(points_win)











