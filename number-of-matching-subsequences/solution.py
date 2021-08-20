#!/usr/bin/env python3

class Solution(object):
    def __init__(self):
        self.cache = {}

    def is_in_cache(self, s, word):
        #print("Checking cache with " + s + " " + word)
        #print("Cache is:")
        #print(self.cache)
        if s in self.cache:
            #print("Found s " + s + " in cache ")
            if word in self.cache[s]:
                #print("Found word " + word + " in cache ")
                return True
                #return self.cache[s][word]
        else:
            self.cache[s] = {}

        return False

    def isSubseq(self, s, word):
        if self.is_in_cache(s, word):
            #print("CACHE HIT " + s + " " + word)
            return self.cache[s][word]

        string_start_idx = 0
        word_start_idx = 0

        while string_start_idx < len(s) and word_start_idx < len(word):
            if s[string_start_idx] == word[word_start_idx]:
                # Matching chars
                string_start_idx += 1
                word_start_idx += 1
            else:
                string_start_idx += 1

        if word_start_idx >= len(word):
            self.cache[s][word] = True
            return True

        self.cache[s][word] = False
        return False

    """
    # Recursive solution for the LULs
    def isSubseq(self, s, word):
        if len(s) == 0 and len(word) == 0:
            return True

        if len(s) == 0:
            return False

        if len(word) == 0:
            return True

        if s[0] == word[0]:
            return self.isSubseq(s[1:], word[1:])

        return self.isSubseq(s[1:], word[0:])
    """

    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """

        count = 0
        for word in words:
            if self.isSubseq(s, word):
                #print(s)
                #print(word)
                count += 1

        return count
