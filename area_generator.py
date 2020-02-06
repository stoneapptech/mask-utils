import json

with open("area_tmp.json", encoding='utf8') as f:
    data = json.load(f)

result = {}
cnt = 0

code = {
  "臺北市": "A",
  "臺中市": "B",
  "基隆市": "C",
  "臺南市": "D",
  "高雄市": "E",
  "新北市": "F",
  "宜蘭縣": "G",
  "桃園市": "H",
  "嘉義市": "I",
  "新竹縣": "J",
  "苗栗縣": "K",
  # "臺中縣": "L",
  "南投縣": "M",
  "彰化縣": "N",
  "新竹市": "O",
  "雲林縣": "P",
  "嘉義縣": "Q",
  # "臺南縣": "R",
  # "高雄縣": "S",
  "屏東縣": "T",
  "花蓮縣": "U",
  "臺東縣": "V",
  "金門縣": "W",
  "澎湖縣": "X",
  # "陽明山": "Y",
  "連江縣": "Z"

}

for k in code.keys():
    tmp = {
        "name": k,
        "town": {}
    }
    result[code.get(k)] = tmp

for city in data.keys():
    c = code.get(city)
    ts = data.get(city)
    cnt += len(ts)
    print(city, len(ts))
    for i, t in enumerate(ts):
        i_str = str(i+1)
        if len(i_str) == 1:
            i_str = "0" + i_str
        result.get(c).get("town")[i_str] = t
		
print(cnt)

with open("area_id.json", "w", encoding='utf8') as n:
    json.dump(result, n, ensure_ascii=False, indent=2)
