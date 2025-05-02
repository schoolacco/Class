from game_objects import Player, Weapon, Enemy # MUST have this in the program
import random #For random damage and health
# Create an instance of Player
Characters = ['Gimili', 'Armand', 'Janna', 'Dante']
Weapons = ['Generic Sword', 'Generic Bow', 'Generic Battleaxe', 'Generic Scepter']
def select(List1, List2):
  print('Choose your hero from:')
  for item in List1:
    print(item)
  player_character = None    
  choice = input('').title()
  while choice not in List1 or player_character == None:
    if choice == 'Gimli':
      player_character = Player('Gimli', 'Dwarf', 'Fighter', 3, 180)
    elif choice == 'Armand':
      player_character = Player('Armand', 'Elf', 'Archer', 4, 120)
    elif choice == 'Janna':
      player_character = Player('Janna', 'Ogre', 'Brute', 6, 250)
    elif choice == 'Dante':
      player_character = Player('Dante', 'Human', 'Mystic', 10, 60)
    else:
      if choice not in List1:
        print('Choose from the above.')
        choice = input('').title()
  print(f"So you have chosen: {player_character.name}.")
  print('Now choose a weapon:')
  for item in List2: 
    print(item)
  player_weapon = None    
  choice = input('').title()    
  while choice not in List2 or player_weapon == None:
    if choice == 'Generic Sword':
      player_weapon = Weapon('Generic Sword', 'Melee', random.randint(12,15))
    elif choice == 'Generic Bow':
      player_weapon = Weapon('Generic Bow', 'Ranged', random.randint(10,12))
    elif choice == 'Generic Battleaxe':
      player_weapon = Weapon('Generic Battleaxe', 'Melee', random.randint(15,20))
    elif choice == 'Generic Scepter':
      player_weapon = Weapon('Generic Scepter', 'Mixed', random.randint(20,40))
    else:
      if choice not in List2:
        print('Choose from the above.')
        choice = input('').title()
  print(f'So you have chosen the {player_weapon.name}, do note that it is a {player_weapon.ctgy} weapon.')
  # TODO: Create an instance of Weapon with random damage between 12 and 15
  # TODO: Create an instance of Enemy with random damage between 15 and 18, and random health between 80 and 140
  enemy_character = Enemy('Dark Lord minion', 'Unknown', random.randint(15,18), random.randint(80,140))

  # Print the player character details
  print(f"Player Name: {player_character.name}")
  print(f"Player Race: {player_character.race}")
  print(f"Player Class: {player_character.cls}")
  print(f"Player Attack: {player_character.atk}")
  print(f"Player Health: {player_character.health}")
  
  # TODO: Print the player weapon details
  print(f"Weapon Name: {player_weapon.name}")
  print(f"Weapon Category: {player_weapon.ctgy}")
  print(f"Weapon Damage: {player_weapon.damage}")
  
  
  # TODO: Print the enemy character details
  print(f"Enemy Name: {enemy_character.name}")
  print(f"Enemy Race: {enemy_character.race}")
  print(f"Enemy Attack: {enemy_character.damage}")
  print(f"Enemy Health: {enemy_character.hp}")
select(Characters, Weapons)