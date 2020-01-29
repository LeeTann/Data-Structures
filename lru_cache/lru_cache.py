from doubly_linked_list import DoublyLinkedList

class LRUCache:
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.

  - max number of nodes it can hold
  - current number of nodes it is holding

  - we want to hold key-value entries in order
  - we want to find the lease-recently-used entry and delete it
  - we want to add things in the front (most recently used thing)
  """
  def __init__(self, limit=10):
    self.limit = limit
    self.size = 0
    self.cache = {}
    self.dll = DoublyLinkedList()

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    if key in self.cache:
      node = self.cache[key]
      self.dll.move_to_end(node)
      return node.value[1]
    else:
      return None

  """
  Case 1: Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. 
  
  Case 2: If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. 
  
  Case 3: Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    if key in self.cache:
      node = self.cache[key]
      node.value = (key, value)
      self.dll.move_to_end(node)
      return

    if self.size == self.limit:
      del self.cache[self.dll.head.value[0]]
      self.dll.remove_from_head()
      self.size -= 1

    self.dll.add_to_tail((key, value))
    self.cache[key] = self.dll.tail
    self.size += 1
