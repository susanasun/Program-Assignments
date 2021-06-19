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
