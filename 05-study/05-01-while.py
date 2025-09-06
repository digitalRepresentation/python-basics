treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무가 넘어갑니다.")

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 0
#while number != 4:
#    print(prompt)
#    number = int(input())

count = 0
while count < 3:
    print(f"카운트: {count}")
    count += 1
else:
    print("while 문이 정상 종료되었씁니다.")