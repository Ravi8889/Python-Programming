import csv
df1 =open("df.csv")
data_csv =csv.reader(df1)
lst_csv =list(data_csv)
print(lst_csv)

for i in lst_csv:
    print(i[0], '|',i[3]);
