# Math

### Problems
- [10430 - Remainder](https://www.acmicpc.net/problem/10430)
- [2609 - GCD LCM](https://www.acmicpc.net/problem/2609)
- [1934 - LCM](https://www.acmicpc.net/problem/1934)
- [1978 - Find Prime](https://www.acmicpc.net/problem/1978)
- [1929 - Prime Number](https://www.acmicpc.net/problem/1929)
- [6588 - Goldbach](https://www.acmicpc.net/problem/6588)
- [10872 - Factorial](https://www.acmicpc.net/problem/10872)
- [1676 - Factorial Zero](https://www.acmicpc.net/problem/1676)
- [2004 - Combination Zero](https://www.acmicpc.net/problem/2004)
- [9613 - GCD Sum](https://www.acmicpc.net/problem/9613)
- [17087 - Hide and Seek6](https://www.acmicpc.net/problem/17087)
- [1373 - 2 to 8 decimals](https://www.acmicpc.net/problem/1373)
- [1212 - 8 to 2 decimals](https://www.acmicpc.net/problem/1212)
- [2089 - -2 decimals](https://www.acmicpc.net/problem/2089)
- [17103 - Goldbach Partition](https://www.acmicpc.net/problem/17103)
- [11005 - decimals2](https://www.acmicpc.net/problem/11005)
- [2745 - decimals](https://www.acmicpc.net/problem/2745)
- [11576 - Base Conversion](https://www.acmicpc.net/problem/11576)
- [11653 - Factorization](https://www.acmicpc.net/problem/11653)



##

### Solutions
- [10430](./10430_modulo.py)
- [2609](./2609_GCD_LCM.py)
- [1934](./1934_LCM.py)
- [1978](./1978_prime_number.py)
- [1929](./1929_find_prime.py)
- [6588](./6588_goldbach.py)
- [10872](./10872_factorial.py)
- [1676](./1676_factorial_zero.py)
- [2004](./2004_combinations_zero.py)
- [9613](./9613_GCD_sum.py)
- [17087](./17087_hideandseek6.py)
- [1373](./1373_2_8_decimals.py)
- [1212](./1212_8_2_decimals.py)
- [2089](./2089_neg_binary.py)
- [17103](./17103_goldbach_partition.py)
- [11005](./11005_decimals2.py)
- [2745](./2745_decimals.py)
- [11576](./11576_base_conversion.py)
- [11653](./11653_factorization.py)



##

### Takeaways

- **GCD & LCM Implementation**
  ```
  def GCD(a, b):
      while b:
          a, b = b, a%b
      return a

  def LCM(a, b):
      return abs(a*b) // GCD(a, b) 
  ```
- **Eratosthenes**
    - get all prime numbers in specific region
    ```
    def get_eratos(N):
        nums = [True for _ in range(N)]
        for i in range(2, int(N**0.5)+1):
            if nums[i] == True:
                for j in range(i*2, N, i):
                    if nums[j] == True:
                        nums[j] = False
        return nums
        
    ```
- **Count number of multiplied Ns**
    ```
    def get_N_count(N, a):
        count = 0
        while a >= N:
            count += a//N
            a //= N
        return count
    ```x
    - ex)
    ```
    def two_count(n):  # count number of multiplied 2s in n
    count = 0
    while n >= 2:
        count += n//2
        n //= 2
    return count
    ```

- **Reduce Operation**
    ```
    from functools import reduce

    >>> reduce(math.gcd, A_distance)
    # Returns gcd of all elements in A_distance
    ```
- **Get int with specific decimal**
    ```
    s = '10'
    binary = int(s, 2)
    ```
- **Convert to oct,hex, binary**
    ```
    oct(num)
    hex(num)
    bin(num)
    ```