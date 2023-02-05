# list of user options
options = [
  '1. Exchange',
  '2. Return'
]
# list of clothing options
clothes = [
  '1. Pants',
  '2. Shirts',
  '3. Shorts',
  '4. Hoodies',
  '5. Jackets'
]
'''
making an amount holder for the number pf items being 
returned or exchanged
'''


# making a def to check if the users info is correct
def return_Exchange(amount):
  pants = 0
  shirts = 0
  shorts = 0
  hoodies = 0
  jackets = 0 
  print(clothes)
  for i in range(amount):
    if opt == '1':
      opt2 = input('Alright what are you exchanging? \n')
    elif opt == '2':
      opt2 = input('Alright, what are you returning? \n')
      
    if opt2 == '1':
      pants += 1
    
    elif opt2 == '2':
      shirts += 1
    
    elif opt2 == '3':
      shorts += 1

    elif opt2 == '4':
      hoodies += 1
    
    elif opt2 == '5':
      jackets += 1
  if opt == '1':
    return f'Alright you are exchanging Pants: {pants}, Shirts: {shirts}, Shorts: {shorts}, Hoodies: {hoodies}, Jackets: {jackets}'
  elif opt == '2':
    return f'Alright you are returning Pants: {pants}, Shirts: {shirts}, Shorts: {shorts}, Hoodies: {hoodies}, Jackets: {jackets}'

print('Hello, what are you here for?')
print(options)
opt = input('')



# making responses to the users first option
while opt != 1 or opt != 2:
  if opt == '1':
    amount = int(input('How many items do you want to exchange?:'))
    print(return_Exchange(amount))
    break
  elif opt == '2':
    amount = int(input('How many items do you want to return?:'))
    print(return_Exchange(amount))
    break
  else:
    print("That isn't an option ")
    print()
    print('What are you here for?')
    print(options)
    opt = input('')
