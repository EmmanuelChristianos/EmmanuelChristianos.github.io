from subprocess import *
from csvobj import *
from copy import deepcopy
from random import seed
from random import random

def main():
    print("Hello, World!")
    if __name__== "__main__" :
main()





def mutate_modifyAmountOfKeys(jdict):

	'''
	This generates a random number determine if you will be
	adding or substracting entries from the dict and then 
	generates another random numbers as to how many entries will
	be altered. 

	It then alters the dict passed in.
	'''

	#choose = random.randrange(0,2)
	amount = random.randrange(0,100)

	while (amount <= len(jdict)){
		amount = random.randrange(0,100)
	}

	for i in range(len(jdict),amount):
		
		jdict[f'{i}'.encode()] = ["XXX"]



