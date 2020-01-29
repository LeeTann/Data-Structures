class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    node = BinarySearchTree(value) # call the BinarySearchTree and pass in the value. set it to node.

    if value < self.value: # if the insert value is less than the current value, we go left
      if self.left == None: # and if there is no left node
        self.left = node # then set the left node equal to the node which is BinarySearchTree(value)
      else:
        self.left.insert(value) # else insert value to the left node
    else:
      if self.right == None:
        self.right = node
      else:
        self.right.insert(value)
    
  def contains(self, target):
    if target == self.value:
      return True

    if target < self.value: # if target value is less than current value go left.
      if self.left: # check if we can keep going left, if we can 
        return self.left.contains(target) # return and keep calling contain function on left side recursively
      else:
        return False
    
    if target > self.value:
      if self.right:
        return self.right.contains(target)
      else:
        return False

  def get_max(self):
    if self.right: # if there is a right side, 
      return self.right.get_max() # return and keep calling right side get_max function recursively until there is no more right side
    else:
      return self.value # then if no more right side child we return self.value because we know the current node is the lowest it can go and is the max value

  def for_each(self, cb): # a depth first search

    cb(self.value) # call the callback on self.value

    if self.left: # if there is self.left side
      self.left.for_each(cb) # then keep recursively calling the for_each(cb) function to go thru all the left side

    if self.right:
      self.right.for_each(cb)

  def dft_non_recursive(self, cb):
    stack: []
    stack.append(self)

    while(len(stack)):
      current_node = stack.pop()
      if current_node.left:
        stack.append(current_node.left)
      if current_node.right:
        stack.append(current_node.right)

      cb(current_node.value)

  def bft_for_each(self, cb):
    q = Queue()
    q.enqueue(self)

    while(len(q)):
      current_node = q.dequeue()
      if current_node.left:
        q.enqueue(current_node.left)
      if current_node.right:
        q.enqueue(current_node.right)

      cb(current_node.value)