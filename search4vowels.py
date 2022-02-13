def search4vowels(phrase:str) -> set:
    """Wyświetla samogłoski znalezione w słowie podanym jako argument."""
    vowels = set('aeiou')
    found = vowels.intersection(set(phrase))
    return found
