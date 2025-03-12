import copy

def append_to(num, target=None):
    if target:
        target = copy.copy(target)  # creates a shallow copy of the target
    else:
        target = []
    target.append(num)
    return target

original_list = [1, 2, 3]
new_list = append_to(4, original_list)

print(original_list)  # Outputs: [1, 2, 3]
print(new_list)  # Outputs: [1, 2, 3, 4]