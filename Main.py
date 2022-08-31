import Return
import Rent
import CostumeList
from CostumeList import *

print("\t\t\t█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
print("\t\t\t█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█")
print("\t\t\t█░░║║║╠─║─║─║║║║║╠─░░█")
print("\t\t\t█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█")
print("\t\t\t█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")


continueLoop = True
while continueLoop == True:
  print("\nPlease choose an option which you are here for:" "\n")
  print("\n\t1. Enter 1: To rent costume.")
  print("\t2. Enter 2: To return costume.")
  print("\t3. Enter 3: To Exit the program." "\n")

  # This is a while loop that is checking if the user input is a number. If it is not a number, it
  # will ask the user to enter a number.
  userChoice = input("Enter choose an option:" )
  while True:
    try:
      userChoice = int(userChoice)
      if userChoice in [1,2,3]:
        break
      else:
        print("Enter from option only!")
        userChoice = input("Enter choose an option:" )
    except:
      print("Enter from option only!")
      userChoice = input("Enter choose an option:" )
  
      
  if userChoice == 1:
    print("You have choosed to rent costume." "\n")
    CostumeList.list()
    Rent.rentCostume()

  elif userChoice == 2:
    print("You have choosed to return costume." "\n")
    CostumeList.list()
    Return.returnCostume()


  elif userChoice == 3:
    print("Thank you for visiting. Hope to see you again. " "\n")
    continueLoop = False

  else:
    print("Invalid option entered!")
