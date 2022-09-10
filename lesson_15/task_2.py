
def longest_words(file: str):
    """
    :param file: отримує на вхід назву текстового файла в кавичках
    :return: друкує список найдовших слів у файлі
    """
    with open(file, "r", encoding="utf-8") as f:
        a = f.read()
        a = a.split()
        b = {}
        for i in range(len(a)):
            b.update({a[i]: len(a[i])})
        c = max(b.values())
        for j in b:
            if b[j] == c:
                print(j, "=", c, "літер")


if __name__ == "__main__":
    longest_words("article.txt")
