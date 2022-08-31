import DateTime
import CostumeList
from CostumeList import *
costumes = parseFile('record.txt')


def rentCostume():
    """
    It creates and opens the created file, writes the details of rented costume to it, then closes it.
    """

    rented = False
    while (True):
        fullname = input("Enter the Name of the customer: ")
        if fullname.isalpha():
            break
        print("Please input alphabet only")

    rent = "Rent of-"+fullname+".txt"
    file = open(rent, "w+")
    file.write("\t\t\t\t\t\t\t\tCOSTUME RENTAL SERVICE")
    file.write("\n_____________________________________________________________________________________________________________________________")
    file.write("\n\t\t Client details and rented time\n")
    file.write("\t\t\tRented by: " + fullname + "\n")
    file.write("\t\t\tDate: " + DateTime.getDateTime()+"\n")
    file.write("\t\t\tTime: " + DateTime.getTime()+"\n\n")
    fmt = '{:<3} {:<20} {:<15} {:<10} {:<10} {:<5}'
    file.write(fmt.format("S.n", "Costume Name", "Brand Name",
               "Price",  "Quantity", "Total-Price\n"))
    file.close()

    total = 0.0
    counter = 1

    # A function that is used to rent a costume.
    while rented == False:
        print("\nPlease select a option below:\n")
        printCostumes(costumes)

        a = int(input("Enter ID of the Costume to rent:"))

        """Checking if the quantity of the costume is greater than 0. If it is, it will print the
            message and ask for the quantity of the costume. Then it will write the details of the
            costume to the file. """

        if (checkId(costumes, a)):
            costumeQuantity = int(input("Enter quantity of costume:"))
            if (checkQuantity(costumes, a, costumeQuantity)):
                print("\nThe costume you've selected is added for rent.\n")
                file = open(rent, "a")
                fmt = '{:<3} {:<20} {:<15} {:<10} {:<10} {:<5}'
                file.write(fmt.format(str(counter), CostumeList.costumeName[a], CostumeList.brandName[a], (
                    "$"+CostumeList.price[a]), str(costumeQuantity), ("$" + str(costumeQuantity * int(CostumeList.price[a]))) + "\n"))
                file.close()
                counter += 1
                # Removing rented costume from the records.
                CostumeList.quantity[a] = int(CostumeList.quantity[a])-costumeQuantity
                # calcuating total
                total = total + \
                    int(CostumeList.price[a].strip("$")) * costumeQuantity
                rented=True
            elif ((checkQuantity(costumes, a, costumeQuantity)==False)):
                print("The Entered quantity is greater than we have in stock.")
                rented=False

            # updating the data of the orginal costumes records file
            file = open("record.txt", "w")
            file.write("")
            file.close()

            for i in range(3):
                file = open("record.txt", "a")
                file.write(CostumeList.costumeName[i]+","+CostumeList.brandName[i]+","+str(
                    CostumeList.quantity[i])+","+"$"+CostumeList.price[i]+"\n")
            file.close()

            # code for renting multiple costume
            rentContinue = input("Want to rent more costume? (y/n) ")

            if rentContinue.lower() == "n":
                print("\n---------------------------------------------------------------------------------------------------")
                print("\t\tThe rent invoice has been generated.")
                print("\n---------------------------------------------------------------------------------------------------")
                # console display
                print("\t\t\t\t\t\t\t\tCOSTUME RENTAL SERVICE")
                print("\n_____________________________________________________________________________________________________________________________")
                print("\n\t\t Client details and rented time\n")
                print("\t\t\tRented by: " + fullname + "\n")
                print("\t\t\tDate: " + DateTime.getDateTime()+"\n")
                print("\t\t\tTime: " + DateTime.getTime()+"\n\n")
                print("-------------------------------------------------------------------------------------------------------------------------")
                print("Costume Name \t\t Brand Name \t\t\t Price \t\t\t Quantity \t\t Total Price\n")
                print(CostumeList.costumeName[a]+" \t\t "+CostumeList.brandName[a]+" \t\t\t "+"$"+CostumeList.price[a] + "\t\t\t" + str(costumeQuantity) + "\t\t\t" + "$" + str(costumeQuantity * int(CostumeList.price[a])) + "\n")
                print("\n-------------------------------------------------------------------------------------------------------------------------")
                print("\n\t\t\t\t\t\t\t\t\tTotal: $" + str(total))
                print("\n`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
                print("\n\t\t\t\t\tTHANK YOU FOR YOUR TIME HERE.\nWE HOPE TO SEE YOU AGAIN \n HAVE A GREAT DAY!")
                print("\n-------------------------------------------------------------------------------------------------------------------------")
                
                rented = True
                break
            else:
                print("Adding more costume for renting...")
        elif (checkId(costumes, a) == False):
            print("Please provide a valid Costume-ID")
        else:
            print("Costume is not available right now. Choose a diffrent costume.")
            rented = False

    file = open(rent, "a")
    file.write("\n-------------------------------------------------------------------------------------------------------------------------")
    file.write("\n\t\t\t\t\t\t\t\t\tTotal: $" + str(total))
    file.write("\n`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
    file.write(
        "\n\t\t\t\t\tTHANK YOU FOR YOUR TIME HERE.\nWE HOPE TO SEE YOU AGAIN \n HAVE A GREAT DAY!")
    file.write("\n-------------------------------------------------------------------------------------------------------------------------")
    file.close()
