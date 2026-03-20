S = input().strip()

vowels = set('aeiouAEIOU')
has_vowel = any(ch in vowels for ch in S)

print("Yes" if has_vowel else "No")