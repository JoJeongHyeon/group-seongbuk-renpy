# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 역사 인물 빙의 게임 스크립트

# 배경 이미지 정의
image bg desk = "desk_book.png"           # 책상 배경
image bg ceiling = "blurry_ceiling.png"     # 천장 배경
image bg ceiling_blur = "blurry_ceiling.png"  # 흐릿한 천장
image bg mirror = "mirror.png"       # 거울 배경
image black = "#000000"                 # 검은 화면

# 캐릭터 일러스트 정의
image char jang = "jgy_mock-up.png"       # 장기영 캐릭터
image char im = "lg_mock-up.png"           # 임규 캐릭터  
image char oh = "osc_mock-up.png"           # 오세창 캐릭터

# 거울 속 모습 이미지
image mirror jang = "mirror_jang.png"   # 거울 속 장기영
image mirror im = "mirror_im.png"       # 거울 속 임규
image mirror oh = "mirror_oh.png"       # 거울 속 오세창

# 오브젝트 이미지
image obj gun = "obj_gun.png"           # 총 오브젝트
image obj book = "obj_book.png"         # 책 오브젝트
image obj newspaper = "obj_newspaper.png" # 신문 오브젝트

# 내레이터와 주인공 정의
define narrator = Character(None)
define p = Character('나', color="#ffffff")  # 주인공 (이름 미상)

# 캐릭터 정의 (각각 다른 변수명 사용)
define jang = Character('장기영', color="#ff6b6b")
define im = Character('임규', color="#4ecdc4")
define oh = Character('오세창', color="#45b7d1")

# 화면 전환 효과 정의
define fade = Fade(0.75, 0.25, 0.75)
define dissolve_slow = Dissolve(1.0)

# 게임 변수
default identity = None  # 선택된 인물 ('jang' | 'im' | 'oh')
default awakening_complete = False  # 각성 완료 여부

# 게임 시작
label start:
    # 게임 시작할 때 배경음악(main_bgm) 재생
    play music "main_bgm.mp3" fadein 1.0

    # [Scene1] 책상에서 공부하다 잠든 상황
    scene bg desk with fade
    
    narrator '어젯밤, 나는 역사 시험을 위해 벼락치기로 공부하다 새벽쯤에 그대로 잠들었다.'
    
    # 블랙아웃 전환
    scene black with fade
    pause 1.0
    
    narrator '잠결에 어렴풋이 들려오는 대화 소리…'
    
    p "아 시끄러워… 누가 이렇게 떠들어?"
    
    narrator "더 이상 잠들기 어려워 눈을 떠보려 한다."
    
    # [Scene2] 낯선 천장과 상황 인식
    scene bg ceiling_blur with dissolve_slow
    pause 0.5
    scene bg ceiling with dissolve

    '눈을 뜨자, 낯선 천장이 보인다.'
    '처음 보는 공간, 그리고 들여오는 일본어 소리...'
    p "웬 일본어? 여긴 어디지, 왜 나는 여기 있는 거지?"
    '손을 뻗자 무언가 잡힌다. 이건 뭘까?'
    
    # 분기점: 손에 든 물건 선택
    $ renpy.pause(1.0)  # 잠깐 멈춤으로 긴장감 조성
    
    menu:
        narrator "손에 쥔 물건은…"
        
        "차가운 금속 물체":
            $ identity = "jang"
            narrator "손에 쥔 것은... 총이다."
            p "총?! 왜 내가 총을 들고 있지?"
            narrator "묵직하고 차가운 감촉. 분명히 진짜 총이다."
            
        "두꺼운 종이 뭉치":
            $ identity = "im" 
            narrator "손에 쥔 것은... 책이다."
            p "책? 이건 내가 읽던 책이 아닌데..."
            narrator "낡은 종이의 냄새와 함께 한자가 빼곡히 적힌 책이다."
            
        "바스락거리는 종이":
            $ identity = "oh"
            narrator "손에 쥔 것은... 신문이다."
            p "신문? 그런데 이 글씨들... 일본어인가?"
            narrator "오래된 신문지. 일본어로 쓰여진 기사들이 보인다."
    
    narrator "혼란스러운 마음을 진정시키고 주변을 둘러본다."
    narrator "저쪽에 거울이 보인다. 일단 내 모습부터 확인해보자."

    stop music fadeout 1.0
    
    # 거울 씬으로 전환
    play sound "mirror_reveal.mp3" fadein 1.0
    scene bg mirror with dissolve_slow
    
    # 선택한 인물에 따라 분기
    if identity == "jang":
        jump route_jang
    elif identity == "im":
        jump route_im
    else:
        jump route_oh

# 장기영 루트
label route_jang:
    show mirror jang at left with dissolve_slow
    
    narrator '거울 속에는... 내가 아닌 다른 사람이 서 있다.'
    narrator '끝이 위를 향한 진한 눈썹과 초롱초롱하면서도 의지가 강해 보이는 눈.'
    narrator '이 얼굴... 어디서 본 것 같은데?'
    
    p "이게... 나라고? 아니, 이건 분명..."

    # call screen mirror_scene

    # 기억이 되살아나는 연출
    $ renpy.pause(0.5)
    scene black with Fade(0.3, 0.5, 0.3)
    
    narrator "갑자기 머릿속에 기억들이 쏟아져 들어온다."
    narrator "대한독립군... 청산리 대첩... 자유시 참변..."
    
    scene bg mirror with dissolve_slow
    show char jang at left
    
    jang "나는... 장기영이다."
    jang "대한독립군의 지휘관, 장기영."
    
    $ awakening_complete = True
    narrator "이제 모든 것이 명확해졌다."
    narrator "나는 1920년대 만주에서 독립운동을 하던 장기영이 되어 있다."
    
    jump after_awakening

# 임규 루트  
label route_im:
    show mirror im at left with dissolve_slow
    
    narrator "거울 속에는... 낯선 남성이 서 있다."
    narrator "단정하게 자른 짧은 머리와 지적인 인상을 주는 수염."
    narrator "온화하면서도 굳건한 의지가 느껴지는 눈빛."
    
    p "이 사람은... 누구지? 그런데 왜 내가 이 모습으로..."
    
    # 기억 각성 연출
    $ renpy.pause(0.5)
    scene black with Fade(0.3, 0.5, 0.3)
    
    narrator "머릿속에 무수한 기억들이 스며든다."
    narrator "교육... 계몽... 민족의식... 조선어학회..."
    
    scene bg mirror with dissolve_slow  
    show char im at left
    
    im "나는... 임규다."
    im "조선의 교육자이자 언어학자 임규."
    
    $ awakening_complete = True
    narrator "이제 이해했다."
    narrator "나는 일제강점기 조선어 보존과 민족교육에 힘쓰던 임규가 되어 있다."
    
    jump after_awakening

# 오세창 루트
label route_oh:
    show mirror oh at left with dissolve_slow
    
    narrator "거울 속의 인물은... 나와는 전혀 다른 모습이다."
    narrator "강인한 턱선과 날카로우면서도 깊이 있는 눈빛."
    narrator "근엄하고 위엄 있는 인상의 남성."
    
    p "이 얼굴... 어디서 본 것 같은데. 그런데 왜 내가..."
    
    # 기억 각성 연출
    $ renpy.pause(0.5)  
    scene black with Fade(0.3, 0.5, 0.3)
    
    narrator "순간, 뇌리에 수많은 장면들이 스쳐간다."
    narrator "서예... 언론... 저항... 105인 사건..."
    
    scene bg mirror with dissolve_slow
    show char oh at left
    
    oh "나는... 오세창이로구나."
    oh "서예가이자 언론인, 그리고 독립운동가 오세창."
    
    $ awakening_complete = True  
    narrator "모든 것이 명확해졌다."
    narrator "나는 일제강점기 문화계몽운동을 이끌던 오세창이 되어 있다."
    
    jump after_awakening

# 각성 후 공통 루트
label after_awakening:
    scene black with fade
    
    narrator "이것이 현실인가, 꿈인가..."
    narrator "하지만 이 몸에 스며든 기억들은 너무도 생생하다."
    
    if identity == "jang":
        narrator "장기영의 기억과 의지가 내 안에 살아 숨쉬고 있다."
        narrator "조국의 광복을 위해 싸워야 한다는 사명감이 가슴에 불타오른다."
    elif identity == "im":
        narrator "임규의 지식과 신념이 내 마음에 자리잡았다."
        narrator "민족의 정신을 지키고 후세에 전해야 한다는 책임감이 무겁게 다가온다."
    else:
        narrator "오세창의 예술혼과 저항정신이 내 혼을 채운다."
        narrator "붓과 펜으로 일제에 맞서고 민족의식을 일깨워야 한다."
    
    narrator "과연 나는 이 시대를 어떻게 살아갈 것인가..."
    narrator "역사를 바꿀 수 있을까, 아니면 역사의 흐름에 따라갈 뿐일까..."
    
    # 계속할 내용이 있다면 여기서 다음 씬으로...
    narrator "이야기는 계속됩니다..."
    
    return