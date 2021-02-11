#!/usr/bin/env python3
import math
import sys
num = int(input("---/\/\ enter a number & check if it's prime: "))
def prime_check(b):
	if (b==2):
		return True
	elif ((b<2) or ((b%2)==0)):
		return False
	elif (b>2):
		for i in range(2,b):

			if not(b%i):
				return False
	return True
check_num = prime_check(num)
while (((check_num==False))):
	num = int(input("---/\/\ Try_Again: "))
	check_num = prime_check(num)

print(prime_check(num)) 
