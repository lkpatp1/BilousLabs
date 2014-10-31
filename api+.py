import urllib.request, time, sys, json, csv
day=input('введіть день закінчення:')
api_file=open('d:/Google Drive/Python/api_file.txt', 'r')
api=api_file.read()
api=api.split(';\n')

while int(time.ctime()[8:10])!=int(day):
    for i in range(len(api)):
    
        f=open('d:/Google Drive/Python/bus_table.csv', 'a')
        url=api[i]
        rout_number=api[i].replace('http://api.atp1.lviv.ua/atp1/buses?line=','')
        requesturl=urllib.request.Request(url)
        openurl=urllib.request.urlopen(requesturl)
        readurl=str(openurl.read())
        t=str(time.ctime())
        without_b=readurl.replace('b','')
        without_slash=without_b.replace("\'","")
        all_list=json.loads(without_slash)
        direction_0_keys=list(all_list[0].keys())
        direction_1_keys=list(all_list[1].keys())
        bacis_table_0=[]
        bacis_table_1=[]
        kor_0=len(direction_0_keys)
        kor_1=len(direction_1_keys)
        
        for i in range(kor_0):
            bacis_table_0.append(direction_0_keys[i])
            bacis_table_0[i]=t,rout_number,0,direction_0_keys[i],float(all_list[0][direction_0_keys[i]][0]),float(all_list[0][direction_0_keys[i]][1])
            f.write(str(bacis_table_0[i]).replace('(','').replace(')','')+'\n')
        for i in range(kor_0,kor_0+kor_1):
            bacis_table_0.append(direction_1_keys[i-kor_0])
            bacis_table_0[i]=t,rout_number,1,direction_1_keys[i-kor_0],float(all_list[1][direction_1_keys[i-kor_0]][0]),float(all_list[1][direction_1_keys[i-kor_0]][1])
            f.write(str(bacis_table_0[i]).replace('(','').replace(')','')+'\n')
                      
        #f.writelines(str(bacis_table_0))
        f.close()
    #print(bacis_table_0,bacis_table_1)
    time.sleep(12)
