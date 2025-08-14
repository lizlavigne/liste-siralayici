def liste_sirala(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

liste = input("Sayıları aralarında boşluk olacak şekilde girin: ")
sayilar = [int(x) for x in liste.split()]

sirali = liste_sirala(sayilar)
print("Sıralanmış liste:", sirali)