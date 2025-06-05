from collections import Counter
def find_frequent_string_lengths(strings: list[str]) -> list[str]:
    if not strings:
        return []
    #lấy độ dài của các chuỗi và đếm tần suất của chúng
    length_counts = Counter(len(s) for s in strings)
    #tìm độ dài xuất hiện nhiều nhất
    max_freq = max(length_counts.values())
    #lấy giá trị độ dài xuất hiện nhiều nhất
    frequent_lengths = [length for length, freq in length_counts.items() if freq == max_freq]
    #từ danh sách chuỗi ban đầu, lọc ra các chuỗi có độ dài nằm trong frequent_lengths
    result = [s for s in strings if len(s) in frequent_lengths]
    result.sort(key=len)
    return result

aa = ['a', 'ab', 'abc', 'cd', 'def', 'gh']

def test_find_frequent_string_lengths():
    # Test case 1
    x = ['a', 'ab', 'abc', 'cd', 'def', 'gh', 'q', 'def', 'werv', 'cd', 'def']
    expected = ['ab', 'cd', 'gh', 'cd', 'abc', 'def', 'def', 'def']
    assert find_frequent_string_lengths(x) == expected, "Test case 1 failed"

    # Test case 2: 
    y = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff']
    expected = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff']
    assert find_frequent_string_lengths(y) == expected, "Test case 2 failed"

    # Test case 3:
    z = []
    expected = []
    assert find_frequent_string_lengths(z) == expected, "Test case 3 failed"

    print("All test cases passed.")

if __name__ == "__main__":
    find_frequent_string_lengths(aa)
    test_find_frequent_string_lengths()