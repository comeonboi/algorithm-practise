import collections
from collections import OrderedDict
from typing import List
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        # 如果key在字典中，返回value
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]

        else:
            # 如果key不在字典中，返回-1
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 如果key在字典中，更新value
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                # 如果key不在字典中，且字典已满，删除最近最少使用的元素
                self.cache.popitem(last=False)
            # 如果key不在字典中，且字典未满，添加元素
            # self.cache.move_to_end(key)
            self.cache[key] = value


lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
print(lRUCache.get(1))
lRUCache.put(3, 3)
print(lRUCache.get(2))
lRUCache.put(4, 4);
print(lRUCache.get(1))
print(lRUCache.get(3))
print(lRUCache.get(4))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)