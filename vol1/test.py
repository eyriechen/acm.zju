import string
all = string.maketrans('','')
nodigs_or_letter = all.translate(all, string.digits.join(string.ascii_letters))


def cal_score(search_str, document):
    search_list = search_str.split()

    for i in range(0, len(search_list)):
        search_list[i] = search_list[i].translate(all, nodigs_or_letter)

    score = 0.0

    terms = []

    for line in document:
        words = line.split()
        for word in words:
            terms.append(word.translate(all, nodigs_or_letter))

    for term in list(set(search_list)):
        score += (terms.count(term) * search_list.count(term)) ** 0.5
    return score

print '%.2f' % cal_score('fee fi fo fum',['fee, fi, fo! fum!!'])
print '%.2f' % cal_score('fee fi fo fum',['fee fee fi, me me me'])
print '%.2f' % cal_score('fee fi fo fum',['fee, fi, fo! fum!!','fee fee fi, me me me'])
