#!/usr/bin/env python3

class Solution:
    def compareWords(self, word1, word2, order):
        # Compare first letters, if None
        if word1 == '':
            return True

        if word2 == '':
            return False

        # Compare first letters
        if order.find(word1[0]) < order.find(word2[0]):
            return True

        if word1[0] == word2[0]:
            return self.compareWords(word1[1:], word2[1:], order)

        return False

    def isAlienSorted(self, words, order):
        for i in range(len(words) - 1):
            if self.compareWords(words[i], words[i+1], order):
                pass
            else:
                return False

        return True
