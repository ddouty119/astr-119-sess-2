import numpy as np

def main():
	i = 0		#i is integer initialized to 0
	n = 10		#n initialized to 10
	x = 119.0 	#x in float with value 119
	
	
	#numpy can declare arrays very quickly
	
	y = np.zeros(n, dtype=float)	#declares 10 zeros
	
	#can iterate through elements of y by passing numbers thru an index
	
	for i in range(n):		#i in range [0,n-1]
		y[i] = 2.0 * float(i) +1.0		#set y = 2i+1 as float
		
	#iterate thru array
	
	for y_element in y: 
		print(y_element)
		
#execute main function

if __name__ == "__main__":
	main()