
###Let's transform this pseudocode into working Python code
###This is the Liquid class we brainstormed in lecture.
###How do we make it work? What is it missing?


class Liquid:
    vol=100
    color=''
    typ=''
    container=''

    def empty():
        vol=0

    def fill():
        vol=100


class Potion(Liquid):
    magic_type='fly'
    point=1000

#class Barrel(Liquid)

p1=Liquid()
print(p1.vol)
p1.empty()
#p2=Potion()
#print(p2.vol)
#print(p2.magic_type)
