from coffee_maker import CoffeeMaker

to_add = CoffeeMaker


class AddResources(CoffeeMaker):
    ''' Initialize the resources to refill'''
    def __init__(self):
        super().__init__()
        self.water = 0
        self.milk = 0
        self.coffee = 0

    def add_more_resources(self):
        '''Refills the machine with more resources'''
        self.water = int(input("How much water to add? (ml): "))
        self.milk = int(input("How much milk to add? (ml): "))
        self.coffee = int(input("How much coffee to add? (ml): "))
        to_add.modify_resources(self, self.water, self.milk, self.coffee)
        to_add.report(self)
