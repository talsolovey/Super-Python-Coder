def merge_sorted_lists(list1, list2):
    """Merges two sorted lists into one sorted list."""
    len1, len2 = len(list1), len(list2)
    merged_list = []
    i, j = 0, 0

    while i < len1 and j < len2:
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list

def test_merge_sorted_lists():
    """Tests the merge_sorted_lists function."""
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert not merge_sorted_lists([], [1, 2, 3])
    assert merge_sorted_lists([1, 2, 3], []) == [1, 2, 3]
    assert not merge_sorted_lists([], [])
    assert merge_sorted_lists([1, 2, 3], [0]) == [0, 1, 2, 3]
    assert merge_sorted_lists([10, 20, 30], [5, 15, 25]) == [5, 10, 15, 20, 25, 30]
    assert merge_sorted_lists([1, 1, 1], [1, 1]) == [1, 1, 1, 1, 1]
    assert merge_sorted_lists([-1, 0, 1], [-2, 2]) == [-2, -1, 0, 1, 2]
    assert merge_sorted_lists([5], [1, 2, 3, 4]) == [1, 2, 3, 4, 5]
    assert merge_sorted_lists([100], [50, 75, 200]) == [50, 75, 100, 200]

test_merge_sorted_lists()