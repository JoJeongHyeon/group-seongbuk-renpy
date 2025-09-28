# 임규 루트 스크립트
# script.rpy의 정의들을 모두 사용 가능

label character_im:
    narrator '주변을 둘러보니, 마침 거울이 보인다.'

    scene bg_mirror with fade

    narrator '거울을 살펴보자.'
    
    # Scene 3: 거울 - 임규
    call screen interactive_mirror("im_portrait")
    show im_portrait with dissolve
    play sound mirror_reveal  # 효과음 재생
    
    narrator '짧게 자른 머리와 수염이 눈에 띄는 남성의 모습이다.'
    
    m "이게 나라고? 일단 밖으로 나가보자"
    
    # 테스트: script.rpy에서 정의한 것들이 잘 작동하는지 확인
    scene bg_desk_book with fade_slow
    narrator '임규 파일에서 fade_slow 효과 테스트 완료!'
    
    scene bg_black with fade_fast
    im "안녕하세요! 저는 임규입니다. 이미지와 캐릭터 정의가 잘 작동합니다!"
    
    narrator "✅ script_im.rpy 파일 구조 테스트 성공!"
    
    "임규 루트가 시작됩니다..."
    return
