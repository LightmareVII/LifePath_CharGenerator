import random

class rollDice(object):
    def __init__(self):
        self.totalRolls = 0
        self.Rolls = []
        self.pathRolls = {}
        
    def buildPathRolls(self, userTables):
        for table in userTables:
            tempTable = {}
            tempTable[table] = {'Total': 0,
                                 'Rolls': []}
            self.pathRolls = {**self.pathRolls, **tempTable}
        
    def getTotalRolls(self):
        self.totalRolls = int(input("Total Rolls: "))

    
    def Roll(self):
        for path in self.pathRolls:
            while len(self.pathRolls[path]['Rolls']) < self.pathRolls[path]['Total']:
                currentRoll = random.randint(1,100)
                if currentRoll not in self.pathRolls[path]['Rolls']:
                    self.pathRolls[path]['Rolls'].append(currentRoll)

    def rollsPerPath(self, paths):
        while sum(i['Total'] for i in self.pathRolls.values()) < self.totalRolls:
            print('Rolls Left: %s' % (self.totalRolls - sum(i['Total'] for i in self.pathRolls.values())))
            for p in paths:
                thisRoll = int(input('Add how many rolls to %s?' % p))
                if (sum(i['Total'] for i in self.pathRolls.values()) + int(thisRoll)) > self.totalRolls:
                    print("You don't have that many rolls, sorry...")
                    break
                elif (sum(i['Total'] for i in self.pathRolls.values()) + int(thisRoll)) == self.totalRolls:
                    self.pathRolls[p]['Total'] += thisRoll
                    break
                else:
                    self.pathRolls[p]['Total'] += thisRoll

