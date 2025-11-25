def split_before_each_uppercases(formula):
    parts = []
    current = ""
    for c in formula:
        if c.isupper() and current:
            parts.append(current)
            current = c
        else:
            current += c
    if current:
        parts.append(current)
    return parts
    
def split_at_first_digit(formula):
    for i, c in enumerate(formula):
        if c.isdigit():
            return formula[:i], formula[i:]
    return formula
