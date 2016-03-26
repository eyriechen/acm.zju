class StrStack:
    str = ''
    stack = []
    str_result = ''

    def __init__(self, s):
        self.str = ''
        self.stack = []
        self.op_str = ''
        self.str_result = ''
        self.str = s

    def push(self):
        self.stack.append(self.str[0])
        self.str = self.str[1:]

    def pop(self):
        if len(self.stack) == 0:
            return False
        self.str_result += self.stack.pop()
        return True

    def show(self):
        return self.str_result

    def completed(self):
        if str == '':
            return True
        else:
            return False



def try_push(op, length, possible_moves):
    if op.count('i') < length:
        op += 'i '
        try_push(op, length,possible_moves)
        try_pop(op, length,possible_moves)


def try_pop(op, length, possible_moves):
    if op.count('i') - op.count('o') > 0:
        op += 'o '
        if op.count('o') >= length:
            possible_moves.append(op)
        else:
            try_push(op,length,possible_moves)
            try_pop(op,length,possible_moves)


def cal_moves(first_str, second_str):
    possible_moves = []
    try_push('', len(first_str), possible_moves)
    valid_moves = []
    for moves in possible_moves:
        s = StrStack(first_str)
        for move in moves:
            if move == 'i':
                s.push()
            elif move == 'o':
                s.pop()
        if s.show() == second_str:
            valid_moves.append(moves)
    valid_moves.sort()
    return valid_moves


while True:
    try:
        first = raw_input()
        second = raw_input()
        for f in first:
            if first.count(f) != second.count(f):
                print '['
                print ']'
                break
        else:
            print '['
            for moves in cal_moves(first,second):
                print moves
            print ']'
    except EOFError:
        exit(0)