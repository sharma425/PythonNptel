import csv
with open('countries.csv','r') as f:
    reader = csv.reader(f)
    flag=True
    for row in reader:
        if flag ==True:
            flag=False
            continue
        lang=float(row[1])
        lat=float(row[2])
        #print(row)
        print(lang,end=" ")
        print(lat)

    
