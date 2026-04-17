import random

class Character: #create a character class
    def __init__(self, name='', hp=0, attack=0, **kwargs): #initialize 
        self.name = name #denote the name 
        self.hp = hp #denote the hit points
        self.attack = attack #denote the attack 
        

    #Change operator overloader to print the attack value.    
    def __str__(self):
        return "Name: " + self.name + "\nHP:" + str(self.hp) + "\nAttack: " + str(self.attack)  

    def Attack(self, other): #define the attack 
        other.hp-=random.randint(1,self.attack)

class Wizard(Character): #create a wizard class 
    def __init__(self, name, hp, attack, magic, **kwargs): #initialize 
        super().__init__(name, hp, magic) #use super to inherit traits from character
        self.magic = magic #denote magic
        self.max_hp = hp  #denote max hp 

    def heal(self): #define heal 
        self.heal = self.max_hp 

    def fireball(self, other): #define fireball 
        other.hp-=random.randint(1, self.magic)

#Test the code in a battle! 
if __name__=="__main__":
    print("Ready...Set...Fight!")
    weezle=Wizard('Weezle',200,5,500)
    grognak=Character('Grognak',250,300)
    print(weezle)
    print(grognak) 
    grognak.Attack(weezle) 
    weezle.fireball(grognak)
    print(grognak)
    weezle.heal()
    weezle.fireball(grognak)
    print(weezle)
    print(grognak)

##Set it so that it is a more equal fight
if __name__=="__main__":
    print("\nFair fight!")
    weezle=Wizard('Weezle',200,5,500)
    grognak=Character('Grognak',250,450)
    print(weezle)
    print(grognak)
    grognak.Attack(weezle)
    print(weezle)
    weezle.fireball(grognak)
    print(grognak)
    weezle.heal()
    weezle.fireball(grognak)
    print(weezle)
    print(grognak)


##have it stop when one character or the other reaches a hitpoint = 0
if __name__=="__main__":
    print("\nReady...Set...Fight!")
    weezle=Wizard('Weezle',200,5,500)
    grognak=Character('Grognak',250,300) 
    print(weezle)
    print(grognak)
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



