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
  pant = 20 * pants
  shirt = 30 * shirts
  short = 25 * shorts
  hood = 35 * hoodies
  jack = 35 * jackets
  total = pant + shirt + short + hood + jack
  
  if opt == '1':
    return f'Alright you are exchanging Pants: {pants}, Shirts: {shirts}, Shorts: {shorts}, Hoodies: {hoodies}, Jackets: {jackets}                                         That totals out to: ${total}'
  
  
  elif opt == '2':
    return f'Alright you are returning Pants: {pants}, Shirts: {shirts}, Shorts: {shorts}, Hoodies: {hoodies}, Jackets: {jackets}                                                  That totals out to: ${total}'

print('Hello, what are you here for?')
print(options)
opt = input('')
global total 

def exchange(newtotal):
  global total
  if opt == '1':
    if newtotal == total or newtotal < total:
      return 'Those items can be exchanged!'
    
    elif newtotal > total:
      return 'That exchange cannot be done '
      
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


if opt == '1':
  ask = input('How many weeks have you had these items?: \n')
  if ask > '2':
    print('You cannot return or exchange these items. Apologies')
  else:
    pants = 0
    shirts = 0
    shorts = 0
    hoodies = 0
    jackets = 0 
    print(clothes)
    
    for i in range(amount):
      exch = input('Choose your new items. \n')
      
      if exch == '1':
        pants += 1
      
      elif exch == '2':
        shirts += 1
      
      elif exch == '3':
        shorts += 1
  
      elif exch == '4':
        hoodies += 1
      
      elif exch == '5':
        jackets += 1
    pant = 20 * pants
    shirt = 30 * shirts
    short = 25 * shorts
    hood = 35 * hoodies
    jack = 35 * jackets
    newtotal = pant + shirt + short + hood + jack
    print(exchange(newtotal))
elif opt == '2':
  
  print(exchange(newtotal))