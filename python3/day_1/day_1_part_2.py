ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE = (
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
)

str_to_num_map = {
    ONE: 1,
    TWO: 2,
    THREE: 3,
    FOUR: 4,
    FIVE: 5,
    SIX: 6,
    SEVEN: 7,
    EIGHT: 8,
    NINE: 9,
}

first_letter_to_full_number_map = {
    "o": (ONE,),
    "t": (TWO, THREE),
    "f": (FOUR, FIVE),
    "s": (SIX, SEVEN),
    "e": (EIGHT,),
    "n": (NINE,),
}


def get_number(line: str, do_reverse=False) -> str:
    indices = range(len(line))
    if do_reverse:
        indices = reversed(indices)

    for i in indices:
        val = line[i]

        if val in first_letter_to_full_number_map:
            num_strs = first_letter_to_full_number_map[val]
            for num_str in num_strs:
                if num_str == line[i:i+len(num_str)]:
                    return str(str_to_num_map[num_str])

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