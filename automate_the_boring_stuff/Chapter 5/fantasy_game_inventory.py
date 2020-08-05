inventory1 = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inventory2 = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'dagger']


def display_inventory(inventory):
    item_total = 0
    print("Inventory:")
    for key, value in inventory.items():
        print(value, key)
        item_total += value
    print(f'Total number of items: {item_total}')


def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.setdefault(item, 1)


add_to_inventory(inventory2, dragon_loot)
display_inventory(inventory2)
