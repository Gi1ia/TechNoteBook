import collections
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = collections.Counter(words)   
        
        freqs = []
        heapq.heapify(freqs)
        for word, count in counts.items():
            heapq.heappush(freqs, (-count, word))

        '''
        # Following code doesn't work because if first letter is the same, min heap will give a wrong alphabetical order
        for word, count in counts.items():
            heapq.heappush(freqs, (count, word))
            if len(freqs) > k:
                heapq.heappop(freqs)
        '''
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(freqs)[1])
            
        return res
    
    def topKFrequent_pythonic(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]