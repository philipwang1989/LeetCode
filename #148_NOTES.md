# Leetcode 148

Problem statement:
Sort a linked list in O(n log n) time using constant space complexity.

To solve the problem we need to understand the following:

## Two pointers

To split a singly-linked list:

```python
def listSplit(head):
    if not head or not head.next:
        return head
    fast, slow = head.next, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    second = slow.next
    slow.next = None
```

If fast OR fast.next is None, we reached the end of the linked list. fast start from node 2 whereas slow start from node 1 (head). Therefore, fast always move in even number of node label (2,4,6,8,...) and slow move in odd-even-odd-even-...

In the case of

* Even number of nodes: while loop terminates due to fast.next = None, second start at N/2 + 1, [1,2,3,4,5,6] -> [1,2,3], [4,5,6]
* Odd number of nodes: while loop terminates due to fast = None, second start at N//2 + 1, [1,2,3,4,5,6,7] -> [1,2,3,4], [5,6,7]

One application of two pointers and linked list is one can use the two splited list to check for palindrom.

## Mergesort

```python
def msort(nums):
    if len(nums) <= 1:
        return nums[:] # return a COPY
    midpoint = len(nums) // 2
    left = msort(nums[:midpoint])
    right = msort(nums[midpoint:])
    sorted_nums = merge(left, right)
    return sorted_nums

def merge(left, right):
    l = 0
    r = 0
    q = []
    llen = len(left)
    rlen = len(right)
    while l < llen and r < rlen:
        if left[l] <= right[r]:
            q.append(left[l])
            l += 1
        else:
            q.append(right[r])
            r += 1
    if l < llen:
        q.extend(left[l:])
    elif r < rlen:
        q.extend(right[r:])
    return q
```

## Linked list

```python
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
```

## Solution

```python
# merge sort, recursively
def sortList(self, head):
    if not head or not head.next:
        return head
    # divide list into two parts
    fast, slow = head.next, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    second = slow.next
    # cut down the first part
    slow.next = None
    l = self.sortList(head)
    r = self.sortList(second)
    return self.merge(l, r)

# merge in-place without dummy node
def merge(self, l, r):
    if not l or not r:
        return l or r
    if l.val > r.val:
        l, r = r, l
    # get the return node "head"
    head = pre = l
    l = l.next
    while l and r:
        if l.val < r.val:
            l = l.next
        else:
            nxt = pre.next
            pre.next = r
            tmp = r.next
            r.next = nxt
            r = tmp
        pre = pre.next
    # l and r at least one is None
    pre.next = l or r
    return head
```
