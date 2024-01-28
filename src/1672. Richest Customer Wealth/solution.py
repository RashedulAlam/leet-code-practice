class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max = None
        for account in accounts:
            total = sum(account)
            if max is None:
                max = total
            if total > max:
                max = total
        return max