from collections import Counter


def visualize(money, bar_char='₽'):
    cnt = Counter(money)
    result = ''
    a = cnt.most_common(1)
    index = a[0][1]
    while index >= 0:
        for num in sorted(cnt):
            if cnt[num] == index:
                result = result + str(cnt[num]) + '  '
            elif cnt[num] > index:
                result = result + bar_char * 2 + ' '
            else:
                result = result + '   '
        index -= 1
        result = result[:-1] + '\n'
    for i in range(len(cnt)):
        result = result + '---'
    result = result[:-1] + '\n'
    for elem in sorted(cnt):
        if elem < 10:
            result = result + str(elem) + '  '
        else:
            result = result + str(elem) + ' '
    return result[:-1]


MONEY = (
    1, 20, 2, 5, 20,
    3, 5, 2, 10, 2,
    20, 2, 20, 1, 2,
    1, 1, 10, 20, 3,
)

print(visualize(MONEY, bar_char='$'))
