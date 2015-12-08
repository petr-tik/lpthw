# assign the variable 'cars' a value of 100
cars = 100
# assign the variable 'space_in_a_car' a floating point value of 4.0
space_in_a_car = 4
# assign the variable 'drivers' a value of 30
drivers = 30
# assign the variable 'passengers' a value of 90
passengers = 90
# assign the variable 'cars_not_driven' a value equaling the difference between the number of cars and drivers
cars_not_driven = cars - drivers
# the variable cars_driven is equal to the number of drivers
cars_driven = drivers
# the variable for carpool capacity is calculated as the product of cars driven and space in a car
carpool_capacity = cars_driven * space_in_a_car
# the variable for average passengers per car is the result of division of the number of passengers by the number of cars driven
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available"
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


# = assigns a value to a variable
# == checks if two values/variables are equal

# x = 100 is better than
# x=100


