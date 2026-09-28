class Multi_fuel_dispenser_system:
    def __init__(self, fuel):
        self.fuel = fuel


    def get_price(self, fuel):
        if(fuel == "Petrol"):
            return 650
        elif(fuel == "Diesel"):
            return 720
        elif(fuel == "Kerosene"):
            return 550
        elif(fuel == "Gas"):
            return 480
        else:
            raise ValueError("Unknown fuel type")

    def calculate_cost(self, fuel, liter):
        if(liter >= 1 and liter <= 50):
            price_per_liter = self.get_price(fuel) * liter
            return price_per_liter
        else:
            raise ValueError("Liters must be between 1 - 50 !!!")

    def calculate_liter(self, amount_to_spend, amount_of_liter):

        if amount_to_spend < amount_of_liter:
            raise ValueError("Amount must be above a liter price !!!")

        money_remainder = amount_to_spend % amount_of_liter

        if money_remainder % 1 == 0:
            total_liters = amount_to_spend / amount_of_liter
            return total_liters
        else:
            raise ValueError("Invalid liter")

