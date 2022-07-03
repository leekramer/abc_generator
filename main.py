def abc_generator(_start='A', _stop='Z') -> str:  # [A:65 - Z:90] oder [a:97 - z:122]
    # Wenn leere Angaben gemacht werden, dann Standard-Buchstaben zuweisen
    if _start == '':
        _start = 'A'

    if _stop == '':
        _stop = 'Z'

    # [1.] Nimm nur den Anfangsbuchstaben
    # [2.] Wechsel von Buchstabe auf Zahl
    start = ord(_start[0])
    stop  = ord(_stop[0])

    # Ist [stop] innerhalb des Alphabets? Sonst Standard-Buchstaben zuweisen
    if 65 <= stop <= 90:  # [A - Z]
        pass

    elif 97 <= stop <= 122:  # [a - z]
        pass

    else:
        stop = 90

    # [1.] Ist [start] innerhalb des Alphabets? Sonst Standard-Buchstaben zuweisen
    # [2.] Ist [stop] im selben Alphabet? Sonst verschiebe [stop] in den Bereich von [start]
    if 65 <= start <= 90:  # [A - Z]
        if 97 <= stop <= 122:
            stop = stop - 32

    elif 97 <= start <= 122:  # [a - z]
        if 65 <= stop <= 90:
            stop = stop + 32

    else:
        start = 65

    # Iteriere von [start] nach [stop]
    if start <= stop:
        while start <= stop:
            yield chr(start)
            start += 1

    elif stop <= start:
        while start >= stop:
            yield chr(start)
            start -= 1


# >>> Beispiele <<<

# Standard ohne Angaben
print([x for x in abc_generator()])

# Nur _start Angabe
print([x for x in abc_generator(_start='X')])

# Umgekehrte Ausgabe von Z nach A(Nur der Anfangsbuchstabe wird herangezogen!)
print([x for x in abc_generator(_start='Zebra', _stop='Affe')])

# Umgekehrte Ausgabe von I nach B
print([x for x in abc_generator(_start='I', _stop='D')])

# _start gibt den alphabetischen Bereich vor(Bereich Groß- oder Kleinschreibung)
print([x for x in abc_generator(_start='a', _stop='F')])
