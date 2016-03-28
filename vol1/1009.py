class Enigma:
    codes = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    position = 0
    length = 0
    rotors = []
    rotors_str = []

    def __init__(self, length, str):
        self.position = 0
        self.length = length
        self.codes = self.codes[:length]
        self.rotors_str = str
        rotor_codes = []
        self.rotors = []
        original_rotor = []
        for c in self.codes:
            original_rotor.append(self.codes.index(c))
        for r in self.rotors_str:
            current_rotor = []
            for letter in r:
                current_rotor.append(self.codes.index(letter))
            rotor_codes.append(current_rotor)
        for i in range(0,3):
            current_rotor = []
            for j in range(0, self.length):
                current_rotor.append((rotor_codes[i][j] - original_rotor[j]) % length)
            self.rotors.append(current_rotor)

    def show(self):
        print self.codes
        print self.rotors_str
        print self.rotors

    def encrypt(self, plain_text):
        plain_code = []
        encrypted_code = []
        encrypted_text = ''
        for letter in plain_text:
            plain_code.append(self.codes.index(letter))
        for i in plain_code:
            encrypted_code.append((i + self.rotors[0][i] + self.rotors[1][i] + self.rotors[2][i]) % self.length)
            self.rotate()

        for i in encrypted_code:
            encrypted_text += self.codes[i]
        return encrypted_text


    def decrypt(self,encrypted_text):
        plain_code = []
        plain_text = ''
        encrypted_code = []
        for letter in encrypted_text:
            encrypted_code.append(self.codes.index(letter))

        for i in encrypted_code:
            plain_code.append((i - self.rotors[0][i] - self.rotors[1][i] - self.rotors[2][i]) % self.length)
            self.rotate()

        for i in plain_code:
            plain_text += self.codes[i]

        print encrypted_code
        print plain_code

        return plain_text


    def rotate(self):
        code = self.rotors[0].pop()
        self.rotors[0].insert(0,code)
        self.position += 1
        for i in range(1,3):
            if self.position % (self.length ** i) == 0:
                code = self.rotors[i].pop()
                self.rotors[i].insert(0,code)

        if self.position % (self.length ** 3) == 0:
            self.position = 0

    def reverse_rotate(self):
        for i in range(0, 3):
            if self.position % (self.length ** i) == 0:
                code = self.rotors[i].popleft()
                self.rotors[i].append(code)

        if self.position == 0:
            self.position = self.length ** 3 - 1;
        self.position -= 1


e = Enigma(6,['BADFEC', 'ABCDEF', 'ABCDEF'])
e.show()
print e.encrypt('BBB')