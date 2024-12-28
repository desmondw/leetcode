
#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.key)

class LRUCache:

    # doublely linked list
    # register contains reference to corresponding node
    # maintain pointer to head, tail
    # O(1) to find, delete, insert (newest), pop (oldest)

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.register = {} # { key:node }

    def __prependHead(self, key: int):
        # prepend to linked list
        self.register[key].prev = self.head.prev
        self.register[key].next = self.head
        self.head = self.register[key]
        self.head.prev.next = self.head
        self.head.next.prev = self.head

    # verify this works for register sizes of 0,1,2
    def __access(self, key: int, value: int = None) -> int:
        # print('access')
        # get (doesn't exist)
        if value is None and key not in self.register:
            return -1

        # get (exists) or update
        if key in self.register:
            # update value
            if value is not None:
                self.register[key].value = value

            if self.head.key == key:
                return self.register[key].value

            if len(self.register) >= 3:
                # remove from linked list
                self.register[key].prev.next = self.register[key].next
                self.register[key].next.prev = self.register[key].prev
                self.__prependHead(key)
            elif len(self.register) == 2:
                self.head = self.register[key]
        # create
        elif value is not None:
            # remove tail (least recently used)
            if len(self.register) >= self.capacity:
                tailKey = self.head.prev.key
                self.head.prev = self.head.prev.prev
                self.head.prev.next = self.head
                del self.register[tailKey]


            # create node
            self.register[key] = Node(key, value)
            if len(self.register) == 1:
                self.head = self.register[key]
                self.head.next = self.head
                self.head.prev = self.head
            else:
                self.__prependHead(key)

        return self.register[key].value

    def printLL(self):
        txt = '{'
        for key in self.register:
            # txt += f'{key}:<{self.register[key].prev}->{self.register[key].next}>, '
            txt += f'{key} <{self.register[key].prev}-{self.register[key].next}>, '
        txt += '}'
        return txt

    def get(self, key: int) -> int:
        res = self.__access(key)
        # print(f'[{len(self.register)}] HEAD-TAIL<{self.head}-{self.head.prev if self.head else None}> | get {key} | {self.printLL()}')
        return res

    def put(self, key: int, value: int) -> None:
        self.__access(key, value)
        # print(f'[{len(self.register)}] HEAD-TAIL<{self.head}-{self.head.prev if self.head else None}> | put {key} | {self.printLL()}')



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

