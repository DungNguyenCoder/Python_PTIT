def generate_even_palindromes(limit):
    digits = ['0', '2', '4', '6', '8']
    results = []
    max_len = len(str(limit))

    for length in range(2, max_len + 1, 2):
        half_len = length // 2

        def backtrack(cur):
            if len(cur) == half_len:
                left = ''.join(cur)
                num = int(left + left[::-1])
                if num < limit:
                    results.append(num)
                return
            for d in digits:
                if len(cur) == 0 and d == '0':
                    continue
                cur.append(d)
                backtrack(cur)
                cur.pop()

        backtrack([])
    return results

t = int(input())
for _ in range(t):
    n = int(input())
    nums = generate_even_palindromes(n)
    print(*sorted(nums))