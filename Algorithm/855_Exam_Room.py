import heapq

class ExamRoom(object):
    def __init__(self, N):
        self.N = N
        self.students = []
        self.heap = []
        self.avail_first = {} # used later in leave()
        self.avail_last = {} # used later in leave()
        self.put_seg(0, self.N - 1) # Initialize with empty room
    
    def seat(self):
        while True:
            _, first, last, is_avail = heapq.heappop(self.heap)
            if is_avail: # delete
                del self.avail_last[last]
                del self.avail_first[first]
                break
            
        if first == 0:
            res = 0
            if first != last:
                self.put_seg(first + 1, last)
        
        elif last == self.N - 1:
            res = last
            if first != last:
                self.put_seg(first, last - 1)
        
        else:
            res = (last - first) // 2 + first 
            if res > first: 
                self.put_seg(first, res - 1)
            if res < last: # break the segment and put both into heap
                self.put_seg(res + 1, last)
        
        return res
    
    def leave(self, p):
        left = p - 1 # looking for left and right segment
        right = p + 1

        first, last = p, p # Default value, incase p == 0 or p == N - 1

        if left >= 0 and left in self.avail_last:
            seg_left = self.avail_last.pop(left)
            first = seg_left[1]
            seg_left[3] = False
        
        if (right <= self.N - 1) and right in self.avail_first:
            seg_right = self.avail_first.pop(right)
            last = seg_right[2]
            seg_right[3] = False
        
        self.put_seg(first, last)

    def put_seg(self, first, last):
        if first == 0 or last == self.N - 1:
            l = last - first
        else:
            l = (last - first) // 2
        
        segment = [-l, first, last, True]
        self.avail_last[last] = segment # pass by ref?
        self.avail_first[first] = segment

        heapq.heappush(self.heap, segment)

    def seat_ON(self):
        """ Seat function
        O(N) time
        """
        if not students: # no one in the room
            student = 0
        else:
            # Try to seat from position 0 
            # dist = students[0] - 0 = students[0]
            dist, student = self.students[0], 0
            for i, position in enumerate(self.students):
                if i > 0:
                    prev_position = self.students[i - 1]
                    current_dist = (self.students[i] - prev_position) // 2
                    if current_dist > dist:
                        dist, student = current_dist, prev_position + current_dist
            
            last = self.N - 1 - self.students[-1]
            if last > dist:
                student = self.N - 1

        biscuit.insort(self.students, student)
        return student         

    def leave_ON(self, p):
        """ Leave function for `self.seat_ON()`
        """
        self.students.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)

# ref: [heap solution](https://leetcode.com/problems/exam-room/discuss/139941/Python-O(log-n)-time-for-both-seat()-and-leave()-with-heapq-and-dicts-Detailed-explanation)
