# -*- coding: utf-8 -*-
import re
import codecs
import argparse
import selectors
from datetime import datetime
from collections import Counter
startTime = datetime.now()

class WordCount:

    def __init__(self, in_filename, out_filename):
        self.in_filename = in_filename
        self.out_filename = out_filename

        self.myfile = codecs.open(self.in_filename ,'r', encoding = 'utf-8')
        self.writeText = 'INDEX QUANTITY VALUE\n'


    def pairFrequency(self):
        print 'Parsing text'
        data = self.myfile.read()
        pairs = Counter()
        first, second = 0, 1

        for i in data:
            combo = "%s%s" %(data[first], data[second])
            if not combo.__contains__(' '):
                pairs[combo] += 1

            first += 1
            second += 1

            if second == len(data):
                break
        return pairs


    def regexFrequency(self, data):
        print 'Parsing text...'
        count = Counter()

        for i in self.myfile:
            seperate = re.findall(data, i, re.UNICODE)
            for j in seperate:
                count[j] += 1
        return count


    def wordFrequency(self):
        print 'Parsing text...'
        count = Counter()
        punct = u"""!"#%\'()−*+,-.–/:;<=>?@[\]^_`„{|}~।«‘‛“‟‹⸂⸄⸉⸌⸜⸠»’”›⸃⸅⸊⸍⸝⸡¿¡"""
        punctDict = dict((ord(char),u" ") for char in punct)
        for i in self.myfile:
            try:
                seperate = i.lower().translate(punctDict).encode('utf-8')
                for j in seperate.decode('utf-8').split():
                    count[j] += 1
            except:
                UnicodeWarning
        return count


    def txtWriter(self, *args):
        print 'Writing text'
        index = 1
        txtFile = open(self.out_filename,'w')
        txtFile.write('INDEX QUANT VALUE\n')
        for j in args:
            for i in sorted(j, key=j.get):
                l = "%s %s %s\n" %(index, j[i], i.encode('utf-8'))
                txtFile.write(l)
                index += 1
        txtFile.close()


def main():
##########
    #Command line arguement parser
    parser = argparse.ArgumentParser(description='<INPUT.txt> <OUTPUT.txt> <OPTION> Count letters, letter pairs and words in text files. Parser can also handle non-Latin scripts')
    parser.add_argument('i',help="Enter the Name of Input File")
    parser.add_argument('o',help="Enter the Name of Output File")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-w','--words',help="Write word frequency", action='store_true')
    group.add_argument('-l','--letters',help="Write letter frequency", action='store_true')
    group.add_argument('-p','--pairs',help="Write pair frequency", action='store_true')

    group.add_argument('-dc','--Devanagari_Conjuncts',help="Find Devanagari Conjuncts", action='store_true')

    group.add_argument('-bc','--Bengali_Conjuncts',help="Find Bengali Conjuncts", action='store_true')
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
        word = master.wordFrequency()
        master.txtWriter(word)

    elif args.letters:
        letter = master.regexFrequency(selectors.letters)
        master.txtWriter(letter)

    elif args.pairs:
        pair = master.pairFrequency()
        master.txtWriter(pair)

    elif args.Devanagari_Conjuncts:
        dConjunct = master.regexFrequency(selectors.devaConjuncts)
        master.txtWriter(dConjunct)

    elif args.Bengali_Conjuncts:
        bConjunct = master.regexFrequency(selectors.banglaConjuncts)
        master.txtWriter(bConjunct)
    else:
        word = master.wordFrequency()
        master.txtWriter(word)

    print 'Finished in ' + str(datetime.now() - startTime)
##########

if __name__ == "__main__":
    main()
