# 201. Bitwise AND of Numbers Range

# Reference
# https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/594259/100-memory-Python-3-One-line-(Short-with-Math)

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        return 0 if  right >= left*2 else functools.reduce(lambda x, y: x & y, range(left, right+1))

"""
functools.reduce(function, iterable[, initializer])¶
iterable の要素に対して、iterable を単一の値に短縮するような形で 2 つの引数をもつ function を左から右に累積的に適用します。
例えば、 reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) は ((((1+2)+3)+4)+5) を計算します。
左引数 x は累計の値になり、右引数 y は iterable から取り出した更新値になります。
オプションの initializer が存在する場合、計算の際に iterable の先頭に置かれます。
また、 iterable が空の場合には標準の値になります。 initializer が与えられておらず、 
iterable が単一の要素しか持っていない場合、最初の要素が返されます。
https://docs.python.org/ja/3/library/functools.html
"""