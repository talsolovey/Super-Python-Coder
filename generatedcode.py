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


def test_merge_sorted_lists():

    assert merge_sorted_lists([], []) == []

    assert merge_sorted_lists([], [1]) == [1]

    assert merge_sorted_lists([1], []) == [1]

    assert merge_sorted_lists([1], [2]) == [1, 2]

    assert merge_sorted_lists([2], [1]) == [1, 2]

    assert merge_sorted_lists([1, 3], [2, 4]) == [1, 2, 3, 4]

    assert merge_sorted_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]

    assert merge_sorted_lists([4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6]

    assert merge_sorted_lists([1, 2, 2], [2, 3, 3]) == [1, 2, 2, 2, 3, 3]

    assert merge_sorted_lists([-3, 0, 1], [-2, 2, 4]) == [-3, -2, 0, 1, 2, 4]


test_merge_sorted_lists()