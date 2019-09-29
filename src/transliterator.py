import sys

TRANSLIT_TABLE = {
"дя" : "ďa",
"тя" : "ťa",
"ня" : "ńa",
"ся" : "śa",
"де" : "ďə",
"те" : "ťə",
"не" : "ńə",
"се" : "śə",
"дю" : "ďu",
"тю" : "ťu",
"ню" : "ńu",
"сю" : "śu",
"дё" : "ďo",
"дё̄" : "ďō",
"тё" : "ťo",
"нё" : "ńo",
"сё" : "śo",
"а" : "a",
"б" : "b",
"в" : "w",
"г" : "g",
"д" : "d",
"е" : "jə",
"ё" : "jo",
"ж" : "ž",
"з" : "z",
"и" : "i",
"й" : "j",
"к" : "k",
"л" : "l",
"м" : "m",
"н" : "n",
"ӈ" : "ŋ",
"о" : "o",
"п" : "p",
"р" : "r",
"с" : "s",
"т" : "t",
"у" : "u",
"ф" : "f",
"ц" : "ts",
"ч" : "č",
"ш" : "š",
"ы" : "ɨ",
"э" : "ə",
"ю" : "ju",
"я" : "ja",
"h" : "h",
"х" : "h",
"." : "",
"," : "",
"?" : "",
"!" : ""
}


def transliterate(line, mode):
    line_result = ""
    prev_symbol = ""
    for symbol in line:
        new_symbol = None
        if prev_symbol != "":
            possible_symbol = (prev_symbol + symbol).lower()
            if possible_symbol in TRANSLIT_TABLE:
                new_symbol = TRANSLIT_TABLE[possible_symbol]
                line_result = line_result[:-1]
        if new_symbol is  None:
            new_symbol = TRANSLIT_TABLE.get(symbol.lower(), symbol.lower())
        line_result += new_symbol
        prev_symbol = symbol
    return line_result


def transliterate_file(filename, mode):
    filename_output = filename + '_out.txt'
    with open(filename_output, 'w', encoding='utf-8', newline='\r\n') as fout:
        with open(filename, 'r', encoding='utf-8') as fin:
            for line in fin:
                line_transliteration = transliterate(line.strip(), mode)
                fout.write(line_transliteration)
    print('written to %s' % filename_output)

if len(sys.argv) < 2:
    print('usage: transliterator <filename>')
else:
    filename = sys.argv[1]
    transliterate_file(filename, None)