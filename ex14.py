from sys import argv

script, marta = argv
prompt = '> '

print "Hi %s, I'm the %s script. " % (marta, script)
print "I'd like to ask you a few questions. "
print "Do you like me %s? " % marta
likes = raw_input(prompt)

print "Where do you live %s? " % marta
lives = raw_input(prompt)

print "What kind of computer do you have? "
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)