import string
all = string.maketrans('','')
nodigs_or_letter = all.translate(all, string.digits.join(string.ascii_letters))


def cal_score(search_str, document):
    search_l = search_str.split()
    search_list = []

    for i in range(0, len(search_list)):
        search_list[i] = search_list[i].translate(all, nodigs_or_letter)

    for l in search_l:
        x = l.translate(all,nodigs_or_letter)
        if len(x) != 0:
            search_list.append(x)

    score = 0.0

    terms = []

    for line in document:
        words = line.split()
        for word in words:
            w = word.translate(all, nodigs_or_letter)
            if len(w) != 0:
                terms.append(w)

    for term in list(set(search_list)):
        score += (terms.count(term) * search_list.count(term)) ** 0.5
    return score


line = raw_input()
case_nums = int(line)
line = raw_input()
input_lines = []
while True:
    try:
        last_line = line
        line = raw_input()
        input_lines.append(line)
        if line == '----------' and last_line == '----------':
            break
    except EOFError:
        break
blocks = []
block = []
for line in input_lines:
    if line == '':
        blocks.append(block)
        block = []
        continue
    block.append(line)
blocks.append(block)

cases = []
for b in blocks:
    case = []
    case.append(b[0])
    d = []
    for i in range(2,len(b)):
        if b[i] == '----------':
            if len(d) != 0:
                case.append(d)
            d = []
            continue
        d.append(b[i])
    if len(d) != 0:
        case.append(d)

    cases.append(case)

for c in cases:
    print
    search_str = c[0]
    for i in range(1,len(c)):
        print '%.2f' % cal_score(search_str, c[i])
