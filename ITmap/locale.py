from json import load


def localize(language, file_names):
    locales = []
    for name in file_names:
        with open(f'static/locale/{language}/{name}.json', encoding='utf8') as data_json:    
            locales.append(load(data_json))
    return locales