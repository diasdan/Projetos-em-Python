from time import sleep
import argparse
import sys

def writeText(string, speed):
    listOfWords = []
    word = []
    for c in string:
        if "\n" in c:
            c = c.replace("\n", " ")
        if c != " ":
            word.append(c)
        else:
            word = "".join(word)
            listOfWords.append(word)
            word = []

    maxLen = max(len(j) for j in listOfWords)

    for j in listOfWords:

        linha = f"{j.ljust(maxLen)}"

        sys.stdout.write('\r' + "       " + linha)
        sys.stdout.flush()
        sleep(speed)

def writeFromFile(file, speed):
    speed = speed
    file = open(file, "r", encoding="utf-8")
    string = file.read() + " endOfText"
    writeText(string, speed)

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help="Read from file")
parser.add_argument('-t', '--text', help="Read text")
parser.add_argument('-s', '--step', help="Enter the text step")
args = parser.parse_args()

try:
    try:  
        step = float(args.step)

        if args.file:
            file = args.file   
            writeFromFile(file, step)

        if args.text:
            text = args.text + " endOfFile"
            writeText(text, step)

    except TypeError:
        print("Erro. Verifique se os valores informados estão corretos e se todos os parâmetros foram usados.")
except KeyboardInterrupt:
    print("\n\n   Script interrompido.")


    