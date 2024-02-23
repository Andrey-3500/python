cid = str(input('Em que cidade você nasceu? '))

cid2 = cid.rstrip()

cid3 = cid2.lower()

cid4 = 'santo' in cid3[:5]

print(cid4)