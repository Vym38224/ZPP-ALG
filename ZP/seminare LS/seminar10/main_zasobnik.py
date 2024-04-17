import zasobnik

z1 = zasobnik.vytvor_zasobnik()
zasobnik.pridej_do_zasobniku(z1, "world")
zasobnik.pridej_do_zasobniku(z1, "Hello")
z2 = zasobnik.vytvor_zasobnik()
zasobnik.pridej_do_zasobniku(z2, "fist")
zasobnik.pridej_do_zasobniku(z2, "second")

print(zasobnik.odeber_ze_zasobniku(z1))
print(zasobnik.odeber_ze_zasobniku(z1))
print(zasobnik.odeber_ze_zasobniku(z2))
print(zasobnik.odeber_ze_zasobniku(z2))

print(zasobnik.odeber_ze_zasobniku(z1))
print(zasobnik.odeber_ze_zasobniku(z2))