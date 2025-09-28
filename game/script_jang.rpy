# 장기영 루트 스크립트
# script.rpy의 정의들을 모두 사용 가능

label character_jang:
    narrator '주변을 둘러보니, 마침 거울이 보인다.'
    
    scene bg_mirror with fade

    narrator '거울을 살펴보자.'
    
    # Scene 3: 거울 - 장기영
    call screen interactive_mirror("jang_portrait")
    show jang_portrait with dissolve
    play sound mirror_reveal  # 효과음 재생
    
    narrator '끝이 위를 향한 눈썹과 초롱초롱한 눈을 가진 남성의 모습이다.'
    
    m "이게 나라고? 일단 밖으로 나가보자"
    
    # 테스트: script.rpy에서 정의한 것들이 잘 작동하는지 확인
    scene bg_black with fade_fast
    narrator '장기영 파일에서 fade_fast 효과 테스트 완료!'
    
    scene bg_ceiling with fade_slow  
    jang "안녕하세요! 저는 장기영입니다. 캐릭터 정의도 잘 작동하네요!"
    
    narrator "✅ script_jang.rpy 파일 구조 테스트 성공!"
    
    "장기영 루트가 시작됩니다..."
    return
