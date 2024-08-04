import statsapi, datetime, json, pprint

# for player in statsapi.lookup_player('Judge,'):
#     print('Full name: {}, Position: {}'.format(player['fullName'], player['primaryPosition']['abbreviation']))

class Player:
    def __init__(self, name, id, position):
        self.name = name
        self.id = id
        self.position = position

    def __str__(self):
        return f"{self.name}"

class Team:
    def __init__(self, name, id, players):
        self.name = name
        self.id = id
        self.players = players
    
    def __str__(self):
        playersString = ""
        for player in self.players:
            playersString += (str(player) + " ")
        return f"{self.name}: {playersString}" 

teamJSON = statsapi.get('teams', {'sportId':1})

teams = []

for team in teamJSON['teams']:
    players = []
    for player in statsapi.get('team_roster', {'teamId':team['id']})['roster']:
        players.append(Player(player['person']['fullName'], player['person']['id'], player['position']['abbreviation']))

    teams.append(Team(team['teamName'], team['id'], players))

for team in teams:
    print(team)