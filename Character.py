"""Object constructors for Character Instance"""
import math

CANTRIP_LIST = ['Acid Splash', 'Blade Ward', 'Booming Blade', 'Chill Touch', 'Control Flames',
'Create Bonfire', 'Dancing Lights', 'Druidcraft', 'Eldritch Blast', 'Fire Bolt', 'Friends',
'Frostbite', 'Green-Flame Blade', 'Guidance', 'Gust', 'Infestation', 'Light', 'Lightning Lure',
'Mage Hand', 'Magic Stone', 'Mending', 'Message', 'Minor Illusion', 'Mold Earth', 'Poison Spray',
'Prestidigitation', 'Primal Savagery', 'Produce Flame', 'Ray of Frost', 'Resistance', 'Sacred Flame',
'Shape Water', 'Shillelagh', 'Shocking Grasp', 'Spare the Dying', 'Sword Burst', 'Thaumaturgy',
'Thorn Whip', 'Thunderclap', 'Toll the Dead', 'True Strike', 'Vicious Mockery', 'Word of Radiance',]
SPELL_LIST = {'1':['Absorb Elements', 'Alarm', 'Animal Friendship', 'Armor of Agathys', 'Arms of Hadar',
'Bane', 'Beast Bond', 'Bless', 'Burning Hands', 'Catapult', 'Cause Fear', 'Ceremony', 'Chaos Bolt',
'Charm Person', 'Chromatic Orb', 'Color Spray', 'Command', 'Compelled Duel', 'Comprehend Languages',
'Create or Destroy Water', 'Cure Wounds', 'Detect Evil and Good', 'Detect Magic', 'Detect Poison and Disease',
'Disguise Self', 'Dissonant Whispers', 'Divine Favor', 'Earth Tremor', 'Ensnaring Strike', 'Entangle',
'Expeditious Retreat', 'Faerie Fire', 'False Life', 'Feather Fall', 'Find Familiar', 'Fog Cloud',
'Goodberry', 'Grease', 'Guiding Bolt', 'Hail of Thorns', 'Healing Word', 'Hellish Rebuke', 'Heroism',
'Hex', "Hunter's Mark", 'Ice Knife', 'Identify', 'Illusory Script', 'Inflict Wounds', 'Jump', 'Longstrider',
'Mage Armor', 'Magic Missile', 'Protection from Evil and Good', 'Purify Food and Drink', 'Ray of Sickness',
'Sanctuary', 'Searing Smite', 'Shield', 'Shield of Faith', 'Silent Image', 'Sleep', 'Snare', 'Speak with Animals',
"Tasha's Hideous Laughter", "Tenser's Floating Disk", 'Thunderous Smite', 'Thunderwave', 'Unseen Servant',
'Witch Bolt', 'Wrathful Smite', 'Zephyr Strike'],
              '2':['Level2 Spell'],
              '3':['Level3 Spell'],
              '4':['Level4 Spell'],
              '5':['Level5 Spell'],
              '6':['Level6 Spell'],
              '7':['Level7 Spell'],
              '8':['Level8 Spell'],
              '9':['Level9 Spell'],
              '10':['Level10 Spell']}

class PlayerInfo(object):
    """playerInfo Class"""
    def __init__(self, pName, cName, cClass, cRace):
        """INIT"""
        self.PlayerName = pName
        self.CharacterName = cName
        self.CharacterClass = cClass
        self.CharacterRace = cRace
        self.PastExperience = []
        self.Appearance = []
        self.Contacts = 0
        self.Rank = 0

class Str(object):
    def __init__(self):
        self.Score = 10
        self.Mod = 0
        
    def addStrength(self, Value):
        if self.Score + Value > 20:
            self.Core = 20
        else:
            self.Score += Value

class Dex(object):
    def __init__(self):
        self.Score = 10
        self.Mod = 0
        
    def addDexterity(self, Value):
        if self.Score + Value > 20:
            self.Core = 20
        else:
            self.Score += Value

class Con(object):
    def __init__(self):
        self.Score = 10
        self.Mod = 0
        
    def addConstitution(self, Value):
        if self.Score + Value > 20:
            self.Core = 20
        else:
            self.Score += Value

class Int(object):
    def __init__(self):
        self.Score = 10
        self.Mod = 0
        
    def addIntelligence(self, Value):
        if self.Score + Value > 20:
            self.Core = 20
        else:
            self.Score += Value

class Wis(object):
    def __init__(self):
        self.Score = 10
        self.Mod = 0
        
    def addWisdom(self, Value):
        if self.Score + Value > 20:
            self.Core = 20
        else:
            self.Score += Value

class Cha(object):
    def __init__(self):
        self.Score = 10
        self.Mod = 0
        
    def addCharisma(self, Value):
        if self.Score + Value > 20:
            self.Core = 20
        else:
            self.Score += Value

class Stats(object):
    """Stats"""
    def __init__(self):
        self.Str = Str()
        self.Dex = Dex()
        self.Con = Con()
        self.Int = Int()
        self.Wis = Wis()
        self.Cha = Cha()
        self.HP = 0
        self.FS = 0
        self.Speed = 0
        self.Renown = 0

    def setMods(self):
        self.Str.Mod = math.floor((self.Str.Score - 10) / 2)
        self.Dex.Mod = math.floor((self.Dex.Score - 10) / 2)
        self.Con.Mod = math.floor((self.Con.Score - 10) / 2)
        self.Int.Mod = math.floor((self.Int.Score - 10) / 2)
        self.Wis.Mod = math.floor((self.Wis.Score - 10) / 2)
        self.Cha.Mod = math.floor((self.Cha.Score - 10) / 2)
        
    def addHP(self, Hitpoints):
        self.HP += Hitpoints
        
    def addFS(self, FightingSpirit):
        self.FS += FightingSpirit
        
    def addSpeed(self, S):
        self.Speed += S
        
    def addRenown(self, R):
        self.Renown += R

class Skills(object): #break out into classes for char sheet build to evaluate proficiency
    """Skills"""
    def __init__(self):
        self.Athletics = 0
        self.Acrobatics = 0
        self.SleightOfHand = 0
        self.Stealth = 0
        self.Arcana = 0
        self.History = 0
        self.Investigation = 0
        self.Nature = 0
        self.Religion = 0
        self.AnimalHandling = 0
        self.Insight = 0
        self.Medicine = 0
        self.Perception = 0
        self.Survival = 0
        self.Deception = 0
        self.Intimidation = 0
        self.Performance = 0
        self.Persuasion = 0
        self.Tools = []
        self.Instruments = []
        self.BonusSkills = []
        self.Handicap = []
        self.Languages = {'Bonus':0,
                          'Known':[]}

class Cantrips(object):         #FEEDER
    """Cantrips"""
    def __init__(self):
        self.Bonus = 0
        self.Known = []

class Spells(object):           #FEEDER
    """Spells"""
    def __init__(self):
        self.Bonus = 0
        self.Known = {'1':[],
                      '2':[],
                      '3':[],
                      '4':[],
                      '5':[],
                      '6':[],
                      '7':[],
                      '8':[],
                      '9':[],
                      '10':[]}

class Magic(object):
    """Magic"""
    def __init__(self):
        self.Cantrips = Cantrips()
        self.Spells = Spells()

class Inventory(object):
    """Inventory"""
    def __init__(self):
        self.Currency = {'Platinum':0,
                         'Gold':0,
                         'Silver':0,
                         'Copper':0}
        self.ExtraItems = []
        self.Carry = 0

class Character(object):
    """Create Character Class"""
    def __init__(self, playerName, charName, charClass, charRace):
        """"Put it all together"""
        self.PlayerInfo = PlayerInfo(playerName, charName, charClass, charRace)
        self.Stats = Stats()
        self.Skills = Skills()
        self.Magic = Magic()
        self.Inventory = Inventory()

        self.Stats.setMods()

    def addPastExperience(self, Event):
        if isinstance(Event, int):
            self.PlayerInfo.Contacts += Event
        elif isinstance(Event, str):
            self.PlayerInfo.PastExperience.append(Event)

    def addSkills(self, Skill, Amount):
        if Skill == 'Languages':
            if isinstance(Amount, int):
                self.Skills.Languages['Bonus'] += Amount
            elif isinstance(Amount, str):
                if Amount:
                    self.Skills.Languages['Known'].append(Amount)
        else:
            if isinstance(Amount, int):
                setattr(self.Skills, Skill, getattr(self.Skills, Skill) + Amount)
            elif isinstance(Amount, str):
                if Amount:
                    getattr(self.Skills, Skill).append(Amount)


    def addCurrency(self, Fiat, Amount):
        self.Inventory.Currency[Fiat] += Amount

    def addItem(self, Item):
        if Item:
            self.Inventory.ExtraItems.append(Item)

    def addCantrip(self, Cantrip):
        if isinstance(Cantrip, int):
            self.Magic.Cantrips.Bonus += Cantrip
        elif isinstance(Cantrip, str):
            if Cantrip:
                self.Magic.Cantrips.Known.append(Cantrip)
        elif isinstance(Cantrip, list):
            for C in Cantrip:
                self.addCantrip(C)

    def addSpell(self, Spell):
        if isinstance(Spell, int):
            self.Magic.Spells.Bonus += Spell
        elif isinstance(Spell, str):
            if Spell:
                print('Checking List for %s' % Spell)
                for spellLevel in SPELL_LIST:
                    for sL in SPELL_LIST[spellLevel]:
                        if sL == Spell:
                            print('Adding %s to Level %s Chapter' % (Spell, spellLevel))
                            self.Magic.Spells.Known[spellLevel].append(Spell)
        elif isinstance(Spell, list):
            for S in Spell:
                self.addSpell(S)
                
    def increaseCarry(self, Weight):
        self.Inventory.Carry += Weight
        
    def changeAppearance(self, trait):
        if trait:
            self.PlayerInfo.Appearance.append(trait)
            
    def addRank(self, increase):
        self.PlayerInfo.Rank += increase
        
    def buildCharacter(self, csvList, pathRoll):
        type(csvList)
        type(pathRoll)
        for value in pathRoll:
            type(value)
            num = value - 1
            result = csvList[num]
            
            self.addPastExperience(result['PastExperience'])
            self.addPastExperience(int(result['Contacts']))
            self.Stats.Str.addStrength(int(result['STR']))
            self.Stats.Dex.addDexterity(int(result['DEX']))
            self.Stats.Con.addConstitution(int(result['CON']))
            self.Stats.Int.addIntelligence(int(result['INT']))
            self.Stats.Wis.addWisdom(int(result['WIS']))
            self.Stats.Cha.addCharisma(int(result['CHA']))
            self.Stats.setMods()
            self.Stats.addSpeed(int(result['Speed']))
            self.Stats.addRenown(int(result['Renown']))
            self.addSkills('Athletics', int(result['Athletics']))
            self.addSkills('Acrobatics', int(result['Acrobatics']))
            self.addSkills('SleightOfHand', int(result['SleightOfHand']))
            self.addSkills('Stealth', int(result['Stealth']))
            self.addSkills('Arcana', int(result['Arcana']))
            self.addSkills('History', int(result['History']))
            self.addSkills('Investigation', int(result['Investigation']))
            self.addSkills('Nature', int(result['Nature']))
            self.addSkills('Religion', int(result['Religion']))
            self.addSkills('AnimalHandling', int(result['AnimalHandling']))
            self.addSkills('Insight', int(result['Insight']))
            self.addSkills('Medicine', int(result['Medicine']))
            self.addSkills('Perception', int(result['Perception']))
            self.addSkills('Survival', int(result['Survival']))
            self.addSkills('Deception', int(result['Deception']))
            self.addSkills('Intimidation', int(result['Intimidation']))
            self.addSkills('Performance', int(result['Performance']))
            self.addSkills('Persuasion', int(result['Persuasion']))
            self.addSkills('Tools', result['Tools'])
            self.addSkills('Instruments', result['Instruments'])
            self.addSkills('BonusSkills', result['BonusSkills'])
            self.addSkills('Handicap', result['Handicap'])
            self.addSkills('Languages', int(result['ExtraLanguages']))
            self.addSkills('Languages', result['Language'])
            self.addCantrip(int(result['ExtraCantrips']))
            self.addCantrip(result['Cantrip'])
            self.addSpell(int(result['ExtraSpells']))
            self.addSpell(result['Spells'])
            self.addItem(result['ExtraItems'])
            self.increaseCarry(int(result['CarryWeight']))
            self.addCurrency('Copper', int(result['Copper']))
            self.addCurrency('Silver', int(result['Silver']))
            self.addCurrency('Gold', int(result['Gold']))
            self.addCurrency('Platinum', int(result['Platinum']))
            self.addRank(int(result['Rank']))
