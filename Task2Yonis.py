# Author: Yonis Ismail

# Created: 09/11/2019

# Revised: 20/11/2019

# What to do: Done




import csv


def quicksort(my_list):         # Function to quick sort the data
    if not my_list:         
        return []       # prevent maximum recursion depth exceeded
    else:
        return (quicksort([i for i in my_list[1:] if i <  my_list[0]])
            + [my_list[0]] +
            quicksort([i for i in my_list[1:] if i >= my_list[0]]))         # Sort in ascending order


def newentry(myList = []):  # Function the add new entry
    data = []
    data2 = []
    data2 = input("Enter the data you want to append to the list")
    data.append(data2)  # Create a sublist as the rest of the data are in sublists
    myList.append(data) # append the data to the main list
    print("The list was updated! \n", myList)

def sanctidsearch(my_list = []): # Function to find the sanctuary ID
    sanct_id = input("Enter the sanctuary id of the row that you want to find \n")
    for row in my_list:         # Search for each row in a list         
        if sanct_id in row:   
             print(row, "\n")
    
def abusers(my_list = []):    # Function to find the abusers of animals
    data = []
    i = 0
    for row in treatment_list:       # search through every column in a list
        data.append(my_list[i][6]) # append to the empty list, the 6th element in each row
        i = i +1
    data.pop(0) # Remove first element in list
    
    data = quicksort(data)         # sort in alphabetical order
    while '' in data:   # Remove empty string
        data.remove('')
    print("These are the abusers: \n", data, "\n")
    

def abandoned(my_list = []):    # Function to find the people who abandoned their animals
    data = []
    i = 0
    for row in treatment_list:       # search through every column in a list
        data.append(my_list[i][7]) # append to the empty list, the 6th element in each row
        i = i +1
    data.pop(0) # Remove first element in list
    
    data = quicksort(data)         # sort in alphabetical order
    while '' in data:   # Remove empty string
        data.remove('')
    print("These are the abandoners: \n", data, "\n")


def animals(my_list = []): # Function the find Cats or dogs that are ready for adoption
    data = []
    data2 = []
    
    animal = input("Enter the species of animal you want to look for Cats or Dogs only. Type in Cat for cats or Dog for dogs \n") 
    
    for row in my_list:         # Search for each row to see if the animal exists and append it to an empty list         
        if animal in row:
            data.append(row)
             
    
    for row in data:            # if they are ready for adoption append to empty list
        if 'Yes' in row[4]:
            data2.append(row)
            
    print("The ones that are ready are \n" ,data2, "\n")
    

def AllPETSready(my_list = []):         # Function to find all the pets that are ready
    data = []
    data2 = []
    global data3
    data3 = []

    
    for row in my_list:         # Search for each row in list         
        if ('Dog' in row) or ('Cat' in row):        # If Cats or dogs are in the list append to first empty list
            data.append(row)
    
    
    for row in data:            # If they are ready then append to 2nd empty list
        if 'Yes' in row[4]:
            data2.append(row)
    for row in my_list:
        if ('Parrot' in row) or ('Canary' in row):      # If Parrot and Canary are in the main list then append to data2
            data2.append(row)
            
            
    print(data2)
    for row in data2: 
        data3.append(row[0])    #Add only the sanctuary IDs of the pets into the final empty list

    data3 = quicksort(data3)            # Sort
    print("These are all the pets that are ready: \n", data3, "\n")              
                             
                     
                
def AllWAready(my_list = []):   # Function the find all the wild animals that are ready
    data = []
    
    global data2
    data2 = []

   
    for row in my_list:
        if 'Yes' in row[2]:     # If they are ready then append to the empty list
            data.append(row)

    
           
    for row in data:            # Append only the sanctuary Ids into the final empty list
        data2.append(row[0])
        
    data2 = quicksort(data2)                
    print("These are all the wild animals that are ready: \n", data2, "\n")



with open("DADSA 2019-20 CWK A TREATMENT.csv", mode="r") as treatment:          # Opening treatment csv file
    treader = csv.reader(treatment)     # Read contents
    
    treatment_list = list(treader)    # Convert treatment csv file into a list

    print(treatment_list, "\n")
    
    sanctidsearch(treatment_list) # Call function to find sanctuary ID

    abusers(treatment_list) # Call function to find abusers

    abandoned(treatment_list) # Call function the find abandoners
    newentry(treatment_list)  # Call function to enter new data



with open("DADSA 2019-20 CWK A WILD ANIMALS.csv", mode="r") as wildanimals:     #open the wild animals csv file

    wreader = csv.reader(wildanimals)   # read contents

    wanimal_list = list(wreader) # wild animals csv file into a list

    print(wanimal_list, "\n")   
    
    
    sanctidsearch(wanimal_list) # call function to find sanctuary ID
    
    AllWAready(wanimal_list) # Call function to find all the wild animals that are ready
    newentry(wanimal_list)  # Call function to enter new data


with open("DADSA 2019-20 CWK A DATA PETS.csv", mode= "r") as pets:        # open the pets csv file
    preader = csv.reader(pets)

    pet_list = list(preader) # turn the contents of the csv file into a list
    print(pet_list, "\n")

    
    sanctidsearch(pet_list) # call function to find sanctuary ID
    
    AllPETSready(pet_list) # Call function to find all pets ready
    
    animals(pet_list) # call function the see if cats or dogs are ready
    ####################################################
    data3.append(data2) # Task 2E -> see if all of the animals at the shelter are ready, pets first then wild animals
    print("These are all the animals in the sanctuary that are ready: \n", data3)
    
    ################################################# 
    newentry(pet_list)  # Call function to enter new data


