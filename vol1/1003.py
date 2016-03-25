def add_factor(l, num):
    if num > 100:
        return []
    return l.append(num)


def break_factor(num, start, factors):
    if start >= num:
        return []
    for i in range(start, 101):
        if num % i == 0:
            if num / i < i + 1:
                factors.append(num)
                if num > 100:
                    factors = []
                break
            else:
                factors.append(i)
                factors = break_factor(num/i, i+1, factors)
                break
    else:
        factors.append(num)
        if num > 100:
            factors = []
    return factors


def cal_factors(num):
    factors_list = []
    i = 2
    while i < 101:
        f = break_factor(num, i, [])
        if len(f) == 0:
            i += 1
        else:
            i = f[0]+1
            factors_list.append(f)
    return factors_list;


def every_one_contains(l, num):
    for e in l:
        if not num in e:
            return False
    else:
        return True

def validte(high, lows):
    for i in high:
        if every_one_contains(lows, i):
            return False
    else:
        return True

while True:
    try:
        scores = []
        line = raw_input()
        scores = line.split()
        if len(scores) != 2:
            continue
        high_score = max(map(int, scores))
        low_score = min(map(int, scores))
        low_factors = cal_factors(low_score)
        if len(low_factors) == 0:
            print high_score
            continue
        high_factors = cal_factors(high_score)
        if len(high_factors) == 0:
            print  low_score
            continue
        valid_high_factors = []
        for f in high_factors:
            if validte(f, low_factors):
                valid_high_factors.append(f);
        if len(valid_high_factors) == 0:
            print low_score
        else:
            print high_score
    except EOFError:
        exit(0)
