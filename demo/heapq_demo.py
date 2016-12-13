# -*- coding:utf-8 -*-  
"""
Create on 16/12/13
Author xiaoyy
"""

import heapq
import io
import math

# 堆以树状显示
def show_tree(tree, total_width=36, fill=' '):
   output = io.StringIO()
   last_row = -1
   for i, n in enumerate(tree):
     if i:
       row = int(math.floor(math.log(i+1, 2)))
     else:
       row = 0
     if row != last_row:
       output.write('\n')
     columns = 2**row
     col_width = int(math.floor((total_width * 1.0) / columns))
     output.write(str(n).center(col_width, fill))
     last_row = row
   print(output.getvalue())
   print('-' * total_width)
   print()
   return

li = [4, 2, 6, 9, 1, 0]
test = [3, 5, 11, 4, 6, 12, 15, 10, 9, 8, 7, 1]

heapq.heapify(li)

print("The created heap is:", end="")
print(list(li))
show_tree(li)

heapq.heappush(li, 5)
show_tree(li)
heapq.heappush(li, 3)
show_tree(li)

heapq.heapify(test)

print(list(test))

print("The modified heap after push is:", end="")
print(list(li))
