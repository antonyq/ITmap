@register.filter(name='joinby')
def joinby(value, arg):
    return arg.join(value)

@register.filter(name='in')
def inside(value, arg):
    return value in arg