import sys


class Descrambler:

    # class variables for storing word banks
    THREE_LETTER_WORDS = []
    FOUR_LETTER_WORDS = []
    FIVE_LETTER_WORDS = []
    SIX_LETTER_WORDS = []
    SEVEN_LETTER_WORDS = []

    # flag for printing sorted word output
    verboseFlag = False


    # function name: __init__
    # paramters: bool verbose: Determines whether or not 
    #            to output final product to console
    # returns: N/A
    # algorithm: set verbose flag, make call to populateWordBank
    def __init__(self, verbose):
        self.populateWordBank()
        self.verboseFlag = verbose


    # function name: descramble
    # parameters: str originalWord: anagram to be descrambled
    # returns: a dictionary containing de-scrambled words of length 3 - 5.
    #          keys of this dictionary are the desired word length.
    # algorithm: compute all permutations of the anagram. crosscheck these 
    #            permutations with the words in the word banks. sort these 
    #            words into a dictionary based on length. return.
    def descramble(self, originalWord):
        allPermutations = set()
        allPermutations.update(self.descrambleHelper(originalWord.lower(), '', allPermutations))

        crossChecked = self.crossCheck(allPermutations)
        sortedWords = self.sortByLength(crossChecked)

        return sortedWords


    # function name: descrambleHelper
    # parameters: str originalWord: remaining characters of the original anagram, 
    #                  at the current level of recursion. 
    #             str workingWord: permutation thus far at the current level of recursion.
    #             set descrambledSet: set of all permutations up until this point
    # returns: set of all permutations computed thus far.
    # algorithm: Recursively adds a new letter to the end of the working word.
    #            if the working word is of length three or greater, add to the descrambled set. 
    def descrambleHelper(self, originalWord, workingWord, descrambledSet):
        if len(workingWord) > 2:
            descrambledSet.add(workingWord)

        for i in range(len(originalWord)):
            selectedChar = originalWord[i]
            newWorkingWord = workingWord + selectedChar
            newWord = originalWord.replace(selectedChar, '', 1)
            descrambledSet.update(self.descrambleHelper(newWord, newWorkingWord, descrambledSet))

        
        return descrambledSet


    # function name: populateWordBank
    # parameters: N/A.
    # returns: N/A.
    # algorithm: checks for unpopulated word banks. If found, the contents
    #            of the corresponding word file will be loaded into the word bank.
    def populateWordBank(self):
        if len(self.THREE_LETTER_WORDS) == 0:
            wordFile = open('words/3-letter.txt')
            workingWords = wordFile.readlines()
            wordFile.close()

            for word in workingWords:
                word = word.strip("\n")
                self.THREE_LETTER_WORDS.append(word.lower())

        if len(self.FOUR_LETTER_WORDS) == 0:
            wordFile = open('words/4-letter.txt')
            workingWords = wordFile.readlines()
            wordFile.close()

            for word in workingWords:
                word = word.strip("\n")
                self.FOUR_LETTER_WORDS.append(word.lower())

        if len(self.FIVE_LETTER_WORDS) == 0:
            wordFile = open('words/5-letter.txt')
            workingWords = wordFile.readlines()
            wordFile.close()

            for word in workingWords:
                word = word.strip("\n")
                self.FIVE_LETTER_WORDS.append(word.lower())

        if len(self.SIX_LETTER_WORDS) == 0:
            wordFile = open('words/6-letter.txt')
            workingWords = wordFile.readlines()
            wordFile.close()

            for word in workingWords:
                word = word.strip("\n")
                self.SIX_LETTER_WORDS.append(word.lower())

        if len(self.SEVEN_LETTER_WORDS) == 0:
            wordFile = open('words/7-letter.txt')
            workingWords = wordFile.readlines()
            wordFile.close()

            for word in workingWords:
                word = word.strip("\n")
                self.SEVEN_LETTER_WORDS.append(word.lower())


    # function name: sortByLength
    # parameters: set wordSet: set of permutations to be sorted.
    # returns: dictionary of sorted words with an integer key corresponding
    #          the list of the words. (i.e. accessing with a key of 3 will yield)
    #          a list of words of length 3.
    # algorithm: loops through the word set, adds the indiviual words into the dict
    #            according to their length. returns the dict.
    def sortByLength(self, wordSet):
        sortedWords = {
            3: [],
            4: [],
            5: [],
            6: [],
            7: []
        }

        for word in wordSet:
            wordLen = len(word)
            sortedWords[wordLen].append(word)

        if self.verboseFlag:
            for key in sortedWords:
                print("\nLENGTH OF " + str(key) + " ===============")
                for word in sortedWords[key]:
                    print(word)


        return sortedWords


    # function name: crossCheck
    # parameters: set wordSet: set of words to be cross checked with the word banks
    # returns: set of words that are in both the original word set and any of the word banks
    # algorithm: uses python set functions to grab the words common in the word set
    #            and any of the word banks.
    def crossCheck(self, wordSet):
        verifiedWordSet = set() 

        verifiedWordSet.update(wordSet.intersection(set(self.THREE_LETTER_WORDS)))
        verifiedWordSet.update(wordSet.intersection(set(self.FOUR_LETTER_WORDS)))
        verifiedWordSet.update(wordSet.intersection(set(self.FIVE_LETTER_WORDS)))
        verifiedWordSet.update(wordSet.intersection(set(self.SIX_LETTER_WORDS)))
        verifiedWordSet.update(wordSet.intersection(set(self.SEVEN_LETTER_WORDS)))

        return verifiedWordSet


def main():
    d = Descrambler(True)

    if (len(sys.argv) > 1):
        word = sys.argv[1]
        d.descramble(word)
    
    else:
        print("========================================================")
        print("|             Welcome to the descrambler!!             |")
        print("| Type in an anagram and press enter to descramble it. |")
        print("| At any time, type '\\exit' to terminate the program.  |")
        print("========================================================")

        while True:
            word = input("\n\nEnter a word to be descrambled (type '\\exit' to terminate the program): ")

            if word == '\\exit':
                break

            d.descramble(word)

if __name__ == "__main__":
    main()