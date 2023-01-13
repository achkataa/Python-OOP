# def list_manipulator(ll, action, place, *args):
#     if action == "add":
#         if place == "beginning":
#             for num in reversed(args):
#                 ll.insert(0, num)
#         else:
#             for num in args:
#                 ll.append(num)
#     else:
#         if place == "beginning" and not args:
#             ll.pop(0)
#         elif place == "beginning" and args:
#             for i in range(args[0]):
#                 ll.pop(0)
#         elif place == "end" and not args:
#             ll.pop(-1)
#         else:
#             for i in range(args[0]):
#                 ll.pop(-1)
#     return ll

def add_beginning(args, ll):
    for num in reversed(args):
        ll.insert(0, num)
    return ll

def add_end(args, ll):
    for num in args:
        ll.append(num)
    return ll

def remove_beginning_with_args(args, ll):
    for i in range(args[0]):
        ll.pop(0)
    return ll

def remove_beginning_without_args(ll):
    ll.pop(0)
    return ll

def remove_end_with_args(args, ll):
    for i in range(args[0]):
        ll.pop(-1)
    return ll

def remove_end_without_args(ll):
    ll.pop(-1)
    return ll


def list_manipulator(ll, action, place, *args):
    if action == "add":
        if place == "beginning":
            add_beginning(args, ll)
        else:
            add_end(args, ll)
    else:
        if place == "beginning" and not args:
            remove_beginning_without_args(ll)
        elif place == "beginning" and args:
            remove_beginning_with_args(args, ll)
        elif place == "end" and not args:
            remove_end_without_args(ll)
        else:
            remove_end_with_args(args, ll)
    return ll

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
