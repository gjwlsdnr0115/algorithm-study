# Data Structure

### Problems
- [10828 - Stack](https://www.acmicpc.net/problem/10828)
- [9093 - Reverse string](https://www.acmicpc.net/problem/9093)
- [9012 - VPS](https://www.acmicpc.net/problem/9012)
- [1874 - Stack sequence](https://www.acmicpc.net/problem/1874)
- [1406 - Editor](https://www.acmicpc.net/problem/1406)
- [10845 - Queue](https://www.acmicpc.net/problem/10845)

##

### Solutions
- [10828](./10828_stack.py)
- [9093](./9093_reverse_string.py)
- [9012](./9012_parenthesis.py)
- [1874](./1874_stack_sequence.py)
- [1406](./1406_editor.py)
- [10845](./10845_queue.py)

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