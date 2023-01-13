from collections import deque
bomb_effects = deque([int(num) for num in input().split(", ")])
bomb_cases = [int(num) for num in input().split(", ")]

bomb_dict = {"Cherry Bombs": 0, "Datura Bombs": 0, "Smoke Decoy Bombs": 0}

def is_pouch_full(bomb_dict):
    return all(value >= 3 for value in bomb_dict.values())


while bomb_effects and bomb_cases:
    current_bomb_effect = bomb_effects.popleft()
    current_bomb_case = bomb_cases.pop()

    current_sum = current_bomb_effect + current_bomb_case

    if current_sum == 40:
        bomb_dict["Datura Bombs"] += 1
    elif current_sum == 60:
        bomb_dict["Cherry Bombs"] += 1
    elif current_sum == 120:
        bomb_dict["Smoke Decoy Bombs"] += 1
    else:
        bomb_cases.append(current_bomb_case - 5)
        bomb_effects.insert(0, current_bomb_effect)

    if is_pouch_full(bomb_dict):
        break


if is_pouch_full(bomb_dict):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")


if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(bomb) for bomb in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_cases:
    print(f"Bomb Casings: {', '.join([str(bomb) for bomb in bomb_cases])}")
else:
    print("Bomb Casings: empty")

for key, value in bomb_dict.items():
    print(f"{key}: {value}")



