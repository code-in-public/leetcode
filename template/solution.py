#!/usr/bin/env python3

class Solution(object):
    def get_predecessors(self, word):
        """
        Return a list of words with 1 character removed from the
        provided word
        """
        predecessors = []
        for idx in range(len(word)):
            predecessors.append(word[:idx]+word[idx+1:])

        return predecessors

    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # Sort to ensure predecessor length has been calculated
        words.sort(key=lambda word:len(word))

        # ["a","ba","bda","bdca"].
        #   1   2     3     4
        word_to_chain_length = {}
        max_chain_length = 1

        # For each word, find possible predecessors, and their
        # number of predecessors
        for word in words:
            word_to_chain_length[word] = 1
            predecessors = self.get_predecessors(word)
            max_predecessor_chain_length = word_to_chain_length[word]

            # Get the chain length for each predecessor
            for predecessor in predecessors:
                if predecessor in word_to_chain_length:
                    chain_length = word_to_chain_length[predecessor]
                    max_predecessor_chain_length = max(max_predecessor_chain_length, chain_length + 1)

            word_to_chain_length[word] = max_predecessor_chain_length
            max_chain_length = max(max_chain_length, max_predecessor_chain_length)

        print(word_to_chain_length)
        return max_chain_length
