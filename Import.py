import csv
import sys
import os

class tableActivity(object):
    def __init__(self):
        self.filepath = './CSVs'
        self.filepathTables = [filename.split('.')[0] for root, dirs, files in os.walk(self.filepath) for filename in files]
        self.availableTables = ['Exit'] + self.filepathTables
        self.userTables = []
        self.selection = 0

    def addUserTable(self, selectedTable):
        self.userTables.append(self.availableTables.pop(selectedTable))

    def listTables(self):
        num = 1
        for AT in self.availableTables:
            print(str(num) + ". ", AT)
            num += 1
            
        self.selection = int(input('Choose your destiny: ')) - 1
                
    def firstTableSelection(self):
        self.listTables()

        if self.selection == 0:
            input('No Tables Selected.  Quitting Character Creation\nPlease press Enter...')
            sys.exit(0)
        else:
            self.addUserTable(self.selection)
            self.availableTables[0] = 'Continue'

    def continueTableSelection(self):
        while self.selection != 0:
            self.listTables()                
            if self.selection == 0:
                break
            else:
                self.addUserTable(self.selection)

class tables():
    def importTables(tables):
        returnTables = {}
        for table in tables:
            temp = {}
            path = './CSVs/' + table + '.csv'
            with open(path) as pathCSV:
                temp[table] = list(csv.DictReader(pathCSV))
            returnTables = {**returnTables, **temp}
        return returnTables
