from fpdf import FPDF
#width, height, text, border, ln, align, fill, link
class generatePDF(object):
    def __init__(self):
        self.pdf = FPDF()
        self.pdf.set_display_mode('fullpage')
        self.pdf.add_page()
        
        self.parentpath = 'PDFS\\'
        
    def newPage(self):
        self.pdf.add_page()
    
    def pageTitle(self,playerInfo):
        self.pdf.set_font('Arial', 'B', 18)

        self.pdf.cell(0, 8, playerInfo.CharacterName, 0, 2, 'C')
        self.pdf.cell(0, 8, playerInfo.CharacterClass, 0, 2, 'C')
        self.pdf.cell(0, 8, playerInfo.CharacterRace, 'B', 2, 'C')
        
    def sectionTitle(self, Title):
        self.pdf.ln()
        
        self.pdf.set_font('Arial', 'B', 14)
        self.pdf.cell(0, 6, Title, 0, 1, 'L')

    def writeStats(self, Value, Speed, Renown):
        
        self.pdf.set_font('Arial', 'I', 12)
        self.pdf.cell(31.6, 8, 'Strength', 0, 0, 'C')
        self.pdf.cell(31.6, 8, 'Dexterity', 0, 0, 'C')
        self.pdf.cell(31.6, 8, 'Constitution', 0, 0, 'C')
        self.pdf.cell(31.6, 8, 'Intelligence', 0, 0, 'C')
        self.pdf.cell(31.6, 8, 'Wisdom', 0, 0, 'C')
        self.pdf.cell(31.6, 8, 'Charisma', 0, 1, 'C')
        
        self.pdf.set_font('Arial', '', 12)
        self.pdf.cell(31.6, 8, '%s' % Value.Str.Score, 0, 0, 'C')
        self.pdf.cell(31.6, 8, '%s' % Value.Dex.Score, 0, 0, 'C')
        self.pdf.cell(31.6, 8, '%s' % Value.Con.Score, 0, 0, 'C')
        self.pdf.cell(31.6, 8, '%s' % Value.Int.Score, 0, 0, 'C')
        self.pdf.cell(31.6, 8, '%s' % Value.Wis.Score, 0, 0, 'C')
        self.pdf.cell(31.6, 8, '%s' % Value.Cha.Score, 0, 1, 'C')
        
        if Value.Str.Mod >= 0:
            self.pdf.cell(31.6, 8, '+%s' % Value.Str.Mod, 0, 0, 'C')
        else:
            self.pdf.cell(31.6, 8, '%s' % Value.Str.Mod, 0, 0, 'C')
            
        if Value.Dex.Mod >= 0:
            self.pdf.cell(31.6, 8, '+%s' % Value.Dex.Mod, 0, 0, 'C')
        else:
            self.pdf.cell(31.6, 8, '%s' % Value.Dex.Mod, 0, 0, 'C')
            
        if Value.Con.Mod >= 0:
            self.pdf.cell(31.6, 8, '+%s' % Value.Con.Mod, 0, 0, 'C')
        else:
            self.pdf.cell(31.6, 8, '%s' % Value.Con.Mod, 0, 0, 'C')
            
        if Value.Int.Mod >= 0:
            self.pdf.cell(31.6, 8, '+%s' % Value.Int.Mod, 0, 0, 'C')
        else:
            self.pdf.cell(31.6, 8, '%s' % Value.Int.Mod, 0, 0, 'C')
            
        if Value.Wis.Mod >= 0:
            self.pdf.cell(31.6, 8, '+%s' % Value.Wis.Mod, 0, 0, 'C')
        else:
            self.pdf.cell(31.6, 8, '-%s' % Value.Wis.Mod, 0, 0, 'C')
            
        if Value.Cha.Mod >= 0:
            self.pdf.cell(31.6, 8, '+%s' % Value.Cha.Mod, 0, 1, 'C')
        else:
            self.pdf.cell(31.6, 8, '%s' % Value.Cha.Mod, 0, 1, 'C')
        
        
        if Speed or Renown:
            self.sectionTitle('Bonus Stats')
            self.pdf.set_font('Arial', '', 12)
        
        if Speed:
            self.pdf.cell(35, 8, 'Speed: ' , 0, 0, 'L')
            self.pdf.cell(35, 8, '%s' % Speed, 0, 1, 'L')

        if Renown:
            self.pdf.cell(35, 8, 'Renown: ' , 0, 0, 'L')
            self.pdf.cell(35, 8, '%s' % Renown, 0, 1, 'L')
            
    def writeSkills(self, Skill, Score):
        self.pdf.set_font('Arial', '', 12)
        self.pdf.cell(35, 8, '%s:' % Skill, 0, 0, 'L')
        self.pdf.cell(35, 8, '%s' % Score, 0, 1, 'L')
        
    def writeLanguage(self, Language):
        self.pdf.set_font('Arial', '', 12)
        if Language['Bonus']:
            self.pdf.cell(35, 8, 'Bonus: ', 0, 0, 'L')
            self.pdf.cell(35, 8, '%s' % Language['Bonus'], 0, 1, 'L')
            
        if Language['Known']:
            self.pdf.cell(35, 8, 'Known: ', 0, 0, 'L')
            for i in Language['Known']:
                self.pdf.cell(35, 8, '%s' % Language['Known'][i], 0, 2, 'L')
        
    def writeMagic(self, Cantrips, Spells):
        self.pdf.set_font('Arial', '', 12)
        if Cantrips.Bonus or Cantrips.Known:
            self.pdf.set_font('Arial', 'I', 12)
            self.pdf.cell(35, 8, 'Cantrips', 0, 1, 'L')
            self.pdf.set_font('Arial', '', 12)
        if Cantrips.Bonus:
            self.pdf.cell(35, 8, 'Bonus: ', 0, 0, 'L')
            self.pdf.cell(35, 8, '%s' % Cantrips.Bonus, 0, 1, 'L')
            
        if Cantrips.Known:
            self.pdf.cell(35, 8, 'Known: ', 0, 0, 'L')
            for i in Cantrips.Known:
                if Cantrips.Known.index(i) < (len(Cantrips.Known) - 1):
                    line = 2
                else:
                    line = 1
                self.pdf.cell(35, 8, i, 0, 2, 'L')

        if Spells.Bonus or any(x for x in Spells.Known for x in Spells.Known[x]):
            self.pdf.set_font('Arial', 'B', 12)
            self.pdf.cell(35, 8, 'Spells', 0, 1, 'L')
            self.pdf.set_font('Arial', '', 12)
        
        if Spells.Bonus:
            self.pdf.cell(35, 8, 'Bonus: ', 0, 0, 'L')
            self.pdf.cell(35, 8, '%s' % Spells.Bonus, 0, 1, 'L')
            
        for Level in Spells.Known:
            if Spells.Known[Level]:
                self.pdf.cell(35, 8, 'Level %s' % Level, 0, 0, 'L')
                for Spell in Spells.Known[Level]:
                    if Spells.Known[Level].index(Spell) < (len(Spells.Known[Level]) - 1):
                        line = 2
                    else:
                        line = 1
                    self.pdf.cell(35, 8, Spell, 0, line, 'L')

    def writeExperience(self, Experience):
        self.pdf.add_page(orientation = 'P')
        self.sectionTitle('Past Experiences')
        self.pdf.set_font('Arial', '', 12)
        num = 1
        for i in Experience:
            self.pdf.multi_cell(0, 8, '%s. %s' % (num, i), 0, 1, 'L')
            num += 1
        
    def writeProficiencies(self, Tools, Instruments):
        self.pdf.set_font('Arial', '', 12)
        if Tools:
            self.pdf.cell(35, 8, 'Tools: ', 0, 0, 'L')
            for i in Tools:
                self.pdf.cell(35, 8, i, 0, 2, 'L')

        if Instruments:
            self.pdf.cell(35, 8, 'Instruments: ', 0, 0, 'L')
            for i in Instruments:
                self.pdf.cell(35, 8, i, 0, 2, 'L')
                
    def writeCurrency(self, Currency):
        self.pdf.set_font('Arial', '', 12)
        if Currency['Platinum']:
            self.pdf.cell(35, 8, 'Platinum: ', 0, 0, 'L')
            self.pdf.cell(25, 8, '%s' % Currency['Platinum'], 0, 1, 'L')
            
        if Currency['Gold']:
            self.pdf.cell(35, 8, 'Gold: ', 0, 0, 'L')
            self.pdf.cell(35, 8, '%s' % Currency['Gold'], 0, 1, 'L')
        
        if Currency['Silver']:
            self.pdf.cell(35, 8, 'Silver: ', 0, 0, 'L')
            self.pdf.cell(35, 8, '%s' % Currency['Silver'], 0, 1, 'L')
            
        if Currency['Copper']:
            self.pdf.cell(35, 8, 'Copper: ', 0, 0, 'L')
            self.pdf.cell(35, 8, '%s' % Currency['Copper'], 0, 1, 'L')
            
    def writeBonusItems(self, Items):
        self.pdf.set_font('Arial', '', 12)
        if Items:
            self.pdf.cell(35, 8, 'Items: ')
            for i in Items:
                self.pdf.cell(35, 8, i, 0, 2, 'L')
                
    def writeCarryWeight(self, Weight):
        self.pdf.set_font('Arial', '', 12)
        if Weight:
            self.pdf.cell(35, 8, 'Weight: ', 0, 0, 'L')
            self.pdf.cell(35, 8, '%s' % Weight, 0, 1, 'L')
        
    def writeBonusFeatures(self, Contacts, Handicap, BonusSkills):
        self.pdf.set_font('Arial', '', 12)
        if Contacts:
            self.pdf.cell(35, 8, 'Contacts: ', 0, 0, 'L')
            self.pdf.cell(35, 8, '%s' % Contacts, 0, 1, 'L')
                
        if Handicap:
            self.pdf.cell(35, 8, 'Handicap: ', 0, 0, 'L')
            for i in Handicap:
                print(i, Handicap.index(i))
                if Handicap.index(i) < len(Handicap) - 1:
                    line = 2
                else:
                    line = 1
            self.pdf.cell(25, 8, i, 0, line, 'L')
    
        if BonusSkills:
            self.pdf.cell(35, 8, 'Bonus Skills: ', 0, 0, 'L')
            for i in BonusSkills:
                if BonusSkills.index(i) < len(BonusSkills) - 1:
                    line = 2
                else:
                    line = 1
            self.pdf.cell(35, 8, i, 0, line, 'L')
                
    def writeAppearance(self, Appearance):
        self.pdf.set_font('Arial', '', 12)
        if Appearance:
            self.pdf.cell(35, 8, 'Appearance: ', 0, 0, 'L')
            for i in Appearance:
                self.pdf.cell(35, 8, i, 0, 2, 'L')

    def savePDF(self, PlayerName):
        self.pdf.output(self.parentpath + PlayerName + '.pdf')










