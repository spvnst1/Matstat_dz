weather = input()
weather = [int(val) for val in weather.split(' ')]

max_delta = -float('inf')
start = 0
end = len(weather)

for i, val1 in enumerate(weather):
    for j, val2 in enumerate(weather[i+1:], start=i+1):
        if val2 - val1 > max_delta:
            max_delta = val2 - val1
            start = i
            end = j

        elif val2 - val1 == max_delta and j - i < end - start:
            max_delta = val2 - val1
            start = i
            end = j


print(' '.join((str(max_delta), str(start), str(end))))