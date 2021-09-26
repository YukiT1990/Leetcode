# 1118. Number of Days in a Month

class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                return days[1] + 1
            else:
                return days[1]
        else:
            return days[month-1]