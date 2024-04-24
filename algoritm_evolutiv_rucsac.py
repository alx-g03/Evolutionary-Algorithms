import random


def generare_individ(n):
    return [random.randint(0, 1) for _ in range(n)]


def evaluare_individ(individ, obiecte, capacitate_rucsac):
    valoare_totala = 0
    greutate_totala = 0
    for i in range(len(obiecte)):
        if individ[i] == 1:
            valoare_totala += obiecte[i][2]
            greutate_totala += obiecte[i][1]
    if greutate_totala > capacitate_rucsac:
        return 0
    else:
        return valoare_totala


def selectie_parinti(populatie, obiecte, capacitate_rucsac):
    parinti = []
    for _ in range(len(populatie)):
        a, b = random.sample(populatie, 2)
        parinti.append(max(a, b, key=lambda x: evaluare_individ(x, obiecte, capacitate_rucsac)))
    return parinti


def incrucisare(parinte1, parinte2, obiecte):
    punct_incrucisare = random.randint(1, len(obiecte) - 1)
    descendent1 = parinte1[:punct_incrucisare] + parinte2[punct_incrucisare:]
    descendent2 = parinte2[:punct_incrucisare] + parinte1[punct_incrucisare:]
    return descendent1, descendent2


def mutatie(individ):
    pozitie_mutatie = random.randint(0, len(individ) - 1)
    individ[pozitie_mutatie] = 1 - individ[pozitie_mutatie]
    return individ


def algoritm_evolutiv_rucsac(obiecte, capacitate_rucsac, marime_populatie, numar_generatii, prob_incrucisare, prob_mutatie):
    populatie = [generare_individ(len(obiecte)) for _ in range(marime_populatie)]

    for generatie in range(numar_generatii):
        parinti = selectie_parinti(populatie, obiecte, capacitate_rucsac)

        descendenti = []
        for i in range(0, len(parinti), 2):
            parinte1 = parinti[i]
            parinte2 = parinti[i + 1]
            if random.random() < prob_incrucisare:
                descendent1, descendent2 = incrucisare(parinte1, parinte2, obiecte)
            else:
                descendent1, descendent2 = parinte1[:], parinte2[:]
            if random.random() < prob_mutatie:
                descendent1 = mutatie(descendent1)
            if random.random() < prob_mutatie:
                descendent2 = mutatie(descendent2)
            descendenti.extend([descendent1, descendent2])

        populatie.extend(descendenti)
        populatie = sorted(populatie, key=lambda x: evaluare_individ(x, obiecte, capacitate_rucsac), reverse=True)[:marime_populatie]

        cel_mai_bun = max(populatie, key=lambda x: evaluare_individ(x, obiecte, capacitate_rucsac))
        print(f"Generatia {generatie + 1}: Cel mai bun individ: {cel_mai_bun}, Valoare: {evaluare_individ(cel_mai_bun, obiecte, capacitate_rucsac)}")
