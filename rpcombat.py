__Version__ = 0.2

#import moduals at the top, always
import random

#setup constant data
#setup shop = {'item':(price, attack, speed,)}
stock = {'Sword':(10,40,25),
        'Mace':(15,45,40),
        'Ak47':(70,80,75),
        'Shield':(30,20,5),
        'Armour':(35,60,8),
        'Cuirass':(30,45,20),
        'Club':(15,30,30),
        'Rope':(10,5,70)}
armour_types = set(['Shield', 'Cuirass', 'Armour'])
#setup decriptive list
# hits = (), misses = (), damage_report = (), life_changing = ()
hits = ('hits', 'bash', 'whack')
misses = ('miss', 'near hit', 'no where close')
damage_report = ('small abrasion', 'just a flesh wound', 'holy hell')
life_changing = ('a scar', 'amputation', 'broken bones', 'gash', 'hole in the head')

#preferrnces
#set to true to trace variables
trace = False
max_players = 2

players = []

#dice roll simutator
def roll(sides, dice=1):
    result = 0
    for rolls in range(1,dice):
        result += random.randint(1,sides)
    return result
#generate characters
#1 loop while players < 2
while len(players) < max_players:
    print()
    print('New Character')
    print()
    #1.1 create profile dictionary
    profile = {'Name':'', 'Desc.':'',
    'Gender':'', 'Race':'', 'Life':0,
    'Brains':0, 'Speed':0,
    'Strenth':0, 'Charm':0,
    'Magic':0, 'Deff':0,
    'Gold':0, 'Inventory':[]}
    #1.2 prompt user for defined info
    #input(Name, Description, Gender, Race)
    name = input('What is your name? ')
    desc = input('Decribe your self: ')
    gender = input('What is your gender? (Male/Female/Unsure ) ')
    race = input('What Race are you? (Pixie/Vulcan/Troll/Elf) ')

    #1.3 validate user input
    profile['Name'] = name.capitalize()
    profile['Desc.'] = desc.capitalize()
    gender = gender.lower()
    if gender.startswith('f'):
        profile['Gender'] = 'Female'
    elif gender.startswith('m'):
        profile['Gender'] = 'Male'
    else:
        profile['Gender'] = 'Nuter'

    race = race.capitalize()
    if race.startswith('P'):
        profile['Race'] = 'Pixie'
    elif race.startswith('V'):
        profile['Race'] = 'Vulcan'
    elif race.startswith('T'):
        profile['Race'] = 'Troll'
    else:
        profile['Race'] = 'Elf'

    #1.4 generate stats (Strenth, Brains, Speed, Charm)
    profile['Strenth'] = roll(3,33)
    profile['Brains'] = roll(3,33)
    profile['Speed'] = roll(3,33)
    profile['Charm'] = roll(3,33)

    #1.5 work out combat stats (Life, Magic, Deff, Gold)
    #and modify based on user-defined info
    life = (profile['Strenth'] + (profile['Speed'] / 2)) + roll(9,49)
    magic = (profile['Brains'] + (profile['Charm'] / 2)) + roll(9,49)
    deff = (profile['Speed'] + (profile['Brains'] / 2)) + roll(9,49)
    gold = roll(9,49) * 3
    #1.6 Validate stats
    if life > 0 and life < 100:
        profile['Life'] = life
    else:
        profile['Life'] = roll(3,33)
    if magic > 0 and magic < 100:
        profile['Magic'] = magic
    else:
        profile['Magic'] = roll(3,33)
    if deff > 0 and deff < 100:
        profile['Deff'] = deff
    else:
        profile['Deff'] = roll(3,33)
    if gold > 10 and gold < 100:
        profile['Gold'] = gold
    else:
        profile['Gold'] = roll(3,33)

    #1.7 Output characher sheet
    fancy_line = '<============&==============>'
    print()
    print(fancy_line)
    print('\t', profile['Name'])
    print('\t', profile['Race'], profile['Gender'])
    print('\t', profile['Desc.'])
    print('\t', 'Strenth: ', profile['Strenth'], '\t', 'Life: ', profile['Life'])
    print('\t', 'Brains: ', profile['Brains'], '\t', 'Magic: ', profile['Magic'])
    print('\t', 'Speed: ', profile['Speed'], '\t', 'Deff: ', profile['Deff'])
    print('\t', 'Charm: ', profile['Charm'], '\t', 'Gold: ', profile['Gold'])

    #1.8 Prompt user to buy some equipment
    purchase = input('Would you like to buy equipment? ')
    #1.9 Loop while purchase not 'no'
    while purchase != 'Done':
        #1.9.1 Display Shop list with prices
        print()
        print('<<<<<<<<<SHOP>>>>>>>>>>>')
        for item in stock:
            print('\t', item, stock[item][0])
        print('>>>>>>>>>^^^^<<<<<<<<<<<')
        print()
        print('You have', profile['Gold'], 'Gold')
        #1.9.2 prompt user to make a purchase
        purchase = input('Please choose an item or type "done" to exit. ')
        purchase = purchase.capitalize()
        #1.9.3 if item is in stock and player has enough gold, buy it
        if purchase in stock:
            if stock[purchase][0] <= profile['Gold']:
                print('You bought a ', purchase, 'for ', stock[purchase][0], ' gold.')
                profile['Gold'] -= stock[purchase][0]
                profile['Inventory'].append(purchase)
                print('You have a', ' '.join(profile['Inventory']), ' in your bag!')
                print('You have ', profile['Gold'], ' gold left.')
            elif purchase == 'Done':
                break
            else:
                print('You dont have enough gold for that!')
        else:
            print([purchase], ' is out of stock.')
    print('You own a ', ''.join(profile['Inventory']))
    ##combat
    #2 prompt user to enter combat
    print(profile['Name'], ', are you ready for mortal combat?')
    #prompt user to choose a weapon
    weapon_stats = [stock[item] for item in profile['Inventory'] if item not in armour_types]
    if len(weapon_stats) == 1:
        profile['Weapon'] = weapon_stats[0]
        #default to 'fist' if no weapon is avalible
    elif len(weapon_stats) < 1:
        profile['Weapon'] = (0, 20, 50)
    else:
        weapon = input('What weapon will you choose? ')
        #weapon input validation
        weapon = weapon.capitalize()
    #the weapon must be in the players inventory
        if weapon in profile['Inventory']:
            profile['Weapon'] = stock[weapon]

    #see if player has any armour
    for armour_type in armour_types:
        if armour_type in profile['Inventory']:
            profile['Armour'] = stock[armour_type]
        else:
            profile['Armour'] = (0,0,20)

    print(profile['Name'], ' is now ready for Battle!')
        #1.10 add new player to list of players
    players.append(profile)
    ##Active Combat
print()
print('Then let the battle begin!')
print()

vel_max = 23
vel_min = 1
dam_max = 23
#3 Loop while attacker health > 0 and tharget health > 0
while players[0]['Life'] > 0 and players[1]['Life'] > 0:
    for attacker, player in enumerate(players):
        target = int(not bool(attacker))
        life_left = players[target]['Life']
        #3.1.1 calculate velocity of blow
        attack_speed = players[attacker]['Speed']
        weapon_speed = players[attacker]['Weapon'][2]
        attack_chance = roll(1,players[attacker]['Brains'])
        attack_velocity = attack_speed + weapon_speed + attack_chance
        target_defence = players[target]['Deff']
        armour_speed = players[target]['Armour'][2]
        target_velocity = target_defence + armour_speed
        velocity = (attack_velocity - target_velocity) / 2
        if trace:
            print('\t', velocity)
        if velocity > 0:
            if velocity > vel_max:
                vel_max = velocity
            hit_type = int(7 * velocity / vel_max)
            if hit_type > 7:
                hit_type = 7
            if trace:
                print('\t\t HIT', hit_type)
            print(players[attacker]['Name'], 'hits', players[target]['Name'])
        else:
            if velocity < vel_min:
                vel_min = velocity
            miss_type = int(velocity / vel_max)
            if miss_type > 7:
                miss_type = 7
            if trace:
                print('\t\tMISS', miss_type)
            print(players[attacker]['Name'], 'misses', players[target]['Name'])
            continue

        #3.1.2 calculate damage inflicted by blow
        attack_strength = players[attacker]['Strenth']
        weapon_damage = players[attacker]['Weapon'][1]
        attack_damage = attack_strength + weapon_damage + velocity
        target_strength = players[target]['Strenth']
        armour_strength = players[target]['Armour'][1]
        target_chance = roll(9,players[target]['Brains'])
        target_prot = target_strength + target_defence + target_chance
        potential_damage = (attack_damage - target_prot)
        if potential_damage < 1:
            potential_damage = 2
        damage = roll(1,potential_damage)
        if trace:
            print()
        print('\t\tDamage: ', damage)

        if damage > dam_max:
            dam_max = damage
        #3.1.3 print(damage_report)
        damage_type = int(7 * damage/dam_max)
        if damage_type > 7:
            damage_type = 7
        if trace:
            print('\t\tDamage!', damage_type)
        change_type = int(5 * damage/life_left)
        if change_type > 7:
            change_type = 7
        if trace:
            print('\t\t\t\tChange ', change_type)
        print('inflicted a blow')

        players[target]['Life'] -= damage
        #check if player is still alive
        if players[target]['Life'] <= 0:
            print()
            print(players[attacker]['Name'], ' is the winner!')
            break

if trace:
    print()
    print('\t\tMax ', dam_max, vel_max, ':: min ', vel_min)
    print()



        #3.1.4 if attacker health > 0 and target health > 0: break
        #3.2 print(progress_report)

    #4 print(winner)
