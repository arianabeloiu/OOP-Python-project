
import random

#create an equipment class 
class Equipment:
    def __init__(self, equipment=None, inventory=None, **kwargs): #initialize 
        super().__init__(**kwargs) #initializes the object for multiple inheritance 
        self.equipment = equipment or [] #denotes equipment 
        self.inventory = inventory or [] #denotes inventory

    def collect(self, item): #defines collect 
        self.inventory.append(item)

    def equip(self, item): #defines equip 
        if item in self.inventory: #if there is an item in the inventory 
            self.inventory.remove(item) #removes item from the inventory list 
            self.equipment.append(item) #adds item to the equipment list 
            print(f"Equipped {item}!")
        else:
            print(f"You don't have {item} in your inventory.")

            
#creates a character class 
class Character: #create a character class

    def __init__(self, name='', hp=0, attack=0, **kwargs): #initialize
        super().__init__(**kwargs)
        self.name = name #denote the name
        self.hp = hp #denote the hit points
        self.attack = attack #denote the attack   

    def __str__(self):
        equip_list = getattr(self, 'equipment', 'None (Standard Character)') #gets the attribute of the equipment list 
        return f"\nName: {self.name}\nHP: {self.hp}\nAttack: {self.attack}\nEquipped: {equip_list}"

    def Attack(self, other): #define the attack 
        other.hp-=random.randint(1,self.attack)

#use multiple inheritance for the wizard class 
class Wizard(Character, Equipment): #inherit character + equipment classes 
    def __init__(self, name, hp, attack, magic, **kwargs): #initialize 
        super().__init__(name=name, hp=hp, attack=attack, **kwargs) #use super() to initialize multiple inheritance 
        self.magic = magic 
        self.max_hp = hp  

    def heal(self): 
        self.hp = self.max_hp 

    def fireball(self, other): 
        damage = random.randint(1, self.magic)
        other.hp -= damage

    def protect(self): #define a protect 
        protection = 0 #denote protection 
        if 'armor' in self.equipment:
            protection += 10 #add 10 points to protection 
        if 'shield' in self.equipment: 
            protection += 5 #add 5 points to protection 
        
        self.hp += protection #add protection to hit points 

if __name__=="__main__":
    weezle = Wizard('Weezle', 200, 5, 500)
    grognak = Wizard('Grognak', 250, 10, 300) #I made grognak a wizard so that he could pick up a shield 
    print(weezle)
    weezle.collect('armor')
    weezle.equip('armor')
    weezle.protect()
    print(weezle)
    grognak.collect('shield')
    grognak.equip('shield')
    grognak.protect()
    print(grognak)
    print("Ready...Set...Fight!")
    while grognak.hp > 0 and weezle.hp > 0:
        grognak.Attack(weezle)
        print(weezle)
        if weezle.hp <= 0:
            break
        weezle.fireball(grognak)
        print(grognak)
        if grognak.hp <= 0:
            break
    if grognak.hp <= 0:
        print("Weezle vaporizes Grognak!")
    else:
        print("Grognak crushes Weezle!")
    
