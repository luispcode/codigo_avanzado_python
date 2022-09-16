from ast import Str


def make_repeater_of(n):

    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas de texto"
        return string * n

    return repeater

def run():
    repeater_5 = make_repeater_of(5)
    print(repeater_5("Hola"))

if __name__ == '__main__':
    run()