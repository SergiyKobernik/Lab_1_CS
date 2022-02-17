import codecs
import bz2
global Symbol_base64

def Binary_conv(Letters_list):
    Binary_list = ""
    for i in Letters_list:
        x = ord(i)
        y = bin(x)
        z = y.replace("0b",(18-len(y))*"0")
        Binary_list += z
    if(len(Binary_list)%6 == 2):
        Binary_list += 4 * "0"
    else: Binary_list += 2 * "0"
    return Binary_list

def Base64_conv(Text_for_conv):
    Symbol_base64 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+',
                '/']

    Letters_list = list(Text_for_conv)
    Output_list = ""
    LettersInBinary = Binary_conv(Letters_list)

    for k in range(0, len(LettersInBinary), 6):
        x = LettersInBinary[k:k + 6]
        Output_list += Symbol_base64[int(x, 2)]

    Output_list += "="*(len(Letters_list)%3)
    return Output_list

StartPath1 = "C:/Users/sgkob/Desktop/Зацвіла в долині червона калина.txt"
file = codecs.open(StartPath1, "r", encoding='utf-8')
Text_for_conv = file.read()
file.close()

File=codecs.open("C:/Users/sgkob/Desktop/1.txt","w",encoding='utf-8')
File.write(Base64_conv(Text_for_conv))
File.close

StartPath2 = "C:/Users/sgkob/Desktop/Таємниця козацької шаблі.txt"
file = codecs.open(StartPath2, "r", encoding='utf-8')
Text_for_conv = file.read()
file.close()

File=codecs.open("C:/Users/sgkob/Desktop/2.txt","w",encoding='utf-8')
File.write(Base64_conv(Text_for_conv))
File.close

StartPath3 = "C:/Users/sgkob/Desktop/Технічний огляд UDP.txt"
file = codecs.open(StartPath3, "r", encoding='utf-8')
Text_for_conv = file.read()
file.close()

File=codecs.open("C:/Users/sgkob/Desktop/3.txt","w",encoding='utf-8')
File.write(Base64_conv(Text_for_conv))
File.close

StartPath4="C:/Users/sgkob/Desktop/Зацвіла_в_долині_червона_калина.txt.bz2"
with bz2.open(StartPath4, "rt") as ArFile:
    ArText = ArFile.read()

File=codecs.open("C:/Users/sgkob/Desktop/4.txt","w",encoding='utf-8')
File.write(Base64_conv(ArText))
File.close

StartPath5="C:/Users/sgkob/Desktop/Таємниця_козацької_шаблі.txt.bz2"
with bz2.open(StartPath4, "rt") as ArFile:
    ArText = ArFile.read()

File=codecs.open("C:/Users/sgkob/Desktop/5.txt","w",encoding='utf-8')
File.write(Base64_conv(ArText))
File.close

StartPath6="C:/Users/sgkob/Desktop/Технічний_огляд_UDP.txt.bz2"
with bz2.open(StartPath6, "rt") as ArFile:
   ArText = ArFile.read()

File=codecs.open("C:/Users/sgkob/Desktop/6.txt","w",encoding='utf-8')
File.write(Base64_conv(ArText))
File.close