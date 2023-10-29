def 팀의_승점과_득실차():
    점수 = 0
    득실차 = 0

    for match in range(1, 39):
        # 사용자로부터 경기 결과 입력 받기
        while True:
            result = input(f"경기 {match} 결과 입력 (W: 승, L: 패, D: 무승부): ")
            if result in ('W', 'L', 'D'):
                break
            else:
                print("올바른 입력이 아닙니다. 다시 입력하세요.")

        # 승점 및 득실차 계산
        if result == 'W':
            점수 += 3
        elif result == 'D':
            점수 += 1

        while True:
            팀의_득점 = input(f"경기 {match} 득점 수 입력: ")
            if 팀의_득점.isdigit():
                팀의_득점 = int(팀의_득점)
                break
            else:
                print("올바른 입력이 아닙니다. 숫자를 입력하세요.")

        while True:
            팀의_실점 = input(f"경기 {match} 실점 수 입력: ")
            if 팀의_실점.isdigit():
                팀의_실점 = int(팀의_실점)
                break
            else:
                print("올바른 입력이 아닙니다. 숫자를 입력하세요.")

        득실차 += (팀의_득점 - 팀의_실점)

    print(f"총 승점: {점수}")
    print(f"득실차: {득실차}")

팀의_승점과_득실차()




