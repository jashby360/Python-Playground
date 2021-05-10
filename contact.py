#Create a database for future use.
#Add to contacts, show all contacts, show one specific contact(PRIORITY), delete contacts, update contacts; Simply build a contact book that
#will be able to be used for future uses. Also build a better terminal UI than current, It's currently a jumbled mess(PRIORITY). 

import sqlite3

def createdb():
    conn = sqlite3.connect('C:/Users/jashb/OneDrive/Desktop/test.db')
    #conn = sqlite3.connect('test.db')
    print ("Opened database successfully")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Contact (Name TEXT, PhoneNumber TEXT, BirthDate TEXT) ''')
    print ("Created table successfully")
    conn.commit()
    conn.close()

#function used to add values to contact table.
def addvalues(Name,PhoneNumber,BirthDate):
    conn = sqlite3.connect('C:/Users/jashb/OneDrive/Desktop/test.db')
    #conn = sqlite3.connect('test.db')
    print ("Opened database successfully")
    conn.execute("INSERT INTO Contact (Name, PhoneNumber, BirthDate) VALUES (?, ?, ?)", (Name, PhoneNumber, BirthDate))
    conn.commit()
    print("Record created successfully")
    conn.close()

def delvalues(Name):
    conn = sqlite3.connect('C:/Users/jashb/OneDrive/Desktop/test.db')
    #conn = sqlite3.connect('test.db')
    print ("Opened database successfully");

    #suq = SQL_Update_Query
    suq = """DELETE from Contact where Name = ?"""
    conn.execute(suq, (Name,))
    conn.commit()
    print("Record deleted successfully")

    print ("Total number of rows deleted :"), conn.total_changes

    cursor = conn.execute("SELECT * from Contact")
    for row in cursor:
        print ("Name = ", row[0])
        print ("Phone-Number = ", row[1])
        print ("Birth-Date = ", row[2], "\n")
        print ("Operation done successfully")
    conn.close()

#Function used to show all values in contact table.
def shwvalues():
    conn = sqlite3.connect('C:/Users/jashb/OneDrive/Desktop/test.db')
    #conn = sqlite3.connect('test.db')
    print ("Opened database successfully")

    cursor = conn.execute("SELECT * from Contact")
    for row in cursor:
        print ("Name = ", row[0])
        print ("Phone-Number = ", row[1])
        print ("Birth-Date = ", row[2], "\n")
        print ("Operation done successfully")
    conn.close()

#Create a table inside of the db if not created already.
createdb()

##UI OF BASIC CONTACT BOOK##
addval = input("Would you like to add a value? y/n ")
if addval == 'y':
    name = input("Enter the name of the contact you want added. ")
    phnumber = input("Enter the phone number  of your contact. ")
    bdate = input("Enter the birthdate of your contact. ")
    addvalues(name,phnumber,bdate)

    addval2 = input("Would you like to add another? y/n ")
    while addval2 != 'n':
        name = input("Enter the name of the contact you want added. ")
        phnumber = input("Enter the phone number  of your contact. ")
        bdate = input("Enter the birthdate of your contact. ")
        addvalues(name,phnumber,bdate)
        addval2 = input("Would you like to add another? y/n ")
else:
    print("you didn't want to add a value.")

#delete a value
delval = input("Would you like to delete a value? y/n ")
if delval == 'y':
    name = input("Enter the name of the contact you want deleted. ")
    delvalues(name)

    delval2 = input("Would you like to del another? y/n ")
    while delval2 != 'n':
        name = input("Enter the name of the contact you want deleted. ")
        
        delvalues(name)
        delval2 = input("Would you like to delete another? y/n ")
else:
    print("you didn't want to delete a value.")

#Show all table values if you want to.
shwval = input("Would you like to show all table values? y/n ")
if shwval == 'y':
    shwvalues()
    i = input('Press ENTER to continue: ')
else:
    print("You didn't want to show all table values.")