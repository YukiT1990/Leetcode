# 1185. Day of the Week

# Reference
# https://scrapbox.io/imasaraC/%E6%9B%9C%E6%97%A5%E3%82%92%E6%B1%82%E3%82%81%E3%82%8B

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        if month < 3:
            month += 12
            year -= 1
            
        w = (year + year // 4 - year // 100 + year // 400 + (13 * month + 8) // 5 + day) % 7
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        
        return days[w]