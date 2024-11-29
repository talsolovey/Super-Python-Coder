def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list

# Unit tests
def test_merge_sorted_lists():
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted_lists([1, 2, 3], []) == [1, 2, 3]
    assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]
    assert merge_sorted_lists([], []) == []
    assert merge_sorted_lists([1, 2, 3], [1, 2, 3]) == [1, 1, 2, 2, 3, 3]
    assert merge_sorted_lists([5, 10, 15], [1, 2, 3]) == [1, 2, 3, 5, 10, 15]
    assert merge_sorted_lists([0, 4, 8], [2, 6, 10]) == [0, 2, 4, 6, 8, 10]
    assert merge_sorted_lists([-3, -1], [0, 2, 4]) == [-3, -1, 0, 2, 4]
    assert merge_sorted_lists([1], [2]) == [1, 2]
    assert merge_sorted_lists([1, 2, 3], [0, 5]) == [0, 1, 2, 3, 5]

test_merge_sorted_lists()