tailleGrille = 15
lesReines = []

def main():
    backTrack(lesReines.__len__())
    printPositions()


def backTrack(ligne):
    if lesReines.__len__() == tailleGrille:
        return True
    for i in range(0, tailleGrille):
        if estLibre(i):
            lesReines.append(i)
            if backTrack(ligne + 1):
                return True
            else:
                lesReines.remove(i)


def estLibre(val):
    res = True
    for i in range(0, lesReines.__len__()):
        if lesReines[i] == val:
            res = False
        if val == (lesReines[i] - (lesReines.__len__() - i)) or val == (lesReines[i] + (lesReines.__len__() - i)):
            res = False
    return res


def printPositions():
    grille = [[0] * tailleGrille for i in range(tailleGrille)]
    output = ""
    it = 0
    for i in lesReines:
        grille[it][i] = 1
        it = it + 1

    for i in range(tailleGrille):
        for j in range(tailleGrille):
            if grille[i][j] == 1:
                output = output + " ♛ "
            else:
                output = output + " _ "
        output = output + "\n"
    print(output)


if __name__ == "__main__":
    main()
