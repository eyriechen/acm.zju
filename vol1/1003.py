def validate(score):
    if score <= 100:
        return True


def is_prime_num(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def add_factor(l, num):
    if num > 100:
        return []
    return l.append(num)

def break_factor(num, start, factors):
    #print 'facotr ' + str(num) + ' ' + str(start)
    for i in range(start, 101):
        if num % i == 0:
            if num / i < i + 1:
                factors.append(num)
                break
            else:
                factors.append(i)
                break_factor(num/i, i+1, factors)
                break
    else:
        factors.append(num)
    return factors


def cal_factors(num):
    factors_list = []
    i = 2
    while i < 101:
        f = break_factor(num, i, [])
        factors_list.append(f)
        i = f[0]+1
    return factors_list;

print cal_factors(206)



while True:
    try:
        scores = []
        line = raw_input()
        scores = line.split()
        if len(scores) != 2:
            break
        high_score = max(map(int, scores))
        low_score = min(map(int, scores))
        print high_score
        print low_score
    except EOFError:
        exit(0)