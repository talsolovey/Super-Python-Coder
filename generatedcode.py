def merge_sorted_lists(list1, list2):
    merged = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

def test_merge_sorted_lists():
    assert merge_sorted_lists([], []) == []
    assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]
    assert merge_sorted_lists([1, 2, 3], []) == [1, 2, 3]
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted_lists([1, 1, 1], [1, 1, 1]) == [1, 1, 1, 1, 1, 1]
    assert merge_sorted_lists([5, 10], [1, 2, 3]) == [1, 2, 3, 5, 10]
    assert merge_sorted_lists([-3, -1, 0], [2, 4, 5]) == [-3, -1, 0, 2, 4, 5]
    assert merge_sorted_lists([1, 2, 3], [0]) == [0, 1, 2, 3]
    assert merge_sorted_lists([1], [1]) == [1, 1]
    assert merge_sorted_lists([10, 20, 30], [5, 15, 25]) == [5, 10, 15, 20, 25, 30]

test_merge_sorted_lists()