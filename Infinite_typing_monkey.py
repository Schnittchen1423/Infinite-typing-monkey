#Preperation
import random
import string
import time
import os

generation = 0
floatgen = 0.0
seconds = 0.0
found = False
#Select

os.system("clear")
print("Please type a word.")
print("Notice: Only lowercase letters, a-z. No special characters.")

searchFor = raw_input()
searchLenghts = len(searchFor)

#Generation

while found == False:
	
	generation = generation + 1
	text = ''.join(random.choice(string.ascii_lowercase) for i in range(searchLenghts))
	print ("Generated text: %s Generation number: %s" % (text, generation))
	time.sleep(0.05)

	if text == searchFor:
		floatgen = float(generation)
		seconds = floatgen / 20
		found = True
		print("Found %s at generation %s. Estimated time: %s seconds" % (searchFor, generation, seconds)) 
		os.system("exit")