class AnimaliaKingdom:
    def eat(self):
        print('Oww, tasty')


class ChordataPhylum(AnimaliaKingdom):
    def sleep(self):
        print('Sleeping is good')


class ActinopterygiiClass(ChordataPhylum):
    def __init__(self):
        self.flipper1 = 'first flipper'
        self.flipper2 = 'second flipper'
        self.tail = 'tail'

    def swim(self):
        print(f'{self.flipper1} is moving')
        print(f'{self.flipper2} is moving')
        print(f'{self.tail} is moving')


class ClupeidaeFamily(ActinopterygiiClass):
    def __init__(self):
        ActinopterygiiClass.__init__(self)
        self.food_supply = []

    def add_to_food_supply(self, *new_food):
        self.food_supply.extend([*new_food])
        print('My food supply consists of', end=' ')
        print(*self.food_supply, sep=', ')


class AtlanticHerringSpecies(ClupeidaeFamily):
    def __init__(self):
        ClupeidaeFamily.__init__(self)

    def move_to_salted_water(self):
        self.swim()
        print('This water is salted enough. I will stay here')


class CyprinidaeFamily(ActinopterygiiClass):
    def escape_from_fishman(self):
        self.swim()
        print('Huh, I escaped safely')


class Bream(CyprinidaeFamily):
    def find_food(self):
        self.swim()
        print('I see food')
        self.eat()


Patrick = AtlanticHerringSpecies()
Sam = Bream()

Patrick.add_to_food_supply('bread', 'seaweed')
Patrick.move_to_salted_water()
print()
Sam.sleep()
Sam.find_food()
