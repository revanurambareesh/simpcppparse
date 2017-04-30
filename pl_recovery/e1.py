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
	#input_array[index+1] = 'fid'
	#9dindex += 1
	print '----Phrase level recovery initiated---'

	print 'stack', stack
	print 'inp_array', input_array
	print 'index', index
	print 'input', input_array[index]

	index += 4
	input_array[index]='fid'
	print '\n'
	time.sleep(1)

	print 'stack', stack
	print 'inp_array', input_array
	print 'index', index
	print 'input', input_array[index]
	time.sleep(2)
	return stack, input_array, index