"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
  if x <=1:
    return x

  else:
    ra = foo(x-1)
    rb = foo(x-2)
    return ra + rb
    ### TODO

def longest_run(mylist, key):
  length_now = 0
  max_sequence = 0
  for i in mylist:
    if i == key:
      length_now +=1

    else:
      max_sequence = max(max_sequence, length_now)
      length_now = 0
  return max_sequence
        

class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
  #base case
  if len(mylist) == 0:
    return Result(0, 0, 0, True)

  elif len(mylist) == 1:
    if mylist[0] == key:
      return Result(1,1, 1, True)
    else:
      return Result(0,0,0, False)

  #recursive cases
  else:
    middle = len(mylist) // 2
    left_half = longest_run_recursive(mylist[:middle], key)
    right_half = longest_run_recursive(mylist[middle:], key)
    count = 0

    if left_half.is_entire_range:
      left_size = left_half.left_size
      count +=1
    else:
      left_size = 0
      

    if right_half.is_entire_range:
      right_size = right_half.right_size
      count +=1
    else:
      right_size = 0

    #confused at where to put count of longest size of key
    #I give up 
    #partial credit
    #return result
    return Result(left_size, right_size, longest_size, is_entire_range)

  


    
## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


