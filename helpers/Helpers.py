def imc(weight=0, height_cm=0):
    if weight and height_cm:
        height_m = height_cm / 100
        return round((weight / (height_m ** 2)), 2)
    return 0
