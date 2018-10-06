#!/usr/bin/env python3
# Soubor:  caesar.py
# Datum:   02.10.2018 00:36
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
############################################################################
import unicodedata
from sys import argv, stdin, stdout, stderr


PISMENA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

try:
    KLIC = int(argv[1])
except IndexError:
    stderr.write(argv[0])
    stderr.write(': CHYBA: Jak parametr musíš zadat klíč!\n\n')
    exit(2)
except ValueError:
    stderr.write(argv[0])
    stderr.write(': CHYBA: Klíč je celé číslo!.\n\n')
    exit(3)

if stdin.isatty():
    print('Zadej text a ukonči ho Ctrl+D. (Ve Widlích Ctrl+Z)')
text = stdin.read()

text = ''.join(text.split())
text = unicodedata.normalize('NFD', text).upper()\
        .encode('ascii', 'ignore').decode('ascii')

if len(argv) > 2:
    print()
    print(text)
    print()

for c in text:
    try:
        i = PISMENA.index(c)
    except ValueError:
        continue
    stdout.write(PISMENA[(i + KLIC) % len(PISMENA)])
print()
