from pakuri import *

class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.size = 0
        self.prisoners = []

    def get_size(self):
        return self.size
    
    def get_capacity(self):
        return self.capacity
    
    def get_species_array(self):
        if self.prisoners == []:
            return None
        else:
            return [each_pakuri.species for each_pakuri in self.prisoners]
        
    def get_stats(self, species):
        for each_pakuri in self.prisoners:
           if each_pakuri.species == species:
                stats = []
                stats.append(each_pakuri.get_attack())
                stats.append(each_pakuri.get_defense())
                stats.append(each_pakuri.get_speed())
                return stats
        return None

    
    def sort_pakuri(self):
        updated = []
        for f in sorted(self.prisoners, key=lambda x: x.species):
            new = Pakuri(f.species)
            updated.append(new)
        self.prisoners = updated
        return self.prisoners
            
    
    def add_pakuri(self, species):
        if self.size == self.capacity:
            return False
        for each_pakuri in self.prisoners:
            if each_pakuri.get_species() == species:
                return False
        self.prisoners.append(Pakuri(species))
        self.size += 1
        return True
    
    def evolve_species(self, species):
        for pakuri in self.prisoners:
            if pakuri.species == species:
                pakuri.evolve()
                return True
            else:
                continue
        return False