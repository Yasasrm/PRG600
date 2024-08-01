''' 
Team Members: 
    · Hasini Jayasekara - 165513235
    · Yasas Maddumage - 170308233
    · Sayona Perera - 169835238
    · Iresha Lakmali - 162279236
    · Nimshi Fernando - 170739239
Description: Assigment 4 Store stock calculator.  
''' 

import csv
import re
import math
import sys

# Function to import CSV file with current stock
def readCsv(filename):
    stock = {}
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            itemCode, itemName, quantity, price = row
            stock[itemCode] = [itemName, int(quantity), getPrice(price), 0]
    return stock

#  Function to get item price from the csv
def getPrice(stringPrice):
    try:
        return float(stringPrice)
    except:
        return float(re.sub(r'[^\d.]', '', stringPrice))

# Function to display the current stock report
def displayCurrentStock(stock):
    print(f"{'Current Stock Report' :^100}")
    print(f"{'Item Code' :^25} | {'Item Name' :^25} | {'Quantity' :^25} | {'Price' :^25} ")
    print("-"*100)
    for itemCode, itemDetails in stock.items():
        print(f"{itemCode :^25} | {itemDetails[0] :^25} | {itemDetails[1] :^25} | {"$"+str(itemDetails[2]) :^25}")
    print("-"*100)

# Function to handle sales
def handleSales(stock):
    while True:
        user_input = input("Enter a number to indicate a sale or 'e' to exit: ")
        if user_input.lower() == 'e':
            break

        if user_input not in stock:
            print("Invalid item code.")
            continue

        if getCurrentStock(stock[user_input]) < 1:
            print("Not enough stock.")
        
        stock[user_input][3] += 1

# Function to display the total sales report
def displayTotalSales(stock):
    print("")
    print(f"{'Total Sales Report' :^100}")
    print(f"{'Item' :^25} | {'Sales' :^25} | {'Price per item' :^25} | {'Total' :^25} ")
    print("-"*100)
    for _,itemDetails in stock.items():
        qty = getSalesQty(itemDetails)
        if qty > 0:
            print(f"{itemDetails[0] :^25} | {qty :^25} | {"$"+str(itemDetails[2]) :^25} | {"$"+str(qty * itemDetails[2]) :^25}")
    print("-"*100)

# Function to get total sales quantity
def getSalesQty(itemDetails):
     return itemDetails[3] if itemDetails[1] - itemDetails[3] > 0 else itemDetails[1]


# Function to display the lost sales report
def displayTotalLostSales(stock):
    print("")
    print(f"{'Lost Sales Report' :^100}")
    print(f"{'Item' :^25} | {'Sales' :^25} | {'Price per item' :^25} | {'Total' :^25} ")
    print("-"*100)
    for _,itemDetails in stock.items():
        qty = getLostSalesQty(itemDetails)
        if qty > 0:
            print(f"{itemDetails[0] :^25} | {qty :^25} | {"$"+str(itemDetails[2]) :^25} | {"$"+str(qty * itemDetails[2]) :^25}")
    print("-"*100)

# Function to get total sales quantity
def getLostSalesQty(itemDetails):
     return 0 if itemDetails[1] - itemDetails[3] > 0 else itemDetails[3] - itemDetails[1]

# Function to display the restock report
def displayRestock(stock):
    print("")
    print(f"{'Restock Report' :^150}")
    print(f"{'Item' :^25} | {'Demand' :^25} | {'20%' :^25} | {'Total Demand' :^25} | {'Current Stock' :^25} | {'From Warehouse' :^25} ")
    print("-"*160)
    for _,itemDetails in stock.items():
        qty = getCurrentStock(itemDetails)
        print(f"{itemDetails[0] :^25} | {itemDetails[3] :^25} | {math.ceil(itemDetails[3]*0.2) :^25} | {math.ceil(itemDetails[3]*1.2) :^25} | {qty :^25} | {getFromWarehouseQty(itemDetails) :^25}")    
    print("-"*160)

# Function to get current quantity
def getCurrentStock(itemDetails):
     return itemDetails[1] - itemDetails[3] if itemDetails[1] - itemDetails[3] > 0 else 0

# Function to get from warehouse quantity
def getFromWarehouseQty(itemDetails):
     return 0 if getCurrentStock(itemDetails) > math.ceil(itemDetails[3]*1.2) else math.ceil(itemDetails[3]*1.2)

# Function to generate updated stock report to CSV
def generateUpdatedStockReport(stock, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Item Code", "Item Name", "Quantity", "Price"])
        for itemCode, itemDetails in stock.items():
            writer.writerow([itemCode, itemDetails[0], getCurrentStock(itemDetails)+ getFromWarehouseQty(itemDetails), f"${itemDetails[2]}"])

# Entry point
if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python <fileName>.py <sourceFileAs_arg1> <destinationFileAs_arg2>")
        sys.exit(1)

    stockFilename = sys.argv[1]
    updatedStockFilename = sys.argv[2]

    stock = readCsv(stockFilename)
    displayCurrentStock(stock)
    handleSales(stock)
    displayTotalSales(stock)
    displayTotalLostSales(stock)
    displayRestock(stock)
    generateUpdatedStockReport(stock, updatedStockFilename)
    print("Updated stock report generated.")
