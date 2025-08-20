import math

def calculate_simple_syrup(target_quarts):
    """Calculate sugar and water needed for simple syrup"""
    # 1 quart water + 1 quart sugar = 1.5 quarts simple syrup
    # So each quart of ingredient makes 0.75 quarts of syrup
    
    quarts_per_ingredient = target_quarts / 1.5
    cups_per_ingredient = quarts_per_ingredient * 4
    
    return {
        'water_cups': math.ceil(cups_per_ingredient),
        'sugar_cups': math.ceil(cups_per_ingredient),
        'target_quarts': target_quarts
    }

def main():
    try:
        target = float(input("Enter desired simple syrup volume (quarts): "))
        result = calculate_simple_syrup(target)
        
        print(f"\nTo make {result['target_quarts']} quarts of simple syrup:")
        print(f"Water: {result['water_cups']} cups")
        print(f"Sugar: {result['sugar_cups']} cups")
        
    except ValueError:
        print("Please enter a valid number")

if __name__ == "__main__":
    main()