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