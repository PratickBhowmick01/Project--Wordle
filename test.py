arr1 = []
f = open("Modern word list.txt", "r")
for word in f:
	word = word.upper()
	arr1.append(word[:5])
f.close()

arr1.sort()
# print(arr1[-1])

f2 = open("New_Words.txt", "w")
for word2 in arr1:
    f2.write(word2 + "\n")

f2.close()


# # List all the words from arr2 that are not in arr1.
# arr3 = []
# for w in arr2:
# 	if w not in arr1:
# 		arr3.append(w)
# print(arr3)