import csv
import sys
#from fpdf import FPDF

class tableActivity(object):
    def __init__(self):
        self.availableTables = ['Exit','Academic','Life','Military']
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
    class Import():
        def academicTable():
            path = "./CSVs/Academic.csv"
            with open(path) as pathCSV:
                temp = csv.DictReader(pathCSV)
                return list(temp)

        def lifeTable():
            path = "./CSVs/Academic.csv"
            with open(path) as pathCSV:
                temp = csv.DictReader(pathCSV)
                return list(temp)

        def militaryTable():
            path = "./CSVs/Academic.csv"
            with open(path) as pathCSV:
                temp = csv.DictReader(pathCSV)
                return list(temp)
"""            
    class export():
        pdf = FPDF()
        class Header(self):
            pdf.set_font('Arial', 'B', 18)
"""
            
            
        


"""
with open('./CSVs/Academic.csv') as AcademicPath:
    test = csv.DictReader(AcademicPath)
    Academic = list(test)
"""
