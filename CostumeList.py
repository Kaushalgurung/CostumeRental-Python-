costumeName = []
brandName = []
quantity = []
price = []


def list():
    """
    It reads the file, splits the lines into a list, and then splits each line into a list of strings.
    """
    file=open("record.txt","r")
    lines=file.readlines()
    lines=[a.strip('\n') for a in lines]
    for i in range(len(lines)):
        x = 0
        for j in lines[i].split(','):
            if(x==0):
                costumeName.append(j)
            elif(x==1):
                brandName.append(j)
            elif(x==2):
                quantity.append(j)
            elif(x==3):
                price.append(j.strip("$"))
            x+=1


# The Costume class is a blueprint for creating objects that represent a costume.
class Costume:
    def __init__(self,id,  name, brand, quantity, price):
        self.id = id
        self.name = name
        self.brand = brand 
        self.quantity = quantity
        self.price =price 

def parseFile(filename):
    """
    It reads a file and returns a list of Costume objects
    
    :param filename: the name of the file to be parsed
    :return: A list of Costume objects.
    """
    costumes = []
    with open(filename) as file:
        contents = file.readlines()
        for line in contents:
            info = line[:-1].split(',')
            costume = Costume(len(costumes), info[0], info[1], int(info[2]), info[3])
            costumes.append(costume)
    return costumes

def printCostumes(costumes):
    """
    The above function prints the costumes in a table format.
    
    :param costumes: list of Costume objects
    """
    fmt = '{:<3} {:<20} {:<15} {:<10} {:<4}'

    print("---------------------------------------------------------------------")
    print(fmt.format("ID", "Costume Name", "Costume Brand", "Quantity", "Price"))
    print("---------------------------------------------------------------------")
    for c in costumes:
        print(fmt.format(c.id, c.name, c.brand, c.quantity,  c.price))
    print("---------------------------------------------------------------------\n")

def displayCostumes(costumes):
    """
    It takes a list of costumes and prints them out in a nice format.
    
    :param costumes: a list of Costume objects
    """
    fmt = '{:<3} {:<20} {:<15} '

    print("-------------------------------------------------")
    print(fmt.format("ID", "Costume Name", "Costume Brand"))
    print("-------------------------------------------------")
    for c in costumes:
        print(fmt.format(c.id, c.name, c.brand))
 
def checkId(costumes, id):
    """
    It returns True if the id is found in the list of costumes, otherwise it returns False
    
    :param costumes: a list of Costume objects
    :param id: The id of the costume
    :return: A list of costumes
    """
    for c in costumes:
        if id == c.id:
            return True
    return False

def checkQuantity(costumes, id, costumeQuantity):
    """
    If the quantity is greater than the quantity of the costume, return false. Otherwise, return true.
    
    :param costumes: a list of Costume objects
    :param id: the id of the costume
    :param quantity: The number of costumes the user wants to buy
    :return: a boolean value.
    """
    for c in costumes:
        if id == c.id:
            if int(c.quantity)<int(costumeQuantity):
                return False
            elif int(costumeQuantity)<0:
                return False
            else:
                return True
    return False