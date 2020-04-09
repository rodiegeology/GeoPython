ice_cream_rating = 8
sleeping_rating = 10

first_name = input("What is your first name?")
last_name = input("What is your last name?")

happiness_rating = (ice_cream_rating+sleeping_rating)/2

print("ice_cream_rating is ", type(ice_cream_rating))
print("sleeping_rating is ", type(sleeping_rating))
print("happiness_rating is ", type(happiness_rating))

print("My name is {} and I give eating icecream a score of {} out of 10!".format(first_name, ice_cream_rating))
print("I am {} {} and my sleeping enjoyment rating is {} out of 10!".format(first_name,last_name,sleeping_rating))
print("Based on the factors above, my happiness rating is {} out of 10, or {}%".format(happiness_rating, happiness_rating*10))
