from sys import exit
import random
# import highscore.py 

# Title of Game/Intro
def intro():
	print("\n\n")
	print("*" * 25)
	print("Escape from Buffalo.")
	print("A Vaguely Autobiographical Zombie Apocalypse Game.")
	print("By Nick and Vera")
	# print("Note: At any time type 'status' for the stuff you have and amount of money in your wallet.\n")
	print("*" * 25)
	print("\n")
	pause()
	
def pause():
	print("[Press enter to continue]")
	choice = input("> ")

# Variable and list start points. $200 in your wallet and no inventory, start with an empty list
wallet = 200
rocks = 0
xp = 0
nanas_wallet = 100
inventory_items = []
monicafood = 4
thirsty = 1
nana_cheat_code = 1

# Declaring Stuff so I don't get an Unbound Local Error
nana_visited = False
zombies_have_begun = True
	
# Status updates in any room
def score():
	print("*" * 25)
	print(f"Wallet has ${wallet}")
	print(f"Inventory: {inventory_items}")
	print(f"XP: {xp}")
	print(f"Rocks: {rocks}")
	print("*" * 25)

# Buy Items
def make_purchase(item, item_value):
	global wallet
	if int(wallet) >= int(item_value):
		inventory_items.append(item)
		wallet = int(wallet) - int(item_value)
		print(f"You now have ${wallet} left in your wallet, and {inventory_items} in your stuff.")
	else:
		print(f"Sorry, ${wallet} is not enough to buy a {item}")  
		
# Attack the zombies
# Hands ~50% chance
# Slingshot ~75% chance
def attack(weapon):
	dieroll = (random.randint(1, 20))
	global xp
	global rocks
	print(dieroll)
	print(f"You rolled a \a{dieroll}/20")
	pause()
	
	if weapon == "hands" and dieroll >= 10:
		print("You defeat the zombie.") 
		xp = xp + 10
		zombiecoins()
		score()
	elif weapon == "hands" and dieroll < 10:
		dead("Sorry, your attack fails. The zombie eats your brain.")
	elif "slingshot" in inventory_items:
		if weapon == "slingshot" and rocks > 0 and dieroll >= 5:
			print("You defeat the zombie.") 
			xp = xp + 10
			rocks = rocks - 1
			zombiecoins()
			score()
		elif weapon == "slingshot" and rocks > 0 and dieroll < 5:
			dead("Sorry, your slingshot breaks. The zombie eats your brain.")
		elif weapon == "slingshot" and rocks == 0:
			dead("You don't have rocks for your slingshot. You toss the slingshot at the zombie, but it misses. The Zombie captures you.")
	elif dieroll >= 10:
		print("You defeat the zombie.") 
		xp = xp + 10
		zombiecoins()
		score()
	elif dieroll < 10:
		dead("Sorry, your attack fails. The zombie eats your brain.")

# Zombie defeat coins earned
def zombiecoins():
	dieroll = (random.randint(1, 10))
	global wallet
	print(f"You found \a{dieroll} dollars on the zombie's corpse, and add it to your wallet.")
	wallet += dieroll


# END GAME / ESCAPE SEQUENCES	
		
def win(why):
		print(why)
		print("*" * 25)
		print("Congratulation you win the game!")
		print("YOU ESCAPED FROM BUFFALO!")
#		score()
# WOULDN'T IT BE COOL TO ADD IN A HIGH SCORE FEATURE VIA WRITING TO A FILE?
		print("*" * 25)
		exit(0)
		
def dead(why):
	print(why)
	print("\u2620" * 25)
	print("Game Over!")
	print("\u2620" * 25)
	exit(0)
	
	
	
	
		
# ROOMS
#############
# ART STORE #
#############
def artstore():
	print(f"""
################
#  ART STORE   #
################""")
	print("Welcome to the art store. Would you like to buy paint for $15?")
	choice = input("> ")
	
	global wallet
	if "y" in choice:
		make_purchase("paint", 15)
		score()
	elif "n" in choice:
		print(f"Good idea to save your money. You have ${wallet} in your wallet.")

	print("\nThe art store worker accidentally mixes paint with radioactive stuff like polonium and uranium. This creates an apocalypse of zombies. Their goal is to turn everyone else into zombies and collect precious artifacts from Buffalo and...")
	print("TAKE OVER THE WORLD!\n")
	print("The cashier is now a zombie and shuffles towards you menacingly. What do you do?")
	print("hints: *run away*, *attack*, *throw paint*")
	zombies_have_begun = True
	 
	choice = input("> ")
	if choice == "run away":
		nanas_house()
	elif choice == "attack":
		print("You chose to attack. There's a 50% chance this will succeed. Rolling the computer 20-sided die now.")
		attack("hands")
		print("You book it to Nana's house")
		pause()
		nanas_house()
	elif choice == "throw paint":
		print("The zombie is now covered in drippy rainbow paint and blinded. It slips on the ground and you live to escape from Buffalo another day. You hop in the car and drive to Nana's")
		global xp
		xp = xp + 5
		pause()
		print("Good move, you earn 5 XP for escaping the zombie.")
		score()
		nanas_house()	
	else:
		print("I don't quite understand, but your feet do, and run you to the car.")
		nanas_house()
			
			
			
			
			
			
			
			
################
# NANA's HOUSE #
################
def nanas_house():
	print(f"""
################
# NANA's HOUSE #
################""")
	print("Welcome to Nana's house. She gives you a big hug and says hello.")
	
# Fixing some local variable errors here by making them global variables, is the best way to do it?
	global nanas_wallet
	global wallet
	global xp
	global thirsty
	global nana_cheat_code
# Haha, Grandma gives you $20 each time you visit. But she only has $100 total!
	if nanas_wallet > 0:
		print("Nana slips you a $20 bill.")	
		wallet = wallet + 20
		nanas_wallet = nanas_wallet - 20
		print(f"You now have ${wallet} in your wallet")
	
#		print = ("'The zombie apocolypse has begun. Luckily your grandpa has a generator in case we lose power.'")	
	
# Water trap. Lookup Love Canal and how polluted the watershed is in the Buffalo region.	
	if thirsty > 0:
		print("You're very thirsty, would you like to drink the tap water? (Y/N)")
		choice = input("> ")
	
		if "y" in choice:
			dead("You drink the tap water, which is quite polluted in Buffalo, you become sick and don't recover.")
		elif "n" in choice:
			print(f"Good idea, you should wait to get bottled water.")
		elif choice == "c" and nana_cheat_code > 0:
			print(f"Sneaky! You discovered the +20 XP cheat code!")
			xp += 20
			nana_cheat_code -= 1
			score()
				
		if 'water bottle' in inventory_items:
			print("Drink from your water bottle instead?")
			print("Y/N?")
			choice = input("> ")
	
			if choice == "y":
				print("The pure, spring water quenches your thirst. Good news, you get 10xp!")
				inventory_items.remove('water bottle')
				xp = xp + 10
				score()
				thirsty = 0
			elif choice == "n":
				print("You go thirsty...again.")

# Next room options		
	print("\nWhere do you want to go next? [Target, Monica's, the Rock Farm, or to the Airport]")
	choice = input("> ")
	
	if "target" in choice:
		target()
	elif "moni" in choice:
		monicas_house()
	elif "art" in choice:
		artstore()
	elif "train" in choice:
		start()
	elif "rock" in choice:
		rock_farm()
	elif "airport" in choice:
		airport()
	else:
		dead("A zombie bursts through the window with an ear-shattering crash. It knocks over the house plants on the way in and devours everyone.")
		
		
		
		
		
		
################
# TARGET       #
################
def target():
	print(f"""
################
#    TARGET    #
################""")
	print("You arrive at Target, luckily the zombies haven't arrived yet, but people have purchased nearly everything in the store.")
	print("A *water bottle* for $1 and a *slingshot* for $50.")
	print("What would you like to buy?")
	
	choice = input("> ")
	if "water" in choice:
		make_purchase('water bottle', 1)
		score()
	elif "slingshot" in choice:
		make_purchase('slingshot', 50)
		score()
	elif "both" in choice:
		make_purchase('slingshot', 50)
		make_purchase('water bottle', 1)
		score()
		
	pause()
	print("The windows shatter and zombies break in.")
	print("You flee! Do you want to go back to Nana's house, the rock farm, or Monica's house?")
	print("[nanas, rock farm, monica's?]")
	choice = input("> ")
	if "target" in choice:
		target()
	elif "monica" in choice:
		monicas_house()
	elif "rock" in choice:
		rock_farm()
	elif "nana" in choice:
		nanas_house()
	else:
		dead("Sorry, that's not an option. As the zombies rush through the store, they get you. There is no escape from Buffalo. [EVIL LAUGH] WAHAHAHAHAHAHA")
	




################
# ROCK FARM    #
################
def rock_farm():
	print(f"""
################
#  ROCK FARM   #
################""")
	global rocks
	global xp
	print("Just out of town, the quarry!")
	print("Fossil hunting in the shale is not for today.")
	print("Would you like to buy some rocks that happen to fit perfectly into a slingshot, 10 for $10?")
	print("[Y/N?]")
	choice = input("> ")
	if "y" in choice: 
		make_purchase('rocks', 10)
		rocks = rocks + 10
		score()
	elif "n" in choice: 
		print("OK, no rocks for you.")
	else:
		dead("A zombie sneaks up from behind and chews on your legs.")
# Zombie attack
	print("A Zombie attacks!!!!!")
	print("hints: *run away*, *attack* with hands, use *slingshot*")
	 
	choice = input("> ")
	if choice == "run away":
		nanas_house()
	elif "attack" in choice:
		print("You chose to attack. There's a 50% chance this will succeed. Rolling the computer 20-sided die now.")
		attack("hands")
		pause()
	elif "hand" in choice:
		print("You chose to attack. There's a 50% chance this will succeed. Rolling the computer 20-sided die now.")
		attack("hands")
		pause()
	elif "sling" in choice:
		print("You chose to attack. There's a 75% chance this will succeed. Rolling the computer 20-sided die now.")
		attack("slingshot")
		pause()
	elif "run" in choice: 
		print("You run away")
	else:
		dead("The zombie dines well tonight.")
	
#Next Move
	print("Where to next?")
	print("[nanas, target]")
	choice = input("> ")
	if "target" in choice:
		target()
	elif "nana" in choice:
		nanas_house()
#special zombie battle "cheat code" to attack zombies as long as you want.
	elif "zom" in choice:
		zombie_party()
	else:
		dead("What were you thinking? More zombies arise out of the gravel and drag yoy down under the ground.")
	

################
# ZOMBIE XP WAR   #
################
def zombie_party():
	print(f"""
################
#  ZOMBIE PARTY  #
################""")

	global rocks
	global xp
	print("You head to another area of the quarry, the Zombie Party. Here you can attack zombies as long as you like, or until you meet your untimely fate and fail in your quest to ESCAPE FROM BUFFALO!!!")
	zombie_war = 1
	
	while zombie_war > 0:	
		print("There are hundreds, no thousands of zombies. Would you like to attack?")
		print("[Y/N?]")
		choice = input("> ")
	
		if "y" in choice: 
			print("Get ready to rumble.")
		else:
			print("OK, back to the Rock Farm.")
			zombie_war -=1
			rock_farm()
		
	# Zombie attack

		print("A Zombie stands before you.")
		print("*attack* with hands or *slingshot*?")
		choice = input("> ")
		
		if "attack" in choice:
			print("You chose to attack. There's a 50% chance this will succeed. Rolling the computer 20-sided die now.")
			attack("hands")
			pause()
		if "hand" in choice:
			print("You chose to attack. There's a 50% chance this will succeed. Rolling the computer 20-sided die now.")
			attack("hands")
			pause()
		elif "sling" in choice:
			print("You chose to attack. There's a 75% chance this will succeed. Rolling the computer 20-sided die now.")
			attack("slingshot")
			pause()
		else:
			dead("The zombie eats you, starting with your toes, it tickles, who knew it would?")
	

	

	

##################
# MONICA'S HOUSE #
##################
def monicas_house():
	print(f"""
####################
#  Monica's House  #
####################""")

	global xp
	global monicafood
	
	print("Monica says, 'Hello, it's so good to see you. My house is a respite from the zombie apocalypse!")
	
	# Eat food for XP, max of 4 times
	if monicafood > 0:
		print("Would you like some food? [Y/N]")
		choice = input("> ")
		if "y" in choice:
			print("Yum, you've been chased by zombies so long you didn't realize how hungry you were. +10 xp points for you.")
			xp = xp + 10
			score()
		elif "n" in choice:
			print("suit yourself")		
		monicafood = monicafood - 1

	
	# Where to go?	
	print("You look around Monica's house and notice some stairs leading up the attic.")
	print("What would you like to do?")
	print("[hint: go up the stairs to the *attic*, *nanas*, try to escape buffalo on the *highway*, or go to the *broadway market*]")
	
	choice = input("> ")
	if "attic" in choice:
		attic()
	elif "highway" in choice:
		highwaytohell()
	elif "broadway market" in choice:
		broadway_market()
	elif "nana" in choice:
		nanas_house()
	else:
		dead("Not safe here after all, a zombie gets you.")
	



	
#########
# Attic #
#########
def attic():
	print(f"""
#########
# Attic #
#########""")
	global xp
	print("You climb up the creaky stairs to the attic. Sunlight filters through the dust.")
	
	if "toy car" not in inventory_items:
		print("On the ground you see a peculiar toy car, would you like to take it?")
		choice = input("[Y/N?]")
	
		if "y" in choice:
			make_purchase('toy car', 0)
			xp += 10
			print("You take the car and earn 10 XP. Good job!")
			score()
		if "n" in choice:
			print("You pick up the car, look at it, and decide to leave it to gather dust.")
	
	pause()
	print("You walk back down the stairs and see Monica in her kitchen.")
	monicas_house()
	
		
#########
# Highway #
#########
def highwaytohell():
	print(f"""
###########
# Highway #
###########""")
	global win
	print("You are trying to escape from Buffalo by car. Will it work?")
	score()
	print("zombies and shells of cars litter the streets. You step on the gas...")
	if xp > 100:
		pause()
		win("You have enough xp to make it out of Buffalo!!!! Zombies will not eat you today!")
	elif 'toy car' in inventory_items:
		pause()
		win("The toy car you picked up turns into a car that can change from an airplane to a train to a car and shoes that can be a scooter jetpack skateboard roller blades and ice skates and you escape!")
	else:
		dead("A zombie dragon swoops down and slime roasts the car. [hint: next time get more XP or there's something else...]") 
		
		
###################
# Broadway Market #
###################
def broadway_market():
	print(f"""
###################
# Broadway Market #
###################""")

	print("You drive to the Broadway Market, Buffalo's historic Polish bazaar. The place is swarming with zombies, however, a pierogi shop is open and a vendor selling wooden easter eggs.")
	print("Would you like to buy *pierogi* for $10, buy a hand painted wooden easter *egg* for $5, or *leave*?")
	choice = input("> ")
	
	# buy stuff	
	if "pierogi" in choice:
		make_purchase("pierogi", 10)
		score()
	elif "egg" in choice:
		make_purchase("egg", 5)
		score()

	# zombie attack
	print("A group of a dozen zombies approach. You must make a choice.")
	print ("[*flee*/*attack*/*slingshot* [if you have one]")
	choice = input("> ")
	
	if "flee" in choice:
		dead("You just can't outrun this pack of zombies.")
	if "run" in choice:
		print("How did you invade those zombies? Instinct? Anyway, you survive, but you still must escape from Buffalo.")
	elif "atta" in choice:
		print("You chose to attack. There's a 50% chance this will succeed. Rolling the computer 20-sided die now.")
		attack("hands")
		pause()
	elif "sling" in choice:
		print("You chose to attack. There's a 75% chance this will succeed. Rolling the computer 20-sided die now.")
		attack('slingshot')
		pause()
	else:
		dead("Sorry.")		

	# go places
	print("Phew, zombies are so annoying.")
	print("It's time to leave the Broadway Market. Where to?")
	choice = input("[monicas, nanas, rock_farm]")
	if "nana" in choice:
		nanas_house()
	elif "highway" in choice:
		highwaytohell()
	elif "moni" in choice:
		monicas_house()
	elif "rock" in choice:
		rock_farm()
	else:
		print("For no good reason, you are transported back to the train station")
		pause()
		start()
	
	
			
#######################
# BLIZZARD / AIRPORT  #
#######################
def airport():
	print(f"""
###########
# Airport #
###########""")

	print("On the drive to the airport a BLIZZARD BEGINS!")
	print("This is pretty scary. Do you want to continue driving to the Buffalo International airport?")
	choice = input("[Y/N?]")
	
	if "n" in choice:
		print("You turn around and head back to Nana's")
		nanas_house()
	
	print("Grandpa drops you off at the airport. As soon as his car pulls out a zombie jumps in and eats him. Guess if this plane doesn't work out you have to take a taxi.")
	print("You walk into the airport and walk over to the counter to buy a ticket to NYC, where there's absolutely no chance there are any zombies. None. Really.")
	pause()
	print("The travel agent says, 'A ticket to NYC is $200', would you like to buy it?")
	choice = input("[Y/N?]")
	
	if "y" in choice:
		make_purchase('plane ticket', 200)
	elif "n" in choice:
		print("You walk back to the passenger drop off zone, and wait for a taxi to take you back to Nana's.")
		dead("A zombie gets you. You were so close to escaping Buffalo.")
		
	if 'plane ticket' in inventory_items:
		print("You walk to security.")
		print("The TSA agent says, the only way to pass is to have 100 xp. Do you have this?")
		pause()
		score()
		if xp >= 100:
			win("YAY! YOU BOARD YOUR FLIGHT!")
		else:
			dead("You were so close. You may have guessed by now, a zombie busts out of a pretzel shop and devours everyone.")	
	else:
		dead("Thanks for playing, but you become a zombie snack. Buffalo stinks.")	
	
		

	
	
#######################
# TRAIN STATION       #
#######################	
# Starting at the Train Station
def start():
	print(f"""
You arrive at the train station in Buffalo and walk off the train, suitcase in hand.
You shiver.
The air is cold and the sky is foreboding.
You pick up your phone and call Grandpa to come pick you up in his car. 

He arrives and asks, 
'Do you want to go to straight to Nana's house or would you like to stop at the art store first?'

What is your choice? [art store/nanas]
	""")
	
	choice = input("> ")

	if "art" in choice:
		artstore()
	elif "nana" in choice:
		nanas_house()
	else:
		dead("Bad choice, you're attacked by a zombie.")
		
# End functions

# Begin Game
intro()		
start()
	