class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.relative_benefit = round(value/weight, 2)

    def __gt__(self, item):
        if self.relative_benefit == item.relative_benefit:
            return self.weight < item.weight
        return self.relative_benefit > item.relative_benefit

    def __eq__(self, item):
        return self.relative_benefit == item.relative_benefit and self.weight == item.weight

    def __repr__(self):
        return '<Item v:%i w:%i rb:%i>' % (self.value, self.weight, self.relative_benefit)

"""
Basic greedy multiple knapsacks algorithem
"""
def greedy_multiple_knapsacks(capacities, items):
    knapsacks = []  # list of m knapsacks 
    mkp = 0 #final value in the knapsack(s)
    
    for i in range(len(capacities)):
        knapsacks.append([]) #each knapsack gets a list for the items
    
    # Sorting list
    # First value in tuple is relativeBenefit whitch should be sorted highest
    # Second value is weight which should be sorted by lowest first (that's why we do -value)  
    items.sort(reverse=True)
   
    #each item is tried to fit in one knapsack
    #when the capacity of one knapsack is big enough - the item is put inside and is removed from the itemlist
    for _ in range(len(items)):
        current_item = items[0]
        for j in range(len(knapsacks)):
            if capacities[j] >= current_item.weight:
                knapsacks[j].append(current_item)
                capacities[j] -= current_item.weight
                mkp += items[0].value # total value in the bag(s)
                break                
        del items[0]
            
    #complete list of knapsacks content and final value
    return mkp, knapsacks

"""
Neighbouring algorithem
"""
def neighbouring_search(capacities, weights, benefits):
    resoult_value, result_knapsacks = greedy_multiple_knapsacks(capacities, weights, benefits)

#    while True:

    return resoult_value, result_knapsacks