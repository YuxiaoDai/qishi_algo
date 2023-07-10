# 1、我们先找到a,b,c里最小的那个数，比如是a，那么第n个丑数肯定是小于等于n * a的对不对？
#    因为 0 到 n*a范围内是有可能出现数字，可以被b或c整除的
# 2、然后就开始二分法的做法了，将n * a置为上限ceil，0置为下限0。
# 3、我们求解mid = (ceil+floor)/2这个数里包含了多少丑数，具体解法下面另外说。
# 4、如果上一步的数字等于n,那最好啦，判断当前的mid是否是丑数，如果是，直接返回mid，如果不是，将ceil置为mid - 1；
#    如果上一步的数字大于n,将ceil置为mid - 1；
#    如果上一步的数字小于n,将floor置为mid + 1；
#    为啥数字等于n，不能直接返回当前mid值呢？
#    比如：在a = 2, b = 21, c = 31的情况下，14和15这两个范围里都包含了7个丑数，如下所示
#    2 4 6 8 10 12 14. 但是很明显，14才是第7个丑数。

# 本题的关键是对于选中的值x，得出x是丑数序列中的第几个丑数。
# 我们这里需要用到容斥原理。
# long count = x/a + x/b + x/c - x/lcm_ab - x / lcm_ac - x / lcm_bc + x / lcm_abc;
# 这里的lcm的含义为最小公倍数。
# 这里解释一下为何后面要加上x / lcm_abc？
# 因为 前面x/a + x/b + x/c - x/lcm_ab - x / lcm_ac - x / lcm_bc，将x/lcm_abc这部分加了3次又减了3次，相当于x / lcm_abc没有了，所以要加上这部分。

from math import lcm

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def count_ungly_number(x,a,b,c):
            lab, lbc, lac, labc = lcm(a, b), lcm(b, c), lcm(a, c), lcm(a, b, c)
            return  x // a + x // b + x // c - x // lab - x // lbc - x // lac + x // labc

        l, r = 1 , min(min(a, b, c) * n, 2 * pow(10, 9)) 
        while l <= r:
            mid = (r - l)//2 + l
            count = count_ungly_number(mid, a,b,c)
            if count == n:
                if mid%a ==0 and mid%b==0 and mid%c == 0:
                    return mid
                else:
                    r = mid -1
            elif count < n:
                l = mid + 1
            else:
                r = mid - 1
        return l
    
S = Solution()
n = 14
a = 3
b = 7
c = 13
result = S.nthUglyNumber(n,a,b,c)
print(result)