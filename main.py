import threading
import time

tailleGrille = 16


def main(lesReines=[]):
    th1 = threading.Thread(target=thread1, args=(lesReines.__len__(), True, lesReines))
    th1.start()

    lesReines = []
    th2 = threading.Thread(target=thread2, args=(lesReines.__len__(), False, lesReines))
    th2.start()

    lesReines = []
    th3 = threading.Thread(target=thread3, args=(lesReines.__len__(), lesReines))
    th3.start()

    lesReines = []
    th4 = threading.Thread(target=thread4, args=(lesReines.__len__(), lesReines))
    th4.start()

def thread1(taille, bool, tableau):
    start_time1 = time.time()
    backTrackFailOrSuccessHeuristic(taille, bool, tableau)
    stop_time1 = time.time() - start_time1
    printPositions(tableau)
    print("temps placement moins de place : ", stop_time1 * 1000)

def thread2(taille, bool, tableau):
    start_time2 = time.time()
    backTrackFailOrSuccessHeuristic(taille, bool, tableau)
    stop_time2 = time.time() - start_time2
    printPositions(tableau)
    print("temps placement plus de place : ", stop_time2*1000)

def thread3(taille, tableau):
    start_time3 = time.time()
    backTrack(taille, tableau)
    stop_time3 = time.time() - start_time3
    printPositions(tableau)
    print("temps placement sans heuristique : ", stop_time3*1000)


def thread4(taille, tableau):
    start_time4 = time.time()
    backTrackPlusCasesLibres(taille, tableau)
    stop_time4 = time.time() - start_time4
    printPositions(tableau)
    print("temps placement plus de case libre : ", stop_time4*1000)

def backTrackFailOrSuccessHeuristic(ligne, order, lesReines):
    if lesReines.__len__() == tailleGrille:
        return True
    placements = dict()
    for i in range(0, tailleGrille):
        if estLibre(i, lesReines):
            placements[i] = notation(i, ligne)

    placementsTries = {k: v for k, v in sorted(placements.items(), key=lambda item: item[1], reverse=order)}
    for i in placementsTries:
        lesReines.append(i)
        if backTrackFailOrSuccessHeuristic(ligne + 1, order, lesReines):
            return True
        else:
            lesReines.remove(i)
    return False


def notation(val, ligne):  # note la valeur de cases qui ne seront plus disponibles si on place la reine sur la ligne
    res = (tailleGrille - ligne)  # colonne
    for i in range(0, tailleGrille):
        if val <= i:
            res = res + 1  # une diagonale a droite en plus
        if val >= i:
            res = res + 1  # une diagonale a gauche en plus
    return res


def backTrackPlusCasesLibres(ligne, lesReines):
    if lesReines.__len__() == tailleGrille:
        return True
    placements = dict()
    for i in range(0, tailleGrille):
        if estLibre(i, lesReines):
            placements[i] = 0
            if ligne < tailleGrille:
                placements[i] = placements[i] + 1
            if i <= ligne:  # diagonale gauche
                placements[i] = placements[i] + 1
            if i >= ligne:  # diagonale droite
                placements[i] = placements[i] + 1

    placementsTries = {k: v for k, v in sorted(placements.items(), key=lambda item: item[1])}
    #print("ligne : ", ligne, " placements : ", placementsTries)
    for i in placementsTries:
        lesReines.append(i)
        if backTrackPlusCasesLibres(ligne + 1, lesReines):
            return True
        else:
            lesReines.remove(i)
    return False


def backTrack(ligne, lesReines):
    if lesReines.__len__() == tailleGrille:
        return True

    for i in range(0, tailleGrille):
        if estLibre(i, lesReines):
            lesReines.append(i)
            if backTrack(ligne + 1, lesReines):
                return True
            else:
                lesReines.remove(i)


def estLibre(val, lesReines):
    res = True
    for i in range(0, lesReines.__len__()):
        if lesReines[i] == val:
            res = False
        if val == (lesReines[i] - (lesReines.__len__() - i)) or val == (lesReines[i] + (lesReines.__len__() - i)):
            res = False
    return res


def printPositions(lesReines):
    grille = [[0] * tailleGrille for _ in range(tailleGrille)]
    output = ""
    it = 0
    for i in lesReines:
        grille[it][i] = 1
        it = it + 1

    for i in range(tailleGrille):
        for j in range(tailleGrille):
            if grille[i][j] == 1:
                output = output + " 👸 "
            else:
                output = output + " _ "
        output = output + "\n"
    print(output)


if __name__ == "__main__":
    main()
