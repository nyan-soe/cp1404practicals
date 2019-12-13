from operator import itemgetter

words = "this is a collection of words of nice words this is a fun thing it is"
word_lists = words.split()
word_to_count = {}
for word in word_lists:
    word_to_count[word] = word_to_count.get(word, 0) + 1

sorted_x = sorted(word_to_count.items())

max = -99
for x in sorted_x:
    if len(x[0]) > max:
        max = len(x[0])

for x in sorted_x:
    print("{:{}s} : {}".format(x[0], max, x[1]))
