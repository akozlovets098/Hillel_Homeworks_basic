# Сортировка
def sorting(list_to_sort):
    list_to_use = list_to_sort[:]
    result_list = []
    for _ in range(len(list_to_use)):
        result_list.append(min(list_to_use))
        list_to_use.pop(list_to_use.index(min(list_to_use)))
    return result_list

def bubble_sort(list_to_sort):
    list_to_use = list_to_sort[:]
    for j in range(len(list_to_use) - 1):
        for i in range(len(list_to_use) - 1 - j):
            if list_to_use[i] > list_to_use[i + 1]:
                list_to_use[i], list_to_use[i + 1] = list_to_use[i + 1], list_to_use[i]
    return list_to_use

mylist = [1,4,6,4,8,34,67,6,89,4,7,0,-3,-5,6]
print(sorting(mylist))
print(bubble_sort(mylist))