import random
menu = ["구내식당","후문편의점","자가도시락","굶기","과자"]
lunch = random.choice(menu) # 기존의 리스트에서 랜덤값 뽑기
print(f'오늘 선택된 메뉴는? { {lunch} }')