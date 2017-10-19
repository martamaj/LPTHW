# this defines x 
x = "There are %d types of people." % 10
# this defines binary
binary = "binary"
# this defines do_not
do_not = "don't"
# this defines y, using binary and do_not 
y = "Those who know %s and those who %s." % (binary, do_not)

# this prints x 
print x
# this prints y 
print y 

# this prints a string with an x 
print "I said: %r." % x 
# this prints a string with an y 
print "I also said: '%s'." % y 

# this defines hilarious 
hilarious = False
# this defines joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

# this prints joke evaluation and hilarious
print joke_evaluation % hilarious

# this defines w 
w = "This is the left side of..."
# this defines e 
e = "a string with a right side."

# this prints w and e 
print w + e