# inventory.py
# Simple Yarn Inventory Tracker

inventory = {}

def add_yarn(name, quantity):
    if name in inventory:
        inventory[name] += quantity
    else:
        inventory[name] = quantity
    print(f"Added {quantity} units of {name}.")

def remove_yarn(name, quantity):
    if name in inventory and inventory[name] >= quantity:
        inventory[name] -= quantity
        print(f"Removed {quantity} units of {name}.")
    else:
        print(f"Not enough {name} in stock or item does not exist.")

def show_inventory():
    print("\nCurrent Inventory:")
    for name, quantity in inventory.items():
        print(f"{name}: {quantity} units")
    print("")

# Example usage
add_yarn("Cotton 30s", 100)
add_yarn("Polyester 50s", 50)
remove_yarn("Cotton 30s", 20)
show_inventory()
