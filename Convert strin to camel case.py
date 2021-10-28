def to_camel_case(text):
    if len(text) == 0:
        return text
    return  text[0] + text.replace('-',' ').replace('_',' ').title().replace(' ','')[1:]