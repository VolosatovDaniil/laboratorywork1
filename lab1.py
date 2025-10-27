from math import sqrt, floor, ceil

# Вибіркове середнє
def mean(data):
    return sum(data) / len(data)

# Вибіркова дисперсія
def sample_variance(data):
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / (len(data) - 1)

# Стандартне відхилення
def std_deviation(data):
    return sqrt(sample_variance(data))

# Медіана
def median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    middle = n // 2
    if n % 2 == 1:
        return sorted_data[middle]
    else:
        med = (sorted_data[middle - 1] + sorted_data[middle]) / 2
        return int(med) if med.is_integer() else med

# Мода
def mode(data):
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    max_count = max(freq.values())
    modes = [x for x, count in freq.items() if count == max_count]
    return modes[0] if len(modes) == 1 else modes

# Мінімум
def min_value(data):
    min = data[0]
    for x in data[1:]:
        if x < min:
            min = x
    return min

# Максимум
def max_value(data):
    max = data[0]
    for x in data[1:]:
        if x > max:
            max = x
    return max

# Розмах
def data_range(data):
    return max_value(data) - min_value(data)

# Квантиль
def quantile(data, p):
    sorted_data = sorted(data)
    n = len(sorted_data)
    index = p * (n - 1)
    low = floor(index)
    high = ceil(index)
    if low == high:
        value = sorted_data[int(index)]
    else:
        value = sorted_data[low] + (sorted_data[high] - sorted_data[low]) * (index - low)
    return int(value) if value.is_integer() else round(value, 3)

data = [
    62, 81, 44, 46, 84, 96, 47, 41, 50, 72, 70, 25, 88, 84, 33, 22, 5, 53, 35, 87, 32, 99, 18, 87, 18, 99, 43, 79, 43, 42, 2, 4, 56, 15, 91, 50, 71, 17, 14, 64, 46, 39, 7, 20, 21, 22, 6, 56, 65, 77, 93, 94, 39, 27, 79, 85, 34, 57, 65, 89, 98, 88, 86, 56, 12, 59, 3, 29, 68, 7, 95, 1, 48, 76, 5, 10, 83, 30, 61, 9, 75, 40, 19, 52, 28, 92, 67, 31, 8, 45, 90, 73, 58, 69, 24, 13, 38, 90, 23, 55
]

print("Вхідні дані:", data)
print("Кількість спостережень:", len(data), "\n")

print("Вибіркове середнє:", round(mean(data), 3))
print("Вибіркова дисперсія:", round(sample_variance(data), 3))
print("Стандартне відхилення:", round(std_deviation(data), 3))
print("Медіана:", median(data))
print("Мода:", mode(data))
print("Мінімум:", min_value(data))
print("Максимум:", max_value(data))
print("Розмах:", data_range(data))
print("Квантиль 0.1:", round(quantile(data, 0.1), 3))
print("Квантиль 0.25:", round(quantile(data, 0.25), 3))
print("Квантиль 0.5:", round(quantile(data, 0.5), 3))
print("Квантиль 0.75:", round(quantile(data, 0.75), 3))