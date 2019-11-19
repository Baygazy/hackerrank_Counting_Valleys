# Внутри def countingValleys(n, s):
z = s.upper().strip()
bylo_nije = 0
lvl = 0
gora = 0
for i in z:
    if i == "U":
        lvl += 1
        if bylo_nije > 0 and lvl == 0:
            gora += 1
            bylo_nije = 0
    else:
        lvl -= 1
        if lvl < 0:
            bylo_nije += 1
return gora
# Внутри def countingValleys(n, s):