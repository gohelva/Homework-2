from flask import Flask,abort
from flask import jsonify
from flask import request
from flask import json
import csv

app = Flask(__name__)

with open('/var/www/html/flaskapp/dailyweather.csv', 'rt') as csvfile:
    read = csv.reader(csvfile)
    list1 = list(read)
print(list1)
listall = []


totlen = len(list1)
@app.route('/historical/', methods=['GET'])
def Alldates():
    for x in list1:
        if (x[0] != "DATE"):
            listall.append(x[0])
    print(listall)
    alldates = []
    for x in listall:
        a ={"DATE":x}
        alldates.append(a)
    return json.dumps(alldates)

@app.route('/historical/<dateid>',methods=['GET'])
def info(dateid):
    data =  [x for x in list1 if dateid in x]
    if len(data)==0:
        return 404
    data2 = {"DATE":str(data[0][0]), "TMAX":float(data[0][1]), "TMIN":float(data[0][2])}
    return json.dumps(data3),200

@app.route('/historical/',methods=['POST'])
def addinfo():
    new = request.get_json(force=True)
    if new:
       DATE=str(new['DATE'])
       TMAX=float(new['TMAX'])
       new1=[]
       new1.append(DATE)
       new1.append(TMAX)
       new1.append(TMIN)
       list1.append(new1)
       with open('/var/www/html/flaskapp/dailyweather.csv', 'ab') as file:
           wrt = csv.writer(file)
           wrt.writerow(new1)
    return json.dumps({"DATE":DATE, "TMAX": TMAX, "TMIN": TMIN}),201

@app.route('/historical/<dateid>',methods=['DELETE'])
def deleteinfo(dateid):

    return jsonify("The date has been deleted"),200
@app.route('/forecast/<dateid>',methods=['GET'])
def forecast(dateid):
    count=0
    send = []
    fore = []
    tot = len(list1)
    print(tot)
    for x in list1:
        count = count + 1
        if(x[0] == dateid ):
            break
    print(count)
    if(abs(count-tot)>=6):
        for y in range(count-1,count+6):
            print(y)
            m = {"DATE":list1[y][0], "TMAX":float(list1[y][1]),"TMIN":float(list1[y][2])}
            fore.append(m)
        send = fore

    else:
        foreca = []
        foreca1 =[]
        final = []
        final1 = []
        for z in range(count-3,count):
            foreca.append(list1[z])
        print(foreca)
        if(count == tot):
            count2 = len(foreca)
            for d in range(6):
                tmax2 = (float(foreca[count2 - 1][1]) + float(foreca[count2 - 2][1]) + float(foreca[count2 - 3][1])) / 3
                tmax2 = round(tmax2, 2)
                tmin2 = (float(foreca[count2 - 1][2]) + float(foreca[count2 - 2][2]) + float(foreca[count2 - 3][2])) / 3
                tmin2 = round(tmin2, 2)
                date2 = int(foreca[count2 - 1][0]) + 1
                g = [date2,tmax2,tmin2]
                foreca.append(g)
                count2  =count2 +1
            for b in range(2,len(foreca)):
                o = {"DATE": str(foreca[b][0]), "TMAX":float(foreca[b][1]),"TMIN":float(foreca[b][2])}
                foreca1.append(o)
            print(foreca1)

            return jsonify(foreca1),200
        if(count!=tot):
            for a in range(count-1,tot):
                final.append(list1[a])
        count1 = len(final)
        print(final)
        print(count1)
        for b in range(7-count1):
            print(b)
            tmax1 = (float(final[count1-1][1])+ float(final[count1-2][1])+float(final[count1-3][1]))/3
            tmax1 = round(tmax1,2)
            tmin1 = (float(final[count1-1][2]) + float(final[count1 -2][2]) + float(final[count1 - 3][2])) / 3
            tmin1 = round(tmin1,2)
            date1 = int(final[count1-1][0]) + 1
            m = [date1,tmax1,tmin1]
            final.append(m)
            foreca.append(m)
            count1 = count1 + 1
        for x in range(len(final)):
            print(x)
            n = {"DATE": str(final[x][0]), "TMAX": float(final[x][1]), "TMIN": float(final[x][2])}
            final1.append(n)
            send =final1
        print(foreca)
        print(final)
        print(final1)
    return jsonify(send),200

if __name__ == '__main__':
 app.run()
