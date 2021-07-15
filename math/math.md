# Math

### Problems
- [10430 - Remainder](https://www.acmicpc.net/problem/10430)
- [2609 - GCD LCM](https://www.acmicpc.net/problem/2609)
- [1934 - LCM](https://www.acmicpc.net/problem/1934)


##

### Solutions
- [10430](./10430_modulo.py)
- [2609](./2609_GCD_LCM.py)
- [1934](./1934_LCM.py)



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
