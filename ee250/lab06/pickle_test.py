import pickle
import os.path
from os import path

notes = []

# TODO: Using the pickle module...

# A. If notes.pickle exists, read it in using pickle and assign the content to
#   the notes variable
if path.exists("notes.pickle"):
    test = open("notes.pickle", "rb")
    notes = pickle.load(test)
    test.close()


# B. Print out notes
print(notes)

# C. Read in a string from the user using input() and append it to notes
input = input("Enter notes addition: ")
notes.append(input)
# D. Save notes to notes.pickle

test = open("notes.pickle", "wb")
pickle.dump(notes, test)
test.close()







# take user input to take the amount of data
#number_of_data = int(input('Enter the number of data : '))
#data = []

# take input of the data
#for i in range(number_of_data):
    #raw = input('Enter data '+str(i)+' : ')
    #data.append(raw)

# open a file, where you ant to store the data
#file = open('important', 'wb')

# dump information to that file
#pickle.dump(data, file)

# close the file
#file.close()

