"""
inventory_system.py

A simple inventory management program that supports adding, removing,
saving, and loading stock data while ensuring code quality and safety.
"""


import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add an item to the inventory."""
    if logs is None:
        logs = []

    # Validate input types
    if not isinstance(item, str):
        print(f"Invalid item name type: {item} (must be a string)")
        return
    if not isinstance(qty, int):
        print(f"Invalid quantity type: {qty} (must be an integer)")
        return
    if qty < 0:
        print(f"Invalid quantity: {qty} (cannot add negative numbers)")
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove a specified quantity of an item from inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in inventory.")
    except TypeError:
        print(f"Invalid quantity type for item '{item}'.")


def get_qty(item):
    """Return the quantity available for a given item."""
    return stock_data[item]


def load_data(file="inventory.json"):
    """Load stock data from a JSON file."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            stock_data.clear()
            stock_data.update(data)
    except FileNotFoundError:
        print(f"File '{file}' not found. Starting with an empty inventory.")
        stock_data.clear()
    except json.JSONDecodeError:
        print(f"Error decoding JSON from '{file}'. Resetting inventory.")
        stock_data.clear()


def save_data(file="inventory.json"):
    """Save stock data to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
    except OSError as e:
        print(f"Error saving file '{file}': {e}")


def print_data():
    """Print current inventory report."""
    print("Items Report")

    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")


def check_low_items(threshold=5):
    """Return a list of items whose stock quantity is below the threshold."""
    result = []
    for item, quantity in stock_data.items():
        if quantity < threshold:
            result.append(item)

    return result


def main():
    """Main function to demonstrate inventory operations."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")
    remove_item("apple", 3)
    remove_item("orange", 1)

    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    print("Eval function removed for safety.")


main()
