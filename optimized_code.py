def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
    len1, len2 = len(list1), len(list2)

    while i < len1 and j < len2:
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
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

    assert merge_sorted_lists([], [2, 4, 6]) == [2, 4, 6]

    assert merge_sorted_lists([1, 3, 5], []) == [1, 3, 5]

    assert merge_sorted_lists([], []) == []

    assert merge_sorted_lists([1, 1, 1], [1, 1, 1]) == [1, 1, 1, 1, 1, 1]

    assert merge_sorted_lists([1, 2, 3], [1, 2, 3]) == [1, 1, 2, 2, 3, 3]

    assert merge_sorted_lists([1, 4, 5], [2, 3, 6]) == [1, 2, 3, 4, 5, 6]

    assert merge_sorted_lists([5, 6, 7], [1, 2, 3, 4]) == [1, 2, 3, 4, 5, 6, 7]

    assert merge_sorted_lists([-5, 3, 4.5], [-4, 0, 1.5]) == [-5, -4, 0, 1.5, 3, 4.5]

    assert merge_sorted_lists([-1, 0, 1], [-2, -1, 1]) == [-2, -1, -1, 0, 1, 1]

  
test_merge_sorted_lists()