def large_one(a, b):
    if a > b:
        return a
    elif a< b:
        return b


def small_one(a, b):
    if a < b:
        return a
    elif a > b:
        return b;


while True:
    try:
        scores = []
        line = raw_input()
        scores = line.split()
        if len(scores) != 2:
            break
        high_score = large_one(int(scores[0]), int(scores[1]))
        low_score = small_one(int(scores[0]), int(scores[1]))
        print high_score
        print low_score
    except EOFError:
        exit(0)