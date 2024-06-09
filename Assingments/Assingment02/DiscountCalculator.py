''' 
Team Members: 
    · Hasini Jayasekara - 165513235
    · Yasas Maddumage - 170308233
    · Sayona Perera - 169835238
    · Iresha Lakmali - 162279236
    · Nimshi Fernando - 170739239
Description: Assigment 2 Discount Calculator.  
''' 

discountedList =  [
    "candy",
    "eggs",
    "flour",
    "hummus",
    "ice cream",
    "chicken soup",
    "diapers"
]

cart = {}
grandTotal = 0.0
grandDiscount = 0.0

def isItemAvailableInDiscountList(itemName):
    return itemName in discountedList
    
def addOrUpdateCart(itemName, unitPrice, quantity, discountFlag):
    if itemName in cart:
        cart[itemName]['quantity'] += quantity
    else:
        cart[itemName] = {
            'unitPrice': unitPrice,
            'quantity': quantity,
            'discountFlag': discountFlag
        }

def calculateItemDiscountPrice(itemName):
    item = cart[itemName]
    if item['discountFlag'] == 'Y':
        return item['unitPrice'] * item['quantity'] * getRate(item['quantity'])
    return 0

def getRate(qty):
    if 1 < qty < 6:
        return 0.05*qty
    elif qty >= 6:
        return 0.2
    else:
        return 0.0
    
def calculateItemTotal(itemName):
    item = cart[itemName]
    return item['unitPrice'] * item['quantity']

def updateGrandTotal():
    global grandTotal
    grandTotal = sum(calculateItemTotal(item) for item in cart)

def updateGrandDiscount():
    global grandDiscount
    grandDiscount = sum(calculateItemDiscountPrice(item) for item in cart)

def printReceipt():
    global cart
    global grandTotal
    global grandDiscount

    if not cart:
        print("The cart is empty. Exiting...")
        return

    print("\nRECEIPT")
    for i, (itemName, details) in enumerate(cart.items(), 1):
        itemTotal = calculateItemTotal(itemName)
        print(f"{i}. {itemName} {details['quantity']} x $ {details['unitPrice']:.2f} = $ {itemTotal:.2f}")
    print(f"Total: $ {grandTotal:.2f}")
    print(f"You saved: $ {grandDiscount:.2f}")

def getItemName():
     while True:
        itemName = input("Please enter an item of food, or press Enter to exit:").strip().lower()
        if itemName == "":
            return ""
        try:
            int(itemName.strip())
            print("IItem name cannot be a numerical value.")
            continue
        except ValueError:
            return itemName
        
def getItemValue():
    while True:
        try:
            unitPrice = float(input("Item is: "+itemName+". Please enter the price for this item:").strip())
            if unitPrice <= 0:
                print("Unit price must be a positive number.")
                continue
        except ValueError:
            print("Unit price must be a numerical value.")
            continue
        return unitPrice

def getItemQuantity():
    while True:
        try:
            quantity = int(input("Item is: "+itemName+". How many will you purchase:").strip())
            if quantity <= 0:
                print("Number of items must be a positive number.")
                continue
        except ValueError:
            print("Number of items must be a integer value.")
            continue
        return quantity


if __name__ == "__main__":
    print("Shopping Calculator")
    while True:
        itemName = getItemName()
        if itemName == "":
            break
        unitPrice = getItemValue()
        quantity = getItemQuantity()

        if isItemAvailableInDiscountList(itemName):
            discountFlag = 'Y'
        else:
            discountFlag = 'N'
        addOrUpdateCart(itemName, unitPrice, quantity, discountFlag)
    updateGrandTotal()
    updateGrandDiscount()
    printReceipt()