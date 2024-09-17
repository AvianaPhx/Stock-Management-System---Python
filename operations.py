
def buyer_name():
    while True: 
        buyerName = input("Please enter your name: ")
        if buyerName.isalpha():
            break
        else:
            print("Error: Enter the valid name...!")

    return buyerName

def buyer_contact():
    while True:
        buyercontact = input("Please enter your contact number: ")
        if buyercontact.isdigit():
            buyercontact = int(buyercontact)
            break
        else:
            print("Error: Enter the valid contact number...!")

    return buyercontact

def buyer_address():
    while True:
        buyeraddress = input("Please enter your address: ")
        if buyeraddress.isalnum():
            break
        else:
            print("Error: Enter the valid address...!")

    return buyeraddress

def ID_number(Stocks):
    laptopNumber = None

    while not laptopNumber:
        
        laptopNumber = input("Enter the ID of the laptop you want to buy: ")

        if not laptopNumber.isdigit():
            print("Error: The ID you entered is not valid...!")
            laptopNumber = None

        elif int(laptopNumber) <= 0 or int(laptopNumber) > len(Stocks):
            print("Error: The ID is not mentioned in the list above...!")
            laptopNumber = None

    return int(laptopNumber)

def N_selection(Stocks, idNumber):

    selectedQuantity = Stocks[idNumber][3]
    try:
        while True:
            countBuy = input("How many does the customer want to buy? ")
            if countBuy.isdigit():
                countBuy = int(countBuy)
                if countBuy <= 0 or countBuy > int(selectedQuantity):
                    print("Dear Admin, the selected quantity is not available in our shop. Please look again in the table.")
                    print("\n")
                    break
                else:
                    print("\n")
                    print("The product is available!")
                    break
            else:
                print("Error: Please enter a number")
    except(ValueError):
        print("Error: Please enter a number")

    return countBuy

def updating_text(Stocks, idNumber, selecting):
    # Update laptopDictionary with new quantity
    if Stocks[idNumber][3] != "0":
    
        Stocks[idNumber][3] = str(int(Stocks[idNumber][3]) - int(selecting))

    # Create a list to store the updated laptops
    laptopList = []     
    for values in Stocks.values():         
        laptopList.append(str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(values[3]) + "," + str(values[4]) + "," + str(values[5]))

    # Write the updated laptops to the file
    with open("Stocks.txt", "w") as file:
        file.write(''.join(laptopList))

    return laptopList

def bill(buylaptop, Stocks, idNumber, selecting, update):
    product_name = Stocks[idNumber][0]
    company_name = Stocks[idNumber][1]
    userquantity = selecting
    laptop_price = Stocks[idNumber][2].replace("$", "")
    total_price = int(laptop_price) * int(userquantity)

    shipping_cost = 1500

    buylaptop.append([product_name, company_name, userquantity, laptop_price, total_price])

    return buylaptop

# For user_input 2

# Defining quantity validation function
def quantity_validation(Stocks, laptop_id): 

    while True: # Using while loop
        
        quantity = input("Enter the quantity: ") # Asking user for input
        if quantity.isdigit():
            quantity = int(quantity)
            laptop_selected = Stocks[laptop_id][3] # Quantity is accessed using [laptop_id] = key and [3] = index

            if quantity > 0: # If the quantity is greater than zero it returns quantity
                return quantity
            else: # Shows an error message
                print("Quantity error. Please enter a valid quantity.") 
        else:
            print("Error: Please enter a number")
                    

# Defining Items restock function
def Items_restock(Stocks, laptop_id, qnty): 
    Stocks[laptop_id][3] = int(Stocks[laptop_id][3]) + int(qnty) # increase the quantity of the selected laptop
    
    laptop_data = [",".join(map(str, info)) for info in Stocks.values()]
    data_to_write = "".join(laptop_data)

    with open("Stocks.txt", "w") as file:
        file.write(data_to_write)
            

# Defining data for restock function
def data_for_restock(restock_purchased_laptop, Stocks, idNumber, qnty, qnty_restock):
    productname = Stocks[idNumber][0]
    companyname = Stocks[idNumber][1]
    selected_qnty = qnty
    laptopPrice = Stocks[idNumber][2].replace("$", "")
    selectedItemPrice = Stocks[idNumber][2].replace("$", "")
    totalPrice = int(selectedItemPrice) * int(selected_qnty)
    totalPriceDollar = str("$" + str(totalPrice))
    withVat = totalPrice + (totalPrice * 0.13)

    restock_purchased_laptop.append([productname, companyname, selected_qnty, laptopPrice, totalPrice])
    return restock_purchased_laptop