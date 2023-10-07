
n = int(input("Entrez le nombre de photocopies effectuées : "))
facture = 0.0
if n <= 10:
    facture = n * 0.30
    print("votre facture est :", facture)
elif n <= 30:
    facture = (10 * 0.30) + ((n - 10) * 0.25)
    print("votre facture est :", facture)
else:
    facture = (10 * 0.30) + (20 * 0.25) + ((n - 30) * 0.20) 
    print("votre facture est :", facture)

