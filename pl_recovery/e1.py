__author__ = 'Ambareesh Revanur'

#MIT License

'''
State 17 
terminal id
f(()
caused the problem and panic recovery also failed
'''

#TODO
def e1(stack, input_array, index):
	input_array[index+1] = 'fid'
	index += 1
	return stack, input_array, index