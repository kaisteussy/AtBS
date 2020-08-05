import pyinputplus as pyip

sandwich = []
extras = []
price = 0
tax = 0

prices = {'Wheat': .5, 'White': .25, 'Sourdough': .75,                          # Bread
          'Chicken': 2, 'Turkey': 2.5, 'Ham': 2, 'Tofu': 2.5,                   # Protein
          'Cheddar': .5, 'Swiss': .5, 'Mozzarella': .75,                        # Cheese
          'Mayo': .25, 'Mustard': .25, 'Ketchup': .25,                          # Extras
          'Lettuce': .25, 'Tomato': .50, 'Cucumber': .50, 'Black Olives': .50}


print('Hi! Welcome to Sandwich Maker!')
bread = pyip.inputMenu(['Wheat', 'White', 'Sourdough'], numbered=True)
sandwich.append(bread)

protein = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], numbered=True)
sandwich.append(protein)

cheese = pyip.inputYesNo('Do you want cheese on your sandwich?\n')
if cheese == 'yes':
    cheeseType = pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], numbered=True)
    sandwich.append(cheeseType)

print('Would you like to add any extras?\n')
while True:
    extra = pyip.inputMenu(['Mayo', 'Mustard', 'Ketchup', 'Lettuce',
                            'Tomato', 'Cucumber', 'Black Olives', 'No'], numbered=True)
    if extra == 'No':
        break
    sandwich.append(extra)
    print(f'Added {extra}, would you like anything else?')

quantity = pyip.inputInt('How many sandwiches would you like? ', min=1)


print('\nGenerating recept: ')
for item in sandwich:
    print(f'{item}: {prices[item]}')
    price += prices[item]

price = price * quantity
tax = price * .08
price = price + tax

print(f'Quantity: {quantity}')
print(f'Tax: {tax}')
print(f'Your total will be: ${price}')

