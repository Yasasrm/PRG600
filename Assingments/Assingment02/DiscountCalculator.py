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

def isValidNumber(value):
    try:
        return float(value) > 0
    except ValueError:
        return False
    
def addOrUpdateCart(itemName, unitPrice, quantity, discountFlag):
    if itemName in cart:
        cart[itemName]['quantity'] += quantity
    else:
        cart[itemName] = {
            'unit_price': unitPrice,
            'quantity': quantity,
            'discount_flag': discountFlag
        }

def calculateItemDiscountPrice(itemName):
    item = cart[itemName]
    if item['discount_flag'] == 'Y':
        return item['unit_price'] * item['quantity'] * getRate(item['quantity'])
    return 0

def getRate(qty):
    if 1 < qty < 6:
        return 0.05
    elif qty >= 6:
        return 0.2
    else:
        return 0.0
    
def calculateItemTotal(itemName):
    item = cart[itemName]
    return item['unit_price'] * item['quantity']

def updateGrandTotal():
    global grandTotal
    grandTotal = sum(calculateItemTotal(item) for item in cart)

def updateGrandDiscount():
    global grandDiscount
    grandDiscount = sum(calculateItemDiscountPrice(item) for item in cart)

def printReceipt():
    global grandTotal
    global grandDiscount
    print("\nRECEIPT")
    for i, (itemName, details) in enumerate(cart.items(), 1):
        itemTotal = calculateItemTotal(itemName)
        print(f"{i}. {itemName} {details['quantity']} x $ {details['unit_price']:.2f} = $ {itemTotal:.2f}")
    print(f"Total: $ {grandTotal:.2f}")
    print(f"You saved: $ {grandDiscount:.2f}")

if __name__ == "__main__":
    print("Shopping Calculator")
    while True:
        itemName = input("Please enter an item of food, or press Enter to exit:").strip().lower()
        if itemName == "":
            break
        if isItemAvailableInDiscountList(itemName):
            discount_flag = 'Y'
        else:
            discount_flag = 'N'

        try:
            unit_price = float(input("Item is: "+itemName+". Please enter the price for this item:").strip())
            if unit_price <= 0:
                print("Unit price must be a positive number.")
                continue
        except ValueError:
            print("Unit price must be a numerical value.")
            continue

        try:
            quantity = int(input("Item is: "+itemName+". How many will you purchase:").strip())
            if quantity <= 0:
                print("Number of items must be a positive number.")
                continue
        except ValueError:
            print("Number of items must be a numerical value.")
            continue

        addOrUpdateCart(itemName, unit_price, quantity, discount_flag)

    updateGrandTotal()
    updateGrandDiscount()
    printReceipt()