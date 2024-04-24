from algoritm_evolutiv_rucsac import algoritm_evolutiv_rucsac
from algoritm_evolutiv_tsp import evolutionary_algorithm_tsp
from citeste_fisier import citeste_rucsac_din_fisier, citeste_tsp_din_fisier


def main():
    rucsac_file = "rucsac-20.txt"  # Numele fișierului cu datele problemei rucsacului
    obiecte, capacitate_rucsac = citeste_rucsac_din_fisier(rucsac_file)

    tsp_file = "kroC100.tsp"  # Numele fișierului cu datele tsp
    cities = citeste_tsp_din_fisier(tsp_file)

    def afisare_meniu():
        print("Meniu:")
        print("1. Algoritm evolutiv pentru problema rucsacului")
        print("2. Algoritm evolutiv pentru tsp")
        print("x. Exit")

    while True:
        afisare_meniu()
        optiune = input("Selectați o opțiune: ")

        if optiune == "1":
            algoritm_evolutiv_rucsac(obiecte, capacitate_rucsac, marime_populatie=50, numar_generatii=100, prob_incrucisare=0.7, prob_mutatie=0.1)
        elif optiune == "2":
            evolutionary_algorithm_tsp(cities, population_size=100, num_generations=100, crossover_prob=0.8, mutation_prob=0.2)
        elif optiune == "x":
            break
        else:
            print("Opțiune invalidă! Vă rugăm să selectați din nou.")


if __name__ == "__main__":
    main()
