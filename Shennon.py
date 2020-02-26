import math as m
import collections as coll

def SummBin(a, l):
    num = ""
    for i in range(0,l):
        a *= 2.0
        num += str(m.trunc(a))
        if a >= 1.0:
            a -= 1.0
    return num


class Cod:
    text = ''
    def Coder(self):
        sum = 0.0
        a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = a9 = a10 = a11 = a12 = a13 = a14 = a15 = a16 = a17 = a18 = a19 = a20 = a21 = a22 = a23 = a24 = a25 = a26 = a27 = a28 = a29 = a30 = a31 = a32 = 0
        word_new = {}
        word = {
        'а':[a1,0,0.0,''],
        'б':[a2,0,0.0,''],
        'в':[a3,0,0.0,''],
        'г':[a4,0,0.0,''],
        'д':[a5,0,0.0,''],
        'е':[a6,0,0.0,''],
        'ж':[a7,0,0.0,''],
        'з':[a8,0,0.0,''],
        'и':[a9,0,0.0,''],
        'й':[a10,0,0.0,''],
        'к':[a11,0,0.0,''],
        'л':[a12,0,0.0,''],
        'м':[a13,0,0.0,''],
        'н':[a14,0,0.0,''],
        'о':[a15,0,0.0,''],
        'п':[a16,0,0.0,''],
        'р':[a17,0,0.0,''],
        'с':[a18,0,0.0,''],
        'т':[a19,0,0.0,''],
        'у':[a20,0,0.0,''],
        'ф':[a21,0,0.0,''],
        'х':[a22,0,0.0,''],
        'ц':[a23,0,0.0,''],
        'ч':[a24,0,0.0,''],
        'ш':[a25,0,0.0,''],
        'щ':[a26,0,0.0,''],
        'ъ':[a27,0,0.0,''],
        'ы':[a28,0,0.0,''],
        'ь':[a29,0,0.0,''],
        'э':[a30,0,0.0,''],
        'ю':[a31,0,0.0,''],
        'я':[a32,0,0.0,'']
        }

        for word_mini in self.text:
            word[word_mini][0] += 1

        for k in word.keys():
            if word[k][0] != 0.0:
                word[k][0] /= len(self.text)
                word[k][1] = m.ceil(m.log2(float(word[k][0]))*(-1))

        word_new.update(coll.OrderedDict(sorted(word.items(),key = lambda i:i[1][0],reverse=-1)))

        for k in word_new.keys():
            word_new[k][2] = sum
            sum += word_new[k][0]
            word_new[k][3] = SummBin(word_new[k][2], word_new[k][1])

        for w in self.text:
            print(word_new[w][3], end='')

    def Decoder(self):
        print(self.text)


code = Cod()
code.text = input().lower()
code.text = code.text.replace(' ','')
code.Coder()
print()
l = (''.join(format(ord(x), 'b') for x in code.text))
print("Данные сжимаются в ", len(l)/len((code.text)), " раз")
