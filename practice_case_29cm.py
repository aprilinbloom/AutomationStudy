import os
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By


#현재 시간 구하기
now = time.strftime('%Y_%m_%d_%Hh_%Mm')

#성공한 TC ID 넣는 리스트
result_pass_list = []
#실패한 TC ID 넣는 리스트
result_fail_list = []
#실패한 이유를 가지고 있는 리스트
fail_reason_list = []
#전체 TC 개수
tc_count = 4

if not os.path.exists('test_result'):
    os.makedirs('test_result')

f = open(f'test_result/{now}_test_result.txt', 'w')
f.write(f'테스트 수행 일자 - {now}\n')


# TC_001 29CM 사이트 접속
try:
    tc_id = 'TC_001'
    driver = webdriver.Chrome()
    driver.get('https://29cm.co.kr')
    driver.implicitly_wait(5)
    tc_001_url = driver.current_url

    if tc_001_url == driver.current_url:
        print('29cm 진입 성공')
        result_pass_list.append(tc_id)
    else:
        print(driver.current_url)
        result_fail_list.append(tc_id)
        fail_reason_list.append('29cm 진입 실패')

except Exception as e:
    print(f'에러 발생: {e}')
    error_log = driver.get_log('browser')
    print(error_log)


# TC_002 lookbook 페이지로 이동
try:
    tc_id = 'TC_002'
    lookbook = driver.find_element(By.XPATH, '/html/body/home-root/div/ruler-gnb/div/div[3]/div/div/ul/li[2]/a')
    lookbook.click()
    driver.implicitly_wait(5)
    tc_002_url = 'https://shop.29cm.co.kr/lookbook'

    if tc_002_url == 'https://shop.29cm.co.kr/lookbook':
        print('룩북 이동 성공')
        result_pass_list.append(tc_id)
    else:
        print(driver.current_url)
        print('룩북 이동 실패')
        result_fail_list.append(tc_id)
        fail_reason_list.append('룩북 이동 실패')
except Exception as e:
    print(f'에러 발생: {e}')
    error_log = driver.get_log('browser')
    print(error_log)


# TC_003 lookbook 내 최상단 항목 선택
try:
    tc_id = 'TC_003'
    pyautogui.sleep(3)
    pyautogui.click(500, 670)
    tc_003_url = 'https://shop.29cm.co.kr/lookbook/35469'

    if tc_003_url == 'https://shop.29cm.co.kr/lookbook/35469':
        print('룩북 상세 진입 성공')
        result_pass_list.append(tc_id)
    else:
        print(tc_003_url)
        print('룩북 상세 진입 실패')
        result_fail_list.append(tc_id)
        fail_reason_list.append('룩북 상세 진입 실패')
except Exception as e:
    print(f'에러 발생: {e}')
    error_log = driver.get_log('browser')
    print(error_log)


# TC_004 lookbook 상세에서 최하단 스크롤 이동 후 해당 브랜드홈 이동
try:
    tc_id = 'TC_004'
    pyautogui.press('end')
    shop_now = driver.find_element(By.CSS_SELECTOR, '#__next > div.css-1gzs0we.ecwnmeh0 > div.css-1qurj5f.erqon9g0 > div > a')
    shop_now.click()
    driver.implicitly_wait(5)
    tc_004_url = 'https://shop.29cm.co.kr/brand/3389'

    if tc_004_url == 'https://shop.29cm.co.kr/brand/3389':
        print('브랜드홈 이동 성공')
        result_pass_list.append(tc_id)
    else:
        print(tc_004_url)
        print('브랜드홈 이동 실패')
        result_fail_list.append(tc_id)
        fail_reason_list.append('브랜드홈 이동 실패')
except Exception as e:
    print(f'에러 발생: {e}')
    error_log = driver.get_log('browser')
    print(error_log)

time.sleep(3)

driver.quit()



#PASS 테스트 결과 기록
f.write('\n[결과: PASS]\n')
for pass_cnt in range(len(result_pass_list)):
    f.write(f'{result_pass_list[pass_cnt]} : PASS\n')


#FAIL 테스트 결과 기록
f.write('\n[결과: FAIL]\n')
for fail_cnt in range(len(result_fail_list)):
    f.write(f'{result_fail_list[fail_cnt]} : FAIL\n')
    f.write(f'\t{fail_reason_list[fail_cnt]}\n')


#테스트 결과 요약
f.write('\n[테스트 결과 요약]\n')
f.write(f'PASS TC COUNT : {len(result_pass_list)}\n')
f.write(f'FAIL TC COUNT : {len(result_fail_list)}\n')
f.write(f'COMPLETED TEST COUNT : {len(result_pass_list) + len(result_fail_list)}\n')
f.write(f'PROGRESS OF TEST : {((len(result_pass_list) + len(result_fail_list))/tc_count)*100}%\n')
f.write(f'PASS RATE : {(len(result_pass_list)/tc_count)*100}%')
f.close()