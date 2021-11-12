from FoodCropsDataset import *


end = False

print("Welcome to the Food Crops database researcher")
fcd = FoodCropsDataset()

while not end:
    print("We will define what you are looking for.")
    print("You can look at the different option of research in the source folder")
    print("")
    commodityGroup = None
    indicatorGroup = None
    geographicalLocalisation = None
    unit = None

    commodityGroup = input("Which commodity do you search ?  ")
    indicatorGroup = input("Which type of indicator are you searching ?  ")
    geographicalLocalisation = input("Where is the factory you are searching for?  ")
    unit = input("Which is the unit of your commodity ?  ")

    result = fcd.findmeasurements(commodityGroup, indicatorGroup, geographicalLocalisation, unit)

    for measurement in result:
        print(measurement.describe())
    print(" Number of measurements corresponding: ", len(result))

    print("")
    exit = input("Do u wanna do another research bro? yes/no")
    if exit == "yes" or "Yes":
        end = True
