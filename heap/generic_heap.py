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

  def get_priority(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    # while index is greater than 0
    # get the parent (i-1 / 2)
    # if child is greater than parent
    # swap them
    # if not, then we're still inside the while loop, but we have nothing to do
    # break

  def _sift_down(self, index):
    # while the index is less than max index
    # look at both children, choose the biggest
    # left child: 2 * index, + 1
    # right child: 2 * index, +1
    # swap with that child, update index to the new location
