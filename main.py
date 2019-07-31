"""This is the docstring they fucking meant"""
import Character
import ImportExport
from rolls import rollDice
import SavePDF

buildPDF = SavePDF.generatePDF()

skillList = ['Athletics','Acrobatics','SleightOfHand','Stealth','Arcana','History','Investigation',
             'Nature', 'Religion', 'AnimalHandling', 'Insight', 'Medicine','Perception','Survival',
             'Deception','Intimidation','Performance','Persuasion']

Rolls = rollDice()
Tables = ImportExport.tableActivity()
tableContent = {"Academic":ImportExport.tables.Import.academicTable(),
                "Life":ImportExport.tables.Import.lifeTable(),
                "Military":ImportExport.tables.Import.militaryTable()}

Player = input("Player Name: ")
Char = input("Character Name: ")
Class = input("Character Class: ")
Race = input("Character Race: ")
Char = Character.Character(Player, Char, Class, Race)

Tables.firstTableSelection()
Tables.continueTableSelection()

Rolls.getTotalRolls()
Rolls.rollsPerPath(Tables.userTables)
Rolls.Roll()

for i in Rolls.pathRolls:
    if Rolls.pathRolls[i]['Total'] > 0:
        Char.buildCharacter(tableContent[i], Rolls.pathRolls[i]['Rolls'])


buildPDF.pageTitle(Char.PlayerInfo)
buildPDF.writeStats(Char.Stats, Char.Stats.Speed, Char.Stats.Renown)


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

Char.Skills.Handicap.append('Picks nose all the time')
if Char.PlayerInfo.Contacts or Char.Skills.Handicap or Char.Skills.BonusSkills:
    buildPDF.sectionTitle('Extra')
    buildPDF.writeBonusFeatures(Char.PlayerInfo.Contacts, Char.Skills.Handicap, Char.Skills.BonusSkills)
    
if any(x for x in Char.Inventory.Currency):
    buildPDF.sectionTitle('Currency')
    buildPDF.writeCurrency(Char.Inventory.Currency)
    
buildPDF.writeExperience(Char.PlayerInfo.PastExperience)

buildPDF.savePDF(Char.PlayerInfo.CharacterName)
