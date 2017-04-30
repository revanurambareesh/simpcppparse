__author__ = 'Ambareesh Revanur'

#MIT License

'''
State 17 
terminal id
f(()
caused the problem and panic recovery also failed
'''

import time

#TODO
def e1(stack, input_array, index):
	input_array[index+1] = 'fid'
	index += 1
	print 'stack', stack
	print 'inp_array', input_array
	print 'index', index
	time.sleep(3)
	return stack, input_array, index