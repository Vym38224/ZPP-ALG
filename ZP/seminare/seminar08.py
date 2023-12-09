text = "Prvkem seznamu."
text = text.lower()
znaky_seznam = []

for znak in text:
    nalezen = False
    for item in znaky_seznam:
        if item[0] == znak:
            item[1] += 1
            nalezen = True
            break
    if not nalezen:
        znaky_seznam.append([znak, 1])


for item in znaky_seznam:
    print(f"{item[0]}: {item[1]}x")