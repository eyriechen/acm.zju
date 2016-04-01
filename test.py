import string
all = string.maketrans('','')
nodigs_or_letter = all.translate(all, string.digits.join(string.ascii_letters))

line = raw_input()
search = line.split()

for i in range(0, len(search)):
    search[i] = search[i].translate(all, nodigs_or_letter)

line = raw_input()


def cal_score(search_str, document):
    score = 0.0
    for term in list(set(search_str)):
        score += (document.count(term) * search_str.count(term)) ** 0.5
    return score


while True:
    document = []
    while True:
        line = raw_input()
        if line == '' or line == '----------':
            break
        t = line.split()
        for i in range(0, len(t)):
            t[i] = t[i].translate(all, nodigs_or_letter)
            document.append(t[i])
    print document
    print "%.2f" % cal_score(search, document)
