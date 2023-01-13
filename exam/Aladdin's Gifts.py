from collections import deque
mix_materials = [int(num) for num in input().split()]
magic_levels = deque([int(num) for num in input().split()])

my_dict = {"Diamond Jewellery": 0, "Gemstone": 0, "Gold": 0, "Porcelain Sculpture": 0}


def is_in_range(current_sum, my_dict):
    if current_sum >= 100 and current_sum <= 199:
        my_dict["Gemstone"] += 1
    elif current_sum >= 200 and current_sum <= 299:
        my_dict["Porcelain Sculpture"] += 1
    elif current_sum >= 300 and current_sum <= 399:
        my_dict["Gold"] += 1
    elif current_sum >= 400 and current_sum <= 499:
        my_dict["Diamond Jewellery"] += 1

while mix_materials and magic_levels:
    current_mix_material = mix_materials.pop()
    current_magic_level = magic_levels.popleft()

    current_sum = current_mix_material + current_magic_level

    if is_in_range(current_sum, my_dict):
        pass

    elif current_sum < 100:
        if current_sum % 2 == 0:
            current_mix_material *= 2
            current_magic_level *= 3
            current_sum = current_mix_material + current_magic_level
            is_in_range(current_sum, my_dict)
        else:
            current_mix_material *= 2
            current_magic_level *= 2
            current_sum = current_mix_material + current_magic_level
            is_in_range(current_sum, my_dict)

    elif current_sum > 499:
        current_sum /= 2
        is_in_range(current_sum, my_dict)


def is_winning_first(my_dict):
    return my_dict["Gemstone"] >= 1 and my_dict["Porcelain Sculpture"] >= 1

def is_winning_second(my_dict):
    return my_dict["Gold"] >= 1 and my_dict["Diamond Jewellery"] >= 1


if is_winning_first(my_dict) or is_winning_second(my_dict):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")


if mix_materials:
    print(f"Materials left: {', '.join([str(num) for num in mix_materials])}")

if magic_levels:
    print(f"Magic left: {', '.join([str(num) for num in magic_levels ])}")


for key, value in my_dict.items():
    if value > 0:
        print(f"{key}: {value}")


