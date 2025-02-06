# for x in ["도희", "도희", "소희"]: # 도희가 아닌 사람이 껴있다면 print 문은 실행되지 않음
#     if x != "도희":
#         break;
# else:
#     print("모두 도희군요")

# input = 10
# def find_prime_list_under_number(number):
#     prime_list = []
#     print("주어진 정수", number, "이하의 모든 소수를 찾아보겠습니다\n")
#     for n in range(2, number + 1): # 2부터 10까지의 수를 주어진 수 이하의 모든 소수를 반환해야 하기에
#         for i in range(2, n): # 소수는 자기 자신과 1 이외에는 나누어 떨어지지 않기 때문에 (1과 n=자기 자신 을 제외하여 검사)
#             print("\n주어진 정수: ", i)
#             print("소수인지 판단할 수: ", n)
#             print(n, "%", i, "=", n%i )
#             if n%i == 0: # 주어진 정수를 2부터 자기 자신 제외한 수로 나누어보며 나누어 떨어지는지 검사
#                 print(n, "가", i, "로 나누어 떨어지는군요.")
#                 print(n, "은 소수가 아닙니다.")
#                 break;
#         else:
#             print(n, "은 소수입니다.")
#             prime_list.append(n)
#     return prime_list
#
# result = find_prime_list_under_number(input)
# print(result)

"""
1. 소수는 자기 자신과 1 외에는 아무것도 나눌 수 없다
range 함수를 써서 2부터 number까지 반복문을 돌고
그리고 각 숫자를 n이라고 한다면, 2부터 n-1까지 n을 나눠본다
그 때까지 안 나누어 떨어진다면 바로 소수

2. 그러나 2와 3으로 나누어 떨어지지 않는다면, 2 X 3 인 6으로도 당연히 안 나누어 떨어짐
즉, 2부터 n-1 까지 모든 수 로 나누어 떨어지지 않는지 확인하는 것이 아니라
2부터 n-1 까지 모든 소수 로 나누어 떨어지지 않는지 알아보는게 효율적

3. 주어진 자연수 N이 소수이기 위한 필요충분 조건은 N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다는 것
수가 수를 나누면 몫이 발생하게 되는데 몫과 나누는 수, 둘 중 하나는 반드시 N의 제곱근 이하이기 때문
-> 11이 소수이려면 11이하의 소수인 7,5,3 으로도 나누어 떨어지면 안됨

"""
input = 20

def find_prime_list_under_number(number):
    prime_list = []

    for n in range(2, number + 1):
        for i in prime_list:
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)



