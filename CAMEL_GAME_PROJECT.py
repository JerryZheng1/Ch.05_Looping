'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random

#all the vairables set to 0 at the beginning of the game

done=False
miles_traveled_total=0
fuel=200
hunger=0
zombie_distance=-20
foodcans_left=10
miles_driven_inturn=0
tiredness=0
cans_gas_left=100
win=0
gas_station_found=0
foodcans_find=0
x=0
y=0
a=0
b=0

#introduction

print("\033[1;33;40mWhat difficulty would you like to play the game at?")
print("")
print("A.Easy\nB.Medium\nC.HARD")
diff=(input("\033[1;33;40m"))

if diff.lower()=="a":
    x=5
    y=10
    a=2
    b=2
elif diff.lower()=="b":
    x=10
    y=15
    a=3
    b=3
elif diff.lower()=="c":
    x=20
    y=25
    a=4
    b=4

print("\033[1;31;40mGo! Go! Go! The zombie horde is right behind us.")
print("Get into the truck, you have to outrun them.")
print("Drive through the city to the military base before the zombie reaches you.")
print("\033[1;31;40m")
print("")



while not done:
    if foodcans_find==1:
        print("\033[1;33;40mYou found 10 cans of food randomly on the streets")
        foodcans_left+=10
        foodcans_find=0


    if gas_station_found==1:
        print("")
        print("\033[1;33;40mYou found a empty gas station along the way!")
        print("You found 20 cans of food and refilled your truck")
        print("")
        fuel=200
        foodcans_left+=20
        gas_station_found=0
    if miles_traveled_total>200: #winning message
        win = 1
        done = True
        break

    if (miles_traveled_total-zombie_distance)>0 and (miles_traveled_total-zombie_distance)<15:
        print("\033[1;31;40mThe zombies are getting close!")
        print("")

    elif (miles_traveled_total-zombie_distance)<0:
        print("The zombies caught up!")
        print("")
        done = True
        break

    if not done and hunger > 15 and hunger <= 20: #died of hunger
        print("\033[1;31;40mYou are hungry!")
        print("")
    elif not done and hunger > 20:
        print("\033[1;31;40mYou died of hunger!")
        print("")
        done = True
        break

    if not done and fuel<=25 and fuel>0: #died of no fuel in truck
        print("\033[1;31;40mYou are getting low on gas.")
        print("")

    elif not done and done==True:
        break

    elif not done and fuel<=0:
        print("\033[1;31;40mYour car ran out of gas!")
        print("")
        done = True
        break

    if not done and tiredness > 15 and tiredness <= 20: #died of hunger
        print("\033[1;31;40mYou are tired!")
        print("")
    elif not done and tiredness > 20:
        print("\033[1;31;40mYou are too tired and died!")
        done = True
        print("")




    print("\033[1;32;40mChoose your options:")
    print("A: Refuel the truck")
    print("B: Move ahead at moderate speed")
    print("C: Move ahead at full speed")
    print("D: Stop to rest and eat")
    print("E. Attempt to find food")
    print("F: Status check")
    print("Q: Quit")
    print("")
    user_input=input("What is your option?")

    if user_input.upper()=="Q": #option quit
        win=2
        done=True


    elif user_input.upper()=="F": #option status
        print("")
        print("\033[1;37;40mStatus:")
        print("Miles driven:",miles_traveled_total)
        print("Food cans left:",foodcans_left)
        print("The Zombie Horde is",(miles_traveled_total-zombie_distance),"miles behind you")
        print("Gas left:",fuel,"gallons")
        print("Hunger Status:",hunger)
        print("Tiredness:",tiredness)
        print("Extra gas cans:",cans_gas_left,"gallons")
        print("")


    elif user_input.upper()=="D": #option rest, sets tiredness=0 and hunger = 0
        print("\033[1;35;40m")
        print("You stopped to eat and rest for an hour")
        print("")
        tiredness=0
        if foodcans_left>0:
            print("")
            hunger = 0
            foodcans_left-=3
            zombie_distance += random.randint(5, 15)
        else:
            print("You have no food left :(")
            zombie_distance += random.randint(5,15)


    elif user_input.upper()=="C": #move ahead at full speed
        print("\033[1;36;40m")
        miles_driven_inturn=0
        print("---------------------------------------------------------")
        print("You drove ahead at full speed")
        print("")
        miles_driven_inturn+=random.randint(15,25)
        hunger+=a
        tiredness+=b
        fuel-=(miles_driven_inturn)*(1.25)
        miles_traveled_total+=miles_driven_inturn
        print("You drive",miles_driven_inturn,"miles ahead")
        print("")
        print("In total, you have drove",miles_traveled_total,"miles")
        print("---------------------------------------------------------")
        gas_station_found= random.randint(0,20)
        zombie_distance += random.randint(x, y)


    elif user_input.upper()=="B": #move ahead at moderate speed
        print("\033[1;36;40m")
        miles_driven_inturn = 0
        print("---------------------------------------------------------")
        print("You drove ahead at moderate speed")
        print("")
        miles_driven_inturn += random.randint(15, 20)
        hunger += 1
        tiredness +=1
        fuel -= (miles_driven_inturn)
        miles_traveled_total += miles_driven_inturn
        print("You drive", miles_driven_inturn, "miles ahead")
        print("")
        print("In total, you have drove", miles_traveled_total, "miles")
        gas_station_found = random.randint(0, 20)
        print("---------------------------------------------------------")
        zombie_distance += random.randint(x, y)

    elif user_input.upper()=="E": #tries to find food
        print("\033[1;35;40m")
        foodcans_find = random.randint(0, 3)
        zombie_distance+=random.randint(x,y)
        if foodcans_find!=1:
            print("You found nothing")




    elif user_input.upper()=="A": #refuels the truck, adds 50 cans to the tank
        print("\033[1;35;40m")

        if cans_gas_left>0:
            print("You refilled your truck by 50 cans")
            print("")
            fuel+=50
            cans_gas_left-=50
        else:
            print("You have no extra gas cans left :(")
            zombie_distance +=random.randint(3,5)

    elif miles_traveled_total>200: #winning message
        win = 1
        done = True
        break




if win==1: #win message, where it detects win==1 to give message of winning
    print("\033[1;33;40mCongrats on getting to the military base")
    print("You feel safe knowing the military will protect you from the zombies")
    print("")
    print("")
    print("\033[1;34;40m5 Years later, with your help of killing zombies, the world has returned to normal")

elif win==2:
    print("\033[1;33;40mThanks for playing!")

else:
    print("\033[1;31;40mR.I.P")
    print("")
    print("")
    print("5 years later, the zombies takes over the world. Humans are now extinct.")
    print("\033[1;33;40mThanks for playing!")
