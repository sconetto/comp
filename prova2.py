import ox

lexer = ox.make_lexer([
    ('SEL', r'SELECT|select'),
    ('FR', r'FROM|from'),
    ('WH', r'WHERE|where'),
    ('OP', r'((<>|(<|>)(=)?)|=)'),
    ('WRD', r'[a-z]+')
])

parser = ox.make_parser([
    ('select : ', lambda x, select: li.append(x)),
    ('from : ', lambda x, li: li.append(x)),
    ('where : ', lambda x, li: li.append(x)),
    ('command : WH', ),
    ('command : FR', ),
    ('command : SEL', ),
    ('value : WRD', lambda x: str(x)),
], ['SEL', 'FR', 'WH', 'OP', 'WRD'])


in = input("Escreva o SQL: \n")
