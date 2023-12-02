import functools
from dataclasses import dataclass


@dataclass
class Game:
    id: int
    largest_red: int
    largest_green: int
    largest_blue: int

    @property
    def power_of_lowest_required(self) -> int:
        return self.largest_red * self.largest_green * self.largest_blue

    def is_possible(self, reds: int, greens: int, blues: int) -> bool:
        return all((self.largest_red <= reds, self.largest_green <= greens, self.largest_blue <= blues))

    @classmethod
    def from_game_str(cls, game_str: str) -> "Game":
        plays_strs = game_str.split(";")
        game_and_play = plays_strs[0]
        game, first_play = tuple(game_and_play.split(":"))
        plays = [first_play]
        plays.extend(plays_strs[1:])

        largest_counts = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for play in plays:
            for color_count in play.split(","):
                count, color = tuple(color_count.strip().split(" "))
                count = int(count)

                if largest_counts[color] < count:
                    largest_counts[color] = count

        return cls(
            id=int(game.split(" ")[1]),
            largest_red=largest_counts["red"],
            largest_green=largest_counts["green"],
            largest_blue=largest_counts["blue"],
        )

def get_games(game_data: str) -> list[Game]:
    game_strs = game_data.split("\n")
    return [Game.from_game_str(gs) for gs in game_strs]

def get_possible_game_id_sum(game_data: str, reds: int, greens: int, blues: int) -> int:
    return functools.reduce(lambda s, e: s + e, [g.id for g in get_games(game_data) if g.is_possible(reds, greens, blues)])

def get_lowest_required_pow(game_data: str) -> int:
    return functools.reduce(lambda s, e: s + e, [g.power_of_lowest_required for g in get_games(game_data)])

def print_possibilities(game_data: str, reds: int, greens: int, blues: int):
    game_strs = game_data.split("\n")
    print(game_strs)
    games = [Game.from_game_str(gs) for gs in game_strs]
    for game in games:
        print(
            "Game -> id: ", game.id, " - ", game.largest_red, " reds, ", game.largest_green, " greens, ", game.largest_blue, " blues, ",
            "✅" if game.is_possible(reds, greens, blues) else "❌",
            reds, " reds, ", greens, " greens, ", blues,  " blues, "
        )

if __name__ == "__main__":
    with open("input-test.txt") as f1:
        contents1 = f1.read()
        print("(test) possible game id sum", get_possible_game_id_sum(contents1, reds=12, greens=13, blues=14))
        print("(test) power sum of lowest requried", get_lowest_required_pow(contents1))
        # print_possibilities(contents1, 12, 13, 14)

    with open("input.txt") as f2:
        contents2 = f2.read()
        print("possible game id sum", get_possible_game_id_sum(contents2, reds=12, greens=13, blues=14))
        print("(test) power sum of lowest requried", get_lowest_required_pow(contents2))
        # print_possibilities(contents2, 12, 13, 14)
