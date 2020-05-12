obj = open('data.csv').read().split("\n")

LABEL = {"gate":0, "flare":1}
for i in range(len(obj)-1):
    img = obj[i].split(",")
    filename = img[0].split("/")[1].split(".")[0]
    label = LABEL[img[-1]]
    w = (int(img[3]) - int(img[1]))/1936
    h = (int(img[4]) - int(img[2]))/1216
    x = ((int(img[3]) +  int(img[1]))/2)/1936
    y = ((int(img[4]) +  int(img[2]))/2)/1216

    txt = str(label) + " " + str(round(x,6)) + " " + str(round(y,6)) + " " + str(round(w,6)) + " " + str(round(h,6))
    file = open("txt_out/" + filename + '.txt', 'a')
    file.write(txt+"\n")
    file.close()


