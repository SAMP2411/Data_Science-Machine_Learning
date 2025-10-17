import json
import time


def check_disc_add_tax(total_amt, tax):
    if total_amt > 5000:
        total_amt = total_amt * 0.9
    return total_amt * (1 + (tax / 100))


def add_customer_data(quantity, total_amt):
    return (
        ui_name
        + ","
        + ui_mail
        + ","
        + ui_ph
        + ","
        + ui_pr
        + ","
        + record[ui_pr]["Name"]
        + ","
        + str(quantity)
        + ","
        + str(record[ui_pr]["Price"])
        + ","
        + str(total_amt)
        + ","
        + time.ctime()
        + "\n"
    )


# Importing Inventory data from Record.json file
fd = open("Record.json", "r")
js = fd.read()
fd.close()

# Converting String data to Dictionary
record = json.loads(js)
print(record)
# Displaying Menu
print("--------------------MENU---------------------")
for key in record.keys():
    print(record.get(key))
    print(record[key])
    print(key, record[key]["Name"], record[key]["Price"], record[key]["Qn"])
print("---------------------------------------------")
print("")

# Taking Inputs from the user about their details and purchase
ui_name = str(input("Enter your name    : "))
ui_mail = str(input("Enter Mail ID      : "))
ui_ph = str(input("Enter Phone No     : "))
ui_pr = str(input("Enter product ID   : "))
ui_qn = int(input("Enter Quantity     : "))

print("---------------------------------------------")
print("")

# If we're having equal or more quantity then the user wants
if record[ui_pr]["Qn"] >= ui_qn:
    print("Name      : ", record[ui_pr]["Name"])
    print("Price (Rs): ", record[ui_pr]["Price"])
    print("Quantity  : ", ui_qn)
    print("---------------------------------------------")
    total_amt = check_disc_add_tax(
        total_amt=ui_qn * record[ui_pr]["Price"],
        tax=record[ui_pr]["Tax"],
    )

    print("Billing   : ", str(total_amt), "Rs (incl. Tax, Disc.)")
    print("---------------------------------------------")

    # Updating Inventory in Dictionary
    record[ui_pr]["Qn"] = record[ui_pr]["Qn"] - ui_qn

    # Generating CSV Transection Detail
    sale = add_customer_data(ui_qn, total_amt)

# If we're less quantity then the user wants
else:
    print("Sorry, We're not having enough quanity of product in our Inventory.")
    print("We're only having " + str(record[ui_pr]["Qn"]) + " quantity.")
    print("---------------------------------------------")

    ch = str(input("Press Y to purchase: "))

    # If user wants to purchase the whole quantity for that product
    if ch == "Y" or ch == "y":
        print("---------------------------------------------")
        print("Name      : ", record[ui_pr]["Name"])
        print("Price (Rs): ", record[ui_pr]["Price"])
        print("Quantity  : ", record[ui_pr]["Qn"])
        print("---------------------------------------------")
        total_amt = check_disc_add_tax(
            total_amt=record[ui_pr]["Qn"] * record[ui_pr]["Price"],
            tax=record[ui_pr]["Tax"],
        )
        print("Billing   : ", str(total_amt), "Rs (incl. Tax, Disc.)")
        print("---------------------------------------------")

        # Updating Inventory in Dictionary
        record[ui_pr]["Qn"] = 0

        # Generating CSV Transection Detail
        sale = add_customer_data(record[ui_pr]["Qn"], total_amt)

    # If user pressed anything except Y or y
    else:
        print("Thanks!")

# Converting Inventory Dictionary to String
js = json.dumps(record)

# Updating Inventory and Saving in to my Records.json
fd = open("Record.json", "w")
fd.write(js)
fd.close()

# Adding Transection on Sales File
fd = open("Sales-json.txt", "a")
fd.write(sale)
fd.close()

print("")
print("---------------------------------------------")
print("  Thanks for your order, Inventory Updated!  ")
print("---------------------------------------------")
