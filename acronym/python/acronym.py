import re

def acronymize(input):
    input = input.strip()
    words = re.split(f"[- ]+", input)
    acronym = [word[0].capitalize() for word in words]
    return ''.join(acronym)