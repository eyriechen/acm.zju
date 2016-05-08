class Computer:
    memory = []
    reg_accu = 0
    reg_pc = 0
    reg_ir = ''
    flag_running = False

    def __init__(self, lines):
        self.memory = lines
        self.reg_accu = 0
        self.reg_pc = 0
        self.reg_ir = ''

    def read_memery(self, address):
        return self.memory[address]

    def run(self):
        self.flag_running = True
        while self.flag_running:
            self.step()

    def step(self):
        self.reg_ir = self.read_memery(self.reg_pc)
        self.reg_pc += 1
        self.reg_pc %= 32
        ins = self.reg_ir[:3]
        add = self.reg_ir[3:]
        if ins == '000':
            self.ins_STA(add)
        elif ins == '001':
            self.ins_LDA(add)
        elif ins == '010':
            self.ins_BEQ(add)
        elif ins == '011':
            self.ins_NOP()
        elif ins == '100':
            self.ins_DEC()
        elif ins == '101':
            self.ins_INC()
        elif ins == '110':
            self.ins_JMP(add)
        elif ins =='111':
            self.ins_HLT()

    def show(self):
        accu = bin(self.reg_accu)[2:]
        accu = '0000000' + accu
        accu = accu[-8:]
        print accu

    def ins_STA(self, address):
        add = int(address, 2)
        accu = bin(self.reg_accu)[2:]
        accu = '0000000' + accu
        accu = accu[-8:]
        self.memory[add] = accu

    def ins_LDA(self, address):
        add = int(address, 2)
        accu = self.memory[add]
        accu = int(accu, 2)
        self.reg_accu = accu

    def ins_BEQ(self, address):
        if self.reg_accu == 0:
            self.reg_pc = int(address, 2)

    def ins_NOP(self):
        pass

    def ins_DEC(self):
        self.reg_accu -= 1
        self.reg_accu %= 256

    def ins_INC(self):
        self.reg_accu += 1
        self.reg_accu %= 256


    def ins_JMP(self, address):
        self.reg_pc = int(address, 2)

    def ins_HLT(self):
        self.flag_running = False


lines = []
while True:
    try:
        line = raw_input()
        if len(line) == 8:
            lines.append(line)
        if len(lines) == 32:
            c = Computer(lines)
            c.run()
            c.show()
            lines = []

    except EOFError:
        exit(0)
