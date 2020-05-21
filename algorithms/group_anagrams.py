input = ['cat', 'dog', 'tac', 'god', 'act']

anagrams = dict()
for i in input:
    s = tuple(sorted(i))
    if s not in anagrams:
        anagrams[s] = list()
    anagrams[s].append(i)

for k, v in anagrams.items():
    print(v)