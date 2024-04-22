import random

def generate_combinations(regex):
    result = ""
    for i in range(len(regex)):
        current_builder = ""
        ch = regex[i]

        # Handle character repetition and choices based on regular expression syntax
        if ch.isalpha() or ch.isdigit():
            if i + 1 < len(regex) and regex[i + 1] == '^':
                power = min(int(regex[i + 2]), 5)  # Limit the repetition to 5 times
                current_builder = ch * power
                i += 2
            elif i + 1 < len(regex) and regex[i + 1] == '*':
                current_builder = ch * random.randint(0, 5)  # Random repetition up to 5 times
                i += 1
            elif i + 1 < len(regex) and regex[i + 1] == '+':
                current_builder = ch * random.randint(1, 5)  # Random repetition from 1 to 5 times
                i += 1
            elif i + 1 < len(regex) and regex[i + 1] == '?':
                current_builder = ch if random.choice([True, False]) else ""
                i += 1

        # Handle grouped characters within parentheses
        if ch == '(':
            chars = set()
            next_ch = regex[i + 1]
            while next_ch != ')':
                if next_ch != '|':
                    chars.add(next_ch)
                next_ch = regex[i + 1]
                i += 1

            if i + 1 < len(regex) and regex[i + 1] == '^':
                power = min(int(regex[i + 2]), 5)  # Limit the repetition to 5 times
                current_builder = ''.join(random.choices(list(chars), k=power))
                i += 2
            else:
                current_builder = random.choice(list(chars))

        print(regex[:i + 1] + " -> " + current_builder)  # Print debug information
        result += current_builder

    return result

def main():
    # Define regular expression
    regex = "(S|T)(u|v)w*y+"

    # Generate combinations and print
    print("====Variant 4====")
    for _ in range(5):
        print(generate_combinations(regex))
        print()

if __name__ == "__main__":
    main()
