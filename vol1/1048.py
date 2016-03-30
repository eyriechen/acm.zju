balance = []
for i in range(0, 12):
    line = raw_input()
    balance.append(float(line))
print '$' + str(round(sum(balance) / len(balance), 2))
