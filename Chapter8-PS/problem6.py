# strip a givrn word
def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

l =["Abhihsek","Abhinav","Anirudh","Abhiyank"]
print(rem(l,"Abhi"))