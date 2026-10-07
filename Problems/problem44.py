# wap to remove a given word from the list and strip it at the same Time 


def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n  

l = ["Jack", "Joe", "Boe", "Oggy", "oe"]

print(rem(l, "oe"))