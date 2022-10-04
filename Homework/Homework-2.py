print("2021741034 백종욱\n")

f = open("hw2.csv", 'r', encoding="utf-8-sig")

line = []

for i in f:
    line.append(i)

f.close

def slice(index):
    a = ','
    backup_index = 0
    slicedline = []

    for i in range(len(line[index])):
        if line[index][i] == a:
            slice = line[index][backup_index:i]
            backup_index = i + 1
            slicedline.append(slice)
    slicedline.append(line[index][backup_index:len(line[index]) - 1])

    return slicedline

def menu1():
    name = input("\n선수명을 입력하세요: ")

    IsExist = 0

    for i in range(len(line)):
        if name in line[i]:
            print("\n" + line[0] + line[i])
            IsExist += 1

    if IsExist == 0:
        print("\n그런 선수는 존재하지 않습니다\n")

def menu2():
    name = input("\n선수명을 입력하세요: ")

    IsExist = 0

    for i in range(len(line)):
        if name in line[i]:
            IsExist += 1
            player_idx = i

    if IsExist == 0:
        print("\n그런 선수는 존재하지 않습니다\n")

    else:
        player_list = slice(player_idx)

        details = input("\n특정항목을 입력하세요: ")

        details_list = slice(0)

        if details not in details_list:
            print("\n그런 항목은 존재하지 않습니다\n")

        else:
            for i in range(len(details_list)):
                if details == details_list[i]:
                    details_idx = i
      
            print("\n" + name, details, ":", player_list[details_idx] + "\n")

def menu3():
    details = input("\n특정항목을 입력하세요: ")

    details_list = slice(0)

    if details not in details_list:
            print("\n그런 항목은 존재하지 않습니다\n")

    else:
        dic = {}

        for i in range(len(details_list)):
            if details == details_list[i]:
                details_idx = i

        for i in range(1, len(line)):
            names = slice(i)[0]
            dic[names] = slice(i)[details_idx]

        print("\n" + slice(0)[0] + "   :   " + slice(0)[details_idx])

        sortdic = sorted(dic.items(), key = lambda x:x[1], reverse=True)
        for i in range(len(line) - 1):
            print(sortdic[i])

while True:    
    print("========MENU========\n")
    print("1번: 선수별 세부항목 출력\n")
    print("2번: 선수별 특정항목 출력\n")
    print("3번: 특정항목 내림차순 정렬\n")
    print("그 외: 프로그램 종료\n")
    print("========MENU========\n")

    menu = int(input("원하는 메뉴를 선택하세요: "))
    
    if menu == 1:
        menu1()

    elif menu == 2:
        menu2()

    elif menu == 3:
        menu3()

    else:
        print("\n프로그램을 종료합니다")
        break