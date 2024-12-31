def tri_rap(liste):
    if len(liste) <= 1:
        return liste
    pivot = liste.pop()

    petit = []
    grand = []

    for number in liste:
        if number < pivot:
            petit.append(number)
        else:
            grand.append(number)
    return tri_rap(petit) + [pivot] + tri_rap(grand)

l = [1,22,238,10]
print(tri_rap(l))