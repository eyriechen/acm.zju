class Rotor:
    length = 0
    codes = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypt_code = []
    decrypt_code = []

    def __init__(self, length, str):
        self.length = length
        self.codes = self.codes[:length]
        self.encrypt_code = []
        self.decrypt_code = []
        original_rotor = []
        for c in self.codes:
            original_rotor.append(self.codes.index(c))
        encrypt_codes = []
        decrypt_codes = []
        for letter in str:
            encrypt_codes.append(self.codes.index(letter))
            decrypt_codes.append(self.codes.index(letter))

        for j in range(0, self.length):
            self.encrypt_code.append((encrypt_codes[j] - original_rotor[j]) % length)

        current_rotor = []
        for j in range(0, self.length):
            current_rotor.append(0)

        for j in range(0,self.length):
            c = self.codes.index(str[j])
            current_rotor[c] = (original_rotor[j] - c) % length

        self.decrypt_code = current_rotor

    def rotate(self):
        code = self.encrypt_code.pop()
        code2 = self.decrypt_code.pop()
        self.encrypt_code.insert(0,code)
        self.decrypt_code.insert(0,code2)

    def encrypt(self, c):
        i = self.codes.index(c)
        i += self.encrypt_code[i]
        i %= self.length
        return self.codes[i]

    def decrypt(self, c):
        i = self.codes.index(c)
        i += self.decrypt_code[i]
        i %= self.length
        return self.codes[i]


class Enigma:
    position = 0
    length = 0
    rotors = []

    def __init__(self, length, str):
        self.position = 0
        self.length = length
        self.rotors = []

        for s in str:
            self.rotors.append(Rotor(self.length, s))

    def rotate(self):
        self.position += 1
        for i in range(0, len(self.rotors)):
            if self.position % (self.length ** i) == 0:
                self.rotors[i].rotate()

        if self.position % (self.length ** len(self.rotors)) == 0:
            self.position = 0

    def encrypt(self, str):
        plain_text = ''
        for c in str:
            code = c
            for r in self.rotors:
                code = r.encrypt(code)
            plain_text += code
            self.rotate()
        return plain_text

    def decrypt(self, str):
        secret_text = ''
        for c in str:
            code = c
            for r in reversed(self.rotors):
                code = r.decrypt(code)
            secret_text += code
            self.rotate()
        return secret_text

    def show(self):
        pass





e_num=0
while True:
    try:
        s = raw_input()
        l = int(s)
        if l == 0:
            break
        str0 = raw_input()
        str1 = raw_input()
        str2 = raw_input()
        s = raw_input()
        num = int(s)
        e_num += 1
        if e_num != 1:
            print
        print 'Enigma ' + str(e_num) + ':'
        for i in range(0,num):
            e = Enigma(l,[str0, str1, str2])
            cryptographs = raw_input()
            print e.decrypt(cryptographs).lower()


    except EOFError:
        exit(0)