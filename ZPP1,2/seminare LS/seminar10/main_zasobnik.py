import zasobnik

z1 = zasobnik.vytvor_zasobnik()
zasobnik.pridej_do_zasobniku(z1, "world")
zasobnik.pridej_do_zasobniku(z1, "Hello")

print(z1)
print(zasobnik.odeber_ze_zasobniku(z1))
print(z1)
print(zasobnik.odeber_ze_zasobniku(z1))
print(z1)


