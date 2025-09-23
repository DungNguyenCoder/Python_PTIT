t = int(input())

for i in range(t):
    s1 = input()
    s2 = input()
    s1 = "".join(sorted(s1))
    s2 = "".join(sorted(s2))
    if s1 == s2:
        print(f"Test {i + 1}: YES")
    else:
        print(f"Test {i + 1}: NO")