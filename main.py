"""This is the docstring they fucking meant"""
import Character
import Import
from rolls import rollDice
import ExportPDF
from header import Title

print(Title)
buildPDF = ExportPDF.generatePDF()

skillList = ['Athletics','Acrobatics','SleightOfHand','Stealth','Arcana','History','Investigation',
             'Nature', 'Religion', 'AnimalHandling', 'Insight', 'Medicine','Perception','Survival',
             'Deception','Intimidation','Performance','Persuasion']

Rolls = rollDice()
myTables = Import.tableActivity()



Player = input("Player Name: ")
Char = input("Character Name: ")
Class = input("Character Class: ")
Race = input("Character Race: ")
Char = Character.Character(Player, Char, Class, Race)

myTables.firstTableSelection()
myTables.continueTableSelection()

tableContent = Import.tables.importTables(myTables.userTables)

Rolls.buildPathRolls(myTables.userTables)
Rolls.getTotalRolls()
Rolls.rollsPerPath(myTables.userTables)
Rolls.Roll()

for i in Rolls.pathRolls:
    if Rolls.pathRolls[i]['Total'] > 0:
        Char.buildCharacter(tableContent[i], Rolls.pathRolls[i]['Rolls'])


buildPDF.pageTitle(Char.PlayerInfo)
buildPDF.writeStats(Char.Stats, Char.Stats.Speed, Char.Stats.Renown)
buildPDF.writeRank(Char.PlayerInfo.Rank)


if any(getattr(Char.Skills, x) for x in skillList):
    buildPDF.sectionTitle('Skills')
for i in skillList:
    if getattr(Char.Skills, i):
        buildPDF.writeSkills(i, getattr(Char.Skills, i))
        
if Char.Skills.Languages['Bonus'] or Char.Skills.Languages['Known']:
    buildPDF.sectionTitle('Language')
    buildPDF.writeLanguage(Char.Skills.Languages)

if Char.Magic.Cantrips.Bonus or \
   Char.Magic.Cantrips.Known or \
   Char.Magic.Spells.Bonus or \
   any(x for x in Char.Magic.Spells.Known for x in Char.Magic.Spells.Known[x]):
       buildPDF.sectionTitle('Magic')
       buildPDF.writeMagic(Char.Magic.Cantrips, Char.Magic.Spells)

if Char.Inventory.ExtraItems or Char.Inventory.Carry:
    buildPDF.sectionTitle('Inventory')
    buildPDF.writeBonusItems(Char.Inventory.ExtraItems)
    buildPDF.writeCarryWeight(Char.Inventory.Carry)

if Char.PlayerInfo.Appearance:
    buildPDF.sectionTitle('Physical Traits')
    buildPDF.writeAppearance(Char.PlayerInfo.Appearance)

if Char.PlayerInfo.Contacts or Char.Skills.Handicap or Char.Skills.BonusSkills:
    buildPDF.sectionTitle('Extra')
    buildPDF.writeBonusFeatures(Char.PlayerInfo.Contacts, Char.Skills.Handicap, Char.Skills.BonusSkills)
    
if any(x for x in Char.Inventory.Currency):
    buildPDF.sectionTitle('Currency')
    buildPDF.writeCurrency(Char.Inventory.Currency)
    
buildPDF.writeExperience(Char.PlayerInfo.PastExperience)

buildPDF.savePDF(Char.PlayerInfo.CharacterName)
