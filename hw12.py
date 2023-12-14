import random

# PART A (10 points)
#########################################################################

class Member:
    '''
    Purpose: 
        Represents a player in the game
    Instance variables: 
        self.name = a string that represents the name of the player
        self.socialStatus = a int that represents the player's social status
    Methods: 
        __init__ = the constructor of the class
            Parameter(s)
                name = a string representing the name of the player
        updateStatus = randomly adds or substracts 1 from self.socialStatus
        __repr__ = changes the output of the Member object
    '''
    def __init__(self, name):
        self.name = name
        self.socialStatus = 5

    def updateStatus(self):
        if self.socialStatus < 10 and self.socialStatus > 1:
            self.socialStatus += random.randrange(-1,2,2)
    
    def __repr__(self):
        return ("Name: {}, Social Status: {}").format(self.name,self.socialStatus)

class Tribe:
    '''
    Purpose: 
        Represents a tribe in the game
    Instance variables: 
        self.tribename = a string representing the name of the tribe
        self.members = a list of Member objects, representing the members of the tribe
    Methods: 
        __init__ = the constructor of the class
            Parameter(s)
                tribeName = a string representing the name of the tribe
                playerNames = a list of strings representing the name of each player in the tribe
        updateStatusForAll = each member of the tribe updates thier social status
    '''
    def __init__(self, tribeName, playerNames):
        self.tribeName = tribeName
        self.members = []
        for i in playerNames:
            self.members.append(Member(i))

    def updateStatusForAll(self):
        for i in self.members:
            i.updateStatus()

#########################################################################

# PART B (20 points)
#########################################################################

class Game:
    '''
    Purpose: 
        Simulates the game of Survivor by having the computer make random choices
    Instance variables: 
        self.redTribe = a Tribe object representing Red Tribe
        self.blueTribe = a Tribe object represent Blue Tribe
        self.merge = a Tribe object representing the Merged Tribe when the game
            moves to the Merged Tribe phase
    Methods: 
        __init__ = the constructor of the class
            Parameter(s)
                redTribe = a Tribe object representing Red Tribe
                blueTribe = a Tribe object representing Blue tribe
        challengeWinner = returns a string representing the winner of the immunity 
            challenge depending on the phase of the game
        getOdds = returns a list representing the odds of the players in the tribe
            Parameter(s)
                tribe = a Tribe object representing a tribe of the game
        vote = returns a string representing which member of the tribe is voted 
            out or which member of the tribe is the winner
            Parameter(s)
                tribe = a Tribe object representing a tribe of the game
                immune = a string reprsenting the name of the immune player in the game
        playSurvivor = simulates an entire game of Survivor
    '''
    def __init__(self, redTribe, blueTribe):
        self.redTribe = redTribe
        self.blueTribe = blueTribe
        self.merge = Tribe("Merge",[])

    def challengeWinner(self): 
        if self.merge.members == []:
            return random.choice((self.redTribe.tribeName,self.blueTribe.tribeName))
        else:
            return random.choice(self.merge.members).name

    def getOdds(self, tribe): 
        odds = []
        for i in tribe.members:
            odds += [i.name] * (i.socialStatus)
        return odds

    def vote(self, tribe, immune):
        chosen = random.choice(self.getOdds(tribe))
        while chosen == immune:
            chosen = random.choice(self.getOdds(tribe))
        for i, v in enumerate(tribe.members[:]):
            if v.name == chosen:
                tribe.members.pop(i)
        return chosen

    def playSurvivor(self):
        for _ in range(4):
            winner = self.challengeWinner()
            print(("{} wins the challenge!").format(winner))
            if winner == self.redTribe.tribeName:
                print(("{} voted out of the {}\n").format(self.vote(self.blueTribe,""),self.blueTribe.tribeName))
            else:
                print(("{} voted out of the {}\n").format(self.vote(self.redTribe,""),self.redTribe.tribeName))
            self.redTribe.updateStatusForAll()
            self.blueTribe.updateStatusForAll()
        self.merge.members = self.redTribe.members + self.blueTribe.members
        for _ in range(6):
            winner = self.challengeWinner()
            print(("{} wins the challenge!").format(winner))
            print(("{} voted out of the Merged Tribe\n").format(self.vote(self.merge,winner)))
            self.merge.updateStatusForAll()
        self.vote(self.merge,"")
        print(("The sole survivor is {}").format(self.merge.members[0].name))

#########################################################################

def main():
    names = ["Isaac", "Arunima", "Nakul", "Micah", "David", "Alice", 
            "Tarik", "Ian", "Charley", "Demond", "Abdourahman", "Vin"] 
    redTribeNames = []

    while len(redTribeNames) < 6:
        randName = random.choice(names)
        redTribeNames.append(randName)
        names.remove(randName)

    blueTribeNames = names

    #UNCOMMENT THE FOLLOWING TO CREATE TRIBES AND TEST THE SIMULATION 
    redTribe = Tribe("Red Tribe", redTribeNames)
    blueTribe = Tribe("Blue Tribe", blueTribeNames)

    simulation = Game(redTribe, blueTribe)
    simulation.playSurvivor()

if __name__ == '__main__':
   main()
