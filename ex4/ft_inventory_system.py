import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        parts = arg.split(":")

        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item_name = parts[0]
        item_quantity_text = parts[1]

        if item_name == "":
            print(f"Error - invalid parameter '{arg}'")
            continue
        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            item_quantity = int(item_quantity_text)
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")
            continue

        inventory[item_name] = item_quantity

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

    for item_name in inventory:
        item_quantity = inventory[item_name]

        if total_quantity != 0:
            percentage = item_quantity / total_quantity * 100
        else:
            percentage = 0.0

        print(f"Item {item_name} represents {round(percentage, 1)}%")

    if inventory:
        first_item = list(inventory.keys())[0]
        most_item = first_item
        least_item = first_item
        most_quantity = inventory[first_item]
        least_quantity = inventory[first_item]

        for item_name in inventory:
            item_quantity = inventory[item_name]

            if item_quantity > most_quantity:
                most_item = item_name
                most_quantity = item_quantity

            if item_quantity < least_quantity:
                least_item = item_name
                least_quantity = item_quantity

        print(
            f"Item most abundant: {most_item} "
            f"with quantity {most_quantity}"
        )
        print(
            f"Item least abundant: {least_item} "
            f"with quantity {least_quantity}"
        )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
