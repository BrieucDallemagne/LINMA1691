def comparer_fichiers_texte(fichier1, fichier2):
    try:
        with open(fichier1, 'r') as file1, open(fichier2, 'r') as file2:

            lines1 = file1.readlines()
            lines2 = file2.readlines()

        differences = []

        for i, (line1, line2) in enumerate(zip(lines1, lines2), 1):
            if line1 != line2:
                differences.append(f'Différence à la ligne {i}:\nFichier 1: {line1}\nFichier 2: {line2}')

        if len(lines1) > len(lines2):
            for i in range(len(lines2), len(lines1)):
                differences.append(f'Ligne en plus dans fichier 1 à la ligne {i + 1}: {lines1[i]}')
        elif len(lines2) > len(lines1):
            for i in range(len(lines1), len(lines2)):
                differences.append(f'Ligne en plus dans fichier 2 à la ligne {i + 1}: {lines2[i]}')

        if not differences:
            differences.append('Les fichiers sont identiques.')

        return differences

    except FileNotFoundError:
        return "Un ou les deux fichiers n'ont pas été trouvés."

fichier1 = 'tmp/output4.txt'
fichier2 = 'tests/output4.txt'
resultat = comparer_fichiers_texte(fichier1, fichier2)

for diff in resultat:
    print(diff)
