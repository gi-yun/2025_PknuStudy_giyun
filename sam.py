import sys 
class Data:
    import requests as req
    def __init__(self,name):    
        self.name=sys.argv[1]
        self.url="https://finance.naver.com/sise/sise_market_sum.naver"
        self.web = self.req.get(self.url)
        self.html = self.web.text
        self.f1 =self.html.find(self.name)
    def Sam(self):
        print(self.html[self.f1:self.f1+100])
        return f'{self.name}\n{self.html[self.f1:self.f1+100][19:50].replace('<td class="number">',"").replace('<td class="number">',"").replace('</td>',"원")}'
dd = Data(sys.argv[1])
print(dd.Sam())
if __name__ == "__main__":
    print("전 파일로 실행이 되었어요.")
else:
    print("전 모듈로 임포트 되었어요.")