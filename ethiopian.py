
def hello():
    print("Good luck!")

def  ethiopian(numA,numB):
    """
    ethiopian
    두 수를 입력받아 ethiopian multiplication의 방법으로
    계산한 곱셈 결과를 반환
    """
    res=0
    while numA>0:     
        if numA%2==1:
            res+=numB
        numA=int(numA/2)
        numB*=2
    return res


if __name__=='__main__':
    hello()
    user_input=input('곱셈 결과를 알고자 하는 두 수를 입력하세요(공백으로 구분)')   
    [numA,numB]=map(int,user_input.split(' '))
    print(ethiopian(numA,numB))
