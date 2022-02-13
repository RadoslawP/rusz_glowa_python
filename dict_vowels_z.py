def search4vowels(word:str) -> set:
    """Wyświetla samogłoski znalezione w słowie podanym jako argument."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return found

search4vowels()
