# Created and commented by Shane Borges (F3stive-Ya)
# Description: A program that randomly creates cars and races them


import random


#Parent Class
class Car:
    def __init__(self, brand, year, color, make, speed=0):
        self.brand = brand
        self.year = year
        self.color = color
        self.speed = speed
        self.make = make  # 'electric' or 'gas'

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        if speed < 0:
            raise ValueError("Speed cannot be negative")
        self.speed = speed

    #abstract methods
    def __str__(self):
        pass
            

    def move(self):
        pass


#ElectricCar subclass
class ElectricCar(Car):
    def __init__(self, brand, year, color):
        super().__init__(brand, year, color, "electric")
        self.battery = 0
        
    def charge(self):
        self.battery = 1000  # Fully recharge
        return "The battery is fully charged."

    def __str__(self):
        return f"ElectricCar({self.color}, {self.brand}, {self.year}, Speed={self.speed}, Battery={self.battery})"
    
    def move(self, hours):
        #deduct battery by hours driven
        if self.battery >= hours:
            self.battery -= hours
            return self.color,self.brand,hours,self.battery
        else:
            actual_distance = self.battery
            self.battery = 0
            return self.color,self.brand,actual_distance


# GasCar subclass
class GasCar(Car):
    def __init__(self, brand, year, color):
        super().__init__(brand, year, color, "gas")
        self.fuel = 0

    def fuel_up(self):
        self.fuel = 1000  # Fully refuel
        return "The gas tank is full."

    def __str__(self):
        #return desscriptive string
        return f"GasCar({self.color}, {self.brand}, {self.year}, Speed={self.speed}, Gas={self.fuel})"
    
    def move(self, hours):
        #deduct fuel by hours driven
        if self.fuel >= hours:
            self.fuel -= hours
            return self.color,self.brand,hours,self.fuel
        else:
            actual_distance = self.fuel
            self.fuel = 0
            return self.color,self.brand,actual_distance


# CarGame class
class CarGame:
    def __init__(self, brands, colors, year_start, year_end):
        self.brands = brands
        self.colors = colors
        self.year_start = year_start
        self.year_end = year_end
        self.cars = []

    def get_cars(self, num_cars):
        self.cars = []
        for _ in range(num_cars):
            brand = random.choice(self.brands)
            color = random.choice(self.colors)
            year = random.randint(self.year_start, self.year_end)
            make = random.choice(['electric', 'gas']) #random choose car

            if make == "electric":
                car = ElectricCar(brand, year, color)
            else:
                car = GasCar(brand, year, color)

            self.cars.append(car)
        return self.cars

    def check_cars_in(self):
        electric_count = 0
        gas_count = 0

        #fueling and charging cars
        for car in self.cars:
            if car.make == "electric":
                car.charge()
                electric_count += 1
            elif car.make == "gas":
                car.fuel_up()
                gas_count += 1

        return electric_count, gas_count

    def car_race(self,hours):
        
        print(f"\nRacing for {hours} hours! Ready...Set...Go!")
    
        # Initialize variables
        race_results = []  # List to store car details and distance
        max_distance = 0  # Track the maximum distance traveled
        winners = []  # List of winners
        speeds = [] #List of car speeds
        distances = [] #List of car distances

        #Race each car
        for car in self.cars:
            speed = random.randint(30, 100)  # Random speed
            car.set_speed(speed)  # Set speed
            speeds.append(car.speed)
            intended_distance = car.speed * hours  # Distance based on speed and time
            distances.append(intended_distance)

            #Move the car and calculate actual distance traveled
            if isinstance(car, ElectricCar):
                car.move(intended_distance)
                actual_distance = min(intended_distance, car.battery)
            elif isinstance(car, GasCar):
                car.move(intended_distance)
                actual_distance = min(intended_distance, car.fuel)
            
            distances.append(actual_distance)

            # Update race results
            race_results.append((car, actual_distance))

            # Determine winners
            if actual_distance > max_distance:
                max_distance = actual_distance
                winners = [car]
            elif actual_distance == max_distance:
                winners.append(car)

        #Print race details
        print(f"\nSpeeds: {speeds}\n\nDistance: {distances}")
        
        #Announce winner(s)
        if len(winners) == 1:
            print(f"\nThe winner is: \n\t{winners[0]}!")
        else:
            print(f"\nIt's a tie! The winners are:")
            for winner in winners:
                print(f"\t{winner}")

        #Stop all cars
        for car in self.cars:
            car.set_speed(0)

# == DO NOT MODIFY ANY CODE BELOW THIS LINE ==
    
def main():
    brands = ['Benz', 'BMW', 'Ford', 'Honda', 'Toyota']
    colors = ['Black', 'Blue', 'Grey', 'Red', 'White']
    year_start, year_end = 1999, 2023
    game = CarGame(brands, colors, year_start, year_end)

    print('== Step 1: Getting new cars ===')
    game.get_cars(5) # 5 random cars
    for car in game.cars: print(f'\t{car}') # speed & energy = 0

    print('\n== Step 2: Checking cars in race ===')
    e_car, g_car = game.check_cars_in()   
    print(f'\t## We have {e_car} ElectricCars, {g_car} GasCars.')
    for car in game.cars: print(f'\t{car}') # fully charged/fueled

    print('\n=== Step 3: Starting car race ===')
    game.car_race(5) # 5 hours race, print winners
    
    print('\n=== Step 4: Race finished ===')
    for car in game.cars: print(f'\t{car}') # check speed & energy
    print('\n== Thank You! ==\n\n')

if __name__ == '__main__':
    main()