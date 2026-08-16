print ("welcome to the CLI-Diary application!")


ask = input("what  do you want to do? (read/write) :")

def write():

    date = input("enter the date for the diary entry (dd.mm.yy) :") # edit this line if you want another format
    file = open (date + ".txt", "w")
    file.write(date + "\n")
    n = input("enter your entry for today:")
    file.write(n)
    file.close()

def read():

    which = input("Enter the date of the entry")
    file = open(which + ".txt", "r")
    contents = file.read()
    print (contents)
    file.close()

if ask == "write" or ask == "w":
    write()

elif ask == "read" or ask == "r":
    read()
else:
    print ("please enter a valid option")


