import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coordinates = input(
            "Enter new coordinates as floats in format 'x,y,z': "
            )
        parts = coordinates.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue
        values: list[float] = []
        try:
            for part in parts:
                values.append(float(part))
            return (values[0], values[1], values[2])
        except ValueError as e:
            print(
                f"Error on parameter '{part}': {e}"
                )


def main() -> None:
    pass


if __name__ == "__main__":
    main()
