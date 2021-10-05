# 1507. Reformat Date

class Solution:
    def reformatDate(self, date: str) -> str:
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        index = date.index(' ')
        day = date[:index]
        if len(day) == 3:
            DD = '0' + day[0]
        else:
            DD = day[:2]
        MM = str(month.index(date[-8:-5])+1)
        if len(MM) == 1:
            MM = '0' + MM
        return date[-4:] + '-' + MM + '-' + DD

# one line
# Reference
# https://leetcode.com/problems/reformat-date/discuss/932108/One-Liner-Python-re-sub
# from datetime import datetime as D
# def reformatDate(self, date: str) -> str:
#        return D.strptime(re.sub('rd|nd|th|st|','',date),'%d %b %Y').strftime('%Y-%m-%d')