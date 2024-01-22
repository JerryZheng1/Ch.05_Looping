# for i in range(1,11,):
#     print(i)
# print("This program takes three integers and returns the sum.")
# total = 0
# for i in range(3):
#     x = int(input("Enter a number: "))
#     total+=x
#
# print("The total is:", total)

# for i in range(2,102,2):
#     print(i)

# i=10
# while i>-1:
#     print(i)
#     i-=1
# print("Blast off!")

# import random
# my_number=random.randint(1,10)
# print(my_number)
#
# total=0
# positive=0
# negative=0
# zero=0
# for i in range(7):
#     input_number=float(input("Enter a number"))
#     total+=input_number
#     if input_number>0:
#         positive+=1
#     elif input_number==0:
#         zero+=1
#     else:
#         negative+=1
#
# print("you sum is:",total)
# print("You entered a total of",positive,"positive numbers")
# print("You entered a total of",negative,"negative numbers")
# print("You entered a total of",zero,"zeros")

# import random
# heads=0
# tails=0
# for i in range(50):
#     number=random.randint(0,1)
#     if number==1:
#         print("heads")
#         heads+=1
#     else:
#         print("tails")
#         tails+=1
# print("")
# print("TOTAL:")
# print("You got",heads,"heads")
# print("You got",tails,"tails")
#
# import random
# done = False
# user_input=0
# computer_input=0
# computer_score=0
# user_score=0
# tied_score=0
#
# print("ROSHAMBO PROGRAM V1.0")
# while not done:
#     print("")
#     user_input=int(input("Choose an option, 1 for rock, 2 for paper, 3 for scissors and 4 to quit."))
#     print("")
#     if user_input==4:
#         done = True
#     elif user_input==1 or user_input==2 or user_input==3:
#         if user_input==1:
#             print("You chose Rock")
#         elif user_input == 2:
#             print("You chose Paper")
#         else:
#             print("You chose Scissors")
#         computer_input=random.randint(1,3)
#         if computer_input==1:
#             print("Computer chooses Rock")
#         elif computer_input==2:
#             print("Computer chooses paper")
#         else:
#             print("Computer chooses scissors")
#         if computer_input==user_input:
#             print("It's a tie!")
#             tied_score+=1
#         elif user_input==1 and computer_input==2:
#             print("The Computer won! Paper > Rock")
#             computer_score+=1
#         elif user_input == 1 and computer_input == 3:
#             print("You won! Rock > Scissors")
#             user_score+=1
#         elif user_input == 2 and computer_input == 3:
#             print("The Computer won! Scissors > Paper")
#             computer_score += 1
#         elif user_input == 2 and computer_input == 1:
#             print("You won! Paper > Rock")
#             user_score+=1
#         elif user_input == 3 and computer_input == 1:
#             print("The Computer won! Rock > Scissors")
#             computer_score += 1
#         elif user_input == 3 and computer_input == 2:
#             print("You won! Scissors > Paper")
#             user_score += 1
#         else:
#             print("Hey that's not an option!")
#     else:
#         print("Hey that's not an option!")
# print("")
# print("YOUR FINAL SCORE")
# print("WINS:",user_score)
# print("LOSES:",computer_score)
# print("TIES:",tied_score)

# var = 0
#
# while var <=10:
#
#    var += 1
#
#    if var%2 != 0:
#         pass
#     print ('Current value :', var)
#
# print ("Good bye!")
var = 0

while var <=10:

   var += 1

   if var%2 != 0:

      pass

   print ('Current value :', var)

print ("Good bye!")