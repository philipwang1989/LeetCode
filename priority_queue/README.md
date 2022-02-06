# Applications:

## Heap Sort
1. Heapify all elements
2. Pop top element from heap and append to result
3. Repeat

Time: O(NlogN)

Space: O(N)

## Top-K problem (largest for example)
### Approach 1
1. Construct a max heap from input.
2. Pop top element from heap and append to result K times.

Time: O(KlogN+N)

Space: O(N)

### Approach 2
1. Construct a min heap of size K.
2. Add elements to the min heap one by one.
3. When there are K elements in min heap, compare top of min heap with current:
- if the current element is no larger than the top element of the Heap, drop it and - proceed to the next element.
- if the current element is larger than the Heap’s top element, delete the Heap’s top element, and add the current element to the Min Heap.
4. Repeat 2-3 until all elements iterated.

Time: O(NlogK)

Space: O(K)

## K-th (largest for example) element
### Approach 1
1. Construct a max heap from input.
2. Pop top from max heap K times.

Time: O(KlogN+N) -> pop K times, logN each time, construct takes N

Space: O(N)

### Approach 2
1. Construct a min heap of size K.
2. Add elements to the min heap one by one.
3. When there are K elements in min heap, compare top of min heap with current:
- If the current element is not larger than the top element of the Heap, drop it and proceed to the next element.
- If the current element is larger than the Heap’s top element, delete the Heap’s top element, and add the current element to the “Min Heap”.
4. Repeat 2-3 until all elements iterated.

Time: O(NlogK)

Space: O(K)

# Examples:


# Time and space complexity of priority queue operations:

## Heapify
Time: [O(N)](https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/)

Space: O(N)

## Insert
Time: O(logN)

Space: O(1)

## Peek
Time: O(1)

Space: O(1)

## Delete
Time: O(logN)

Space: O(1)

## Size
Time: O(1)

Space: O(1)
