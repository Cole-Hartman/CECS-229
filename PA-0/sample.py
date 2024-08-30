"""PROBLEM 1"""
def hello(subject):
  return "Hello, " + str(subject) + "!"

"""PROBLEM 2"""
class Bug:
  def __init__(self, name, position = [0, 0]):
    # todo
    pass

  # todo: implement accessor and mutator methods

  def __str__(self):
    return f"Name: {self.name}\nPosition: ({self.position[0]}, {self.position[1]})"
    