"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length
  
  """Wraps the given value in a ListNode and inserts it 
  as the new head of the list. Don't forget to handle 
  the old head node's previous pointer accordingly."""

  def add_to_head(self, value):
    new_node = ListNode(value) # create a new node w/ ListNode class passing in value
    self.length += 1 # and increment self.length +1

    if not self.head and not self.tail: # check if there's not a head and tail in node
      self.head = new_node # then assign head to new_node
      self.tail = new_node # and assign tail to new_node
    else:
      new_node.next = self.head # assign next node to self.head
      self.head.prev = new_node # assign prev head to new mode
      self.head = new_node # assign head to new node
  
  """Removes the List's current head node, making the
  current head's next node the new head of the List.
  Returns the value of the removed Node."""

  def remove_from_head(self):
    if self.head is None: # if there is no head, return none
      return_value = None
    elif self.head is self.tail: # if there is only one node, set head and tail to None
      return_value = self.head.value # set the head value to return_value and return it
      self.head = None
      self.tail = None
    else:
      return_value = self.head.value # set the head value to return_value and return it
      self.head = self.head.next # set head to the next node head
      self.head.prev = None # set prev head to None.
    
    self.length -= 1 # remove length by 1
    return return_value

  """Wraps the given value in a ListNode and inserts it 
  as the new tail of the list. Don't forget to handle 
  the old tail node's next pointer accordingly."""

  def add_to_tail(self, value):
    new_tail = ListNode(value)
    self.length +=1

    if not self.head and not self.tail: # if there is no node, create one
      self.head = new_tail # by setting head to new node which we are calling new_tail
      self.tail = new_tail # set tail to new node
    else:
      new_tail.prev = self.tail # set new tail node (previous arrow) to old current tail.  
      self.tail.next = new_tail # set current tail (next arrow) to new tail node
      self.tail = new_tail # set current tail = new tail node
     
      new_tail.next = None # this is the last node so there is no next.


  """Removes the List's current tail node, making the 
  current tail's previous node the new tail of the List.
  Returns the value of the removed Node."""
  def remove_from_tail(self):

    if not self.tail: # if no tail to remove return None.
      return_value = None
    elif self.tail is self.head: # if only one node, set tail and head to None to remove
      return_value = self.tail.value
      self.tail = None
      self.head = None
    else: 
      return_value = self.tail.value 
      self.tail = self.tail.prev # set tail to previous tail
      self.tail.next = None # set tail's next arrow to None.
    
    self.length -= 1
    return return_value

  """Removes the input node from its current spot in the 
  List and inserts it as the new head node of the List."""

  def move_to_front(self, node):
    
    if self.head is None:
      return
    elif node is self.head:
      return None
    elif node is self.tail:
      node.prev.next = None # set previous node (next arrow) to None
    else: # make surrounding nodes point to each other
      node.prev.next = node.next # set previous node (next arrow) to next node
      node.next.prev = node.prev # set next node (previous arrow) to previous node
      
    # Make a new head
    node.next = self.head # make it the head, by setting the next node to self.head
    self.head.prev = node # set the previous head to node
    self.head = node # set the head to node


  """Removes the input node from its current spot in the 
  List and inserts it as the new tail node of the List."""

  def move_to_end(self, node):

    if self.head is None:
      return
    elif node is self.tail:
      return None
    elif node is self.head: 
      self.head = node.next # set head to the next node
      self.head.prev = None # then set the previous head to None
    else: # make surrounding nodes point to each toher
      node.prev.next = node.next # set previous node (next arrow) to next node
      node.next.prev = node.prev # set next node (prev arrow) to previous node
    
    # Make a new tail
    node.prev = self.tail # set incoming node (previous arrow) to the current tail
    self.tail.next = node # set current tail (next arrow) to incoming node
    self.tail = node # set the current tail to coming node


  """Removes a node from the list and handles cases where
  the node was the head or the tail"""

  def delete(self, node):
    
    self.length -= 1
    
    if self.head is self.tail: # if it is the first node only, set it to head and tail to None to delete
      self.head = None
      self.tail = None
    elif node is self.head:
      self.head = self.head.next
      self.head.prev = None
    elif node is self.tail:
      self.tail = self.tail.prev
      self.tail.next = None
    else:
      node.prev.next = node.next
      node.next.prev = node.prev
    
  """Returns the highest value currently in the list"""

  def get_max(self):
    
    if self.head is None:
      return None
    
    max_value = self.head.value
    current = self.head

    while current: # while there is a current index, loop thru the array
      if current.value > max_value: # compare if current value is greater than max value
        max_value = current.value # if it is, we want to set the max value to current value

      current = current.next # increment

    return max_value

  """Find middle element in one pass"""

  def find_middle_element(self):
    one_step_pointer = self.head  # set up two different pointers
    two_step_pointer = self.head

    while two_step_pointer is not None: # while two_step_pointer is not at the end of list which is none, loop thru the list
      two_step_pointer = two_step_pointer.next # iterate the two step pointer to next the node

      if two_step_pointer is not None: # if two step pointer is still none
        one_step_pointer = one_step_pointer.next # iterate both the pointers once
        two_step_pointer = two_step_pointer.next # now, the two step pointer has iterated twice for each loop while one step has iterated only once for each loop
    
    return one_step_pointer
  
  """Reverse a single linked list"""

  def reverse_single_linked_list(self):
    current = self.head
    new = current.next
    current.next = None

    while new is not None:
      previous = current 
      current = new
      new = current.next
      current.next = previous

    self.head, self.tail = self.tail, self.head

