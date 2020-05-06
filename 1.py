class CyrillicException(Exception):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return "Невозможно записать кириллицу в файл"

    def writeInFile(self, s):
        with open(self.path, "w") as f:
            f.write(s)


def checkCyrilic(s, path):
    cyrrilic = "АБВГДИЙКЛМНОПРСТУФХЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    for i in s:
        if i in cyrrilic:
            raise CyrillicException(path)


if __name__ == "__main__":
    s = input("Запись в файл: ")
    cyr = CyrillicException("crlcException.txt")
    try:
        checkCyrilic(s, "crlcException.txt")
        cyr.writeInFile(s)
    except CyrillicException as e:
        print(e)
        cyr.writeInFile(e.__str__())
    finally:
        print("Печать закончена")