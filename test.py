import string
all = string.maketrans('','')
nodigs_or_letter = all.translate(all, string.digits.join(string.ascii_letters))

line = raw_input()
search = line.split()

for i in range(0, len(search)):
    search[i] = search[i].translate(all, nodigs_or_letter)

line = raw_input()

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
    score = 0
    for s in list(set(search)):
        score += (document.count(s) * search.count(s)) ** 0.5

    print "%.2f" % (score)

