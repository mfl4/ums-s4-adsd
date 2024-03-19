member = ['Freya', 'Gita', 'Gressel', 'Flora', 'Michie', 'Ella', 'Shani']

def linear_search(member, name):
    for i in range(len(member)):
        if member[i] == name:
            return i
    return -1

print(linear_search(member, 'Gita'))