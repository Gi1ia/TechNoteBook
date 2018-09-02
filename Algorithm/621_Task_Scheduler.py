import collections
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        tasks_frequency = collections.Counter(tasks)
        print tasks_frequency
        max_val = tasks_frequency.most_common(1)[0][1]

        # (max_val - 1) * n + (max_val - 1)
        # idle_slots + put the first task into form already
        idle = (max_val - 1) * (n + 1)

        for task in tasks_frequency:
            # If more than one tasks have maximum number, 
            # we only fill (max_val - 1) into the idle slot,
            # the last one should be add to the end
            #  (which is not considered as idle slot)
            v = tasks_frequency[task]
            idle -= min(v, max_val - 1)
        
        if idle > 0:
            return idle + len(tasks)
        
        return len(tasks)
    
tasks = ["A","A","A","B","B","B"]
s = Solution()
print(s.leastInterval(tasks, 2))