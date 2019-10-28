# invetory.py

def displayInventory(inventory):
    print("Inventory: ")
    sum = 0;
    for k, v in inventory.items():
        print(str(v) + " " + k)
        sum += v
    print("Total number of items:", sum)

def addToInventory(inventory, addedItems):
    updatedInventory = inventory
    for x in addedItems:
        if(updatedInventory.get(x, 0) == 0):
            updatedInventory[x] = 1
        else:
            updatedInventory[x] += 1
    return updatedInventory

#stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {'gold coin': 42, 'rope': 1}   

#displayInventory(stuff)
     
displayInventory(inv)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
