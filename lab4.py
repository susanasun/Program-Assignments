groceries = {"chicken": "$1.59", "beef": "$1.99", "cheese": "$1.00", "milk": "$2.50"}
NBA_players = {"Lebron James": 23, "Kevin Durant": 35, "Stephen Curry": 30, "Damian Lillard": 0}
PHONE_numbers = {"Mom": 5102131197, "Dad": 5109088833, "Sophia": 5106939622}
shoes = {"Jordan 13": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk": 20}

chicken_price = groceries["chicken"]
print(chicken_price)

beef_price = groceries["beef"]
print(beef_price)

cheese_price = groceries["cheese"]
print(cheese_price)

milk_price = groceries["milk"]
print(milk_price)

Lebron_number = NBA_players["Lebron James"]
print(Lebron_number)

Kevin_number = NBA_players["Kevin Durant"]
print(Kevin_number)

NBA_players["Lebron James"] = 6
jersey_number = NBA_players["Lebron James"]
print(jersey_number)

NBA_players["Lebron James"] -= 17
jersey_number = NBA_players["Lebron James"]
print(jersey_number)



def total_price(item1, item2):

    sum = groceries[item1] + groceries[item2]

    print("The total price of",item1, "and", item2, "is",  sum)

    return sum 

total_price("Chicken", "Cheese")


def price_difference(item1, item2):

    difference = groceries[item1] - groceries[item2]

    print("The difference between", item1, "and", item2, "is", abs(round(difference, 2)))

    return difference

price_difference("Cheese", "Chicken")



def Restock(shoe, amount):

    Updated_shoe = shoes[shoe] * amount 

    shoes["Jordan 13"] = Updated_shoe

    return(shoes)

Restock("Jordan 13", 3)



#Step V

def Clearance_sale(shoe, amount):

    Updated_shoe = shoes[shoe] / amount 

    shoes["Air Max"] = Updated_shoe 

    return(shoes)

Clearance_sale("Air Max", 3)



def Mix_Numbers(Name1, Name2):

    Updated_shoe1 = PHONE_numbers[Name2]

    Updated_shoe2 = PHONE_numbers[Name1]

    PHONE_numbers["Mom"] = Updated_shoe1

    PHONE_numbers["Sophia"] = Updated_shoe2

    print(PHONE_numbers)



Mix_Numbers("Mom", "Sophia")

empty_list = []

city_list = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
print(city_list)
print(city_list[5])
print(city_list[0])
print(city_list[7])
print(city_list[2])

three_cities = city_list[0:3]
print(three_cities)

US_cities = city_list[4:8]
print(US_cities)
city_list[0] = "San Francisco"
city_list[2] = "Brooklyn"
city_list[7] = "Hollywood"
city_list[5] = "Tampa"
print(city_list)

fruit_list = ["Strawberry", "Apple", "Grape", "Mango", "Banana", "Pear", "Watermelon", "Pineapple", "Raspberry", "Blackberry", "Blueberry"]
print(fruit_list)
print(fruit_list[0])
print(fruit_list[1])
print(fruit_list[2])

def Every_city():
    Longest_city_name = "a"
    i = 0 
    while i < len(city_list):
        print(city_list[i])
        x = city_list[i]
        if len(city_list[i]) > len(Longest_city_name):
            Longest_city_name = x 
            i += 1

    return((Longest_city_name))

Every_city()
 

def Organizing_cities():
    for i in range(0, 16):
        b = city_list[i]
        a = city_list[i + 1]
        if len(b) >= len(a):
            i += 1
    else:
        city_list.remove(b)
        city_list.append(b)

    return city_list

Organizing_cities()


def fruit_with_three_letter_name():
    i = 0
    while i < len(fruit_list):
        if len(fruit_list[i]) == 3:
            print(fruit_list[i])
            i = i + 1

fruit_with_three_letter_name()