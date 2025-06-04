from collections import Counter
def find_frequent_string_lengths(strings: list[str]) -> list[str]:
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

x = ['a', 'ab', 'abc', 'cd', 'def', 'gh', 'q', 'def', 'werv', 'cd', 'def']
print(find_frequent_string_lengths(x))