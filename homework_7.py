class MyIterable:

   def __init__(self, data):

       self.data = data

   def __iter__(self):

       for item in self.data:

           yield item

iterable = MyIterable([5, 6, 7, 8, 9])

for item in iterable:

   print(item)