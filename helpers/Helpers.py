def imc(weight=0, height=0):
    if (weight and height):
        return weight / (height ** 2)
    return 0