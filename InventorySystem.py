from dataclasses import dataclass, field
import datetime
from datetime import datetime, date
import json
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import sqlite3

@dataclass
class Product:
    idproduct: int
    nameproduct: str
    stockproduct: int
    codeproduct: int
    prizeproduct: int = 0
    daily_total: int = 0

@dataclass
class DailyTotal:
    date: str
    total: float

# Database setup - körs en gång
conn = sqlite3.connect('inventory.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS products
             (idproduct INTEGER PRIMARY KEY AUTOINCREMENT,
              nameproduct TEXT, stockproduct INTEGER, codeproduct INTEGER UNIQUE,
              prizeproduct INTEGER, daily_total INTEGER)''')
c.execute('''CREATE TABLE IF NOT EXISTS daily_totals
             (date TEXT PRIMARY KEY, total REAL)''')
conn.commit()

def save_product(product_list):
    """Sparar alla produkter till databas"""
    c.execute("DELETE FROM products")
    for p in product_list:
        c.execute("INSERT INTO products VALUES (?,?,?,?,?,?)", 
                 (p.idproduct, p.nameproduct, p.stockproduct, p.codeproduct, p.prizeproduct, p.daily_total))
    conn.commit()

def load_product():
    """Laddar alla produkter från databas"""
    product = []
    c.execute("SELECT * FROM products")
    for row in c.fetchall():
        product.append(Product(*row))
    return product

def save_daily_totals(daily_list):
    """Sparar dagliga totals till databas"""
    c.execute("DELETE FROM daily_totals")
    for d in daily_list:
        c.execute("INSERT INTO daily_totals VALUES (?,?)", (d.date, d.total))
    conn.commit()

def load_daily_totals():
    """Laddar dagliga totals från databas"""
    daily_list = []
    c.execute("SELECT * FROM daily_totals")
    for row in c.fetchall():
        daily_list.append(DailyTotal(*row))
    return daily_list


def appendproduct(product):
    NameProduct = input("Enter Name of Product: ")
    Stock = int(input("Enter Stock of Products: "))
    CodeProduct= int(input("Enter Code of Product: "))
    prizeProduct = int(input("Enter Prize of Product: "))
    
    try:
        for info in product:
            if info.codeproduct == CodeProduct:
                print("There is already one")
                return
        new_id = len(product) + 1
        Productinfo = Product(new_id, NameProduct, Stock, CodeProduct,prizeProduct)
        product.append(Productinfo)
        save_product(product)  # SPARA TILL DB
        print("Appended New Product")
    except ValueError:
        print("Error")


def updateproductstock(product):
    while True:
        try:
            CodeProduct = int(input("Enter Code: "))
        except ValueError:
            print("❌ Error: Enter a number")
            continue

        found = False

        for info in product:
            if info.codeproduct == CodeProduct:
                info.stockproduct += 1
                save_product(product)
                print("✅ Stock product added")
                found = True
                break

        if not found:
            print("❌ No product with that code found")

        again = input("Update another product? (y/n): ").lower()

        if again != 'y':
            print("Exiting stock update")
            break

def ChangeInformationAboutProduct(product_list):
    while True:
        print("\n📦 Product Update Menu 📦")
        print("1. 🔢 Change product code")
        print("2. ✏️  Change product name")
        print("3. 💰 Change product price")
        print("0. 🚪 Exit")

        try:
            choice = int(input("👉 Enter Choice: "))
        except ValueError:
            print("❌ Error: Enter a number")
            continue

        if choice == 0:
            print("🚪 Exiting menu")
            break

        elif choice == 1:
            try:
                CodeProduct = int(input("🔎 Enter CodeProduct: "))
            except ValueError:
                print("❌ Invalid code")
                continue

            for p in product_list:
                if p.codeproduct == CodeProduct:
                    try:
                        newcode = int(input("🆕 Enter New Code: "))
                    except ValueError:
                        print("❌ Invalid new code")
                        continue

                    p.codeproduct = newcode
                    save_product(product_list)
                    print("✅ Code updated:", p.codeproduct)
                    break
            else:
                print("❌ Product not found")

        elif choice == 2:
            NameProduct = input("🔎 Enter NameProduct: ")

            for p in product_list:
                if p.nameproduct == NameProduct:
                    NewName = input("🆕 Enter New Name: ")
                    p.nameproduct = NewName
                    save_product(product_list)
                    print("✅ Name updated:", p.nameproduct)
                    break
            else:
                print("❌ Product not found")

        elif choice == 3:
            try:
                CodeProduct = int(input("🔎 Enter CodeProduct: "))
            except ValueError:
                print("❌ Invalid code")
                continue

            for p in product_list:
                if p.codeproduct == CodeProduct:
                    try:
                        NewPrice = float(input("🆕 Enter New Price: "))
                    except ValueError:
                        print("❌ Invalid price")
                        continue

                    p.prizeproduct = NewPrice
                    save_product(product_list)
                    print("✅ Price updated:", p.prizeproduct)
                    break
            else:
                print("❌ Product not found")

        else:
            print("❌ Invalid choice")


def removeproduct(product):
    CodeProduct= int(input("Enter Code:"))
    try:
        for info in product:
            if info.codeproduct == CodeProduct:
                product.remove(info)
                save_product(product)  # SPARA TILL DB
                print("removed product")
                return
        print("There nothing")
    except ValueError:
        print("Error")

def showproduct(products):
    print("-" * 50)
    print(f"{'ID':<10}{'Name':<15}{'Stock':<10}{'Code':<10}{'Prize':<10}")
    print("-" * 50)

    for p in products:
        print(f"{p.idproduct:<10}{p.nameproduct:<15}{p.stockproduct:<10}{p.codeproduct:<10}{p.prizeproduct:<10}")
        print("-" * 50)

def ShowProductStatusThatNeedsToBuy(product):
    for info in product:
        if info.stockproduct < 5:
            print("-" * 50)
            print("Warning!")
            print("-" * 50)
            print("This is the Products that needs to buy")
            print("-" * 50)
            print(f"{'ID':<10}{'Name':<15}{'Stock':<10}{'Code':<10}{'Prize':<10}")
            print("-" * 50)
            print(f"{info.idproduct:<10}{info.nameproduct:<15}{info.stockproduct:<10}{info.codeproduct:<10}{info.prizeproduct:<10}")
            print("-" * 50)

def menu():
    print("\n" + "="*50)
    print("         📦 INVENTORY MANAGEMENT SYSTEM 📦")
    print("="*50)
    print("\n1. ➕ Add product\n")
    print("2. ➖ Remove product\n")
    print("3. 📋 Show all products\n")
    print("4. 🔄 Update product stock\n")
    print("5. ⚠️  Show products that need restock\n")
    print("6. 💳 Customer buying\n")
    print("7. 📋 Change information about product\n")
    print("8. 📊 Analysis and Sales Curves\n")
    print("0. 🚪 Exit\n")
    print("="*50)


def CustomerBuyingProduct(product, BuyingProduct, appendnumberinfo, ArrayOfSum):
    while True:
        print("\n🛒 CUSTOMER BUYING")
        print("1. Buy product")
        print("2. End shopping session")
        
        try:
            choice = int(input("Enter (1-2): "))
        except ValueError:
            print("❌ Error: Enter a number")
            continue

        if choice == 1:
            try:
                CodeProduct = int(input("Enter Product Code: "))
            except ValueError:
                print("❌ Error: Enter a number")
                continue

            found = False

            for info in product:
                if info.codeproduct == CodeProduct:
                    found = True

                    if info.stockproduct <= 0:
                        print("❌ Product out of stock!")
                        break

                    # Update stock
                    info.stockproduct -= 1

                    # Get price
                    prize = info.prizeproduct

                    # Update cart
                    appendnumberinfo.append(prize)
                    BuyingProduct.append(prize)

                    # Update product daily total
                    info.daily_total += prize

                    # Save product changes
                    save_product(product)

                    # Handle daily totals
                    today = datetime.now().date()
                    daily_entry_exists = False

                    for entry in ArrayOfSum:
                        if entry.date == today:
                            entry.total += prize
                            daily_entry_exists = True
                            break

                    if not daily_entry_exists:
                        ArrayOfSum.append(DailyTotal(date=today, total=prize))

                    # Save daily totals
                    save_daily_totals(ArrayOfSum)

                    # Output
                    print(f"📦 Cart: {appendnumberinfo}")
                    print(ArrayOfSum)
                    break

            if not found:
                print("❌ No product with that code found")

        elif choice == 2:
            final_sum = sum(appendnumberinfo)

            if final_sum > 0:
                print("\n🧾 PURCHASE SUMMARY")
                print(f"Total: {final_sum:.2f}")

                for item in ArrayOfSum:
                    print(f"🗓️ {item.date} | Total: {item.total:.2f}")
            else:
                print("No items purchased.")

            break

        else:
            print("Enter 1 or 2 only")

def AnalysCurve(ArrayOfSum):
    x_days = list(range(1, 31))
    y_totals = [0] * 30  

    for i, item in enumerate(ArrayOfSum):
        if i < 30: 
            y_totals[i] = item.total

    for day, total in zip(x_days, y_totals):
        print(f"Day {day} | Total: {total:.2f}")

    median_sum = np.median(y_totals)
    mode_result = stats.mode(y_totals, keepdims=True).mode[0]
    average_sum = np.mean(y_totals)

    plt.plot(x_days, y_totals, marker="o", markersize=4, color="#e41a1c", label="Daily Total") 
    plt.axhline(y=average_sum, color="#377eb8", linestyle="--", label=f"Average: {average_sum:.2f}")   
    plt.axhline(y=median_sum, color="#4daf4a", linestyle=":", label=f"Median: {median_sum:.2f}")     
    plt.axhline(y=mode_result, color="#ff7f00", linestyle="-.", label=f"Most Frequent: {mode_result:.2f}") 
    plt.xlabel("Day")
    plt.ylabel("Money Earned")
    plt.title("The sum of money you have earned")
    plt.grid()
    plt.legend()
    plt.show()

def IfStateForProgram():

    product = load_product()
    BuyingProduct = []
    appendnumberinfo = []
    ArrayOfSum = load_daily_totals()
    
    while True:
        menu()
        try:
            choice = int(input("Enter your choice (0-7): "))
        except ValueError:
            print("❌ Please enter a number!")
            continue
            
        if choice == 1:
            appendproduct(product)
        elif choice == 2:
            removeproduct(product)
        elif choice == 3:
            showproduct(product)
        elif choice == 4:
            updateproductstock(product)
        elif choice == 5:
            ShowProductStatusThatNeedsToBuy(product)
        elif choice == 6:
            CustomerBuyingProduct(product,BuyingProduct,appendnumberinfo,ArrayOfSum)
        elif choice ==7:
            ChangeInformationAboutProduct(product)   
        elif choice == 8:
            AnalysCurve(ArrayOfSum)
        elif choice == 0:
            print("\n👋 Thank you for using the system!")
            break
        else:
            print("❌ Invalid choice! Enter 0-7 only")

if __name__ == "__main__":
    IfStateForProgram()