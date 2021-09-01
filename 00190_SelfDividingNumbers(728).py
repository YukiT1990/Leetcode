# 728. Self Dividing Numbers

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1):
            str_num = str(num)
            for d in range(len(str_num)):
                if int(str_num[d]) == 0:
                    break
                if num % int(str_num[d]) != 0:
                    break
                else:
                    if d == len(str_num) - 1:
                        result.append(num)
        return result