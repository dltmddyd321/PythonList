dan = int(input("단을 입력하시오 : "))

def show(message):
    print(message)

for i in range(1,10) :
    message = "{} * {} = {}".format(dan, i, dan*i)
    show(message)

