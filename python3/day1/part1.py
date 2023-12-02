def get_number(line: str, do_reverse=False) -> str:
    indices = range(len(line))
    if do_reverse:
        indices = reversed(indices)

    for i in indices:
        val = line[i]
        if val.isnumeric():
            return val
    return "0"


def get_calibration_sum(document: str) -> int:
    lines = document.split("\n")
    sum = 0
    for line in lines:
        sum += int(f"{get_number(line)}{get_number(line, do_reverse=True)}")
    return sum


if __name__ == "__main__":
    with open("input-test.txt") as f:
        print("test answer", get_calibration_sum(f.read()))

    with open("input.txt") as f:
        print("answer", get_calibration_sum(f.read()))