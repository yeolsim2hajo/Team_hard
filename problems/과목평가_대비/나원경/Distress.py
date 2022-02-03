# Distress.py
# 문제를 내고 그 문제를 틀리면 맞힐 때까지 반복, 맞히면 감탄의 말 + 다음 문제
# 모든 문제를 다 맞히면 종료
# 재귀함수 이용
# 문제를 보여주고 답을 입력받아 정답과 비교

import random

def yeol_sim2(idx = 0):
    quest_list = [
    '진공 속에서 빛의 속도는? (km/s 단위, 만의 자리에서 반올림해서 숫자만 쓰시오)',
    '12시와 1시 사이에 시침과 분침이 정확히 180도를 이루는 시간은? (초 단위 미만은 버림)',
    '물분자 사이의 결합으로, 물보다 얼음의 밀도가 작아지는 이유와 관련된 이 결합을 무엇이라 부르는가?'
    ]
    
    answer = [
    '300000',
    '12시 32분 43초',
    '수소결합'
    ]

    if idx < len(quest_list):
        quest = quest_list[idx] 
        user_answer = input(f'{quest} \n 정답 : ')
        if user_answer != answer[idx]:
            yak_olliki = [
            '일부\'로\' 틀린 고양?',
            '이런 식으로는 \'않\'됩니다.',
            '문제를 다 맞히실 때까지 이 코드는 끝나지 않습니다.',
            # 이하 생략
            ]
            print(random.sample(yak_olliki, 1))
            return yeol_sim2(idx)   
        
        else:
            encouraging = [
            '와, 정답입니다.',
            '오, 정말 대단하군요.',
            '당신의 지식에 파이썬도 감탄합니다.',
            # 이하 생략
            ]  
            print(random.sample(encouraging, 1))
            return yeol_sim2(idx+1)

    else:
        return '시험을 통과하셨습니다.'
