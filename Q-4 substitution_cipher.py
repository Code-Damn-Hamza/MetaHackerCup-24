def count_decodings(s):
    n = len(s)
    if n == 0:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: empty string
    dp[1] = 1 if s[0] != '0' else 0  # First character must not be '0'
    
    for i in range(2, n + 1):
        # Single digit
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        
        # Two digits
        two_digit = int(s[i - 2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]
    
    return dp[n]

def generate_possibilities(s):
    if '?' not in s:
        return [s]

    possibilities = set()
    for i in range(10 ** s.count('?')):
        replacement = str(i).zfill(s.count('?'))
        current_string = s
        for digit in replacement:
            current_string = current_string.replace('?', digit, 1)
        possibilities.add(current_string)
    
    return possibilities

def decode_string(encoded, k):
    max_decodings = 0
    best_strings = []

    possibilities = generate_possibilities(encoded)

    for possibility in possibilities:
        count = count_decodings(possibility)
        if count > max_decodings:
            max_decodings = count
            best_strings = [possibility]
        elif count == max_decodings:
            best_strings.append(possibility)
    
    best_strings = sorted(best_strings)
    if len(best_strings) < k:
        return "Not enough valid strings"
    return best_strings[k - 1], max_decodings

def main():
    t = int(input("Enter number of test cases: "))
    results = []
    
    for i in range(1, t + 1):
        line = input().strip().split()
        encoded = line[0]
        k = int(line[1])
        
        best_string, max_decodings = decode_string(encoded, k)
        results.append(f"Case #{i}: {best_string} {max_decodings % 998244353}")

    print("\n".join(results))

if __name__ == "__main__":
    main()
