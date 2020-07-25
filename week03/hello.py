professor_wizards = [
    {'name': '덤블도어', 'age': 116},
    {'name': '맥고나걸', 'age': 85},
    {'name': '스네이프', 'age': 60},
]


# 이번엔, 반복문과 조건문을 응용한 함수를 만들어봅시다.
# 마법사의 이름을 받으면, age를 리턴해주는 함수
def get_age(name, wizards):
    # wizards! 윗 줄 함수 선언에서 사용한 변수죠? 함수 사용하는 쪽에서 쓰는 변수명 아닙니다!  
    for wizard in wizards:
        if wizard['name'] == name:
            return wizard['age']
    return '해당하는 이름이 없습니다'


print(get_age('덤블도어', professor_wizards))
print(get_age('맥고나걸', professor_wizards))