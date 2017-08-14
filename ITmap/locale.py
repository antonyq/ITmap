from json import load


def localize(file_name, language):
    with open(f'../static/locale/{language}/{file_name}.json', encoding='utf8') as data_json:    
        return load(data_json)