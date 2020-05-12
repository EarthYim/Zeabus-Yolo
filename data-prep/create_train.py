import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input', help='input file')
args = vars(ap.parse_args())
path = = args['input']

obj = open(path).read().split("\n")
file = open('train.txt', 'w')
mem = []
for i in range(len(obj)-1):
    img = obj[i].split(",")
    filename = img[0].split("/")[1]
    print(filename)
    if filename in mem:
        print(filename + "double")
        continue
    file.write('data/obj/'+filename+"\n")
    mem.append(filename)
file.close()
