# 929. Unique Email Addresses

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        sent_address = set()
        for i in range(len(emails)):
            index = emails[i].index('@')
            local = emails[i][:index]
            domain = emails[i][index+1:]
            if '+' in local:
                index1 = local.index('+')
                local = local[:index1]
            if '.' in local:
                local = local.replace('.', '')
            sent_address.add(local + '@' + domain)
           
        return len(sent_address)