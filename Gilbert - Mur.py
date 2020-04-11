import math as m
import collections as coll

def SummBin(a, l):
    num = ''
    for i in range(0,l):
        a *= 2.0
        num += str(m.trunc(a))
        if a >= 1.0:
            a -= 1.0
    return num

class Cod:
    text = ''
    code = ''
    word_new = {}
    deword = {}
    def Coder(self):          
        sum = 0.0
        for i in self.text:
            if i not in self.word_new:
                self.word_new[i.lower()] = [1, 0, 0, '']
            else:
                self.word_new[i][0] += 1
        self.word_new = coll.OrderedDict(sorted(self.word_new.items(),key = lambda i:i[0]))
        for i in self.word_new:
            self.word_new[i][0] /=  len(self.text)
            self.word_new[i][1] = m.ceil(m.log2(1 / self.word_new[i][0])) + 1
            self.word_new[i][2] = self.word_new[i][0] / 2 + sum
            self.word_new[i][3] = SummBin(self.word_new[i][2], self.word_new[i][1])
            sum += self.word_new[i][0]
        for i in self.text.lower():
            self.code += self.word_new[i][3]
        print(self.code)
    def Decoder(self):
        for k, i in self.word_new.items():
            self.deword[i[3]] = k 
        w = ''
        for i in self.code:
            try:
                w += i
                print(self.deword[w], end='')
                w = ''
            except:
                pass
            

code = Cod()
code.text = 'Спасибо'
code.Coder()
code.Decoder()
s = 0.0
H = 0.0
for i in code.text.lower():
    s += code.word_new[i][0] * code.word_new[i][1]
    H += code.word_new[i][0] * m.log2(1 / code.word_new[i][0])
print('\n', s, sep='')
print(H + 2)
