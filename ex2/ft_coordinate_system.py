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
        except ValueError as e:
            print(f"Error on parameter '{part}': {e}")
            continue

        return (values[0], values[1], values[2])


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    first_pos = get_player_pos()
    print(f"Got a first tuple: {first_pos}")
    print(f"It includes: X={first_pos[0]}, Y={first_pos[1]}, Z={first_pos[2]}")

    distance_to_center = math.sqrt(
        first_pos[0] ** 2 + first_pos[1] ** 2 + first_pos[2] ** 2
    )
    print(f"Distance to center: {round(distance_to_center, 4)}")
    print()

    print("Get a second set of coordinates")
    second_pos = get_player_pos()

    distance_between_positions = math.sqrt(
        (second_pos[0] - first_pos[0]) ** 2
        + (second_pos[1] - first_pos[1]) ** 2
        + (second_pos[2] - first_pos[2]) ** 2
    )
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(distance_between_positions, 4)}")


if __name__ == "__main__":
    main()
