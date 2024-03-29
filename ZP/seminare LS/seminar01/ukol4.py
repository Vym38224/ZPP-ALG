    
def Insertion_Sort(arr):
    for j in range(1, len(arr)):
        t = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > t:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = t

def stejne_hodnoty(s1,s2):
    p = 0
    if len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                p += 0
            else:
                p += 1
        if p == 0:
            return True
        else:
            return False

try:
    s1=[4,1,3,4,6,8,9]
    s2=[int("jedna"),8,4,6,3,4,9]

    Insertion_Sort(s1)
    Insertion_Sort(s2)
    print(stejne_hodnoty(s1,s2))
except ValueError:
    print("Operace s kompatibilními datovými typy ale s chybnou hodnotou!")
