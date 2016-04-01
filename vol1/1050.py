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
cases = []
case = []
for line in input_lines:
    if line == '':
        cases.append(case)
        case = []
        continue
    case.append(line)
cases.append(case)

for c in cases:
    search = c[0].split()

