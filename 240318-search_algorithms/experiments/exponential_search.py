member = ['Freya', 'Gita', 'Gressel', 'Flora', 'Michie', 'Ella', 'Shani']

def exponential_search(member, name):
    left = 0
    right = len(member) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if member[mid] == name:
            return mid
        elif member[mid] < name:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(exponential_search(member, 'Gita'))