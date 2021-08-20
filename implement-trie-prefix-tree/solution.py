#!/usr/bin/env python3

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.value = None

        # Terminal flag to indicate the end of the word
        self.is_terminal = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        # Get the first character of the word
        if word:
            character, word = word[0], word[1:]

            # Check if the child exists
            child = None
            if character in self.children:
                child = self.children[character]
            else:
                child = Trie()
                child.value = character

            if len(word) == 0:
                child.is_terminal = True

            child.insert(word)
            self.children[character] = child


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if word:
            character, word = word[0], word[1:]

            if character in self.children:
                child = self.children[character]

                if word:
                    return child.search(word)
                else:
                    return child.is_terminal
            else:
                return False

        return False


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if prefix:
            character, prefix = prefix[0], prefix[1:]

            if character in self.children:
                child = self.children[character]

                if prefix:
                    return child.startsWith(prefix)
                else:
                    return True
            else:
                return False

        return False
