class CachedItem(object):
    def __init__(self, key, value, prev, nxt):
        self.key = key
        self.value = value
        self.previousItem = prev
        self.nextItem = nxt

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

        # Contains cachedItems
        self.cache = {}

        # Head and tail pointers
        # Head is always most recently used item
        self.head = None
        self.tail = None

    def add_to_front_of_list(self, cachedItem):
        # cachedItem is now in front with no previous
        cachedItem.previousItem = None
        cachedItem.nextItem = self.head

        if self.head == None:
            # Add new cachedItem to front of queue
            self.head = cachedItem
            self.tail = cachedItem
        else:
            self.head.previousItem = cachedItem
            self.head = cachedItem

    def remove_from_list(self, cachedItem):
        # Head node
        if self.head == cachedItem:
            self.head = cachedItem.nextItem

        # Tail node
        if self.tail == cachedItem:
            self.tail = cachedItem.previousItem

        # Middle node
        if cachedItem.previousItem != None:
            cachedItem.previousItem.nextItem = cachedItem.nextItem

        if cachedItem.nextItem != None:
            cachedItem.nextItem.previousItem = cachedItem.previousItem

        return cachedItem

    def evict(self):
        """
        Performs eviction on LRU items
        """
        # Check if capacity has been reached
        if len(self.cache) > self.capacity:
            # Remove last cache item
            lastItem = self.tail
            self.remove_from_list(lastItem)

            self.cache.pop(lastItem.key)

    def move_to_front_of_queue(self, cachedItem):
        # Update the items position in the queue
        self.remove_from_list(cachedItem)
        self.add_to_front_of_list(cachedItem)


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            cachedItem = self.cache[key]
            self.move_to_front_of_queue(cachedItem)

            return cachedItem.value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if key in self.cache:
            # The entry already exsists, so update
            cachedItem = self.cache[key]
            cachedItem.value = value

            # Update the items position in the queue
            self.move_to_front_of_queue(cachedItem)

        else:
            cachedItem = CachedItem(value, key, None, None)
            self.cache[key] = cachedItem

            # Add the item to the queue
            self.add_to_front_of_list(cachedItem)

        self.evict()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
