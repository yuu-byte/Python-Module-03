import random


ALL_ACHIEVEMENTS: list[str] = [
    "First Steps",
    "Boss Slayer",
    "Treasure Hunter",
    "Speed Runner",
    "Master Explorer",
    "Crafting Genius",
    "World Savior",
    "Collector Supreme",
    "Untouchable",
    "Strategist",
    "Unstoppable",
    "Survivor",
    "Sharp Mind",
    "Hidden Path Finder"
]


def gen_player_achievements() -> set[str]:
    num_achievements = random.randint(5, 9)
    player_achievements = random.sample(ALL_ACHIEVEMENTS, num_achievements)
    return set(player_achievements)


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()

    alice_achievements = gen_player_achievements()
    bob_achievements = gen_player_achievements()
    charlie_achievements = gen_player_achievements()
    dylan_achievements = gen_player_achievements()
    all_achievements_set = set(ALL_ACHIEVEMENTS)

    all_distinct_achievements = alice_achievements.union(
        bob_achievements,
        charlie_achievements,
        dylan_achievements
    )
    common_achievements = alice_achievements.intersection(
        bob_achievements,
        charlie_achievements,
        dylan_achievements
    )
    only_alice_achievements = alice_achievements.difference(
        bob_achievements,
        charlie_achievements,
        dylan_achievements
    )
    only_bob_achievements = bob_achievements.difference(
        charlie_achievements,
        dylan_achievements,
        alice_achievements
    )
    only_charlie_achievements = charlie_achievements.difference(
        dylan_achievements,
        alice_achievements,
        bob_achievements
    )
    only_dylan_achievements = dylan_achievements.difference(
        alice_achievements,
        bob_achievements,
        charlie_achievements
    )
    alice_missing_achievements = all_achievements_set.difference(
        alice_achievements
    )
    bob_missing_achievements = all_achievements_set.difference(
        bob_achievements
    )
    charlie_missing_achievements = all_achievements_set.difference(
        charlie_achievements
    )
    dylan_missing_achievements = all_achievements_set.difference(
        dylan_achievements
    )

    print(f"Player Alice: {alice_achievements}")
    print(f"Player Bob: {bob_achievements}")
    print(f"Player Charlie: {charlie_achievements}")
    print(f"Player Dylan: {dylan_achievements}")
    print()
    print(f"All distinct achievements: {all_distinct_achievements}")
    print()
    print(f"Common achievements: {common_achievements}")
    print()
    print(f"Only Alice has: {only_alice_achievements}")
    print(f"Only Bob has: {only_bob_achievements}")
    print(f"Only Charlie has: {only_charlie_achievements}")
    print(f"Only Dylan has: {only_dylan_achievements}")
    print()
    print(f"Alice is missing: {alice_missing_achievements}")
    print(f"Bob is missing: {bob_missing_achievements}")
    print(f"Charlie is missing: {charlie_missing_achievements}")
    print(f"Dylan is missing: {dylan_missing_achievements}")


if __name__ == "__main__":
    main()
