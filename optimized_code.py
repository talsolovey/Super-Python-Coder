def merge_sorted_lists(list1, list2):
    merged_list = []
    i = j = 0

    while i < len(list1) and j < len(list2):
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
    
    assert merge_sorted_lists([], []) == []

    assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]

    assert merge_sorted_lists([1, 2, 3], []) == [1, 2, 3]

    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

    assert merge_sorted_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]

    assert merge_sorted_lists([1, 2, 3], [1, 2, 3]) == [
        1, 1, 2, 2, 3, 3]

    assert merge_sorted_lists([1, 2, 2], [2, 2, 3]) == [1, 2, 2, 2, 2, 3]

    assert merge_sorted_lists([100, 200], [10, 20, 30]) == [
        10, 20, 30, 100, 200]

    assert merge_sorted_lists([-5, -3, 0], [-4, -2, 1]) == [
        -5, -4, -3, -2, 0, 1]

    assert merge_sorted_lists([5, 10, 15], [1, 2, 3]) == [
        1, 2, 3, 5, 10, 15]


test_merge_sorted_lists()