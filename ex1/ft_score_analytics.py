import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    scores: list[int] = []

    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if not scores:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        total_players = len(scores)
        total_score = sum(scores)
        high_score = max(scores)
        low_score = min(scores)
        average_score = total_score / total_players

        print(f"Scores processed: {scores}")
        print(f"Total players: {total_players}")
        print(f"Total score: {total_score}")
        print(f"Average score: {average_score}")
        print(f"High score: {high_score}")
        print(f"Low score: {low_score}")
        print(f"Score range: {high_score - low_score}")


if __name__ == "__main__":
    main()
