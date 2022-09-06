
def dict_handler(a: dict, key, def_val):
    assert type(key) == int or type(key) == str or type(key) == tuple or type(key) == float,\
        "Ключ має бути незмінного типу данних"

    try:
        b = a[key]
    except KeyError:
        c = {key: def_val}
        a.update(c)
    finally:
        print(m)
        print("key =", a[key])
        return a[key]


if __name__ == "__main__":
    m = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    dict_handler(m, [1, 2], 10)
