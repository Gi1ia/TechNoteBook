def pagedisplay(input_data, k):
    """
    :input type: List[string]; input_csv_array
    """
    ids = [line.split(',')[0] for line in input_data]
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

    print(pages)
    
test1 = ["1, 113", "1, q25", "2, abc", "2, def", "2, ghi", "1, edf", "3, 253"]
pagedisplay(test1, 3)

    
