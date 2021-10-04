# 1360. Number of Days Between Two Dates

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        year1 = int(date1[:4])
        month1 = int(date1[5:7])
        day1 = int(date1[8:])
        year2 = int(date2[:4])
        month2 = int(date2[5:7])
        day2 = int(date2[8:])
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        leap_years = [1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096]
        days1 = day1
        days2 = day2
        for i in range(month1-1):
            days1 += days[i]
            if i == 1 and year1 in leap_years:
                days1 += 1
        for i in range(month2-1):
            days2 += days[i]
            if i == 1 and year2 in leap_years:
                days2 += 1
        for i in range(1971, year1):
            if i in leap_years:
                days1 += 366
            else:
                days1 += 365
        for i in range(1971, year2):
            if i in leap_years:
                days2 += 366
            else:
                days2 += 365
        return abs(days1 - days2)