# 359. Logger Rate Limiter

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.last_time = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.last_time.keys():
            self.last_time[message] = timestamp
            return True
        else:
            if timestamp - self.last_time[message] >= 10:
                self.last_time[message] = timestamp
                return True
            else:
                return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)