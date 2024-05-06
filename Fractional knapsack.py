class Item:
 def __init__(self, value, weight):
    self.value = value
    self.weight = weight

# Main greedy function to solve problem
def fractionalKnapsack(W, arr):
 # sorting Item on basis of ratio
 arr.sort(key=lambda x: (x.value/x.weight), reverse=True)
 finalvalue = 0.0
# Looping through all Items
 for item in arr:
# If adding Item won't overflow, add it completely
    if item.weight <= W:
        W -= item.weight
        finalvalue += item.value
    else:
        finalvalue += item.value * W / item.weight
        break
 # Returning final value
 return finalvalue

