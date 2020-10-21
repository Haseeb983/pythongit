fhand = open('romeo-full.txt')

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

tmp = sorted([(v,k) for (k,v) in counts.items()],reverse = True)

for v,k in tmp:
    print(k,v)