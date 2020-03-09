import math as m
import collections as coll
import tkinter as tk
from tkinter import filedialog as fd
import pickle

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
    def Coder(self):             
        sum = 0.0
        a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = a9 = a10 = a11 = a12 = a13 = a14 = a15 = a16 = a17 = a18 = a19 = a20 = a21 = a22 = a23 = a24 = a25 = a26 = a27 = a28 = a29 = a30 = a31 = a32 = a33 = 0
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
        'я':[a32,0,0.0,''],
        ' ':[a33,0,0.0,''],
        }
        t = Text1.get(1.0, 'end').lower()
        for t_mini in t:
            try:
                word[t_mini]
            except:
                pass
            else:
                self.text += t_mini

        for word_mini in self.text:
            try:
                word[word_mini][0] += 1
            except:
                pass

        for k in word.keys():
            if word[k][0] != 0.0:
                word[k][0] /= len(self.text)
                word[k][1] = m.ceil(m.log2(float(word[k][0]))*(-1))

        self.word_new.update(coll.OrderedDict(sorted(word.items(),key = lambda i:i[1][0],reverse=-1)))

        for k in self.word_new.keys():
            self.word_new[k][2] = sum
            sum += self.word_new[k][0]
            self.word_new[k][3] = SummBin(self.word_new[k][2], self.word_new[k][1])

        for w in self.text:
            self.code += self.word_new[w][3]

    def Decoder(self):
        line = ''
        zero = ''
        deword = {}
        for k,i in self.word_new.items():
            deword[i[3]] = k
        for i in range(0,6):
            l = ''
            count = 0
            for a in self.code:
                if count <= 10:
                    l += a
                    count += 1
                    try:
                        deword[zero + l]
                    except:
                        pass
                    else:
                        l = ''
                        break
                else:
                    break
            if(l == ''):
                break
            zero += '0'        
        temp = zero + self.code
        print(temp)
        for i in temp:
            line += i
            try:
                deword[line]
            except:
                pass
            else:
                Text2.insert('end', deword[line])
                print(deword[line])
                line = ''  
        print(deword)  

code = Cod()

def open_file():
    file_name = fd.askopenfilename(filetypes=(('texts', '*.txt'), ('All files', '*.*')))
    with open(file_name, 'r', encoding="utf8") as f:
        Text1.delete(1.0, 'end')
        Text1.insert(1.0, f.read())

def make_code():
    Text2.delete(1.0, 'end')
    code.Coder()
    Text2.insert(1.0, code.code)

def save_code():
    new_file = fd.asksaveasfilename(filetypes=(('texts', '*.txt'), ('All files', '*.*')), defaultextension='.txt')
    temp_code = [int(code.code[x:x+8],2) for x in range(0, len(code.code), 8)]
    temp_bytes = bytes(temp_code)
    with open(new_file, 'wb') as f:
        f.write(temp_bytes)
    new_file = fd.asksaveasfilename(filetypes=(('texts', '*.txt'), ('All files', '*.*')), defaultextension='.txt')
    with open(new_file, 'wb') as f:
        pickle.dump(code.word_new, f)

def decode_file():
    Text1.delete(1.0, 'end')
    file_name = fd.askopenfilename(filetypes=(('texts', '*.txt'), ('All files', '*.*')))
    with open(file_name, 'rb') as f:
        temp_int = int.from_bytes(f.read(), byteorder='big')
        code.code = "{0:b}".format(temp_int)
    file_name = fd.askopenfilename(filetypes=(('texts', '*.txt'), ('All files', '*.*')))
    with open(file_name, 'rb') as f:
        code.word_new = pickle.load(f)
    Text2.delete(1.0, 'end')
    code.Decoder()
    
        
form = tk.Tk()
form.wm_title('Алгоритм Шеннона')
form.wm_resizable(width=False, height=False)

label1 = tk.Label(form, text='Текст который хотите закодировать')
label1.grid(row=0, column=0)

label2 = tk.Label(form, text='Код')
label2.grid(row=0, column=2)

Text1 = tk.Text(form, wrap=tk.WORD, height=17, width=60)
Text1.grid(row=1, column=0)

Text2 = tk.Text(form, wrap=tk.WORD, height=17, width=60)
Text2.grid(row=1, column=2)

button_open = tk.Button(form,text='Открыть', height=2, width=15, command=open_file)
button_open.grid(row=2, column=0, pady=10)

button_cod = tk.Button(form,text = 'Кодировать', height=2, width=15, command=make_code)
button_cod.grid(row=2, column=2, pady=10)

button_save = tk.Button(form,text = 'Сохранить код\nи ключ для кода', height=2, width=15, command=save_code)
button_save.grid(row=2, column=1, pady=10)

button_decode = tk.Button(form,text = 'Декодировать с \n помощью ключа', height=2, width=15, command=decode_file)
button_decode.grid(row=1, column=1, pady=10)

form.mainloop()