# -*- coding: utf-8 -*-
import re
import codecs
import argparse
import selectors


class WordCount:

    def __init__(self, in_filename, out_filename):
        self.in_filename = in_filename
        self.out_filename = out_filename

        self.text = ''
        self.writeText = 'INDEX, QUANTITY, VALUE\n'
        with codecs.open(self.in_filename ,'r', encoding = 'utf-8') as myfile:
            for line in myfile:
                self.text += line

    #Generic counter for simple checks
    def counter(self, vars):
        data = {}
        for i in vars:
            if i in data:
                data[i] += 1
            else:
                data[i] = 1
        return data


    def letterFrequency(self):
        letter = self.counter(self.text)
        return letter


    def pairFrequency(self):
        pairs = {}
        first = 0
        second = 1

        while True:
            combo = '%s%s' %(self.text[first], self.text[second])
            if not combo.__contains__(' '):
                if combo in pairs:
                    pairs[combo] += 1
                else:
                    pairs[combo] = 1

            first += 1
            second += 1

            if second == len(self.text):
                break
        return pairs


    def wordFrequency(self):
        #regex for all punctuation characters in unicode, look at module selectors
        #/w was not used since it only selects Latin characters.
        word = re.findall(selectors.words, self.text, re.UNICODE)
        words = self.counter(word)
        return words


    #Converts dictionaries into strings for the file writer
    def txtWriter(self, *args):
        index = 1
        for j in args:
            for i in sorted(j, key=j.get):
                self.writeText += "%s %s %s\n" %(index, j[i], i.encode('utf-8'))
                index += 1
        self.writeText += '\n'


    #Writes the file
    def fileWrite(self, datum):
        txtFile = open(self.out_filename,'w')
        txtFile.write(datum)
        txtFile.close()


def main():
##########
    #Command line arguement parser
    parser = argparse.ArgumentParser(description='<INPUT.txt> <OUTPUT.txt>\nCount letters, letter pairs and words in text files. Parser can also handle non-Latin scripts')
    parser.add_argument('i',help="Enter the Name of Input File")
    parser.add_argument('o',help="Enter the Name of Output File")
    parser.add_argument('-w','--words',help="Write only words", action='store_true')
    parser.add_argument('-l','--letters',help="Write only letter frequency", action='store_true')
    parser.add_argument('-p','--pairs',help="Write only pair frequency", action='store_true')
    args = parser.parse_args()
    i,o = None, None #input, output
##########


##########
    #Check user options
    if args.i: #If input file exists
        in_file = args.i
    else:
        print "Input and Output Files Required <INPUT.txt> <OUTPUT.txt>"
        quit()
    if args.o: #If output file exists
        out_file = args.o
    else:
        out_file = "output.txt"

    #Assign master to WordCount class
    master = WordCount(in_file, out_file)

    if args.words:
        word   = master.wordFrequency()
        master.txtWriter(word)
        print 'Done Words!'


    if args.letters:
        letter = master.letterFrequency()
        master.txtWriter(letter)
        print 'Done Letters'


    if args.pairs:
        pair   = master.pairFrequency()
        master.txtWriter(pair)
        print 'Done Pairs'

    else:
        letter = master.letterFrequency()
        pair   = master.pairFrequency()
        word   = master.wordFrequency()
        master.txtWriter(letter, pair, word)

    master.fileWrite(master.writeText)
    print 'Completed!'
##########

if __name__ == "__main__":
    main()
