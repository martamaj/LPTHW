# this explains how many cars 
cars = 100
# this explains how much space 
space_in_a_car = 4
# this explains how many drivers
drivers = 30
# this explains how many passengers
passengers = 90
# this substracts drivers from cars 
cars_not_driven = cars - drivers
# this equals cars to drivers 
cars_driven = drivers
# this multiplies cars with passengers to create capacity
carpool_capacity = cars_driven * space_in_a_car
# this divides passengers by cars driven 
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpoool today."
print "We need to put about", average_passengers_per_car, "in each car."

print "Hey %s there." % "you"