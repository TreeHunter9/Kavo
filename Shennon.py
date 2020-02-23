import math as m

class Cod:
    text = ''
    def Coder(self):
        l = []
        a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = a9 = a10 = a11 = a12 = a13 = a14 = a15 = a16 = a17 = a18 = a19 = a20 = a21 = a22 = a23 = a24 = a25 = a26 = a27 = a28 = a29 = a30 = a31 = a32 = 0
        word = {
        'а':[a1,0],
        'б':[a2,0],
        'в':[a3,0],
        'г':[a4,0],
        'д':[a5,0],
        'е':[a6,0],
        'ж':[a7,0],
        'з':[a8,0],
        'и':[a9,0],
        'й':[a10,0],
        'к':[a11,0],
        'л':[a12,0],
        'м':[a13,0],
        'н':[a14,0],
        'о':[a15,0],
        'п':[a16,0],
        'р':[a17,0],
        'с':[a18,0],
        'т':[a19,0],
        'у':[a20,0],
        'ф':[a21,0],
        'х':[a22,0],
        'ц':[a23,0],
        'ч':[a24,0],
        'ш':[a25,0],
        'щ':[a26,0],
        'ъ':[a27,0],
        'ы':[a28,0],
        'ь':[a29,0],
        'э':[a30,0],
        'ю':[a31,0],
        'я':[a32,0]
        }
        for word_mini in self.text:
            word[word_mini][0] += 1
        for k in word.keys():
            if word[k][0] != 0.0:
                word[k][0] /= len(self.text)
                word[k][1] = m.ceil(m.log2(float(word[k][0]))*(-1))
        for k,i in word.items():
            if word[k][0] != 0.0:
                l.append(i)
                print(k,i)
        print(l)



    def Decoder(self):
        print(self.text)
code = Cod()
code.text = input()
code.Coder()
#print(''.join(format(ord(x), 'b') for x in code.text))