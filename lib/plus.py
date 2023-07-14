import os

def sum_numbers_from_file(file):
    total = 0
    for line in file:
        try:
            number = float(line)
            total += number
        except ValueError:
            # 예외 처리: 숫자로 변환할 수 없는 줄은 건너뜁니다.
            continue
    return total

# 텍스트 파일 경로를 지정하여 함수를 호출합니다.

if __name__ == '__main__':
    file_path = './data/data.txt'  # 실제 파일 경로로 변경해야 합니다.
    with open(file_path, 'r') as file:
        result = sum_numbers_from_file(file)
    print("숫자의 총합:", result)