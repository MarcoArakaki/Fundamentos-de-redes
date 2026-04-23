def vol(raio):
    return (4/3) * 3.14 * (raio ** 3)

def teste():
    raios = [1, 2, 3, 5, 10]
    for r in raios:
        v = vol(r)
        print(f"Raio = {r} -> Volume = {v:.2f}")
teste()