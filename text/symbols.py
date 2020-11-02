from text import cmudict

_pad        = '_'
_punctuation = '!\'(),.:;? '
_special = '-'
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГҐДЄЕЁЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгґдєеёжзиіїйклмнопрстуфхцчшщъыьэюя'
			
_arpabet = ['@' + s for s in cmudict.valid_symbols]

symbols = [_pad] + list(_special) + list(_punctuation) + list(_letters) + _arpabet
