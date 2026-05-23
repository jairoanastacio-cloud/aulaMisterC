temp = (36.5, 37.2, 38.0, 39.1)

for t in temp:
    if t < 37.5:
        vc = "normal"
    elif t <= 38.5:
        vc = "febre moderada"
    else:
        vc = "febre alta"

    print(f"Temperatura: {t}-C {vc}")