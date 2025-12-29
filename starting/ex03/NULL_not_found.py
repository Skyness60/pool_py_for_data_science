def NULL_not_found(obj) -> int:
    outputs = [
        (obj is None, f"Nothing: {obj} {type(obj)}"),
        (isinstance(obj, float) and obj != obj, f"Cheese: {obj} {type(obj)}"),
        (isinstance(obj, bool), f"Fake: {obj} {type(obj)}"),
        (isinstance(obj, int) and obj == 0, f"Zero: {obj} {type(obj)}"),
        (isinstance(obj, str) and obj == "", f"Empty: {type(obj)}"),
    ]

    for condition, message in outputs:
        if condition:
            print(message)
            return 0

    print("Type not Found")
    return 1
