# !/usr/bin/env python3
# coding: utf-8
# --------------------------------------------------------------------------------

import sys

sys.path.append("../")

from time import sleep
#from Common.qarm_interface_wrapper import *

GRIPPER_IMPLEMENTATION = 1
#arm = QArmInterface(GRIPPER_IMPLEMENTATION)
#scan_barcode = BarcodeScanner.scan_barcode

# --------------------------------------------------------------------------------
# STUDENT CODE BEGINS
# ---------------------------------------------------------------------------------


# arm.home()
print("Initial Arm Homing Process")

import csv
import bcrypt
import random

# working inputs
# userid="baldes"
# password="40062"

def authenticate():
    '''this function logs the user in. It asks the user if they have an account, and if not, it calls sign_up() before authenticating. 
    To authenticate, it compares a userid and password entered by the user to the userids and encrypted passwords stored in users.csv. 
    If the user enters a bad userid or a non-matching password, it allows them to try again until they are successful.
    The function returns their userid once successful There are no parametsrs and it returns the userId that the user inputs'''

    #ask user if they already have an account
    print("=== Warehouse Login ===")
    haveAccount = str(input("Do you have an account? (Y/N)"))

    #loop until user enters either yes or no
    while haveAccount != "N" and haveAccount != "Y":
        if haveAccount != "N" or haveAccount != "Y":
            print("Not a valid input, try again")
        haveAccount = str(input("Do you have an account? (Y/N)"))


    #sign up if user dosent have an account
    if haveAccount == "N":
            sign_up()

    inputsInvalid = True
    while inputsInvalid == True:
        userID = input("Enter your User ID and password\nUserID:\t")
        password = input("Password: ")

        #read stored data and check each line if it is a matching userid and password
        file = open("users.csv","r")
        lines = file.readlines()
        for line in lines:
            storedUserID, storedPass = line.strip().split(",")

            if storedUserID == userID:
                if bcrypt.checkpw(password.encode("utf-8"),storedPass.encode("utf-8")):
                    inputsInvalid = False

        #tell user if they are correct or not
        if inputsInvalid == False:
            print("Correct Information")
        else:
            print("That information is incorrect try again")

    file.close()

    return userID


def sign_up():
    '''
    function takes userinput for a username, if their username exists they are already in the system and wont be able to create a new user,
    function takes a password and saves it to a seperate file, for the password to be saved user must create a password that contains an upper and lowercase, 
    a digit and a passes special character.
    '''

    #variables
    uppercase = False
    lowercase = False
    digit = False
    allowedcharacters = ["!",".","@","#","$","%","^","&","*","(",")","_",'[',"]"]
    ac = False
    running = True
    hasuser = False

    # Read all usernames into a list
    filelist = []
    file = open("users.csv", "r")
    for line in file:
        usernames = line.strip().split(',')
        for user in usernames:
            if user:  # Skip empty strings
                filelist.append(user.strip())
    file.close()

    while True:
        userid = str(input("Create a username: "))

        # reads if username already exists
        if userid in filelist:
            print(f"User exists, {userid}")
        else:
            # Get password and validate it
            password = input(f"Welcome {userid}, create a password: ")

            if len(password) < 6:
                print("Your password must be 6 characters or longer.")
            else:
                # Check password requirements
                for char in password:
                    if char.isupper():
                        uppercase = True
                    if char.islower():
                        lowercase = True
                    if char.isdigit():
                        digit = True
                    if char in allowedcharacters:
                        allowedcharacters = True

                # Check if all requirements are met
                if uppercase and lowercase and digit and allowedcharacters:
                    file = open("users.csv", "a")
                    hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                    file.write(f"{userid},{hash}\n") #Writes user information in file
                    file.close()
                    print("Account created successfully!")
                    break
                else:
                    # Tell user what's to add to password
                    if not allowedcharacters:
                        print("Your password does not fit requirements - needs special character")
                    elif not uppercase:
                        print("needs uppercase")
                    elif not lowercase:
                        print("needs lowercase")
                    elif not digit:
                        print("needs digits")


def lookup_products(products):
    """This function looks up for the inputed product in the product.csv, and returns the user a product name and price
    Parameter: Gets form the user,
    Return: Returns Name and Price of the product after scanning"""
    scanned = products
    for i in range(len(scanned)):
        scanned[i] = scanned[i].strip()

    results = []

    file = open("products.csv", "r")
    reader = csv.reader(file)

    csv_rows = []
    for row in reader:
        if len(row) == 2:
            csv_rows.append(row)

    file.close()

    for product in scanned:
        found = False

        for row in csv_rows:
            name = row[0].strip()
            price = float(row[1])

            if product == name:
                results.append([name, price])
                found = True
                break

        if not found:
            print("Warning:", product, "not found!")

    return results


def pack_products(product_list):

    for product in product_list:

        if product == 'Sponge':
            # arm.control_gripper(180)   # open first
            # arm.set_arm_positon(0.5700847784455721, 0.1782455617649722, 0.09896799887592941)   # move to Sponge
            print("Move Arm to Sponge")

            # arm.control_gripper(-180)  # close to grab sponge
            # arm.shoulder(-20)
            print("Move Arm Up & Rehome")

            # arm.set_arm_positon(0.2680739285194166, -0.3182365164329308, 0.19428816893353162)  # dropbox
            # arm.control_gripper(180)   # release
            # arm.rotate_base(3)
            # arm.rotate_base(-3)
            # arm.home()

        elif(product == 'Bottle'):
            # arm.control_gripper(180)
            # arm.set_arm_positon(0.592886197381999, 0.1127691441318727, 0.07105588040616939)   # Bottle
            print("Move Arm to Bottle")

            # arm.control_gripper(-180)
            # arm.shoulder(-20)
            print("Move Arm Up & Rehome")

            # arm.set_arm_positon(0.2680739285194166, -0.3182365164329308, 0.19428816893353162)
            # arm.control_gripper(180)
            # arm.rotate_base(3)
            # arm.rotate_base(-3)
            # arm.home()

        elif(product == 'Rook'):
            # arm.control_gripper(180)
            # arm.set_arm_positon(0.6046019968684281, 0.046941535675817936, 0.04127910213589611)  # Rook
            print("Move Arm Up & Rehome")

            # arm.control_gripper(-180)
            # arm.shoulder(-20)
            print("move arm")

            # arm.set_arm_positon(0.2680739285194166, -0.3182365164329308, 0.19428816893353162)
            # arm.control_gripper(180)
            # arm.rotate_base(3)
            # arm.rotate_base(-3)
            # arm.home()

        elif(product == 'D12'):
            # arm.control_gripper(180)
            # arm.set_arm_positon(0.5956763959572058, -0.01782791627094222, 0.04140932108643397)  # D12
            print("Move Arm to D12")

            # arm.control_gripper(-180)
            # arm.shoulder(-20)
            print("Move Arm Up & Rehome")

            # arm.set_arm_positon(0.2680739285194166, -0.3182365164329308, 0.19428816893353162)
            # arm.control_gripper(180)
            # arm.rotate_base(3)
            # arm.rotate_base(-3)
            # arm.home()

        elif(product == 'WitchHat'):
            # arm.control_gripper(180)
            # arm.set_arm_positon(0.593234026200123, -0.08848494629695498, 0.027868187675618883)  # Witch Hat
            print("Move Arm to Witch Hat")

            # arm.control_gripper(-180)
            # arm.shoulder(-20)
            print("Move Arm Up & Rehome")

            # arm.set_arm_positon(0.2680739285194166, -0.3182365164329308, 0.19428816893353162)
            # arm.control_gripper(180)
            # arm.rotate_base(3)
            # arm.rotate_base(-3)
            # arm.home()

        elif(product == 'Bowl'):
            # arm.control_gripper(180)
            # arm.set_arm_positon(0.5922231141129967, -0.15079853440711044, 0.03030927994162788)  # Bowl
            print("Move Arm to Bowl")

            # arm.control_gripper(-180)
            # arm.shoulder(-20)
            print("Move Arm Up & Rehome")

            # arm.set_arm_positon(0.2680739285194166, -0.3182365164329308, 0.19428816893353162)
            # arm.control_gripper(180)
            # arm.rotate_base(3)
            # arm.rotate_base(-3)
            # arm.home()

        else:
            print("Product not in stock.")
            print("ReHome Arm")


def complete_order(userid, product_list):
    '''This function gets user id and product list as paratmers and updates orders.csv with new orders as well as outputting a cleanly formatted receipt'''

    prev_orders = []
    f = open("orders.csv","r") #Read orders that already exsit in file

    for line in f:
        prev_orders.append(line) #Add all orders to orders.csv file

    f.close()

    subtotal = 0
    for item in product_list: #get every price from 2d list and add them
        subtotal += item[1]

    percent_disc = random.randint(5,50) #generate rnadom discount
    amount_disc = subtotal * (percent_disc / 100)
    updated_sub = subtotal - amount_disc

    tax = updated_sub * .13

    final_sub = updated_sub + tax

    file  = open("orders.csv", "r")

    new_line = userid + "," + f"{final_sub:.2f}" #creates file to be inputted in order.csv
    for item in product_list:
        new_line += "," + item[0]
    new_line += "\n" #adds a new line to list

    f = open("orders.csv", "w")

    for item in prev_orders:
        f.write(item) #rewrite old orders back into file

    f.write("")
    f.write(new_line) #rewrite new files back into file
    f.close()

    order_count = 0
    f = open("orders.csv", "r")
    for line in f:
        line = line.strip()

        if line != "":     #check if line has actual value
            parts = line.split(",")
            if parts[0] == userid: #if the user id is the same as current user add to order total
                order_count += 1

    f.close()


    print("\n==============================")
    print("         ORDER RECEIPT")
    print("==============================")
    print(f"Customer: {userid}\n")

    for name, price in product_list:
        print(f"{name:<20} {price:>{7}.2f} $")

    print("------------------------------")
    print(f"Subtotal: {subtotal:>{17}.2f} $")
    print(f"Discount: {amount_disc:>{17}.2f} $")
    print(f"Tax (13%): {tax:>{16}.2f} $")
    print("------------------------------")
    print(f"Final Total: {final_sub:>{14}.2f} $")
    print("==============================")

    print(f"\nYou have placed {order_count} orders so far.\n")

    #complete_order("Joesph", [["apple", 322.50], ["grape", 3.00], ["orange", 1.75]])


def check(value,mainlist):
   for element in mainlist:
       if (element[0] == value):
           return True
   return False


def customer_summary(userid):
    """
    Reads the orders file and prints a summary for the given user.
    Counts total orders, total amount spent, and total quantity of each product ordered.
    Takes a userid as input.
    """
    file = open("orders.csv", "r")

    order_count = 0
    total_spent = 0.0
    product_counts = []
    products_ordered = ""

    for line in file:
        parts = line.strip().split(",")
        line_userid = parts[0]

        if line_userid == userid:
            order_count += 1
            total_spent += float(parts[1])
            products_ordered += f"\nOrder #{order_count}: "

            for i in range(2, len(parts)):
                products_ordered += f",{parts[i]}"
                if not check(parts[i], product_counts):
                    product_counts.append([parts[i], 1])
                else:
                    for product in product_counts:
                        if product[0] == parts[i]:
                            product[1] += 1

    file.close()

    print("Customer Summary")
    print("----------------")
    print(f"User ID: {userid}")
    print(f"Total Orders: {order_count}")
    print(f"Total Spent: ${total_spent:.2f}")
    print()
    print("Total Products Ordered:")

    for product in product_counts:
        print(f"{product[0]}: {product[1]}x")


def main():

    print("""
$$$$$$$\      $$$$$$\      $$\   $$\     $$$$$$$$\     $$$$$$\  
$$  __$$\    $$  __$$\     $$ |  $$ |    $$  _____|   $$  __$$\ 
$$ |  $$ |   $$ /  $$ |    \$$\ $$  |    $$ |         $$ /  \__|
$$$$$$$\ |   $$ |  $$ |     \$$$$  /     $$$$$\       \$$$$$$\  
$$  __$$\    $$ |  $$ |     $$  $$<      $$  __|       \____$$\ 
$$ |  $$ |   $$ |  $$ |    $$  /\$$\     $$ |         $$\   $$ |
$$$$$$$  |$$\ $$$$$$  |$$\ $$ /  $$ |$$\ $$$$$$$$\ $$\\$$$$$$  |
\_______/ \__|\______/ \__|\__|  \__|\__|\________|\__|\______/ 
                                                                
             BARELY ORGANIZED XPRESS EXPEDITION SERVICE
    ----------------------------------------------------------------
    """)
    
    userid = authenticate()

    products_list = []

    while True:
        print("\nWelcome to B.O.X.E.S. — where our motto is we tried.")
        order = input("Scan or type 'Quit': ")
        #order = scan_barcode()

        if order.lower() == "quit":
            break

        products = lookup_products(order.split())

        # flatten into a single list for final invoice
        for item in products:
            products_list.append(item)

        pack_products([p[0] for p in products])

    complete_order(userid, products_list)
    customer_summary(userid)


main()

#dropbox - 0.2680739285194166, -0.3182365164329308, 0.19428816893353162
#sponge - 0.5700847784455721, 0.1782455617649722, 0.09896799887592941)
#bishop Position (X, Y, Z): (0.592886197381999, 0.1127691441318727, 0.07105588040616939)
#rook Position (X, Y, Z): (0.6046019968684281, 0.046941535675817936, 0.04127910213589611)
#d12 Position (X, Y, Z): (0.5956763959572058, -0.01782791627094222, 0.04140932108643397)
#cone Position (X, Y, Z): (0.593234026200123, -0.08848494629695498, 0.027868187675618883)
#bowl Position (X, Y, Z): (0.5922231141129967, -0.15079853440711044, 0.03030927994162788)
#----------------------------------------------------------------------------------
# STUDENT CODE ENDS
# ---------------------------------------------------------------------------------

# arm.end_arm_connection()
