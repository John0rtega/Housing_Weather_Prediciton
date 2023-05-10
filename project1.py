# Import pandas for project
import pandas as pd

# Get csv file and demonstrate the data
homeSales = pd.DataFrame(pd.read_csv('houseMarket2021_2022.csv'))
print(homeSales)


# Get average homes sold in the Summer of 2021 and 2022
def getAvgSummer():
    # Find average for months of June, July, August, and September of 2021/2022
    avg_summer = homeSales[['June_2021', 'June_2022', 'July_2021', 'July_2022',
                            'August_2021', 'August_2022', 'September_2021',
                            'September_2022']].mean(axis=1)
    return avg_summer[0]


# Get average homes sold in the Winter of 2021 and 2022
def getAvgWinter():
    # Find average for months of December, January, February, and March 2021/2022
    avg_winter = homeSales[['December_2021', 'December_2022', 'January_2021',
                            'January_2022', 'February_2021', 'February_2022',
                            'March_2021', 'March_2022']].mean(axis=1)
    return avg_winter[0]


# Compare the averages between Summer and Winter
def compare(summer, winter):
    if summer > winter:
        print("My hypothesis was correct! More houses are sold in the Summer compared to in the Winter of 2021/2022.")
    else:
        print("My hypothesis was wrong! The weather does not affect the housing market!")


# Find how many houses listed in the Summer 2021/2022
def findListingsSummer():
    avg_summer_listing = homeSales[['June_2021', 'June_2022', 'July_2021', 'July_2022',
                                    'August_2021', 'August_2022', 'September_2021',
                                    'September_2022']].mean(axis=1)
    return avg_summer_listing[1]


# Find how many houses listed in the Winter 2021/2022
def findListingsWinter():
    avg_winter_listing = homeSales[['December_2021', 'December_2022', 'January_2021',
                                    'January_2022', 'February_2021', 'February_2022',
                                    'March_2021', 'March_2022']].mean(axis=1)
    return avg_winter_listing[1]


# Find if Summer or Winter has more house listings
def compareListings(summer, winter):
    if summer > winter:
        print("On average, there are more listings in the Summer than in Winter in 2021/2022!")
    else:
        print("On average, there are more listings in the Winter than in Summer in 2021/2022!")


# Main function
def Main():
    print("Hello! This program is created to determine my hypothesis!\n"
          "We will learn if more houses are sold in Summer or Winter using data from 2021/2022 in Essex County.\n"
          "----------------------------------------------------------")
    getAvgSummer()
    getAvgWinter()
    print("The average number of houses sold in the Summer in 2021/2022 is:", getAvgSummer())
    print("The average number of houses sold in the Winter in 2021/2022 is:", getAvgWinter())
    print("")
    compare(getAvgSummer(), getAvgWinter())
    print("----------------------------------------------------------")
    print("For some extra information. Here are the number of listings:\n")
    print("The average number of listing in the Summer is:", findListingsSummer())
    print("The average number of listing in the Winter is:", findListingsWinter())
    compareListings(findListingsSummer(), findListingsWinter())


# Run main function
Main()
