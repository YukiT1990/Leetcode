# 1056. Confusing Number

class Solution:
    def confusingNumber(self, n: int) -> bool:
        invalid_num = ['2', '3', '4', '5', '7']
        n = str(n)
        for d in n:
            if d in invalid_num:
                return False
            
        confusing_num_dict = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        rotated_n = []
        for d in n:
            rotated_n.append(confusing_num_dict[d])
        rotated_n.reverse()
        rotated_n = ''.join(rotated_n)
        
        if rotated_n != n:
            return True
        else:
            return False
        