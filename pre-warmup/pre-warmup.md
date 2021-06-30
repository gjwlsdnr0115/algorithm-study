# Warm up

### Problems
- [URL](https://www.acmicpc.net/step)

##

### Solutions
- [Standard in/out](./1.in-out)
- [if](./2.if)
- [for](./3.for)
- [while](./4.while)
- [Array](./5.1d-array)
- [string](./6.string)
- [Function](./7.functions)
- [Math1](./8.math1)
- [Math2](./9.math2)
- [Recursion](./10.recursion)
- [Brute Force](./11.brute)
- [Sort](./12.sort)

##

### Takeaways
- **Standard input / output**
  ```
  int_a, int_b = map(int, input().split())
  data = input().split()
  ```
  or (faster)
  ```
  import sys

  int_a, int_b = map(int, sys.stdin.readline().split())
  data = list(map(int, sys.stdin.readline().split()))
  ```

- **Take random number of inputs**
  ```
  while True:
      try:
          a, b = map(int, input().split())
          print(a+b)
      except:
          break
  ```

- **Print with specific decimal point**
  ```
  print('{:.3f}%'.format(count/student_num*100))
  ```

- **Get Alphabet**
  ```
  import string

  a = string.ascii_lowercase
  ```
- **Reverse string**
  ```
  s = s[::-1]
  ```

- **Check if prime number**
  ```
  def is_prime(num):
      if num <= 1:
          return False
      else:
          for i in range(2, int(num**0.5)+1):
              if num%i==0:
                  return False
          return True
  ```
- **Get all prime numbers below N**
  ```
  def prime_list(n):
      sieve = [True]*n
      m = int(n**0.5)
      for i in range(2, m+1):
          if sieve[i] == True:  # i가 소수인 경우
              for j in range(i+i, n, i):  # i 이후 i의 배수는 False로 판
                  sieve[j] = False
      return [i for i in range(2, n) if sieve[i] == True]
  ```

- <code>**collections.Counter**</code>
  - Sort elements by count
  - returns list of tuples
  ```
  from collections import counter
  
  k = Counter(data).most_common()
  ```

- **Sort by key**
  ```
  data.sort(key=lambda item: item[0])
  ```
- <code>**dict.get(key, default = None)**</code>

  **key** = key to be searched in the dictionary\
  **default** = value to be returned in case key does not exist
  
  ```
  >>> dict = {}
  >>> dict['key1'] = 1
  >>> dict.get(key1, 0)
  1
  >>> dict.get(key2, 0)
  0
  ```
  
- <code>**hash(object)**</code>

  Return the hash value of the object.\
  Hash values are integers.
 
  ```
  >>> hash('example string')
  7369253315943211870
  ```
  
- <code>**max(iterable, *[, key, default])**</code>\
  <code>**max(arg1, arg2, *args[, key])**</code>
  
  Return the largest item in an iterable or the largest of two or more arguments.
  
  ```
  >>> nums = [3, 4, 5, 6]
  >>> max(nums)
  6
  ```

- **Time complexity of list slicing is O(n)**

  **ex)** `for item in list_[int:]` - **not recommended**