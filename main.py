from Queen import Queen

tailleGrille = 4

lesReines = [Queen(0, 0)]

def printPositions():
    grille = [[0]*tailleGrille for i in range(tailleGrille)]
    output = ""
    for i in lesReines:
        grille[i.colonne][i.ligne] = 1

    for i in range(tailleGrille):
        for j in range(tailleGrille):
            if grille[i][j] == 1:
                output = output + "♛"
            else:
                output = output + "_"
        output = output + "\n"
    print(output)

def compute():
    backTrack(0)
    printPositions()

def backTrack(ligne):
    if lesReines.__len__() == tailleGrille:
        return 1

    for colonne in range(tailleGrille):
        ajout = True
        for reine in lesReines:
            if reine.colonne == colonne:
                ajout = False

            c = colonne
            l = ligne
            d = 0
            for i in range(tailleGrille):
                if [l-i, c-i] in lesReines != -1:
                    ajout = False
                d = d+1





"""def backTrack(ligne, colonne):
    if lesReines.__len__() == tailleGrille:
        return 1
    if colonne > tailleGrille or ligne > tailleGrille:
        return 0

    for i in lesReines:
        if i.colonne == colonne:
            return backTrack(ligne, colonne + 1)
        if i.ligne == ligne:
            return backTrack(ligne + 1, 0)

        check1 = i.ligne + ligne
        check2 = i.colonne + ligne
        if (ligne - i.ligne) == colonne or (ligne - i.colonne) == colonne:
            return backTrack(ligne, colonne + 1)  # check si on est sur la diagonale inférieure d'une autre reine
        else:
            lesReines.append(Queen(ligne, colonne))
            return backTrack(ligne+1, 0)

        """"""for j in lesReines:
            if j.colonne == colonne:
                return backTrack(ligne, colonne + 1)
            check11 = ligne - j.ligne
            check22 = ligne - j.colonne
            if (j.ligne - ligne) == colonne or (j.colonne - ligne == colonne):
                return backTrack(ligne, colonne + 1)

        newReine = Queen(ligne, colonne)
        lesReines.append(newReine)
        if backTrack(ligne + 1, 0) == 1:
            break
        lesReines.pop(lesReines.__len__() - 1)
        if colonne < tailleGrille:
            colonne = colonne + 1
        else:
            colonne = 0
            ligne = ligne + 1"""


compute()
