#Equipment class

class Equipment:

    def __init__(self, equipment=None, inventory=None):
        self.equipment = equipment or []
        self.inventory = inventory or []

    def collect(self, item):
        self.inventory.append(item)


if __name__=="__main__":
    #test code
    t=Equipment()
    t.collect('sword')
    print(t.inventory)
