fname = input('Enter name of the file: ')
try:
    fhand = open(fname)
except:
    print('File not found!!!')
    exit()
#fhand = open('romeo-full.txt')

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

tmp = sorted([(v,k) for (k,v) in counts.items()],reverse = True)

for v,k in tmp:
    print(k,v)

bigcount = None
bigword = None
smallword = None
smallcount = None


for count,word in tmp:
    if bigcount is None or bigcount < count:
        bigcount = count
        bigword = word
    elif smallcount is None or smallcount > count:
        smallcount = count
        smallword = word

print('largest: ',bigword,bigcount)
print('smallest: ',smallword,smallcount)

