
# 원소 정보 리스트
elements = [
    ["수소[H]", "비금속원소", "전자를 공유하거나 하나를 얻음", "1주기 1족", "비금속성"],
    ["헬륨[He]", "비금속원소", "전자를 주고받지 않음", "1주기 18족", "비금속성"],
    ["리튬[Li]", "금속원소", "전자를 하나 버려 이온화함", "2주기 1족", "알칼리 금속"],
    ["베릴륨[Be]", "금속원소", "전자를 두 개 버려 이온화함", "2주기 2족", "금속성"],
    ["붕소[B]", "준금속원소", "전자를 공유하는 경향이 있음", "2주기 13족", "준금속성"],
    ["탄소[C]", "비금속원소", "전자를 공유하는 경향이 있음", "2주기 14족", "비금속성"],
    ["질소[N]", "비금속원소", "전자를 세 개 얻거나 공유함", "2주기 15족", "비금속성"],
    ["산소[O]", "비금속원소", "전자를 두 개 얻어 이온화함", "2주기 16족", "비금속성"],
    ["플루오린[F]", "비금속원소", "전자를 하나 얻어 이온화함", "2주기 17족", "할로젠"],
    ["네온[Ne]", "비금속원소", "전자를 주고받지 않음", "2주기 18족", "비금속성"],
    ["나트륨[Na]", "금속원소", "전자를 하나 버려 이온화함", "3주기 1족", "알칼리 금속"],
    ["마그네슘[Mg]", "금속원소", "전자를 두 개 버려 이온화함", "3주기 2족", "금속성"],
    ["알루미늄[Al]", "금속원소", "전자를 세 개 버려 이온화함", "3주기 13족", "금속성"],
    ["규소[Si]", "준금속원소", "전자를 공유하는 경향이 있음", "3주기 14족", "준금속성"],
    ["인[P]", "비금속원소", "전자를 세 개 얻거나 공유함", "3주기 15족", "비금속성"],
    ["황[S]", "비금속원소", "전자를 두 개 얻거나 공유함", "3주기 16족", "비금속성"],
    ["염소[Cl]", "비금속원소", "전자를 하나 얻어 이온화함", "3주기 17족", "할로젠"],
    ["아르곤[Ar]", "비금속원소", "전자를 주고받지 않음", "3주기 18족", "비금속성"],
    ["칼륨[K]", "금속원소", "전자를 하나 버려 이온화함", "4주기 1족", "알칼리 금속"],
    ["칼슘[Ca]", "금속원소", "전자를 두 개 버려 이온화함", "4주기 2족", "금속성"]
]

# 원소 특징을 출력하는 함수
def show_element(number, selected):
    print("\n", number, "번 원소의 특징 =>")

    for j in selected:
        if j == 1:
            print("이름:", elements[number - 1][0])
        elif j == 2:
            print("원소 종류:", elements[number - 1][1])
        elif j == 3:
            print("전자 특징:", elements[number - 1][2])
        elif j == 4:
            print("주기와 족:", elements[number - 1][3])
        elif j == 5:
            print("원소의 성질:", elements[number - 1][4])
        elif j == 6:
            print("이름:", elements[number - 1][0])
            print("원소 종류:", elements[number - 1][1])
            print("전자 특징:", elements[number - 1][2])
            print("주기와 족:", elements[number - 1][3])
            print("원소의 성질:", elements[number - 1][4])


# 프로그램 시작
print("=== 원소 특징 확인 프로그램 ===")

print("1. 이름")
print("2. 원소 종류")
print("3. 전자 특징")
print("4. 주기와 족")
print("5. 원소의 성질")
print("6. 전체 정보")

# 정보 선택
selected = []

try:
    choice = input("확인할 정보를 선택하세요 (예: 1,4): ")
    choices = choice.split(",")

    for i in choices:
        num = int(i)

        if num >= 1 and num <= 6:
            if num == 6:
                selected = [1, 2, 3, 4, 5]
                break
            elif num not in selected:
                selected.append(num)
        else:
            print("잘못된 선택입니다.")
    
    if len(selected) == 0:
        print("정보를 다시 선택해 주세요.")

    else:
        # 원자번호 입력
        for i in range(100):
            try:
                number = int(input("\n원자번호를 입력하세요 (1~20): "))

                if number >= 1 and number <= 20:
                    show_element(number, selected)
                    break
                else:
                    print("다시 선택해 주세요.")

            except ValueError:
                print("숫자를 입력해 주세요.")

except ValueError:
    print("잘못된 선택입니다. 프로그램을 다시 실행해 주세요.")
