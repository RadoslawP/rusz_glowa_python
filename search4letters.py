def search4vowels(phrase:str) -> set:
    """Zwaca samogłoski znalezione we frazie podanej jako argument."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def search4letters(phrase:str, letters:str) -> set:
    """Zwraca zbiór liter ze zmiennej letters znalezionych w zmiennej phrase."""
    return set(letters).intersection(set(phrase))
