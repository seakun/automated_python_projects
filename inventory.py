# invetory.py

def displayInventory(inventory):
    print("Inventory: ")
    sum = 0;
    for k, v in inventory.items():
        print(str(v) + " " + k)
        sum += v
    print("Total number of items:", sum)

def addToInventory(inventory, addedItems):
    for x in addedItems:
        if(inventory.get(x, 0) == 0):
            inventory[x] = 1
        else:
            inventory[x] += 1
    return inventory

#stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {'gold coin': 42, 'rope': 1}   

#displayInventory(stuff)
     
displayInventory(inv)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
