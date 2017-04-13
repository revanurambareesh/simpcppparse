parsetable = 'SSCD Parse table.csv'
lex_outputfile = 'output.txt'


def M(state, terminal):
    # state is an ascii string
    # terminal is an ascii string
    with open(parsetable) as f:
        content = f.readlines()

    return content[int(state) + 1].strip().split(',')[content[0].strip().split(',').index(terminal)]
    pass


def get_reduce(number):
    if number == '0':
        return [['A\''], ['A']]
    elif number == '1':
        return [['A'], ['I', 'D', 'C', 'F']]
    elif number == '2':
        return [['I'], ['i', 'I']]
    elif number == '3':
        return [['I'], ['eps']]
    elif number == '4':
        return [['D'], ['dec', 'D']]
    elif number == '5':
        return [['D'], ['eps']]
    elif number == '6':
        return [['C'], ['cls', 'C']]
    elif number == '7':
        return [['C'], ['eps']]
    elif number == '8':
        return [['F'], ['fun', 'F']]
    elif number == '9':
        return [['F'], ['fun']]
    elif number == '10':
        return [['cls'], ['cla', '{', 'D', 'F', '}', ';']]
    elif number == '11':
        return [['fun'], ['fid', '{', 'D', 'S', '}']]
    elif number == '12':
        return [['S'], ['S', 'ret']]
    elif number == '13':
        return [['S'], ['E', ';', 'S']]
    elif number == '14':
        return [['S'], ['O', 'S']]
    elif number == '15':
        return [['S'], ['in', 'S']]
    elif number == '16':
        return [['S'], ['if', 'S']]
    elif number == '17':
        return [['S'], ['if', 'else', 'S']]
    elif number == '18':
        return [['S'], ['loop', 'S']]
    elif number == '19':
        return [['S'], ['eps']]
    elif number == '20':
        return [['O'], ['cout', '<', '<', 'B']]
    elif number == '21':
        return [['B'], ['id', ';']]
    elif number == '22':
        return [['B'], ['id', '<', '<', 'B']]
    elif number == '23':
        return [['E'], ['E', 'op', 'E']]
    elif number == '24':
        return [['E'], ['id']]
    elif number == '25':
        return [['in'], ['cin', '>', '>', 'B\'']]
    elif number == '26':
        return [['B\''], ['id', ';']]
    elif number == '27':
        return [['B\''], ['id', '>', '>', 'B\'']]
    elif number == '28':
        return [['if'], ['f', '(', 'id', 'op', 'id', ')', '{', 'S', '}']]
    elif number == '29':
        return [['else'], ['el', '{', 'S', '}']]
    elif number == '30':
        return [['loop'], ['for', '(', 'E', ';', 'E', ';', 'E', ')', '{', 'S', '}']]
    else:
        print 'the number is improper'
        return [[''], ['0']]
    pass


def shift(stack, state, terminal):
    stack += ' ' + terminal + ' ' + M(state, terminal)[1:]  # push
    print 'state', state, 'terminal', terminal, 'action', M(state, terminal)
    return stack


def reduce(stack, state, terminal):
    # index=len(stack.split(' '))-1
    reduce_string = get_reduce(M(state, terminal)[1:])
    start_index = len(reduce_string[1])

    if reduce_string[1][0] == 'eps':
        state = stack.split(' ')[len(stack.split(' ')) - 1]
        # stack += ' ' + reduce_string[0][0]
    else:
        while start_index > 0:
            # jump one index simply
            # index-=1

            # edge case
            if len(stack.strip()) < 4:
                print 'unexpected stack length'
                return ''

            # match

            length_to_subtract = len(stack.split(' ')[len(stack.split(' ')) - 1]) + 1  # pop even a space
            stack = stack[:-length_to_subtract]

            if stack.split(' ')[len(stack.split(' ')) - 1] == reduce_string[1][start_index - 1]:
                length_to_subtract = len(stack.split(' ')[len(stack.split(' ')) - 1]) + 1  # pop even a space
                stack = stack[:-length_to_subtract]
                start_index -= 1
                continue
            else:
                print 'Problem comparing the strings for reduction', 'string as seen', stack, 'to reduce, ', ''.join(reduce_string[1])
                return ''

        state = stack.split(' ')[len(stack.split(' ')) - 1]

    # goto

    print 'state', state, 'terminal', terminal, 'goto', M(state, terminal), 'reduce', ''.join(reduce_string[1]), 'reduction production number ', M(state, terminal)
    stack += ' ' + reduce_string[0][0]
    stack += ' ' + M(state, reduce_string[0][0])
    return stack


def parsefile(filename):
    stack = '$ 0'
    error_line_nums = ''
    input_string = ''
    with open(filename, 'r') as f:
        input_string = f.read()

    line_num = 0
    input_array = (input_string + '$').split(' ')
    state = '0'
    index = 1
    terminal = input_array[index]

    while M(state, terminal) != 'a' and stack.strip() != '':
        if input_array[index].isdigit():
            line_num = int(input_array[index])
            index += 1
            continue

        print '====Log===='
        print 'Line number:', line_num
        print 'stack: ', stack
        print 'current input symbol: ', terminal

        state = stack.split(' ')[len(stack.split(' ')) - 1]
        terminal = input_array[index]

        if M(state, terminal) == '':
            print 'Error in line number: ', line_num
            error_line_nums += (str(line_num) + ' ')
            return 'not accepted'

        elif M(state, terminal)[0] == 'a':
            print 'Successfully parsed. C++ program is according to syntax.'
            if error_line_nums!='':
                break
            else:
            	return 'accept'

        elif M(state, terminal)[0] == 's':
            stack = shift(stack, state, terminal)
            index += 1

        elif M(state, terminal)[0] == 'r':
            temp_stack = stack
            stack = reduce(stack, state, terminal)
            if stack == '':
                print 'reduce failed'
                return '-1'

    if error_line_nums != '':
        print 'Error in folowing lines: ', ''.join(list(set(error_line_nums.split(' '))))
        return 'error'

    else:
        print 'Program terminated'


if __name__ == "__main__":
    print parsefile(lex_outputfile)
