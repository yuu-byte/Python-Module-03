import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = [
        "alice",
        "bob",
        "charlie",
        "dylan"
    ]
    actions = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
        "use"
    ]

    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(
    event_list: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while event_list:
        index = random.randrange(len(event_list))
        event = event_list.pop(index)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    events = gen_event()

    for i in range(1000):
        player, action = next(events)
        print(f"Event {i}: Player {player} did action {action}")

    event_list: list[tuple[str, str]] = []

    for i in range(10):
        generated_event = next(events)
        event_list.append(generated_event)

    print(f"Built list of 10 events: {event_list}")

    for consumed_event in consume_event(event_list):
        print(f"Got event from list: {consumed_event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
