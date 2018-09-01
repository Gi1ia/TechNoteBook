class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # tasks_dict = collections.defaultdict(int)
        # for t in tasks:
        #     tasks_dict[t] += 1
        # tasks_dict.sort(key = lambda x: x[1])

        tasks_frequency = Counter(tasks)
        
                