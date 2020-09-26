import csv

# Author: Yonis Ismail

# Created: 17/11/2019

# Revised: 20/11/2019

# What to do: Done!

def editSurgery(my_list= []): # Function to edit surgery
    data = []
    data2 = []


### Part 1: Search for a specific row, copy the row into an empty list and delete row from the old list

    sanct_id = input("Enter the sanctuary ID that you are looking for to change the Surgery details \n")
    for row in treatment_list:                  # Search for specific row 
        if sanct_id in row:   
            # copy the that into a list
            data.append(row)                    # append row into empty list data
            my_list.remove(row)                 # remove the selected row from the old list
        # remove the old list

###Part 2: Turn the list in data from a sublist into a standard list
        
    result = []
    for sublist in data:
        for item in sublist:
            result.append(item)
### Part 3: Remove the surgery details, input in new surgery details and then append onto the main list

    result.remove(result[2])                    # Remove surgery details
    newelement = input("Enter the new surgery details \n")
    result.insert(2, newelement)                  # insert in new surgery details
    my_list.append(result)
    print("Appending new data the the end. \n")
    print(my_list)
    
#• B – enter details of neutering

def editNeutering(my_list= []): # Function to enter details of neutering
    data = []
    data2 = []


###Part 1: Search for a specific row, copy the row into an empty list and delete row from the old list

    sanct_id = input("Enter the row that you want to search for tp change the neutering details \n")
    for row in my_list:                  # Search for specific row 
        if sanct_id in row:   
            
            data.append(row)                    # append row into empty list data
            my_list.remove(row)                 # remove the selected row from the old list
        

###Part 2: Turn the list in data from a sublist into a standard list
        
    result = []
    for sublist in data:
        for item in sublist:
            result.append(item)
###Part 3: Remove the neutering details, input in new neutering details and then append onto the main list

    result.remove(result[4])                    # Remove neutering details
    variable = input("Enter the new neutering details \n")
    result.insert(4, variable)                  # insert in new neutering details
    my_list.append(result)
    print("Appending new data the the end. \n")
    print(my_list)

#• C – enter microchip number
def editMicrochip(my_list= []):             # function the edit microchip number
    data = []
    data2 = []


###Part 1: Search for a specific row, copy the row into an empty list and delete row from the old list

    sanct_id = input("Enter the row that you want to search for to change the microchip details\n")
    for row in my_list:                  # Search for specific row 
        if sanct_id in row:   
            
            data.append(row)                    # append row into empty list data
            my_list.remove(row)                 # remove the selected row from the old list
        

###Part 2: Turn the list in data from a sublist into a standard list
        
    result = []
    for sublist in data:
        for item in sublist:
            result.append(item)
###Part 3: Remove the old details, input in new microchip details and then append onto the main list

    result.remove(result[5])                    # Remove microchip details
    variable = input("Enter the new microchip details \n")
    result.insert(5, variable)                  # insert in new microchip details
    my_list.append(result)
    print("Appending new data the the end. \n")
    print(my_list)

#D – edit the status of an animal (please see data provided)
def editStatusPet(my_list= []):                                 # Function created to edit the status of a pet
    data = []
    data2 = []

###Part 1: Search for a specific row, copy the row into an empty list and delete row from the old list

    sanct_id = input("Enter the row that you want to search for to change the status of a pet \n")
    for row in my_list:                  # Search for specific row 
        if sanct_id in row:   
            # copy the that into a list
            data.append(row)                    # append row into empty list data
            my_list.remove(row)                 # remove the selected row from the old list
        # remove the old list

###Part 2: Turn the list in data from a sublist into a standard list
        
    result = []
    for sublist in data:
        for item in sublist:
            result.append(item)
###Part 3: Remove the old details, input in new details and then append onto the main list

    result.remove(result[6])                    # Remove old details
    variable = input("Enter the new status details \n")
    result.insert(6, variable)                  # insert in new details
    my_list.append(result)
    print("Appending new data the the end. \n")
    print(my_list)

def editStatusWAnimals(my_list= []):                                 # Function created to edit the status of a wild animal
    data = []
    data2 = []

###Part 1: Search for a specific row, copy the row into an empty list and delete row from the old list

    sanct_id = input("Enter the row that you want to search for to change the status of a wild animal \n")
    for row in my_list:                  # Search for specific row 
        if sanct_id in row:   
            # copy the that into a list
            data.append(row)                    # append row into empty list data
            my_list.remove(row)                 # remove the selected row from the old list
        # remove the old list

###Part 2: Turn the list in data from a sublist into a standard list
        
    result = []
    for sublist in data:
        for item in sublist:
            result.append(item)
###Part 3: Remove the old details, input in new details and then append onto the main list

    result.remove(result[3])                    # Remove old details
    variable = input("Enter the new status details \n")
    result.insert(3, variable)                  # insert in new details
    my_list.append(result)
    print("Appending new data the the end. \n")
    print(my_list)
    
#• E – edit date of departure from the sanctuary
def editDateofdeparture(my_list= []):
    data = []
    data2 = []

###Part 1: Search for a specific row, copy the row into an empty list and delete row from the old list

    sanct_id = input("Enter the row that you want to search for to change the date of departure \n")
    for row in my_list:                  # Search for specific row 
        if sanct_id in row:   
            # copy the that into a list
            data.append(row)                    # append row into empty list data
            my_list.remove(row)                 # remove the selected row from the old list
        # remove the old list

###Part 2: Turn the list in data from a sublist into a standard list
        
    result = []
    for sublist in data:
        for item in sublist:
            result.append(item)
###Part 3: Remove the old details, input in new details and then append onto the main list

    result.remove(result[8])                    # Remove old details
    variable = input("Enter the date of departure details \n")
    result.insert(8, variable)                  # insert in new details
    my_list.append(result)
    print("Appending new data the the end. dd/mm/yyyy \n")
    print(my_list)

    
#• F – edit destination of the animal upon departure


def editDestination(my_list= []):
    data = []
    data2 = []

###Part 1: Search for a specific row, copy the row into an empty list and delete row from the old list

    sanct_id = input("Enter the row that you want to search for to change the destination \n")
    for row in my_list:                  # Search for specific row 
        if sanct_id in row:   
            # copy the that into a list
            data.append(row)                    # append row into empty list data
            my_list.remove(row)                 # remove the selected row from the old list
        # remove the old list

###Part 2: Turn the list in data from a sublist into a standard list
        
    result = []
    for sublist in data:
        for item in sublist:
            result.append(item)
###Part 3: Remove the old details, input in new details and then append onto the main list

    result.remove(result[9])                    # Remove old details
    variable = input("Enter the destination details \n")
    result.insert(9, variable)                  # insert in new details
    my_list.append(result)
    print("Appending new data the the end. \n")
    print(my_list)

###################################################

finished = False

finishedP = False

finishedWA = False

with open("DADSA 2019-20 CWK A TREATMENT.csv", mode = 'r') as treatment:            # Open Treatment csv file
    treader = csv.reader(treatment)
    

    treatment_list = list(treader) # treatment csv file into a list

    print(treatment_list)

    
    while finished != True:        # Having choice of what you want to edit
        
        choice = input("Do you want to edit surgery details? type in y for yes or n for no")
        
        choice.lower() # converting to lower case

        if choice == "y":
            editSurgery(treatment_list)
        elif choice == "n":
            finished = True
        else:
            print("unknown data")

   

    
with open("DADSA 2019-20 CWK A DATA PETS.csv", mode = 'r') as pets:    # Open Pets csv file

    preader = csv.reader(pets)
    

    pet_list = list(preader) # pets file into a list

    print(pet_list)

    while finishedP != True:        # Having choice of what you want to edit
        
        choice = input("Choose what you want to edit. Neutering, Microchip, status of pet, date of departure or destination.")
        
        choice.lower() # converting to lower case
        if choice == "neutering":
            editNeutering(pet_list)
        elif choice == "microchip":
            editMicrochip(pet_list)
        elif choice == "status of pet":
            editStatusPet(pet_list)
        elif choice == "date of departure":
            editDateofdeparture(pet_list)
        elif choice == "destination":
            editDestination(pet_list)
        else:
            print("Unknown input")
    
        exit = input("do you want to exit? press y if yes or n for no")
        if exit == "y":
            finishedP = True
        
    
    
  

with open("DADSA 2019-20 CWK A WILD ANIMALS.csv", mode="r") as wildanimals:     #open the wild animals csv file

    wreader = csv.reader(wildanimals)   # read contents

    wanimal_list = list(wreader) # wild animals csv file into a list

    print(wanimal_list, "\n")

    
    while finishedWA != True:        # Having choice of what you want to edit
        
        choice = input("Choose what you want to edit. date of departure, status of wild animal or destination.")
        
        choice.lower() # converting to lower case

        if choice == "date of departure":
            editDateofdeparture(pet_list)
        elif choice == "destination":
            editDestination(pet_list)
        elif choice == "status of wild animal":
            editStatusWAnimals(wanimal_list)
        else:
            print("Unknown input")
    
        exit = input("do you want to exit? press y if yes or n for no")
        if exit == "y":
            finishedWA = True

