import zasobnik

z1 = zasobnik.vytvor_zasobnik()
zasobnik.pridej_do_zasobniku(z1, 16)
zasobnik.pridej_do_zasobniku(z1, 65536)
zasobnik.pridej_do_zasobniku(z1, 65535)
zasobnik.pridej_do_zasobniku(z1, 3)
zasobnik.pridej_do_zasobniku(z1, -3)


print(zasobnik.odeber_ze_zasobniku(z1))
print(zasobnik.odeber_ze_zasobniku(z1))
print(zasobnik.odeber_ze_zasobniku(z1))