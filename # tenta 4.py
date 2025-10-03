res = []                    # Skapar en tom lista för resultatet
listan = [2, 4, 6]          # En lista med siffror
for i in listan:            # Loopar genom varje tal i listan
    res.append((i, i**3))   # Skapar en tuple med talet och dess kub och lägger till i resultatlistan
print(res)