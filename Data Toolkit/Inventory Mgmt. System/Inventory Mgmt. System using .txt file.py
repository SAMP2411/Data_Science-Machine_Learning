import time


def add_customer_data(quantity, total_amt):
    # Adding customer data into sales file
    fd = open("sales-text.txt", "a")
    sales_detail = (
        ui_username
        + ","
        + ui_phone
        + ","
        + ui_mail
        + ","
        + prod_details[1]
        + ","
        + ui_prod_id
        + ","
        + quantity
        + ","
        + str(total_amt)
        + ","
        + time.ctime()
        + "\n"
    )
    fd.write(sales_detail)
    fd.close()


# Reading the inventory
fd = open("Inventory.txt", "r")
products = fd.read().split("\n")
print(products)
fd.close()

# Taking user input
ui_username = input("Enter your Name: ")
ui_phone = input("Enter your Phone No.: ")
ui_mail = input("Enter your Mail: ")
ui_prod_id = input("Enter prodict ID: ")
ui_prod_qn = input("Enter poduct quantity:")

updated_product_lst = []


# Going through each product detail
for product in products:
    prod_details = product.split(",")

    # Checking if the product exist or not
    if prod_details[0] == ui_prod_id:
        # Checking if we have enough quantity
        if int(ui_prod_qn) <= int(prod_details[3]):
            print("--------------------------------")
            print("Product Name  : ", prod_details[1])
            print("Price         : ", prod_details[2])
            print("Quantity      : ", ui_prod_qn)
            print("--------------------------------")
            total_amt = int(ui_prod_qn) * int(prod_details[2])
            print("Billing Amount: ", total_amt)
            print("--------------------------------")

            prod_details[3] = str(int(prod_details[3]) - int(ui_prod_qn))

            add_customer_data(ui_prod_qn, total_amt)

        # If we do not have enough quantity
        else:
            print("Sorry we're not having enough quantity.")
            print("We're having only", prod_details[3], "quantity")
            print("Would you like to purchase it?")

            ch = input("Press Y/N")

            # If you want to purchase the remaining quantity
            if ch.upper() == "Y":
                print("--------------------------------")
                print("Product Name  : ", prod_details[1])
                print("Price         : ", prod_details[2])
                print("Quantity      : ", prod_details[3])
                print("--------------------------------")
                total_amt = str(int(prod_details[3]) * int(prod_details[2]))
                print("Billing Amount: ", total_amt)
                print("--------------------------------")

                prod_details[3] = str(int(prod_details[3]) - int(prod_details[3]))

                add_customer_data(prod_details[3], total_amt)

    # Updating my inventory list
    updated_product_lst.append(prod_details)

print(updated_product_lst)
# Updating my inventory file
fd = open("Inventory.txt", "w")

for i in updated_product_lst:
    # print(updated_product_lst.index(i))
    if updated_product_lst.index(i) == len(updated_product_lst) - 1:
        fd.write(",".join(i))
    else:
        fd.write(",".join(i) + "\n")

fd.close()
