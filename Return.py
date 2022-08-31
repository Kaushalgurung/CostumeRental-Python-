import DateTime
import CostumeList
from CostumeList import *
costumes = parseFile('record.txt')


def returnCostume():
    """
    It creates and opens the created file, writes the details of returned costume to it, then closes it.
    """

    returned = False
    while (True):
        fullname = input("Enter the Name of the customer: ")
        if fullname.isalpha():
            break
        print("Please input alphabet only")

    returndcostume = "Returned by-"+fullname+".txt"
    file = open(returndcostume, "w+")
    file.write("\t\t\t\t\t\t\t\t\t\t\tCOSTUME RENTAL SERVICE")
    file.write("\n_________________________________________________________________________________________________________________________________________________________________")
    file.write("\n\t\t Client details and returned time.\n")
    file.write("\t\t Returned by: " + fullname + "\n")
    file.write("\t\t Date: " + DateTime.getDateTime()+"\n\n")
    file.write("\t\t Time: " + DateTime.getTime()+"\n\n")
    fmt = '{:<3} {:<20} {:<15} {:<10} {:<10} {:<5}'
    file.write(fmt.format("S.n", "Costume Name", "Brand Name",
               "Price", "Quantity", "Total-Price\n"))
    file.close()

    total = 0.0
    counter = 1
    totalfine = 0.0

    while returned == False:
        print("\nPlease select a option below:\n")
        printCostumes(costumes)

        a = int(input("Enter no. of costume to return:"))

        """Checking if the quantity of the costume is greater than 0. If it is, it will print the
            message and ask for the quantity of the costume. Then it will write the details of the
            costume to the file. """

        if (checkId(costumes, a)):
            #print("\nThe costume you've selected is in stock. You have returned one of them. \n")
            userQuantity = int(input("Enter quantity of costume:"))
            userDays = int(input("Enter number of rented days: "))
            file = open(returndcostume, "a")
            fmt = '{:<3} {:<20} {:<15} {:<10} {:<10} {:<5}'
            file.write(fmt.format(str(counter), CostumeList.costumeName[a], CostumeList.brandName[a], (
                "$"+CostumeList.price[a]), str(userQuantity), ("$" + str(userQuantity * int(CostumeList.price[a]))) + "\n"))
            file.close()
            counter += 1

            # calcuating total and adding fine
            if userDays > 5:
                4
            fine = (userDays - 5) * userQuantity * int(CostumeList.price[a])
            total = total+int(CostumeList.price[a].strip("$")) * userQuantity
            totalfine = total + fine

            # Adding returned costume to the record.
            CostumeList.quantity[a] = int(CostumeList.quantity[a])+userQuantity

            # updating original file
            file = open("record.txt", "w")
            file.write("")
            file.close()

            for i in range(3):
                file = open("record.txt", "a")
                file.write(CostumeList.costumeName[i]+","+CostumeList.brandName[i]+","+str(
                    CostumeList.quantity[i])+","+"$"+CostumeList.price[i]+"\n")

            file.close()

            # multiple costume returning code
            returnContinue = input("Return more? (y/n) ")

            if returnContinue.lower() == "n":
                print(
                    "\n-----------------------------------------------------------------")
                print("\t\tThe return invoice has been generated.")
                # console display
                print("\t\t\t\t\t\t\t\tCOSTUME RENTAL SERVICE")
                print("\n_____________________________________________________________________________________________________________________________")
                print("\n\t\t Client details and rented time\n")
                print("\t\t\tRented by: " + fullname + "\n")
                print("\t\t\tDate: " + DateTime.getDateTime()+"\n")
                print("\t\t\tTime: " + DateTime.getTime()+"\n\n")
                print("\n------------------------------------------------------------------------------------------------------------------------------")
                print(
                    "Costume Name \t\t Brand Name \t\t\t Price \t\t\t Quantity \t\t Total Price\n")
                print(CostumeList.costumeName[a]+" \t\t "+CostumeList.brandName[a]+" \t\t\t "+"$"+CostumeList.price[a] + "\t\t\t" + str(
                    userQuantity) + "\t\t\t" + "$" + str(userQuantity * int(CostumeList.price[a])) + "\n")
                print("\n`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                print("\n\t\t\t\t\t\t\t\t\tTotal: $" + str(total)+"\n")
                print("\n-------------------------------------------------------------------------------------------------------------------------")
                print("\nFINE AMOUNT: " + "$" + str(fine)+"\n")
                print("___________________________________________________________________________________________________________________________")
                print("\nTOTAL(with fine):" + str(totalfine))
                print("\n`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                print(
                    "\n\t\t\t\t\tTHANK YOU FOR YOUR TIME HERE.\nWE HOPE TO SEE YOU AGAIN \n HAVE A GREAT DAY!")
                print("\n-------------------------------------------------------------------------------------------------------------------------")

                returned = True
                break
            else:
                print("Returning more costume....")
        elif (checkId(costumes, a) == False):
            print("Please provide a valid Costume-Id")
        else:
            print("Costume can't be returned right now. Please wait for some time.")
            returned = False

    file = open(returndcostume, "a")
    file.write("\n`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
    file.write("\n\t\t\t\t\t\t\t\t\tTotal: $" + str(total)+"\n")
    if userDays > 5:
        file.write("Costume returned late. \t\t\t\t\t\t Fine is applied.\n")
        file.write("\t\t\t\tLate for: " + str(userDays-5)+" Days")
        file.write(
            "\n-------------------------------------------------------------------------------------------------------------------------")
        file.write("\nFINE AMOUNT: " + "$" + str(fine)+"\n")
        file.write(
            "___________________________________________________________________________________________________________________________")
        file.write("\nTOTAL(with fine):" + str(totalfine))
        file.write("\n___________________________________________________________________________________________________________________________")
        file.write(
            "\n\t\t\t\t\tTHANK YOU FOR YOUR TIME HERE.\nWE HOPE TO SEE YOU AGAIN \n HAVE A GREAT DAY!")
        file.write(
            "\n-------------------------------------------------------------------------------------------------------------------------")
        file.close()
    else:
        file.write("Costume returned on time.")
        file.write(
            "\n`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
        file.write(
            "\n\t\t\t\t\tTHANK YOU FOR YOUR TIME HERE.\n\t\t\t\t\tWE HOPE TO SEE YOU AGAIN \n\t\t\t\t\tHAVE A GREAT DAY!")
        file.write(
            "\n-------------------------------------------------------------------------------------------------------------------------")
        file.close()
