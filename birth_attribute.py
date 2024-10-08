import math
'''
하루는 똑같이 24시간
1주 = 12일
한달 = 3주 = 36일

1년 = 12달 = 36주 = 36 * 36 일 
지구에서의 1년을 윌라르브 1년으로 스케일링 하여 계산 (단 윤년은 제외.. 헷갈려)
'''
earth_month = [31,28,31,30,31,30,31,31,30,31,30,31] # 월별 일 수
attribute = ['무', 
             '어둠',
             '부활',
             '창조',
             '바람',
             '빛',
             '불',
             '물',
             '하늘',
             '대지',
             '파괴',
             '죽음',
             '무', 
             '어둠',
             '부활',
             '창조',
             '바람',
             '빛',
             '불',
             '물',
             '하늘',
             '대지',
             '파괴',
             '죽음',
             '무', 
             '어둠',
             '부활',
             '창조',
             '바람',
             '빛',
             '불',
             '물',
             '하늘',
             '대지',
             '파괴',
             '죽음']
wil_month =0
wil_day=0
wil_time=0



def cal_all(month,day,time):
    month = month
    day = day
    time = time

    def cal_rate():
        rate = 0
        for i in range(month-1):
            rate += earth_month[i] # 생일 이전 월 일수 모두 합
        rate += day - 1 # 생일 일자 합 
        rate *= 24 # 구한 모든 일자에 * 24하여 시간단위
        rate += time
        rate /= 365 * 24
        #print(rate)
        return conv_month(rate)

    def conv_month(rate):
        wil_month = math.floor(rate * 12) + 1
        rate_day = rate * 12 - (wil_month - 1)
        return conv_day(rate_day, wil_month)

    def conv_day(rate_day, wil_month):
        wil_day = math.floor(rate_day * 36) + 1
        rate_time = rate_day * 36 - (wil_day - 1)
        return conv_time(rate_time, wil_month, wil_day)

    def conv_time(rate_time, wil_month, wil_day):
        wil_time = math.floor(rate_time * 24)
        if wil_time == 0:
            return [attribute[wil_month - 1], attribute[wil_day - 1], attribute[0]]
        else:
            return [attribute[wil_month - 1], attribute[wil_day - 1], attribute[math.floor(wil_time / 2)]]

    return cal_rate()



#cal_all(12,13,15)