# character issues

s = 'café'
print(len(s))
# 4
b = s.encode('utf8')
print(b)
# b'caf\xc3\xa9'
print(len(b))
# 5
print(b.decode('utf8'))
'café'

# byte essentials

cafe = bytes('café', encoding='utf_8')
print(cafe)
# b'caf\xc3\xa9'
print(cafe[0])  # one item
# 99
print(cafe[:1])  # sequence of one item inside it
# b'c'
cafe_arr = bytearray(cafe)
print(cafe_arr)
# bytearray(b'caf\xc3\xa9')
print(cafe_arr[-1:])
# bytearray(b'\xa9')

print(bytes.fromhex('31 4B CE A9'))
# b'1K\xce\xa9'

import array
numbers = array.array('h', [-2, -1, 0, 1, 2])  # h - short integers of 16 bits
octets = bytes(numbers)
print(octets)
# b'\xfe\xff\xff\xff\x00\x00\x01\x00\x02\x00'

# Structs and Memory Views

import struct
fmt = '<3s3sHH'
with open('filter.gif', 'rb') as fp:
     img = memoryview(fp.read())

header = img[:10] # bytes not copied
print(bytes(header))
# b'GIF89a+\x02\xe6\x00'
print(struct.unpack(fmt, header))
# (b'GIF', b'89a', 555, 230)  # type version width height
del header
del img

# even less byte copying would happen if I used the mmap module to open the image as a memory-mapped file.

# Basic Encoders/Decoders

for codec in ['latin_1', 'utf_8', 'utf_16']:
     print(codec, 'El Niño'.encode(codec), sep='\t')

# latin_1 b'El Ni\xf1o'
# utf_8   b'El Ni\xc3\xb1o'
# utf_16  b'\xff\xfeE\x00l\x00 \x00N\x00i\x00\xf1\x00o\x00'

# Understanding Encode/Decode Problems

# Coping with UnicodeEncodeError

city = 'São Paulo'
city.encode('utf_8')
# b'S\xc3\xa3o Paulo'
# city.encode('utf_16')
b'\xff\xfeS\x00\xe3\x00o\x00 \x00P\x00a\x00u\x00l\x00o\x00'
city.encode('iso8859_1')
# b'S\xe3o Paulo'
city.encode('cp437')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/.../lib/python3.4/encodings/cp437.py", line 12, in encode
#     return codecs.charmap_encode(input,errors,encoding_map)
# UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in
# position 1: character maps to <undefined>
city.encode('cp437', errors='ignore')
# b'So Paulo'
city.encode('cp437', errors='replace')
# b'S?o Paulo'
city.encode('cp437', errors='xmlcharrefreplace')
# b'S&#227;o Paulo'

# Coping with UnicodeDecodeError

# wrong codec

octets = b'Montr\xe9al'
octets.decode('cp1252')  # correct
# 'Montréal'
octets.decode('iso8859_7')  # wrong
# 'Montrιal'
octets.decode('koi8_r')  # wrong
# 'MontrИal'
octets.decode('utf_8')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 5:
# invalid continuation byte
octets.decode('utf_8', errors='replace')
# 'Montr�al'

# SyntaxError When Loading Modules with Unexpected Encoding

'''
If you load a .py module containing non-UTF-8 data and no encoding declaration, you get a message like this:

SyntaxError: Non-UTF-8 code starting with '\xe1' in file ola.py on line
  1, but no encoding declared; see http://python.org/dev/peps/pep-0263/
  for details
'''

# default encoding for Python 3 is UTF-8 across all platforms

# at top of file
# coding: cp1252
print('Olá, Mundo!')

# Python 3 allows non-ASCII identifiers in source code:

ação = 'PBR'  # ação = stock
ε = 10**-6    # ε = epsilon

# other languages need othe characters on source code to be readable

# How to Discover the Encoding of a Byte Sequence

# you can’t. You must be told

#  Chardet is a Python library
# $ chardetect 04-text-byte.asciidoc - cli tool
# 04-text-byte.asciidoc: utf-8 with confidence 0.99

u16 = 'El Niño'.encode('utf_16')
u16
# b'\xff\xfeE\x00l\x00 \x00N\x00i\x00\xf1\x00o\x00' - extra bytes say where encoding was done i.e. byte order mark

>>> u16le = 'El Niño'.encode('utf_16le')
>>> list(u16le)
[69, 0, 108, 0, 32, 0, 78, 0, 105, 0, 241, 0, 111, 0]
>>> u16be = 'El Niño'.encode('utf_16be')
>>> list(u16be)
[0, 69, 0, 108, 0, 32, 0, 78, 0, 105, 0, 241, 0, 111]

# bom not generated on be

# Handling Text Files

decode bytes on input
process pure str
encode text on output

so all you get from my_file.read() and pass to my_file.write(text) are str objects

>>> open('cafe.txt', 'w', encoding='utf_8').write('café')
4
>>> open('cafe.txt').read()  # default encoding Windows 1252 on windows, on unix it will be correct utf-8
'cafÃ©'

# hence use explicit

>>> fp = open('cafe.txt', 'w', encoding='utf_8')
>>> fp  1
<_io.TextIOWrapper name='cafe.txt' mode='w' encoding='utf_8'>
>>> fp.write('café')
4  2
>>> fp.close()
>>> import os
>>> os.stat('cafe.txt').st_size
5  3
>>> fp2 = open('cafe.txt')
>>> fp2  4
<_io.TextIOWrapper name='cafe.txt' mode='r' encoding='cp1252'>
>>> fp2.encoding  5
'cp1252'
>>> fp2.read()
'cafÃ©'  6
>>> fp3 = open('cafe.txt', encoding='utf_8')  7
>>> fp3
<_io.TextIOWrapper name='cafe.txt' mode='r' encoding='utf_8'>
>>> fp3.read()
'café'  8
>>> fp4 = open('cafe.txt', 'rb')  9
>>> fp4
<_io.BufferedReader name='cafe.txt'>  10
>>> fp4.read()  11
b'caf\xc3\xa9'

Encoding Defaults: A Madhouse
----------------------------
import sys, locale

expressions = """
        locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
    """

my_file = open('dummy', 'w')

for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30), '->', repr(value))

# linux and osx

# $ python3 default_encodings.py
#  locale.getpreferredencoding() -> 'UTF-8'
#                  type(my_file) -> <class '_io.TextIOWrapper'>
#               my_file.encoding -> 'UTF-8'
#            sys.stdout.isatty() -> True
#            sys.stdout.encoding -> 'UTF-8'
#             sys.stdin.isatty() -> True
#             sys.stdin.encoding -> 'UTF-8'
#            sys.stderr.isatty() -> True
#            sys.stderr.encoding -> 'UTF-8'
#       sys.getdefaultencoding() -> 'utf-8'
#    sys.getfilesystemencoding() -> 'utf-8'

# windows

'''
Z:\>chcp  1  # shows code package
Página de código ativa: 850
Z:\>python default_encodings.py  2
 locale.getpreferredencoding() -> 'cp1252'  3
                 type(my_file) -> <class '_io.TextIOWrapper'>
              my_file.encoding -> 'cp1252'  4
           sys.stdout.isatty() -> True      5
           sys.stdout.encoding -> 'cp850'   6
            sys.stdin.isatty() -> True
            sys.stdin.encoding -> 'cp850'
           sys.stderr.isatty() -> True
           sys.stderr.encoding -> 'cp850'
      sys.getdefaultencoding() -> 'utf-8'
   sys.getfilesystemencoding() -> 'mbcs'
'''

Z:\>python default_encodings.py > encodings.log
sys.stderr.isatty() -> False
sys.stdout.encoding -> cp1252

getfilesystemencoding - file names notcontents


Normalizing Unicode for Saner Comparisons
==----------------------------------------
>>> s1 = 'café'
>>> s2 = 'cafe\u0301'
>>> s1, s2
('café', 'café')
>>> len(s1), len(s2)
(4, 5)
>>> s1 == s2
False

Normalization Form C (NFC) composes the code points to produce the shortest equivalent string, while NFD decomposes, expanding composed characters into base characters and separate combining characters.

>> > from unicodedata import normalize
>> > s1 = 'café'  # composed "e" with acute accent
>> > s2 = 'cafe\u0301'  # decomposed "e" and acute accent
>> > len(s1), len(s2)
(4, 5)
>> > len(normalize('NFC', s1)), len(normalize('NFC', s2))
(4, 4)
>> > len(normalize('NFD', s1)), len(normalize('NFD', s2))
(5, 5)
>> > normalize('NFC', s1) == normalize('NFC', s2)
True
>> > normalize('NFD', s1) == normalize('NFD', s2)
True

# NFC - recommended for www

    >> > from unicodedata import normalize, name
    >> > ohm = '\u2126'
    >> > name(ohm)
    'OHM SIGN'
    >> > ohm_c = normalize('NFC', ohm)
    >> > name(ohm_c)
    'GREEK CAPITAL LETTER OMEGA'
    >> > ohm == ohm_c
    False
    >> > normalize('NFC', ohm) == normalize('NFC', ohm_c)
    True

# In the NFKC and NFKD forms, each compatibility character is replaced by a “compatibility decomposition” of one or more characters that are considered a “preferred” representation

>>> from unicodedata import normalize, name
>>> half = '½'
>>> normalize('NFKC', half)
'1⁄2'
>>> four_squared = '4²'
>>> normalize('NFKC', four_squared)
'42'
>>> micro = 'µ'
>>> micro_kc = normalize('NFKC', micro)
>>> micro, micro_kc
('µ', 'μ')
>>> ord(micro), ord(micro_kc)
(181, 956)
>>> name(micro), name(micro_kc)
('MICRO SIGN', 'GREEK SMALL LETTER MU')

# NFKC and NFKD normalization should be applied with care and only in special cases—e.g., search and indexing—and not for permanent storage, because these transformations cause data loss.

Case Folding
-------------

>>> micro = 'µ'
>>> name(micro)
'MICRO SIGN'
>>> micro_cf = micro.casefold()
>>> name(micro_cf)
'GREEK SMALL LETTER MU'
>>> micro, micro_cf
('µ', 'μ')
>>> eszett = 'ß'
>>> name(eszett)
'LATIN SMALL LETTER SHARP S'
>>> eszett_cf = eszett.casefold()
>>> eszett, eszett_cf
('ß', 'ss')

Utility Functions for Normalized Text Matching
----------------------------------------------
"""
Utility functions for normalized Unicode string comparison.

Using Normal Form C, case sensitive:

    >>> s1 = 'café'
    >>> s2 = 'cafe\u0301'
    >>> s1 == s2
    False
    >>> nfc_equal(s1, s2)
    True
    >>> nfc_equal('A', 'a')
    False

Using Normal Form C with case folding:

    >>> s3 = 'Straße'
    >>> s4 = 'strasse'
    >>> s3 == s4
    False
    >>> nfc_equal(s3, s4)
    False
    >>> fold_equal(s3, s4)
    True
    >>> fold_equal(s1, s2)
    True
    >>> fold_equal('A', 'a')
    True

"""

from unicodedata import normalize

def nfc_equal(str1, str2):
    return normalize('NFC', str1) == normalize('NFC', str2)

def fold_equal(str1, str2):
    return (normalize('NFC', str1).casefold() ==
            normalize('NFC', str2).casefold())

import unicodedata
import string


def shave_marks(txt):
    """Remove all diacritic marks"""
    norm_txt = unicodedata.normalize('NFD', txt)  1
    shaved = ''.join(c for c in norm_txt
                     if not unicodedata.combining(c))  2
    return unicodedata.normalize('NFC', shaved)  3

>>> order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
>>> shave_marks(order)
'“Herr Voß: • ½ cup of Œtker™ caffe latte • bowl of acai.”'  1
>>> Greek = 'Ζέφυρος, Zéfiro'
>>> shave_marks(Greek)
'Ζεφυρος, Zefiro'  2

def shave_marks_latin(txt):
    """Remove all diacritic marks from Latin base characters"""
    norm_txt = unicodedata.normalize('NFD', txt)  1
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:   2
            continue  # ignore diacritic on Latin base char
        keepers.append(c)                             3
        # if it isn't combining char, it's a new base char
        if not unicodedata.combining(c):              4
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved)   5

single_map = str.maketrans("""‚ƒ„†ˆ‹‘’“”•–—˜›""",  1
                           """'f"*^<''""---~>""")

multi_map = str.maketrans({  2
    '€': '<euro>',
    '…': '...',
    'Œ': 'OE',
    '™': '(TM)',
    'œ': 'oe',
    '‰': '<per mille>',
    '‡': '**',
})

multi_map.update(single_map)  3


def dewinize(txt):
    """Replace Win1252 symbols with ASCII chars or sequences"""
    return txt.translate(multi_map)  4


def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt))     5
    no_marks = no_marks.replace('ß', 'ss')          6
    return unicodedata.normalize('NFKC', no_marks)  7

>>> order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
>>> dewinize(order)
'"Herr Voß: - ½ cup of OEtker(TM) caffè latte - bowl of açaí."'  1
>>> asciize(order)
'"Herr Voss: - 1⁄2 cup of OEtker(TM) caffe latte - bowl of acai."'  2

Sorting Unicode Text
-----------------------
>>> fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
>>> sorted(fruits)
['acerola', 'atemoia', 'açaí', 'caju', 'cajá']

The standard way to sort non-ASCII text in Python is to use the locale.strxfrm function which, according to the locale module docs, “transforms a string to one that can be used in locale-aware comparisons.”

>>> import locale
>>> locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')
'pt_BR.UTF-8'
>>> fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
>>> sorted_fruits = sorted(fruits, key=locale.strxfrm)
>>> sorted_fruits
['açaí', 'acerola', 'atemoia', 'cajá', 'caju']

>>> import pyuca
>>> coll = pyuca.Collator()
>>> fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
>>> sorted_fruits = sorted(fruits, key=coll.sort_key)
>>> sorted_fruits
['açaí', 'acerola', 'atemoia', 'cajá', 'caju']

The Unicode Database
---------------------
import unicodedata
import re

re_digit = re.compile(r'\d')

sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'

for char in sample:
    print('U+%04x' % ord(char),                       1
          char.center(6),                             2
          're_dig' if re_digit.match(char) else '-',  3
          'isdig' if char.isdigit() else '-',         4
          'isnum' if char.isnumeric() else '-',       5
          format(unicodedata.numeric(char), '5.2f'),  6
          unicodedata.name(char),                     7
          sep='\t')

Dual-Mode str and bytes APIs
------------------------------
str Versus bytes in Regular Expressions
------------------------------------------
import re

re_numbers_str = re.compile(r'\d+')     1
re_words_str = re.compile(r'\w+')
re_numbers_bytes = re.compile(rb'\d+')  2
re_words_bytes = re.compile(rb'\w+')

text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"  3
            " as 1729 = 1³ + 12³ = 9³ + 10³.")        4

text_bytes = text_str.encode('utf_8')  5

print('Text', repr(text_str), sep='\n  ')
print('Numbers')
print('  str  :', re_numbers_str.findall(text_str))      6
print('  bytes:', re_numbers_bytes.findall(text_bytes))  7
print('Words')
print('  str  :', re_words_str.findall(text_str))        8
print('  bytes:', re_words_bytes.findall(text_bytes))    9

# str Versus bytes on os Functions
---------------------------------------

    >> > os.listdir('.')
    1
    ['abc.txt', 'digits-of-π.txt']
    >> > os.listdir(b'.')
    2
    [b'abc.txt', b'digits-of-\xcf\x80.txt']

'''
fsencode(filename)
Encodes filename (can be str or bytes) to bytes using the codec named by sys.getfilesystemencoding() if filename is of type str, otherwise returns the filename bytes unchanged.

fsdecode(filename)
Decodes filename (can be str or bytes) to str using the codec named by sys.getfilesystemencoding() if filename is of type bytes, otherwise returns the filename str unchanged.
'''

'''
>>> os.listdir('.')  1
['abc.txt', 'digits-of-π.txt']
>>> os.listdir(b'.')  2
[b'abc.txt', b'digits-of-\xcf\x80.txt']
>>> pi_name_bytes = os.listdir(b'.')[1]  3
>>> pi_name_str = pi_name_bytes.decode('ascii', 'surrogateescape')  4
>>> pi_name_str  5
'digits-of-\udccf\udc80.txt'
>>> pi_name_str.encode('ascii', 'surrogateescape')  6
b'digits-of-\xcf\x80.txt'
'''
