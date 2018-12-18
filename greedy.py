"""
Basic value holder for item
"""
class Item:
    def __init__(self, value: int, weight: int, position: int):
        self.value = value
        self.weight = weight
        self.position = position
        self.relative_benefit = round(value/weight, 2)

    def __gt__(self, item):
        if self.relative_benefit == item.relative_benefit:
            return self.weight < item.weight
        return self.relative_benefit > item.relative_benefit

    def __eq__(self, item):
        return self.relative_benefit == item.relative_benefit and self.weight == item.weight

    def __repr__(self):
        return '<Item v:{value} w:{weight} rb:{relative_benefit}>'.format(
            value=self.value, weight=self.weight, relative_benefit=self.relative_benefit)

"""
Basic Knapsack thingy
"""
class Knapsack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def add_item(self, item: Item):
        # If we can't add it, return False
        if self.capacity < item.weight:
            return False
        
        # Else add it and return True
        self.items.append(item)
        self.capacity -= item.weight
        return True

    def remove_item(self, index: int):
        self.capacity += self.items[index].weight
        del self.items[index]

    @property
    def value(self):
        return sum([item.value for item in self.items])

    def __repr__(self):
        return '<Knapsack v:{value} c:{capacity} i:{items}>'.format(value=self.value, capacity=self.capacity, items=self.items)

"""
Basic greedy multiple knapsacks algorithem
"""
def greedy_multiple_knapsacks(capacities, items):
    knapsacks = []  # list of m knapsacks 
    mkp = 0 #final value in the knapsack(s)
    
    for capacity in capacities:
        knapsacks.append(Knapsack(capacity)) #each knapsack gets a list for the items
    
    # Sort the items 
    items.sort(reverse=True)
   
    # each item is tried to fit in an knapsack
    # when the capacity of one knapsack is big enough - the item is put inside and is removed from the items
    for _ in range(len(items)):
        current_item = items[0]
        for knapsack in knapsacks:
            if knapsack.add_item(current_item):
                mkp += current_item.value # total value in the bag(s)
                break
        del items[0]

    #complete list of knapsacks content and final value
    return mkp, knapsacks
