#Charactes class

class Character:
    def __init__(self, name='', hp=0, attack=0, wound=0, **kwargs):
        self.name = name
        self.hp = hp
        self._attack = attack
        self._wound = wound

    #Change operator overloader to print the attack value.
    
    def __str__(self):
        return "My name: "+self.name+" "+" \nHP: "+str(self.hp)+ "\nAttack:" + str(self._attack) + "\nWound:" + str(self._wound)
    
    def attack(self):
        return self._attack

    def wound(self):
        return self._wound

    def Attack(self, other):
        other.hp-=self._attack
        print(other.hp)
        
    #Another way to output data using the format function        
    def inspect(self): 
        print('Name {0.name} HP {0.hp} HP Attack {0.attack}'.format(self))


if __name__=="__main__":
    #test code
    ariana=Character('Ariana', 90,40,0)
    grognak=Character('Grognak', 100, 5000, armor='chainmail')
    mocha=Character('Mocha',100000,50000,armor='being cute')
    print(ariana) #what does this print?
    print(grognak)#how does this differ?
    print(grognak.attack())
    print(mocha)
    print(mocha.attack())
    mocha.Attack(grognak)


    
