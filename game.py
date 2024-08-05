from stats import Team, Player
from random import randrange

class Game:
    homeTeam: Team
    awayTeam: Team
    isTop = True

    def __init__(self, homeTeam, awayTeam):
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam

    def atBat(self, batter: Player, pitcher: Player):
        batterStats = batter.getHittingStats()
        bats = int(batterStats['plateAppearances'])
        airOuts = int(batterStats['airOuts'])
        walks = int(batterStats['baseOnBalls']) + airOuts
        catcherInterference = int(batterStats['catchersInterference']) + walks
        doubles = int(batterStats['doubles']) + catcherInterference
        groundOuts = int(batterStats['groundOuts']) + doubles
        hitByPitch = int(batterStats['hitByPitch']) + groundOuts
        homeRuns = int(batterStats['homeRuns']) + hitByPitch
        strikeOuts = int(batterStats['strikeOuts']) + homeRuns
        triples = int(batterStats['triples']) + strikeOuts
        singles = int(batterStats['hits']) - (homeRuns - hitByPitch) - (doubles - catcherInterference) - (triples - strikeOuts) + triples
        
        rand = randrange(0, bats)
        print(rand)

        if (rand > triples):
            return 'single'
        elif (rand > strikeOuts):
            return 'triple'
        elif (rand > homeRuns):
            return 'strikeOut'
        elif (rand > hitByPitch):
            return 'homeRun'
        elif (rand > groundOuts):
            return 'hitByPitch'
        elif (rand > doubles):
            return 'groundOut'
        elif (rand > catcherInterference):
            return 'double'
        elif (rand > walks):
            return 'catcherIntereference'
        elif (rand > airOuts):
            return 'walk'
        else:
            return 'airOut'

g = Game(Team('1', '2', list()), Team('1', '2', list))
print(g.atBat(Player("Aaron Judge", "592450", "CF"), Player("Aaron Judge", "592450", "CF")))







    