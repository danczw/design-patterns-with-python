# chain of responsibility method - behavioral design pattern
#   capable to rearrange the condition-action blocks dynamically at the run-time


# create base class
class Creature:
    def __init__(self, name, attack, defence):
        self.name = name
        self.attack = attack
        self.defence = defence

    def __str__(self):
        return f'{self.name}, ({self.attack}/{self.defence})' 


# create abstract handler class for chain of responsibility
# - decouples the coupling between sender and receiver objects
# - makes objects more flexible to implement, redesign and reuse
class CreatureModifier:
    """Abstract Handler"""
    def __init__(self, creature:Creature):
        self.creature = creature
        self.next_modifier = None
    
    """Method adding objects into the chain. """
    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    """Method to call objects in the chain. """
    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


class DoubleAttack(CreatureModifier):
    """Concrete Handlers"""
    def handle(self):
        print(f'Doubling {self.creature.name}\'s attack.')
        self.creature.attack *= 2
        super().handle()


class DoubleDefence(CreatureModifier):
    """Concrete Handlers"""
    def handle(self):
        print(f'Doubling {self.creature.name}\'s defence.')
        self.creature.defence *= 2
        super().handle()


# run method
if __name__ == '__main__':
    dragon = Creature('Dragon', 6, 4)
    print(dragon)
    
    """root is the client """
    root = CreatureModifier(dragon)

    root.add_modifier(DoubleAttack(dragon))
    root.add_modifier(DoubleDefence(dragon))

    root.handle()
    print(dragon)