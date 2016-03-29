class Enigma:
    codes = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    position = 0
    length = 0
    en_rotors = []
    de_rotors = []
    rotors_str = []

    def __init__(self, length, str):
        self.position = 0
        self.length = length
        self.codes = self.codes[:length]
        self.en_rotors_str = str
        self.de_rotors = []
        rotor_codes = []
        self.en_rotors = []
        original_rotor = []

        for c in self.codes:
            original_rotor.append(self.codes.index(c))

        for r in self.en_rotors_str:
            current_rotor = []
            for letter in r:
                current_rotor.append(self.codes.index(letter))
            rotor_codes.append(current_rotor)

        for i in range(0,3):
            current_rotor = []
            for j in range(0, self.length):
                current_rotor.append((rotor_codes[i][j] - original_rotor[j]) % length)
            self.en_rotors.append(current_rotor)

        for i in range(0,3):
            current_rotor = []
            for j in range(0, self.length):
                current_rotor.append(0)
            for j in range(0, self.length):
                c = rotor_codes[i].index(j)
                current_rotor[j] = (c - original_rotor.index(j)) % length
            self.de_rotors.append(current_rotor)

    def show(self):
        print self.codes
        print self.en_rotors_str
        print self.en_rotors
        print self.de_rotors

    def encrypt(self, plain_text):
        plain_code = []
        encrypted_code = []
        encrypted_text = ''
        for letter in plain_text:
            plain_code.append(self.codes.index(letter))
        for i in plain_code:
            encrypted_code.append((i + self.en_rotors[0][i] + self.en_rotors[1][i] + self.en_rotors[2][i]) % self.length)
            self.rotate()

        for i in encrypted_code:
            encrypted_text += self.codes[i]
        return encrypted_text

    def decrypt(self, encrypted_text):
        plain_code = []
        plain_text = ''
        encrypted_code = []
        for letter in encrypted_text:
            encrypted_code.append(self.codes.index(letter))

        for i in encrypted_code:
            plain_code.append((i + self.de_rotors[0][i] + self.de_rotors[1][i] + self.de_rotors[2][i]) % self.length)
            self.rotate()

        for i in plain_code:
            plain_text += self.codes[i]

        return plain_text

    def rotate(self):
        code = self.en_rotors[0].pop()
        code2 = self.de_rotors[0].pop()
        self.en_rotors[0].insert(0,code)
        self.de_rotors[0].insert(0,code2)
        self.position += 1
        for i in range(1,3):
            if self.position % (self.length ** i) == 0:
                code = self.en_rotors[i].pop()
                code2 = self.de_rotors[i].pop()
                self.en_rotors[i].insert(0,code)
                self.de_rotors[i].insert(0,code)

        if self.position % (self.length ** 3) == 0:
            self.position = 0

    def reverse_rotate(self):
        for i in range(0, 3):
            if self.position % (self.length ** i) == 0:
                code = self.en_rotors[i].popleft()
                self.en_rotors[i].append(code)

        if self.position == 0:
            self.position = self.length ** 3 - 1;
        self.position -= 1

e_num=1
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
        print 'Enigma ' + str(e_num) + ':'
        for i in range(0,num):
            e = Enigma(l,[str0, str1, str2])
            cryptographs = raw_input()
            print e.decrypt(cryptographs).lower()

        print

    except EOFError:
        exit(0)