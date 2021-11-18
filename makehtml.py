import os 

print(os.path.isfile("html_test.html")) 

file = open('html_test.html','w',encoding='UTF-8') 

file.write('''<html><head><title>테스트 타이틀</title></head><body> <b style='font-size: 13.3333px;'>★★★&nbsp;</b><b>테스트 하기. ★★★</b></p></body></html>''') 

file.close()


