import shutil
import os

absp = os.path.abspath('.')
p1 = absp+'\\static\\image'
p2 = absp+'\\static\\json'

shutil.rmtree(p1)
os.mkdir(p1)
shutil.rmtree(p2)
os.mkdir(p2)



x = [[0,0],[200,200],[0,50],[200,50],[0,70],[200,70],[0,90],[200,90],[0,90],[350,90],[0,110],[350,110],[0,130],[350,130],[0,150],[350,150],[0,170],[350,170],[0,190],[350,190],[0,210],[350,210],[0,230],[350,230]]

for i in range(len(x)//2):
    # print(x[2*i])
    # print(x[2*i+1])
    if i == 0:
        xm = "0"
    elif i > 0 and i < 4:
        xm = "1"
    else:
        xm = "2"
    x1 = str(x[2*i][0])
    x2 = str(x[2*i+1][0])
    y1 = str(x[2*i][1])
    y2 = str(x[2*i+1][1])

    print("lines.addLine(" + xm+",["+x1+","+x2+"],["+y1+","+y2+"])")