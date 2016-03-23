output_line = []
current_line = ''
while True:
    try:
        line = raw_input()
        words = line.split()
        for word in words:
            if word == '<hr>':
                if current_line != '':
                    output_line.append(current_line)
                    current_line = ''
                output_line.append('--------------------------------------------------------------------------------')
                continue
            elif word == '<br>':
                output_line.append(current_line)
                current_line = ''
                continue
            if len(current_line) + len(word) < 80:
                if current_line == '':
                    current_line = word
                else:
                    current_line = current_line+ ' ' + word
            else:
                output_line.append(current_line)
                current_line = word
    except EOFError:
        break
output_line.append(current_line)
for line in output_line:
    print(line)