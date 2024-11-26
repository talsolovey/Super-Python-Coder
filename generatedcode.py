def find_median_sorted_arrays(nums1, nums2):

    nums = sorted(nums1 + nums2)
    n = len(nums)

    if n % 2 == 1:
        return float(nums[n // 2])
    else:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2.0


def test_find_median_sorted_arrays():

    assert find_median_sorted_arrays([1, 3], [2]) == 2.0

    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5

    assert find_median_sorted_arrays([], [1]) == 1.0

    assert find_median_sorted_arrays([2], []) == 2.0

    assert find_median_sorted_arrays([], []) is None

    assert find_median_sorted_arrays([1, 2], [1, 2]) == 1.5

    assert find_median_sorted_arrays([0, 0], [0, 0]) == 0.0

    assert find_median_sorted_arrays([1], [2]) == 1.5

    assert find_median_sorted_arrays([-1, 3], [-2, 4]) == 1.0

    assert find_median_sorted_arrays([1, 2, 3], [4, 5]) == 3.0


if __name__ == "__main__":
    test_find_median_sorted_arrays() 

