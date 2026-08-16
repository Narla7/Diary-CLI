print ("welcome to the CLI-Diary application!")


ask = input("what  do you want to do? (read/write) :")

# defining functions

def write():
    date = input("enter todays date (dd.mm.yy):")
    with open(date + ".txt", "w") as file:
        entry = input("enter your entry for today: \n")
	file.write(entry)

def read():

    which = input("Enter the date of the entry:")
    with open(which + ".txt", "r") as file:
        a = file.read()
	print (a)


# flow of control 

if ask == "write" or ask == "w":
    write()

elif ask == "read" or ask == "r":
    read()

else:
    print ("please enter a valid option")


