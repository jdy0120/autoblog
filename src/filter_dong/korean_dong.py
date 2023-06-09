import csv
import json

def main():
  # csv 파일을 읽습니다.
  with open('./data/korean_dong_name.csv', 'r') as f:
      reader = csv.reader(f)
      next(reader)  # 헤더 행을 건너뜁니다.
      
      dataSet = set()

      data_list = []
      for row in reader:
        if row[3] == '':
          continue
        
        address = row[2] + ' ' + row[3]
        
        if (address in dataSet):
          continue
        
        dataSet.add(address)
        
        data = {
            'code': row[0],
            'address': address
        }
        data_list.append(data)

  # json 파일에 씁니다.
  with open('./data/korean_dong_name.json', 'w', encoding='utf-8') as f:
      json.dump(data_list, f, ensure_ascii=False, indent=4)
