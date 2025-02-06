import requests
import json
url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=ahHMWEL1Yo4F0ABAqJyLXdrTJm30X8FL&searchdate=20250205&data=AP01' 
res = requests.get(url).text
data = json.loads(res)
result = data[-1]['deal_bas_r']

#스트링을 숫자로 바꾸어라. 단 쉽표는 전처리하여 사용가능하게 하라.
# test = float(result.replace(",",""))
# print(f'{test:,} , {type(test)}')

# print("="*10)
#선생님이 준 답안
test2 = result.replace(",","").replace(".","")
# print(test2,type(test2))
exc = int(test2)/10
print("="*40)
print(f'오늘의 환율은 1달러에 {exc:,} 원 입니다. ')
print("="*40)