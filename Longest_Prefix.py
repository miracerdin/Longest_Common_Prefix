Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".




strs = ["flower","flow","flight"]
b = sorted(strs, key=len)
kısa = b[0]
boş = " "
for i in max(strs, key=len ):
    for t in strs:
        
        if t.startswith(kısa):
            boş = kısa
        else:
            kısa = kısa[:len(kısa)-1]
            if len(kısa) == 0:
                print('""')
print(kısa)
