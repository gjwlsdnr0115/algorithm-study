# Dynamic Programming

### Problems
- [1463 - Make 1](https://www.acmicpc.net/problem/1463)
- [11726 - 2 Tiles](https://www.acmicpc.net/problem/11726)
- [11727 - 2 Tiles2](https://www.acmicpc.net/problem/1727)
- [9095 - 123 Add](https://www.acmicpc.net/problem/9095)
- [11052 - Cards](https://www.acmicpc.net/problem/11052)
- [16194 - Cards2](https://www.acmicpc.net/problem/16194)
- [15990 - 123 Add5](https://www.acmicpc.net/problem/15990)
- [10844 - Stairs](https://www.acmicpc.net/problem/10844)
- [2193 - Pinary Number](https://www.acmicpc.net/problem/2193)
- [11053 - LIS](https://www.acmicpc.net/problem/11053)
- [14002 - LIS4](https://www.acmicpc.net/problem/14002)
- [1912 - Sequence Sum](https://www.acmicpc.net/problem/1912)
- [1699 - Square Sum](https://www.acmicpc.net/problem/1699)
- [2225 - Sum Partition](https://www.acmicpc.net/problem/2225)
- [15988 - 123 Add](https://www.acmicpc.net/problem/15988)
- [1149 - RGB](https://www.acmicpc.net/problem/1149)
- [1309 - Zoo](https://www.acmicpc.net/problem/1309)
- [11057 - Ascending](https://www.acmicpc.net/problem/11507)
- [9455 - Sticker](https://www.acmicpc.net/problem/9455)
- [2156 - Wine](https://www.acmicpc.net/problem/2156)
- [1932 - Triangle](https://www.acmicpc.net/problem/1932)
- [11055 - BIS](https://www.acmicpc.net/problem/11055)
- [11722 - LDS](https://www.acmicpc.net/problem/11722)
- [11054 - LBS](https://www.acmicpc.net/problem/11054)
- [13398 - Sequence Sum2](https://www.acmicpc.net/problem/13398)
- [2133 - Tiles](https://www.acmicpc.net/problem/2133)
- [1309 - Zoo](https://www.acmicpc.net/problem/1309)
- [17404 - RGB2](https://www.acmicpc.net/problem/17404)
- [2225 - Sum Partition](https://www.acmicpc.net/problem/2225)


##

### Solutions
- [1463](./1463_make_one.py)
- [11726](./11726_2tiles.py)
- [11727](./11727_2tiles2.py)
- [9095](./9095_123_add.py)
- [11052](./11052_cards.py)
- [16194](./16194_cards2.py)
- [15990](./15990_123_add5.py)
- [10844](./10844_stairs.py)
- [2193](./2193_pinary_number.py)
- [11053](./11053_LIS.py)
- [14002](./14002_LIS4.py)
- [1912](./1912_seq_sum.py)
- [1699](./1699_sqr_sum.py)
- [2225](./2225_sum_partition.py)
- [15988](./15988_123_add3.py)
- [1149](./1149_RGB.py)
- [1309](./1309_zoo.py)
- [11057](./11057_ascending.py)
- [9455](./9455_sticker.py)
- [2156](./2156_wine.py)
- [1932](./1932_triangle.py)
- [11055](./11055_BIS.py)
- [11722](./11722_LDS.py)
- [11054](./11054_LBS.py)
- [13398](./13398_seq_sum2.py)
- [2133](./2133_tiles.py)
- [1309](./1309_zoo.py)
- [17404](./17404_RGB2.py)
- [2225](./2225_sum_partition.py)



##

### Takeaways

- **Dynamic Programming**
    - Divide problem into smaller problems
    - Only process a problem once
    - Store problem results in memory for reusage
    - Under the premise that the result of the same problem is always identical 

- **LIS Algorithm**
    ```
    import sys
    input = sys.stdin.readline

    length = int(input())
    seq = list(map(int, input().split()))

    dp = [1]*(length)   

    for i in range(length):
        for j in range(i):
            if seq[j] < seq[i]:
                dp[i] = max(dp[i], dp[j]+1)

    print(max(dp)) 
    ```