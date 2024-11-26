def find_median_sorted_arrays(nums1, nums2):

    total_length = len(nums1) + len(nums2)

    half = total_length // 2

    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    len1, len2 = len(nums1), len(nums2)
    imin, imax = 0, len1
    half_length = (len1 + len2 + 1) // 2

    while imin <= imax:
        mid1 = (imin + imax) // 2
        mid2 = half_length - mid1

        if mid1 < len1 and nums2[mid2 - 1] > nums1[mid1]:
            imin = mid1 + 1
        elif mid1 > 0 and nums1[mid1 - 1] > nums2[mid2]:
            imax = mid1 - 1
        else:
            if mid1 == 0:
                max_of_left = nums2[mid2 - 1]
            elif mid2 == 0:
                max_of_left = nums1[mid1 - 1]
            else:
                max_of_left = max(nums1[mid1 - 1], nums2[mid2 - 1])

            if total_length % 2 == 0:
                if mid1 == len1:
                    min_of_right = nums2[mid2]
                elif mid2 == len2:
                    min_of_right = nums1[mid1]
                else:
                    min_of_right = min(nums1[mid1], nums2[mid2])

                return (max_of_left + min_of_right) / 2.0

            return max_of_left



def test_find_median_sorted_arrays():

    assert find_median_sorted_arrays([1, 3], [2]) == 2.0
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5
    assert find_median_sorted_arrays([], [1]) == 1.0
    assert find_median_sorted_arrays([2], []) == 2.0
    assert find_median_sorted_arrays([1, 2], [1, 2]) == 1.5
    assert find_median_sorted_arrays([1, 3], [4, 5, 6]) == 3.0
    assert find_median_sorted_arrays([1, 2, 3], [4, 5, 6]) == 3.5
    assert find_median_sorted_arrays([5], [1, 3, 4, 2]) == 3.0
    assert find_median_sorted_arrays([1, 2, 3, 4], [5, 6, 7, 8]) == 4.5
    assert find_median_sorted_arrays([10, 20, 30], [5, 15, 25]) == 15.0

test_find_median_sorted_arrays()