# # # # # First Example: Prints out death and then stops
# # # #
# # # # for letter in 'DEATH STAR':
# # # #
# # # #    if letter == '':
# # # #
# # # #       break
# # # #
# # # #    print ('Current Letter :', letter)
# # # #
# # # #
# # # #
# # # # # Second Example: Counts down from 10-6 but then stops.
# # # #
# # # # var = 10
# # # #
# # # # while var > 0:
# # # #
# # # #    print ('Current variable value :', var)
# # # #
# # # #    var = var -1
# # # #
# # # #    if var == 5:
# # # #
# # # #       break
# # # #
# # # # print ("Sorry, the Death Star shot early!")
# # #
# # # # First Example: Eliminates the space
# # #
# # # for letter in 'DEATH STAR':
# # #
# # #    if letter == ' ':
# # #
# # #       continue
# # #
# # #    print ('Current Letter :', letter)
# # # Second Example: prints even numbers up to 10
# #
# # var = 0
# #
# # while var <=10:
# #
# #    var = var+1
# #
# #      print ('Current value :', var)
# #
# # print ("Good bye!")
# # Second Example: prints even numbers up to 10
#
# var = 0
#
# while var <=10:
#
#    var = var+1
#
#    if var%2 != 0:
#
#       continue
#
#    print ('Current value :', var)
#
# print ("Good bye!")
var = 0

while var <=10:

   var += 1

   if var%2 != 0:

    pass

   print ('Current value :', var)

print ("Good bye!")