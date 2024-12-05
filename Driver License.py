def get_license_info(license_number):
    # 입력된 번호 길이 확인
    if len(license_number) != 12 or not license_number.isdigit():
        return "올바른 12자리 숫자를 입력하세요."
    
    # 번호 해석
    region_code = int(license_number[:2])
    year = license_number[2:4]
    serial_number = license_number[4:10]
    checksum = license_number[10:11]
    reissue_count = int(license_number[11:])
    
    # 지역 번호 해석
    region_dict = {
        11: "서울", 12: "부산", 13: "경기", 14: "강원", 15: "충북",
        16: "충남", 17: "전북", 18: "전남", 19: "경북", 20: "경남",
        21: "제주", 22: "대구", 23: "인천", 24: "광주", 25: "대전"
    }
    region = region_dict.get(region_code, "알 수 없는 지역")
    
    # 결과 출력
    result = f"""
    운전면허 번호 해석 결과:
    - 지역 코드: {region} ({region_code})
    - 최초 발급 연도: 20{year}년
    - 연도별 일련번호: {serial_number}
    - 체크섬 번호: {checksum}
    - 재발급 횟수: {reissue_count}회
    """
    return result

# 사용자 입력
license_number = input("운전면허 번호를 입력하세요 ('-'없이, 12자리): ")
print(get_license_info(license_number))
