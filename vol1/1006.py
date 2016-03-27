def twisting_encrypt(str, key):
    codes = '_abcdefghijklmnopqrstuvwxyz.'
    plain_code = []
    ciphercode = []
    encryption = ''
    n = len(str)
    for letter in str:
        plain_code.append(codes.index(letter))

    for i in range(0, n):
        ciphercode.append((plain_code[key*i%n] -i) % 28)

    for i in ciphercode:
        encryption += codes[i]

    return encryption


def twisting_decrypt(str, key):
    codes = '_abcdefghijklmnopqrstuvwxyz.'
    decryption = ''
    ciphercode = []
    plain_code = []
    n = len(str)
    for letter in str:
        ciphercode.append(codes.index(letter))
        plain_code.append(0)

    for i in range(0, n):
        plain_code[key*i%n] = (ciphercode[i] + i) % 28

    for code in plain_code:
        decryption += codes[code]
    return decryption


while True:
    try:
        s = raw_input()
        arr = s.split()
        key = int(arr[0])
        if key == 0:
            break
        str = arr[1]
        print twisting_decrypt(str, key)
    except EOFError:
        exit(0)