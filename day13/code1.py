f =open('input.txt', 'r')
# f = open('sample.txt', 'r')
total = 0
while True:
    a = f.readline()
    if not a:
        break
    b = f.readline()
    prize = f.readline()
    # print(a[a.find("+")+1:a.find(",")])
    x1 = int(a[a.find("+")+1:a.find(",")])
    x2 = int(b[b.find("+")+1:b.find(",")])
    y1 = int(a[a.rfind("+")+1:])
    y2 = int(b[b.rfind("+")+1:])
    xp = 10000000000000 + int(prize[prize.find("=")+1:prize.find(",")])
    yp = 10000000000000 + int(prize[prize.rfind("=")+1:])

    try:
        bpresses = (yp-((y1*xp)/(x1)))/(y2-((y1*x2)/x1))
        apresses = (xp-x2*bpresses)/x1
    except Exception as e:
        print(" exception!" + e)
        input()
        continue
    # print(f"{bpresses}, {round(bpresses)}, {apresses}, {round(apresses)}")
    # if round(bpresses)*x2+round(apresses)*x1 == xp and round(bpresses)*y2+round(apresses)*y1 == yp:
    if abs(round(bpresses)-bpresses)<.01 and abs(round(apresses)-apresses)<.01:
        # if apresses > 100 or bpresses>100:
            # print(f"confused! {apresses}, {bpresses}")
        total+=3*round(apresses) + round(bpresses)
        # print(prize)
    _ = f.readline()
print(total)
