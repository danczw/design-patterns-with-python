# facade method - structural design pattern
#   provides simpler unified interface to a more complex system -> allows an
#   easier way to access methods of the underlying system by providing a
#   single entry point

import random


# create "complex" system
class Hawk:
    def __init__(self):
        self.asset = '(`A´)'
        self.alive = True
        self.reproducing = False
    
    def move(self) -> str:
        return 'deflect'
    
    def reproduce(self) -> object:
        return Hawk()
    
    def __str__(self):
        return self.asset
    
class Dove:
    def __init__(self):
        self.asset = '(๑•́ω•̀)'
        self.alive = True
        self.reproducing = False
    
    def move(self) -> str:
        return 'cooperate'
    
    def reproduce(self) -> object:
        return Dove()
    
    def __str__(self):
        return self.asset
        
def iteration(specimen: list) -> list:
    half = len(specimen)//2
    spec1 = specimen[:half]
    spec2 = specimen[half:]
    
    for s1, s2 in zip(spec1, spec2):
        move1 = s1.move()
        move2 = s2.move()
        
        if move1 == 'cooperate':
            # both survive, neither reproduce
            if move2 == 'cooperate':
                pass
            # s1 dies, s2 reproduces
            elif move2 == 'deflect':
                s1.alive = False
                s2.reproducing = True
        elif move1 == 'deflect':
            # s2 dies, s1 reproduces
            if move2 == 'cooperate':
                s2.alive = False
                s1.reproducing = True
            # both die
            elif move2 == 'deflect':
                s1.alive = False
                s2.alive = False
                
    s = spec1 + spec2
    s = [x for x in s if x.alive == True]
    
    for spec in s:
        if spec.reproducing == True:
            s.append(spec.reproduce())
            spec.reproducing = False
                
    return s


# create facade
class Simulation:
    def __init__(self, hawk_number, dove_number):
        self.population = []
        for _ in range(hawk_number):
            self.population.append(Hawk())
        for _ in range(dove_number):
            self.population.append(Dove())
        random.shuffle(self.population)
            
    def iterate(self):
        self.population = iteration(self.population)
        random.shuffle(self.population)
        
    def get_assets(self):
        return [str(x) for x in self.population]
    

# run method
if __name__ == '__main__':
    sim = Simulation(10, 10)
    for _ in range(3):
        sim.iterate()
        print(sim.get_assets())