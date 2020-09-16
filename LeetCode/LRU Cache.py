#Basically the same own solution with change the side of latest 
class DlinkNode:
    def __init__(self, key= None, value = None):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.Cache = {}
        self.dummyhead = DlinkNode()
        self.dummytail = DlinkNode()
        self.dummyhead.next = self.dummytail
        self.dummytail.prev = self.dummyhead
        self.capacity = capacity
        self.size = 0

    def removeNode(self, theNode):
        theNode.prev.next = theNode.next
        theNode.next.prev = theNode.prev

    def addToLatest(self, theNode):
        theNode.next = self.dummytail
        theNode.prev = self.dummytail.prev
        self.dummytail.prev.next = theNode
        self.dummytail.prev = theNode

    def moveToLatest(self, theNode):
        self.removeNode(theNode)
        self.addToLatest(theNode)

    def deleteOldest(self):
        oldestNode = self.dummyhead.next
        self.removeNode(oldestNode)
        return oldestNode

    def get(self, key: int) -> int:
        if key not in self.Cache:
            return -1
        else:
            theNode = self.Cache[key]
            self.moveToLatest(theNode)
            return theNode.value


    def put(self, key: int, value: int) -> None:
        if (key not in self.Cache):
            newNode = DlinkNode(key, value)
            self.Cache[key] = newNode
            self.addToLatest(newNode)
            self.size += 1
            if self.size > self.capacity:
                oldestNode = self.deleteOldest()
                self.Cache.pop(oldestNode.key)
                self.size -= 1
        else:
            theNode = self.Cache[key]
            theNode.value = value
            self.moveToLatest(theNode)
        

        return None
            

        




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
#LeetCode official solution, Dict & Double linked list
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点    
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
    
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node
