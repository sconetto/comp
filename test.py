from collections import OrderedDict

def parse_sql():
    sql = input("Escreva o SQL: \n")
    keys = sql.split(' ')
    wh = []
    fr = []
    sel = []
    command = ''
    result = {}

    for word in keys:
        word = word.replace(',', '')
        word = word.replace(';', '')
        if word == 'SELECT':
            command = 'sel'
        elif word == 'FROM':
            command = 'fr'
        elif word == 'WHERE':
            command = 'wh'

        if command == 'sel' and word != 'SELECT':
            sel.append(word)
        elif command == 'fr' and word != 'FROM':
            fr.append(word)
        elif command == 'wh' and word != 'WHERE':
            if word != '':
                wh.append(word)

    if len(sel) is not 0:
        if len(fr) is not 0:
            result = {'SELECT': sel, 'FROM': fr}
    if len(wh) is not 0:
        result['WHERE'] = wh

    print(result)

if __name__ == '__main__':
    parse_sql()
