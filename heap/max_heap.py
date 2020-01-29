class Heap:
  def __init__(self, comparator):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
    self.storage.append(value)
    value_index = len(self.storage) - 1
    self._bubble_up(value_index)

  def delete(self):
    # Store what's at the front
    # put the smallest value at the front, then remove it from our storage
    # then call shift down
    # return value
    max_value = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()

    self._sift_down(0)
    return max_value


  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    # while index is greater than 0
    # get the parent (i-1 / 2)
    # if child is greater than parent
    # swap them
    # if not, then we're still inside the while loop, but we have nothing to do
    # break
    while index > 0:
      parent_index = (index - 1) // 2
      if self.storage[parent_index] < self.storage[index]:
        self.storage[parent_index], self.storage[index] = self.storage[index], self.storage[parent_index]
        index = parent_index
      
  def _sift_down(self, index):
    # while the index is less than max index
    # look at both children, choose the biggest
    # left child: 2 * index, + 1
    # right child: 2 * index, +1
    # swap with that child, update index to the new location
    max_index = len(self.storage) - 1
    child_index = (2 * index) + 1

    while child_index <= max_index:
      right_child_index = child_index + 1
      if right_child_index <= max_index and self.storage[right_child_index] > self.storage[child_index]:
        child_index = right_child_index

      if self.storage[child_index] > self.storage[index]:
        self.storage[child_index], self.storage[index] = self.storage[index], self.storage[child_index]
        index = child_index
        child_index = (2 * index) + 1

      else:
        break


