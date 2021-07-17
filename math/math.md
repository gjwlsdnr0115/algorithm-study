# Math

### Problems
- [10430 - Remainder](https://www.acmicpc.net/problem/10430)
- [2609 - GCD LCM](https://www.acmicpc.net/problem/2609)
- [1934 - LCM](https://www.acmicpc.net/problem/1934)
- [1978 - Find Prime](https://www.acmicpc.net/problem/1978)
- [1929 - Prime Number](https://www.acmicpc.net/problem/1929)
- [6588 - Goldbach](https://www.acmicpc.net/problem/6588)


##

### Solutions
- [10430](./10430_modulo.py)
- [2609](./2609_GCD_LCM.py)
- [1934](./1934_LCM.py)
- [1978](./1929_find_prime.py)
- [1929](./1978_prime_number.py)
- [6588](./6588_goldbach.py)



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
    ```