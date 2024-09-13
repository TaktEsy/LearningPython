data = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
num_sum = 20
len_sum = 10
def res(a):

  global num_sum, len_sum


  if type(a).__name__ == 'str':
    len_sum = len(a)
  elif isinstance(a, int):
    num_sum += a
  else:
    for i in a:
      print(f"Элемент: {i}")
      return res(num_sum+len_sum)


print(res(data))