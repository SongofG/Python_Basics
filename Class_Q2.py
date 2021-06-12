## Q2)
from Class_Q1 import Friend

def main():
    f1 = Friend('윤지민', '010-111-222')
    f2 = Friend('이선준', '010-333-444')
    f3 = Friend('장지우', '010-555-666')
    f4 = Friend('윤지율', '010-777-888')
    people = [f1, f2, f3, f4]

    for i in range(len(people)):
        print(people[i].get_name(), '    ', people[i].get_phone())

    print('\nQueston2')

    for  i in range(len(people)):
        if people[i].get_name().startswith('윤'):
            print(people[i].get_name(), '    ', people[i].get_phone())
    
    print('\nQuestion3')
    for i in people:
        if i.get_name() == '장지우':
            i.set_phone('010-999-999')

    for i in people:
        if i.get_name() == '장지우':
            print(i.get_name(), '    ', i.get_phone())

main()
