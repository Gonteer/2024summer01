score = []
#입력부분
for i in range(1,6) :
    name = input(str(i)+'번째 학생 이름:')
    s1 = int(input(name+'의 국어 성적 : '))
    s2 = int(input(name+'의 수학 성적 : '))
    s3 = int(input(name+'의 영어 성적 : '))
    score.append([name,s1,s2,s3])
    print('-'*20)

#출력부분
print('-'*50)
print('순번\t이름\t국어\t수학\t영어\t합계\t평균\t성적')
print('-'*50)

cnt = 1
tavg = 0
for i in score :
    total = i[1]+i[2]+i[3]
    avg = total // 3

    tavg += avg 
    level = ''

    if avg >= 90 :
        level = 'A'
    elif avg >= 80 :
        level = 'B'
    elif avg >= 70 :
        level = 'C'
    elif avg >= 60 :
        level = 'D'
    else :
        level = 'F'

    print(cnt,end='\t')
    for j in i:
        print(j,end='\t')

    print(total,'\t',avg,'\t',level)

    cnt += 1


print('-'*50) 
print('전체평균 : ',tavg//len(score))
