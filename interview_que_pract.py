arr = [1,2,3,4,5]
print(arr)
arr.append(8)
print(arr)
arr.insert(2, 10)
print(arr)
val= arr.pop(2)
print(val)
dict = {"apple": 5, "banana": 2}
print(dict)
if "apple" in dict: print(dict["apple"])
dict['cherry'] = 10
print(dict)
val= dict.get('orange',0)
print(val)
#sets
s= {1,2,3}
s.add(4)
print(s)
s.remove(4)
print(s)
s.discard(1)
print(s)
print(6 in s)

#tuples and collections module
point = (10,20)
from collections import Counter, deque
print(Counter("applllle"))

#deque- double ended queue insertion and pops up on both sides
queue= deque([2,3,4])
queue.append(5)
print(queue)
queue.appendleft(1)
print(queue)
queue.pop()
print(queue)
queue.popleft()
print(queue)

#heapq(priority queues)
import heapq
h = []
print(h)
heapq.heappush(h,4)
print(h)
heapq.heappush(h,1)
heapq.heappush(h,3)
heapq.heappush(h,7)
print(h)      
smallest = heapq.heappop(h) 
print(smallest)

#for max=heap,invert values 
max_h = []
heapq.heappush(max_h, -4)
heapq.heappush(max_h, -3)
largest = -heapq.heappop(max_h)
print(largest)


#sorting and comman string methods
arr = [1,2,3,4,58]
arr.sort()
print(arr)
sorted_arr = sorted(arr, reverse = True)
print(arr)

s = " hello world "
print(s)
s= s.strip()
print(s)
print(s.split())
print("-".join(s.split()))
print(s.isalpha())

# stndard input/output parsing snippets

n = int(input().strip())

arr = list(map(int, input().split()))

param1 , param2, = input().split()