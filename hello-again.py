#import Numpy library
import numpy as np

#define main funtion

def main():
	i = 0                       #declare i, initialize to 0
	
	x = 119.0                   #declare float x
	
	for i in range(120):        #loop i from 0-119
	
		if((i%2)==0):           #i%2 mean remainder of i
	
			x += 3              #makes x = x+3
	
		else:                   #if not even
	
			x -=5               #subtract 5 
	
	s = "%3.2e" % x             #makes a string s containing the value of x in
								#sci notation with 2 decimal places showing
	
	print(s)					#prints s 

if __name__ == "__main__":      #call main
	main()						#run main function
