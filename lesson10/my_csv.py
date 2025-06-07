import csv
with open('個股日成交資訊.csv',encoding='utf-8',newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    stacks:list[dict] = list(reader)

   # 印出 stacks 串列中的資料筆數
#print(f"stacks 中共有 {len(stacks)} 筆資料。")


#import csv
#with open('個股日成交資訊.csv',encoding='utf-8',newline='') as csvfile:
#    reader = csv.reader(csvfile)
#    next(reader)
#    stacks:list[list] = list(reader)
print(stacks)