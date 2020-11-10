abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def write_one_result(move_value: int, data: str):
    result = []
    for char in data:
        try:
            result.append(abc[abc.find(char)+move_value])
        except IndexError:
            result.append(abc[abc.find(char)+move_value-len(abc)])

    with open("result.txt", "a") as f:
        f.write("".join(result) + "\n")
        f.write("\n")


with open("sifra.txt", "r") as f:
    data = (f.read()).strip()


for move_value in range(26):
    write_one_result(move_value, data)
