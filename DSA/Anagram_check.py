a = "listen"
b = "silent"

count1 = [0] * 26
count2 = [0] * 26

# pehle word ka count
for i in range(len(a)):
    count1[ord(a[i]) - ord('a')] += 1

# dusre word ka count
for i in range(len(b)):
    count2[ord(b[i]) - ord('a')] += 1


isAnagram = True

# dono counts compare karna
for i in range(26):
    if count1[i] != count2[i]:
        isAnagram = False
        break


if isAnagram:
    print("Anagram")
else:
    print("Not Anagram")