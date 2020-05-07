# def readList():
#     hakbunlist = []
#     namelist = []
#     korlist = []
#     englist = []
#     mathlist = []
class Student:
    def __init__(self):
        self.hakbun = []
        self.name = []
        self.kor = []
        self.eng = []
        self.math = []
        self.tot = []
        self.avg = []
        self.grade = []

    def getScore(self):
        hakbunlist = []
        namelist = []
        korlist = []
        englist = []
        mathlist = []
        flag = True;
        print("프로그램을 종료하려면 학번에 '0'을 입력하세요")
        while flag:
            hakbun = input("학번을 입력하세요: ")
            if hakbun == '0':
                flag = False
            else:
                name = input("이름을 입력하세요: ")
                kor = int(input("국어점수를 입력하세요: "))
                eng = int(input("영어점수를 입력하세요: "))
                math = int(input("수학점수를 입력하세요: "))

                hakbunlist.append(hakbun)
                namelist.append(name)
                korlist.append(kor)
                englist.append(eng)
                mathlist.append(math)

        return hakbunlist, namelist, korlist, englist, mathlist


    def calList(korlist, englist, mathlist):
        totlist = []
        avglist = []
        haksjumlist = []
        total = 0
        avg =0.0

        for i in range(len(korlist)):
            total = korlist[i] + englist[i] + mathlist[i]
            avg = total / 3.0
            totlist.append(total)
            avglist.append(avg)
            if avg >= 90:
                grade = 'A'
            elif avg >= 80:
                grade = 'B'
            elif avg >= 70:
                grade = 'C'
            elif avg >= 60:
                grade = 'D'
            else:
                grade = 'F'
            haksjumlist.append(grade)

        return totlist, avglist, haksjumlist

# def printList(hakbunlist, namelist, korlist, englist, mathlist, totlist,avglist, haksjumlist):
#     print("=" * 70)
#     print("  번호\t이름\t국어\t영어\t수학\t총점\t평균\t학점")
#     print("=" * 70)
#     for i in range(len(hakbunlist)):
#         print("%3s\t%5s\t%3d\t%3d\t%3d\t%3d\t%.2f\t%s"%(hakbunlist[i], namelist[i], korlist[i], englist[i], mathlist[i], totlist[i], avglist[i], haksjumlist[i]))
#
# def main():
#     hakbunlist, namelist, korlist, englist, mathlist = readList()
#     totlist, avglist, haksjumlist = calList(korlist, englist, mathlist)
#     printList(hakbunlist, namelist, korlist, englist, mathlist, totlist, avglist, haksjumlist)
# if __name__ == "__main__":
#     main()

result =