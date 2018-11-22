from collections import deque, defaultdict
from heapq import heappush, heappop, heapify

def page_display_deque(input_data, k):
    ids = [line.split(",")[0] for line in input_data]

    hosts = defaultdict(deque)

    for i, host_id in enumerate(ids):
        hosts[host_id].append(input_data[i])
    # print("hosts:", hosts)

    aggregate = []
    total, i = 0, 0
    while total < len(input_data):
        for host_id, rooms in hosts.items():
            if not rooms:
                continue
            next_room = rooms.popleft()
            aggregate.append(next_room)               
            total += 1

    # Print
    for room in aggregate:    
        print(room)
        if i == k - 1:
            print("-------------")
        i += 1
        i %= k    

def pagedisplay(input_data, k):
    """
    :input type: List[string]; input_csv_array
    This one is faster then the deque one
    """
    ids = [line.split(',')[0] for line in input_data]
    print("ids:", ids)
    seen_ids = {}
    page_index = 0
    pages = []

    for i, id in enumerate(ids):
        if id not in seen_ids or seen_ids[id] < page_index:
            seen_ids[id] = page_index
        
        print("i: ", i, "id: ", id, "page_idx: ", page_index)
        
        if len(pages) == seen_ids[id]:
            pages.append([])
        pages[seen_ids[id]].append(input_data[i])
        if len(pages[page_index]) == k:
            page_index += 1
            print("page_index: ", page_index)
        seen_ids[id] += 1

    i = 0
    for page in pages:
        for item in page:
            print(item)            
            if i == 2:
                print("---------")
            i += 1
            i %= 3

    
test1 = ["1, 113", "1, q25", "2, abc", "2, def", "2, ghi", "1, edf", "3, 253"]
# pagedisplay(test1, 3)
page_display_deque(test1, 3)

