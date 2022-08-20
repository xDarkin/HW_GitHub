
m = str("Любіть Україну, як сонце любіть, як вітер, і трави, і води... "
        " В годину щасливу і в радості мить, любіть у годину негоди. "
        " Любіть Україну у сні й наяву, вишневу свою Україну, красу її, "
        " вічно живу і нову, і мову її солов'їну. Без неї — ніщо ми, як порох і дим, "
        " розвіяний в полі вітрами... Любіть Україну всім серцем своїм і всіми своїми ділами.")
m = m.replace(",", "")
m = m.replace(".", "")
m = m.replace("—", "")
m = m.lower()
m = m.split()
dict_m = dict.fromkeys(m, 0)

for i in dict_m:
    dict_m[i] = m.count(i)

max_m = max(dict_m.values())
min_m = min(dict_m.values())

for k, v in dict_m.items():
    if v == max_m:
        print(k, "=", max_m)

for k, v in dict_m.items():
    if v == min_m:
        print(k, "=", min_m)
