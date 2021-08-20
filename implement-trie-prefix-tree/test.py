#!/usr/bin/env python3

import unittest
from solution import Trie

class TestMethods(unittest.TestCase):
    def test_create_trie(self):
        trie = Trie();
        self.assertTrue(isinstance(trie, Trie))

    def test_insert_a_single_character(self):
        trie = Trie();
        trie.insert('a')

        a_node = trie.children['a']

        # Should be terminal as its the end of the word
        self.assertTrue(a_node.is_terminal)

    def test_insert_a_single_character(self):
        trie = Trie();
        trie.insert('a')
        trie.insert('b')

        a_node = trie.children['a']
        b_node = trie.children['b']

        # Should be terminal as its the end of the word
        self.assertTrue(a_node.is_terminal)
        self.assertTrue(b_node.is_terminal)

    def test_insert_two_characters(self):
        trie = Trie();
        trie.insert('ab')

        a_node = trie.children['a']
        b_node = a_node.children['b']

        # Should be terminal as its the end of the word
        self.assertFalse(a_node.is_terminal)

        self.assertTrue(b_node.is_terminal)
        self.assertEqual('b', b_node.value)

    def test_insert_two_characters_subset(self):
        trie = Trie();
        trie.insert('ab')
        trie.insert('a')

        a_node = trie.children['a']
        b_node = a_node.children['b']

        self.assertTrue(a_node.is_terminal)

        self.assertTrue(b_node.is_terminal)
        self.assertEqual('b', b_node.value)

    def test_insert_and_search_single_character(self):
        trie = Trie();
        trie.insert('a')

        self.assertTrue(trie.search('a'))

    def test_insert_and_search_single_character(self):
        trie = Trie();
        trie.insert('a')

        self.assertFalse(trie.search('b'))

    def test_insert_and_search_single_character_missing(self):
        trie = Trie();
        trie.insert('a')

        self.assertFalse(trie.search('b'))

    def test_insert_and_search_word(self):
        trie = Trie();
        trie.insert('beer')
        trie.insert('beers')

        self.assertTrue(trie.search('beer'))
        self.assertTrue(trie.search('beers'))
        self.assertFalse(trie.search('bears'))

    def test_startswith_two_characters(self):
        trie = Trie();
        trie.insert('ab')

        self.assertTrue(trie.startsWith('a'))

    def test_startswith_two_characters_fail(self):
        trie = Trie();
        trie.insert('ab')

        self.assertFalse(trie.startsWith('b'))

    def test_startswith_beer(self):
        trie = Trie();
        trie.insert('beer')

        self.assertTrue(trie.startsWith('beer'))

    def test_insert_and_search_two_characters(self):
        trie = Trie();
        trie.insert('xy')

        x_node = trie.children['x']
        y_node = x_node.children['y']
        self.assertTrue(y_node.is_terminal)
        self.assertEqual('y', y_node.value)

        self.assertTrue(trie.search('xy'))

    def test_search_empty_tree(self):
        trie = Trie();

        self.assertFalse(trie.search('xy'))

    def test_example(self):
        trie = Trie();
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.startsWith("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))

    def test_complex_example(self):
        ""
        trie = Trie();
        trie.insert("app")
        trie.insert("apple")
        trie.insert("beer")
        trie.insert("add")
        trie.insert("jam")
        trie.insert("rental")

        self.assertTrue(trie.startsWith("ap"))


if __name__ == '__main__':
    unittest.main()
