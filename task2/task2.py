import random
def sum_two_largest_numbers(arr: list[int]) -> tuple[int, int]:
    #nếu mảng có ít hơn 2 phân tử, báo lỗi ít nhất có 2 phần tử
    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements.")
    #khởi tạo hai biến để lưu hai số lớn nhất
    first, second = float('-inf'), float('-inf')
    #duyệt qua từng số trong mảng, nếu số đang duyệt lớn hơn first thì first sẽ là số đó và second sẽ là first cũ
    for number in arr:
        if number >= first:
            second = first
            first = number
        #nếu số đang duyệt lớn hơn second và khác với first thì second sẽ là số đó
        elif number > second and number != first:
            second = number
            print(f"Current number: {number}, First: {first}, Second: {second}")
    return f"The sum of the two largest integers in the array: {first} + {second} = {first + second}"

array_2000 = [random.randint(1, 1000000) for _ in range(2000)]

def test_sum_two_largest_numbers():
    # Test case 1
    x = [1, 2, 3, 4, 5]
    expected = "The sum of the two largest integers in the array: 5 + 4 = 9"
    assert sum_two_largest_numbers(x) == expected, "Test case 1 failed"

    # Test case 2
    y = [10, 20]
    expected = "The sum of the two largest integers in the array: 10 + 20 = 30"
    assert sum_two_largest_numbers(y) == expected, "Test case 2 failed"

    # Test case 3
    z = [100]
    try:
        sum_two_largest_numbers(z)
    except ValueError as e:
        assert str(e) == "Array must contain at least two elements.", "Test case 3 failed"

    print("All test cases passed.")

if __name__ == "__main__":
    print(sum_two_largest_numbers(array_2000))
    test_sum_two_largest_numbers()