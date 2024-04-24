import matice_txt_IO

M = [[1, 2, 3], [4, 5, 6], [7, 8, 555]]
matice_txt_IO.uloz_matici("ZP/seminare LS/seminar10/matice.txt", M)
nactena_matice = matice_txt_IO.nacti_matici("ZP/seminare LS/seminar10/matice.txt")
print(nactena_matice)