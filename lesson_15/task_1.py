
def writing():
    with open("file_task_1.txt", "w+") as f:
        n = "_"
        while n != "":
            n = input("Введіть новий рядок: ")
            f.write(n + "\n")


if __name__ == "__main__":
    writing()
