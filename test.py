def moyenne_notes(liste):
    """fait la moyenne des notes de l'élève

    Args:
        liste (list): la liste des notes du trimestre de l'élève
    """
    cpt_note = 0
    somme_note = 0
    if len(liste) != 0:
        for note in liste:
            cpt_note += 1
            somme_note += note
    
    if cpt_note != 0:
        moyenne = somme_note/cpt_note
    else :
        moyenne = None

    return moyenne

moyenne_notes([12, 18, 14, 16, 14])

def test_moyenne_notes():
    assert moyenne_notes ([12, 18, 14, 16, 14]) == 14.8
    assert moyenne_notes ([15, 13, 19, 15, 16]) == 15.6
    assert moyenne_notes ([]) == None