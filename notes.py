import math

def juggler_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = math.floor(math.sqrt(n))
        else:
            n = math.floor(n ** 1.5)
        sequence.append(n)
    return sequence

def main():
    n = int(input("Enter a positive integer: "))
    sequence = juggler_sequence(n)
    print(f"The Juggler sequence starting at {n} is:")
    print(", ".join(map(str, sequence)))
    print(f"It took {len(sequence) - 1} iterations to reach 1")

if __name__ == "__main__":
    main()
