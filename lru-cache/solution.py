from collections import namedtuple

CachedItem = namedtuple('cachedItem', ['value', 'key', 'previousItem', 'nextItem'])

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

        # Contains cachedItems
        self.cache = {}

        # The key of the most recently used item
        self.head_key = None

        # The key of the least recently used item
        self.tail_key = None


    def evict(self):
        # Check if capacity has been reached
        if len(self.cache) > self.capacity:
            # Remove last cache item
            tailNode = self.cache[self.tail_key]

            self.tail_key = tailNode.previous.key
            self.cache[self.tail_key].next = None

            self.cache.pop(tailNode.key)


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:

            # The entry already exsists
            newHeadNode = self.cache[key]

            # Get the head node
            headNode = self.cache[self.head_key]
            headNode.next = newHeadNode
            newHeadNode.previous = headNode

            return self.cache[key].value
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        # Add new element
        newHeadNode = None
        if key in self.cache:
            # The entry already exsists
            newHeadNode = self.cache[key]
        else:
            newHeadNode = CachedItem(value, key, None, None)
            self.cache[key] = newHeadNode

        # Get the head node
        if self.head_key:
            headNode = self.cache[self.head_key]
            headNode.next = newHeadNode
            newHeadNode.previous = headNode
            self.head_key = newHeadNode.key

        # Evict if required
        self.evict()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
