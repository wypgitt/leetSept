# 146. LRU Cache
'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            n = self.dic[key]
            self.remove(n)
            self.add(n)
            return n.val
        return -1
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dic:
            self.remove(self.dic[key])
        n = Node(key, value)
        self.add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self.remove(n)
            del self.dic[n.key]
            
    def remove(self, node):
        p = node.prev
        x = node.next
        p.next = x
        x.prev = p
    def add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

        
'''
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._cap = capacity 
        self._cache = collections.OrderedDict()  

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self._cache: return -1
        val = self._cache[key]
        self._cache.move_to_end(key)
        return val 
        
        
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self._cache:
            del self._cache[key]
            self._cache[key] = value 
        
        elif len(self._cache) == self._cap:
            self._cache.popitem(last=False)
            
        self._cache[key] = value 

'''        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

