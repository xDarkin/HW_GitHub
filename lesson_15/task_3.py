
def update_hero(**kwargs):
    update_data = {**kwargs}
    update_keys = list(update_data.keys())
    update_values = list(update_data.values())
    with open("hero.ini", "r+") as update:
        a = ""
        for i in update:
            line = i.split("=")
            for j in range(len(update_keys)):
                if line[0] == update_keys[j]:
                    line[1] = str(update_values[j]) + "\n"
            a += line[0] + "=" + line[1]
        with open("hero.ini", "w") as update_1:
            update_1.write(a)


if __name__ == "__main__":
    update_hero(hero="Hulk", power=450, Y=2.3)
