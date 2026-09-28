from datetime import datetime

from multi_fuel_dispenser_system import Multi_fuel_dispenser_system

current_date = datetime.now().strftime("%d/%m/%Y")

my_dispenser_system = Multi_fuel_dispenser_system("Kerosene")

product = ""
amount = 0
liter = 0

transactions = []

while(True):
    available_petroleum = """
    
    APPLICATION SAMPLE
    
    Welcome to GBeda Station!
    Available Petroleum
        1. Buy Petroleum
        2. Show Transaction History
        0. Exit
    """

    print(available_petroleum)
    choice = int(input("Enter operation: "))

    match(choice):
        case 1:
            print("""
            Available petroleum
            1.      Petrol => 650/Liter
            2.      Diesel => 720/Liter
            3.      Kerosene => 550/Liter
            4.      Gas => 480/Liter
            """)

            operation = int(input("Enter operation: "))
            liter_or_amount = input("Liter OR Amount: ")

            if(liter_or_amount == "amount" or liter_or_amount == "Amount"):
                match(operation):
                    case 1:
                        product = "Petrol"
                        amount = int(input("How much Petrol are you buying(650/L): "))

                        liter = int(my_dispenser_system.calculate_liter(amount, 650))

                    case 2:
                        product = "Diesel"
                        amount = int(input("How much Diesel are you buying(720/L): "))

                        liter = int(my_dispenser_system.calculate_liter(amount, 720))

                    case 3:
                        product = "Kerosene"
                        amount = int(input("How much Kerosene are you buying(550/L): "))

                        liter = int(my_dispenser_system.calculate_liter(amount, 550))

                    case 4:
                        product = "Gas"
                        amount = int(input("How much Gas are you buying(480/L): "))

                        liter = int(my_dispenser_system.calculate_liter(amount, 480))

                    case _:
                        print("Invalid input")

            elif(liter_or_amount == "liter" or liter_or_amount == "Liter"):
                match(operation):
                    case 1:
                        product = "Petrol"
                        liter = input("How Many Liters of Petrol are you buying(650/L): ")

                        if not liter.isdigit():
                            print("Baba enter a valid number no characters allowed!")
                            break

                        liter = int(liter)

                        if liter >= 1 and liter <= 50 and liter:
                            amount = my_dispenser_system.calculate_cost(product, liter)

                        else:
                            print("Liters must be between 1 - 50 !!!")
                            break

                    case 2:
                        product = "Diesel"
                        liter = input("How Many Liters of Diesel are you buying(720/L): ")

                        if not liter.isdigit():
                            print("Baba enter a valid number no characters allowed!")
                            break

                        liter = int(liter)

                        if liter >= 1 and liter <= 50:
                            amount = my_dispenser_system.calculate_cost(product, liter)

                        else:
                            print("Liters must be between 1 - 50 !!!")
                            break

                    case 3:
                        product = "Kerosene"
                        liter = input("How Many Liters of Kerosene are you buying(550/L): ")

                        if not liter.isdigit():
                            print("Baba enter a valid number no characters allowed!")
                            break

                        liter = int(liter)

                        if liter >= 1 and liter <= 50:
                            amount = my_dispenser_system.calculate_cost(product, liter)

                        else:
                            print("Liters must be between 1 - 50 !!!")
                            break

                    case 4:
                        product = "Gas"
                        liter = input("How Many Liters of Gas are you buying(480/L): ")

                        if not liter.isdigit():
                            print("Baba enter a valid number no characters allowed!")
                            break

                        liter = int(liter)

                        if liter >= 1 and liter <= 50:
                            amount = my_dispenser_system.calculate_cost(product, liter)

                        else:
                            print("Liters must be between 1 - 50 !!!")
                            break

                    case _:
                        print("Invalid input")

            else:
                print("Invalid input")

            print("\nCustomers Transaction Receipt")
            print("======================================")

            if product == "":
                print("No transaction recorded yet!")

            else:
                print("=    Product:", product, "                =")
                print("=    Amount:", amount, "                   =")
                print("=    Liters: ", liter, "L", "                      =", sep="")
                print("=    Thank you For your Patronage    =")
            print("======================================")
            print("Saving Transaction History......")

            transactions.append([product, amount, liter])
        case 2:
            print("\nAll Transactions")
            print("======================================")

            if len(transactions) == 0:
                print("No transaction recorded yet!")

            else:
                for index in transactions:
                    print("======================================")
                    print("=    Product:", index[0], "                =")
                    print("=    Amount:", index[1], "                   =")
                    print("=    Liters: ", index[2], "L", "                      =", sep= "")
                    print("=    Date:", current_date, "               =")
                    print("======================================\n\n")

        case 0:
            print("Thank you for using GBeda Station!")
            break

        case _:
            print("Invalid input")
