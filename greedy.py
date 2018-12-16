def greedy_multiple_knapsacks(capacities, weights, benefits):
    numOfItems = len(weights) #number of passed items
    relativeBenefits = []  #list with items
    knapsacks = []  # list of m knapsacks 
    numOfKnap = len(capacities) # m
    mkp = 0 #final value in the knapsack(s)
    
    for i in range(numOfKnap):
        knapsacks.append([]) #each knapsack gets a list for the items
    
    #relative benefits are calculated
    for i in range(numOfItems):
        relativeBenefits.append((round(benefits[i]/weights[i],2), weights[i], benefits[i]))
    
    # Sorting list
    # First value in tuple is relativeBenefit whitch should be sorted highest
    # Second value is weight which should be sorted by lowest first (that's why we do -value)  
    relativeBenefits.sort(reverse=True, key=lambda tup:(tup[0], -tup[1]))  
   
    #each item is tried to fit in one knapsack
    #when the capacity of one knapsack is big enough - the item is put inside and is removed from the itemlist
    for _ in range(numOfItems):
        for j in range(len(knapsacks)):
            if capacities[j] > 0:
                if capacities[j] >= relativeBenefits[0][1]:
                    knapsacks[j].append(relativeBenefits[0])
                    capacities[j] -= relativeBenefits[0][1]
                    mkp +=  relativeBenefits[0][2]#total value in the bag(s)
                    break                
        del relativeBenefits[0]
            
    #complete list of knapsacks content and final value
    print (knapsacks)
    return mkp