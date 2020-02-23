import math as m

class Cod:
    text = ''
    def Coder(self):
        l = []
        a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = a9 = a10 = a11 = a12 = a13 = a14 = a15 = a16 = a17 = a18 = a19 = a20 = a21 = a22 = a23 = a24 = a25 = a26 = a27 = a28 = a29 = a30 = a31 = a32 = 0
        word = {
        'а':a1,
        'б':a2,
        'в':a3,
        'г':a4,
        'д':a5,
        'е':a6,
        'ж':a7,
        'з':a8,
        'и':a9,
        'й':a10,
        'к':a11,
        'л':a12,
        'м':a13,
        'н':a14,
        'о':a15,
        'п':a16,
        'р':a17,
        'с':a18,
        'т':a19,
        'у':a20,
        'ф':a21,
        'х':a22,
        'ц':a23,
        'ч':a24,
        'ш':a25,
        'щ':a26,
        'ъ':a27,
        'ы':a28,
        'ь':a29,
        'э':a30,
        'ю':a31,
        'я':a32
        }
        for word_mini in self.text:
            word[word_mini] += 1
        for w in word.keys():
            word[w] /= len(self.text)
        for w in word.keys():
            if word[w] != 0.0:
                l.append(word[w])
                print(word[w])
        print(l)
    def Decoder(self):
        print(self.text)
code = Cod()
code.text = input()
code.Coder()
#print(''.join(format(ord(x), 'b') for x in code.text))