print ("welcome to the CLI-Diary application!")


ask = input("what  do you want to do? (read/write) :")

# defining functions

def write():
    date = input("enter todays date (dd.mm.yy):") # change this line if you  want another format
    with open(date + ".txt", "w") as file:
        entry = input("enter your entry for today: \n")
        file.write(entry)

def read():

    which = input("Enter the date of the entry:")
    try:
        with open(which + ".txt", "r") as file:
            a = file.read()
            print (a)
    except FileNotFoundError:
        print("Looks like there is not Diary Entry for that date!")


if ask == "write" or ask == "w":
    write()

elif ask == "read" or ask == "r":
    read()

else:
    print ("please enter a valid option")


