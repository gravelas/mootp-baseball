import statsapi, datetime, json, pprint

class Player:
    player_stats = None
    def __init__(self, name, id, position):
        self.name = name
        self.id = id
        self.position = position

    def __str__(self):
        return f"{self.name}"
    
    def getHittingStats(self):
        if (self.player_stats == None):
            self.player_stats = statsapi.player_stat_data(self.id, group='hitting', type="career", sportId=1)['stats'][0]['stats']
        return self.player_stats

    def getID(self):
        return self.id
    
    def getName(self):
        return self.name

class Team:
    name: str
    id: str
    players: list[Player]
    def __init__(self, name, id, players):
        self.name = name
        self.id = id
        self.players = players
    
    def __str__(self):
        playersString = ""
        for player in self.players:
            playersString += (str(player) + " ")
        return f"{self.name}: {playersString}" 
    
    def getPlayers(self):
        return self.players


def getTeams():
    teamJSON = statsapi.get('teams', {'sportId':1})

    teams = []

    for team in teamJSON['teams']:
        players = []
        for player in statsapi.get('team_roster', {'teamId':team['id']})['roster']:
            players.append(Player(player['person']['fullName'], player['person']['id'], player['position']['abbreviation']))

        teams.append(Team(team['teamName'], team['id'], players))

    return teams

for team in getTeams():
    for player in team.getPlayers():
        if player.getName() == "Aaron Judge":
            print(player.getID())
            pprint.pprint(player.getHittingStats())

