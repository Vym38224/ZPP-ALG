#skládání funkcí
def get_square(x):
    return x * x
def sum_square(x, y):
    return get_square(x) + get_square(y)

#get_last_digit(123)
def get_last_digit(number):
    return number % 10

#remove_last_digit(123)
def remove_last_digit(number):
    return number // 10

#vrátí předposlední cifru čísla 124
def get_butlast_digit(x):
    return (x // 10) % 10

#vrátí předpředposlední cifru čísla (jakoby první u trojciferného)
def get_butbutlast_digit(x):
    return get_butlast_digit(remove_last_digit(x))

#append_digit(10?)
def append_digit(number, digit):
    return (number * 10) + digit

#get_first_digit(123)
def get_first_digit(x):
    return x // 100

#utvoř trojciferné číslo (1, 2, 5)
def make_number(x, y, z):
    return append_digit(append_digit(x, y), z)

#prohoď cifry trojciferného čísla 157 => 751
def reverse_digits(x):
    return make_number(get_last_digit(x),
                       get_butlast_digit(x),
                       get_butbutlast_digit(x))

#úkol: převod nezáporného čísla menšího než 32 do dvojkové soustavy a zpět (5 => 101)
def number_to_binary(x):
    if x > 0 and x <= 32:
        return(bin(x)[2:])
    else:
        print("Neplatné číslo")

#predikát = fce vždy vracející logickou hodnotu
def is_even1(x):
    return (x % 2) == 0

#úkol:napiš funkci is_nonzero_divisor - napište predikát, který rozhodne, zda nenulové číslo dělí jiné číslo
def is_nonzero_divisor(x, y):
    return (y % x) == 0

#fce is_even s využitím is_nonzero_divisor
def is_even2(x):
    if is_nonzero_divisor(2, x) == True:
        return True
    else:
        return False

#rozhodnout, zda tři čísla tvoří pythagorejskou trojici. (ex. 3, 4, 5 => True)
def pythagoras(a=3,b=4,c=5):
    if a!=0 and b!= 0 and c!= 0 and a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False

#napište funkci, která vrátí absolutní hodnotu čísla
def absolute_value(x):
    if x >= 0:
        return x
    else:
        return -x

#rozhodněte dělitelnost čísel (ex. (2, 4) => True; (3, 4) => False)
def is_divisible(x, y):
    if (y % x) == 0:
        return True
    else:
        return False

#pomocná fce pro rovnoramenný trojúhelník - může to být trojúhelník
def is_triangle(x, y, z):
    if ((x + y) > z and (y + z) > x and (z + x) > y):
        return True
    else:
        return False

#rozhodněte, zda je trojúhelník rovnoramenný
    #hm something wrong here
def is_triangle_isosceles(x, y, z):
    if (((x == y) and (x != z)) or (x != y and x == z) or (y == z and x != y) or (x == y and x == z)) and (is_triangle(x, y, z) == True):
        return True
    else:
        return False
    
