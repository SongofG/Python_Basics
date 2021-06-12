## OOP practice 2
class AgeInfo:
    def up_age(self):
        self.age += 1
    def get_age(self):
        return self.age

def main():
    fa = AgeInfo()
    fa.age = 20

    fa.up_age()
    AgeInfo().up_age(fa) # 바로 위의 코드와 똑같은 동작을 시행한다.
                         # 사실 line 12에 있는 코드를 컴퓨터가 line 13으로
                         # 바꿔서 시행하는 것이다!

    print(fa.get_age())
    print(AgeInfo().get_age(fa))

main()
