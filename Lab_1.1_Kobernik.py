import numpy as np
import os
import codecs


def MainFunc1(Filepath):
    File = codecs.open(Filepath, "r", encoding='utf-8')
    File_3_text = File.read()
    File.close()
    Textlength = int(len(File_3_text))
    Data_receiver_temp = Symbols_and_Probability(File_3_text, Textlength)
    SymbolsProb = Data_receiver_temp[1]
    Symbol_Probability = Data_receiver_temp[0]
    Data_receiver_temp = Entropy_calculate(SymbolsProb, Textlength)
    MainFunc = Data_receiver_temp[0]
    InformationAmount = Data_receiver_temp[1]
    FileSize = os.path.getsize(Filepath) * 8
    Output(Filepath, MainFunc, InformationAmount, Symbol_Probability, FileSize)


def Entropy_calculate(SymbolsProb, TextLength):
    L = np.log2(SymbolsProb)
    MainFunc = (-1) * np.sum(SymbolsProb * L)
    InformationAmount = MainFunc * TextLength
    return [MainFunc, InformationAmount]


def Symbols_and_Probability(File_3_text, Textlength):
    Symbols = list(set(File_3_text))
    Symbol_Frequency = []
    Base = []
    SymbolsProb = []

    for i in range(0, len(Symbols)):
        Symbol_Frequency.append(File_3_text.count(Symbols[i]))
    for i in range(0, len(Symbols)):
        Base.append((Symbols[i], Symbol_Frequency[i]))

    Symbol_Probability = dict(Base)
    for i in range(0, len(Symbols)):
        SymbolsProb.append(int(Symbol_Frequency[i]) / Textlength)
    return [Symbol_Probability, SymbolsProb]


def FileComparison(FileSize, InformationAmount):
    if (FileSize > InformationAmount):
        line = "file size is bigger then Entropy \n " + str(FileSize) + " > " + str(InformationAmount) + "\n"
        return line
    else:
        line = "Entropy is bigger then file size \n " + str(InformationAmount) + " > " + str(FileSize) + "\n"
        return line


def Output(Filepath, MainFunc, InformationAmount, Symbol_Probability, FileSize ):
    Header = "Entropy = " + str(MainFunc) + "\n" + "Data amount = " + str(InformationAmount) + "\n" + FileComparison(FileSize, InformationAmount)
    string = str(Symbol_Probability)
    OutputText = Header + "\n \n" + string
    print(OutputText)


text_1_path = "C:/Users/sgkob/Desktop/Зацвіла в долині червона калина.txt"
text_2_path = "C:/Users/sgkob/Desktop/Таємниця козацької шаблі.txt"
text_3_path = "C:/Users/sgkob/Desktop/Технічний огляд UDP.txt"
MainFunc1(text_1_path)
MainFunc1(text_2_path)
MainFunc1(text_3_path)