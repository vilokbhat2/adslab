# prompt: Implement unlimited size stack

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
    self.size = 0

  def push(self, data):
    node = Node(data)
    if self.top:
      node.next = self.top
    self.top = node
    self.size += 1

  def pop(self):
    if self.top:
      data = self.top.data
      self.size -= 1
      self.top = self.top.next
      return data
    else:
      return None

  def peek(self):
    if self.top:
      return self.top.data
    else:
      return None

  def is_empty(self):
    return self.size == 0

  def get_size(self):
    return self.size


class Browser:
  def __init__(self):
    self.forward_stack = Stack()
    self.back_stack = Stack()
    self.current_url = None

  def go_to(self, url):
    if self.current_url:
      self.back_stack.push(self.current_url)
      self.forward_stack = Stack()
    self.current_url = url
    print("Current URL:", self.current_url)

  def go_back(self):
    if self.back_stack.is_empty():
      print("No previous pages.")
    else:
      self.forward_stack.push(self.current_url)
      self.current_url = self.back_stack.pop()
      print("Current URL:", self.current_url)

  def go_forward(self):
    if self.forward_stack.is_empty():
      print("No pages to go forward.")
    else:
      self.back_stack.push(self.current_url)
      self.current_url = self.forward_stack.pop()
      print("Current URL:", self.current_url)

# Example usage:
browser = Browser()
browser.go_to("www.google.com")
browser.go_to("www.facebook.com")
browser.go_back()
browser.go_forward()
browser.go_to("www.youtube.com")
browser.go_back()
browser.go_back()