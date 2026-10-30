import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players: list[str] = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam"
    ]
    capitalized_players: list[str] = [
        player.capitalize() for player in players
    ]
    originally_capitalized_players: list[str] = [
        player for player in players if player and player[0].isupper()
    ]
    player_scores: dict[str, int] = {
        player: random.randint(0, 1000) for player in capitalized_players
    }
    average_score: float = sum(player_scores.values()) / len(player_scores)
    high_scores: dict[str, int] = {
        player: score
        for player, score in player_scores.items()
        if score > average_score
    }

    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {capitalized_players}")
    print(f"New list of capitalized names only: "
          f"{originally_capitalized_players}")
    print(f"Score dict: {player_scores}")
    print(f"Score average is {round(average_score, 2)}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
