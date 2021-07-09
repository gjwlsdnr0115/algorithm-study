# Data Structure

### Problems
- [10828 - Stack](https://www.acmicpc.net/problem/10828)
- [9093 - Reverse string](https://www.acmicpc.net/problem/9093)
- [9012 - VPS](https://www.acmicpc.net/problem/9012)
- [1874 - Stack sequence](https://www.acmicpc.net/problem/1874)
- [1406 - Editor](https://www.acmicpc.net/problem/1406)
- [10845 - Queue](https://www.acmicpc.net/problem/10845)
- [1158 - Josephus](https://www.acmicpc.net/problem/1158)
- [10866 - Deque](https://www.acmicpc.net/problem/10866)
- [17413 - Reverse String2](https://www.acmicpc.net/problem/17413)
- [10799 - Pipe](https://www.acmicpc.net/problem/10799)
- [17298 - Larger Number](https://www.acmicpc.net/problem/17298)
- [17299 - Frequent Number](https://www.acmicpc.net/problem/17299)
- [1935 - Postfix2](https://www.acmicpc.net/problem/1935)
- [1918 - Postfix](https://www.acmicpc.net/problem/1918)
- [10808 - Alphabet Count](https://www.acmicpc.net/problem/10808)
- [10809 - Find Alphabet](https://www.acmicpc.net/problem/10809)
- [10820 - String](https://www.acmicpc.net/problem/10820)
- [2743 - String Length](https://www.acmicpc.net/problem/2743)
- [11655 - ROT13](https://www.acmicpc.net/problem/11655)
- [10824 - Four Numbers](https://www.acmicpc.net/problem/10824)
- [11656 - Suffix Sort](https://www.acmicpc.net/problem/11656)



##

### Solutions
- [10828](./10828_stack.py)
- [9093](./9093_reverse_string.py)
- [9012](./9012_parenthesis.py)
- [1874](./1874_stack_sequence.py)
- [1406](./1406_editor.py)
- [10845](./10845_queue.py)
- [1158](./1158_josephus.py)
- [10866](./10866_deque.py)
- [17413](./17413_reverse_string2.py)
- [10799](./10799_pipe.py)
- [17298](./17298_larger_num.py)
- [17299](./17299_frequent_num.py)
- [1935](./1935_postfix2.py)
- [1918](./1918_postfix.py)
- [10808](./10808_alphabet_count.py)
- [10809](./10809_find_alphabet.py)
- [10820](./10820_string.py)
- [2743](./2743_string_len.py)
- [11655](./11655_ROT13.py)
- [10824](./10824_four_nums.py)
- [11656](./11656_suffix_sort.py)


##

### Takeaways

- **Reverse String**
  ```
  >>> string = 'Hello'
  >>> string[::-1]
  'olleH'
  ```

- <code>**string.join(iterable)**</code>
  - Takes all items in an iterable and joins them into one string
  - `string`: separator
  ```
  >>> l = [1, 2, 3, 4]
  >>> ''.join(l)
  '1234'
  ```

- **Reverse List**
  ```
  >>> l = [1, 2, 3, 4]
  >>> l.reverse()
  >>> l
  [4, 3, 2, 1]
  ```
  or 
  ```
  >>> l = [1, 2, 3, 4]
  >>> l2 = list(reversed(l))
  >>> l2
  [4, 3, 2, 1]
  ```

- **Get size of `queue` & `deque`**
  ```
  import queue
  from collections import deque

  q = queue.Queue()
  dq = deque([])

  q.qsize()
  len(dq)
  ```

- **Get front and back of `deque`**
  - Use index
  ```
  front = dq[0]
  back = dq[-1]
  ```

- **Check `char` type**
  - alphabet
  ```
  >>> c = 'a'
  >>> c.isalpha()
  True
  ``` 
  - lowercase
  ```
  >>> c = 'a'
  >>> c.islower()
  True
  ``` 
  - uppercase
  ```
  >>> c = 'A'
  >>> c.isupper()
  True
  ``` 
  - numeric
  ```
  >>> c = '1'
  >>> c.isnumeric()
  True
  ``` 
  - space
  ```
  >>> c = ' '
  >>> c.isspace()
  True
  ``` 