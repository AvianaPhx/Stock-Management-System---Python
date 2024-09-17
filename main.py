import datetime
from operations import *
from read import *
from write import *

Stocks = laptop()
now = datetime.datetime.now()
date_string = now.strftime("%Y-%m-%d_%H-%M-%S")
total = 0

while True:
    print("\n")
    print("*" * 62)
    print("Please select an option to purchase, sell or exit our system.")
    print("*" * 62 + "\n")

    print("Press 1 to sell the laptop.")
    print("Press 2 to purchase the laptop.")
    print("Press 3 to exit our system.\n")
    
    user_inputloop = True
    while user_inputloop == True:
        user_input = input("What would you like to: ")
        if user_input.isdigit():
            user_input = int(user_input)
            break
        else:
            print("\n")
            print("Error: Please choose the option giving above...!")
            print("\n")

    buylaptop = []
    restock_purchased_laptop = []

    if user_input == 1:

        print("\n")
        nameOfBuyer = buyer_name()
        print("\n")
        contactOfBuyer = buyer_contact()
        print("\n")
        addressOfBuyer = buyer_address()
        print("\n")
        buyAnother = True
        while buyAnother == True:

            anotherOne = display_laptop()
            print("\n")
            idNumber = ID_number(Stocks)
            print("\n")
            selecting = N_selection(Stocks, idNumber)
            print("\n")
            update = updating_text(Stocks, idNumber, selecting)

            # User purchased items

            neededInfo = bill(buylaptop, Stocks, idNumber, selecting, update)

            # if continueBuying == "Y":

            continueBuying = input("Do you want to buy another laptop? \nPress y to continue \nPress any other key to print the bill\n\nWhat do you want to do: ").upper()
            print()
            if continueBuying == "Y":
                buyAnother = True
            else:
                buyAnother = False
                for i in neededInfo:
                    total += int(i[4])
                terminal_bill = buying(neededInfo, date_string, buyAnother, total, nameOfBuyer, date_string, addressOfBuyer, contactOfBuyer)
                bill_txt(buylaptop, neededInfo, date_string, buyAnother, nameOfBuyer, contactOfBuyer, addressOfBuyer, Stocks, idNumber, selecting, terminal_bill, total)

    
    elif user_input == 2:
        restockloop = True
        print("\n")
        nameOfBuyer = buyer_name()
        print("\n")
        while restockloop == True:
            display_laptop()
            print("\n")
            Stocks = laptop()

            laptop_id = ID_number(Stocks)
            print("\n")
            qnty = quantity_validation(Stocks, laptop_id)
            print("\n")
            qnty_restock = Items_restock(Stocks, laptop_id, qnty)
            restockagain = input("Do you want to buy another laptop? \nPress y to continue \nPress any other key to print the bill\n\nWhat do you want to do: ").upper()
            restock = data_for_restock(restock_purchased_laptop, Stocks, laptop_id, qnty, qnty_restock)

            if restockagain == "Y":
                restockloop = True
            else:
                restockloop = False
                laptopPrice = 0 
                for i in restock:
                    laptopPrice = int(i[3])
                    total += int(i[2])
                price_vat = laptopPrice * total
                vat = price_vat + (price_vat*0.13)
                restockbill(Stocks, laptop_id, qnty, qnty_restock, restock, total, vat, nameOfBuyer, date_string,)
                restockbill_save(Stocks, laptop_id, qnty, qnty_restock, restock, total, vat, nameOfBuyer, date_string)
                print("\n")
                print("Items will get restocked")
    elif user_input == 3:
        print("\n")
        print("Thank you for visiting korone's manufacture!")
        print("\n")
        break
    else:
        print("\n")
        print("Choose the option giving above...!")
        print("\n")