def all_thing_is_obj(obj: any) -> int:
    msgs = {
        list: "List :",
        tuple: "Tuple :",
        set: "Set :",
        dict: "Dict :",
        str: None,
    }

    for t, label in msgs.items():
        if isinstance(obj, t):
            print(
                f"{obj} is in the kitchen : {type(obj)}"
                if t is str
                else f"{label} {type(obj)}"
            )
            break
    else:
        print("Type not found")

    return 42
