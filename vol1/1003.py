def validate(score):
    if score <= 100:
        return True
    if len(cal_factors(score)) == 0:
        return False
    return True


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

print cal_factors(343)
print cal_factors(49)
print
print cal_factors(3599)
print cal_factors(610)
print
print cal_factors(62)
print cal_factors(36)
print

