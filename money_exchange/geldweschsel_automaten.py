weschel_geld = 3.73
print("\n Geld zum Wechseln ist " f"{weschel_geld}")
münzen =[5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
for münze in münzen:
    if (float(weschel_geld) / float(münze)) >= 1:
        zuruckgeben_geld=float(münze)*int(float(weschel_geld)/float(münze))
        print(" > Sie bekommen " f"{(int(float(weschel_geld)/float(münze)))}" " von " f"{münze}" " Euro.")
        weschel_geld = round((float(weschel_geld)- zuruckgeben_geld), 2)