# 이 파일에 게임 스크립트를 입력합니다.

# =============================================================================
# 커스텀 효과 정의
# =============================================================================

# 트랜지션
define fade_slow = Fade(0.5, 1.0, 0.5)
define fade_fast = Fade(0.2, 0.4, 0.2)

# 위치/스케일
transform custom_size:
    size (1920, 1080)
    # fit "cover" 이런 애도 있다고 함. 자세한 건 문서 ㄱ

# 스크린
# 거울 호버 기능
# 다른 오브젝트에도 호버 기능이 지원되도록 범용적이게 만들어보자.
screen interactive_mirror(character_portrait):

    # imagemap을 사용합니다.
    imagemap:
        ground "bg_mirror"
        hover "bg_mirror_hover"
        alpha True
        at custom_size

        hotspot (0, 0, 1920, 1080):
            action Return("mirror_hovered")

screen interactive_table():
    # 기본 테이블 이미지
    add "bg_table" at custom_size
    
    # 신문 영역 (맨 아래)
    imagemap:
        ground Null(1920, 1080)  # 투명한 배경
        hover "bg_table_news_hover"
        alpha True
        at custom_size
        hotspot (0, 0, 1920, 1080):
            action Return("news_selected")

    # 붕대 영역 (중간 아래)
    imagemap:
        ground Null(1920, 1080)  # 투명한 배경
        hover "bg_table_bandage_hover"
        alpha True
        at custom_size
        hotspot (0, 0, 1920, 1080):
            action Return("bandage_selected")
            
    # 책 영역 (중간 위)        
    imagemap:
        ground Null(1920, 1080)  # 투명한 배경
        hover "bg_table_book_hover"
        alpha True
        at custom_size
        hotspot (0, 0, 1920, 1080):
            action Return("book_selected")
    
    # 총 영역 (맨 위)
    imagemap:
        ground Null(1920, 1080)  # 투명한 배경
        hover "bg_table_gun_hover"
        alpha True
        at custom_size
        hotspot (0, 0, 1920, 1080):
            action Return("gun_selected")

# =============================================================================
# 이미지 정의
# =============================================================================
# 배경 
image bg_desk    = At("bg/desk.png", custom_size)
image bg_ceiling        = At("bg/ceiling.png", custom_size)

image bg_mirror         = At("bg/mirror.png", custom_size)             
image bg_mirror_hover   = At("bg/mirror_hover.png", custom_size)  # 거울 호버 이미지

image bg_table             = At("bg/table.png", custom_size) 
image bg_table_book_hover  = At("bg/table_book_hover.png", custom_size)
image bg_table_gun_hover   = At("bg/table_gun_hover.png", custom_size)
image bg_table_news_hover  = At("bg/table_news_hover.png", custom_size)
image bg_table_bandage_hover  = At("bg/table_bandage_hover.png", custom_size)
# 캐릭터 
image jang_portrait = "ch/jang.png"    # 장기영 초상화
image im_portrait = "ch/im.png"        # 임규 초상화
image oh_portrait = "ch/oh.png"        # 오세창 초상화
image yeon_portrait = "ch/yeon_mock-up.png"    # 연미당 초상화

# 효과용
image bg_black = "#000000"          # 블랙아웃용 이미지

# =============================================================================
# 오디오 정의
# =============================================================================
# 배경음
define audio.main_bgm = "audio/bgm/main_bgm.mp3"

# 효과음
define audio.mirror_reveal = "audio/sfx/mirror_reveal.mp3"  # 거울 속 인물 등장

# =============================================================================
# 캐릭터 정의
# =============================================================================
# 나레이터 (생각)
define narrator = Character(None, what_color="#ffffff")

# 주인공 (대사)
define m = Character("나", color="#ffffff")

# 역사 인물들
define jang = Character("장기영", color="#ff6b6b")
define im = Character("임규", color="#4ecdc4")
define oh = Character("오세창", color="#45b7d1")
define yeon = Character("연미당", color="#e3f844")

# =============================================================================
# 게임 시작
# =============================================================================
label start:
    # BGM 시작 - 게임 내내 계속 재생
    play music main_bgm fadein 1.0 loop
    
    # Scene 1: 책상 위 역사책
    scene bg_desk with fade_slow
    
    narrator '어젯밤, 나는 역사 시험을 위해 벼락치기로 공부하다 새벽쯤에 그대로 잠이 들었다.'
    
    # 화면 블랙아웃
    scene bg_black with fade_fast
    
    narrator '잠결에 어렴풋이 들려오는 대화 소리…'
    
    m "아 시끄러워…"
    
    narrator '더 이상 잠들기 어려워 눈을 떠보려 한다.'
    
    # Scene 2: 천장
    scene bg_ceiling with fade_slow
    
    narrator '눈을 뜨자, 낯선 천장이 보인다.'
    
    narrator '처음 보는 공간, 그리고 들려오는 일본어 소리…'
    
    m "웬 일본어? 여긴 어디고, 왜 나는 여기 있지?"
    
    narrator '손을 뻗자 무언가 잡힌다. 이건 뭐지?'
    
    scene bg_table with fade_slow
    
    narrator '테이블 위에 세 가지 물건이 보인다. 마우스를 올려보고 클릭해보자.'
    
    # 인터랙티브 테이블 사용
    call screen interactive_table
    
    # 선택에 따른 분기
    if _return == "gun_selected":
        $ chosen_character = "jang" # 장기영
        narrator '총을 집었다. 차가운 금속의 감촉이 느껴진다.'
        jump intro_mirror_jang
    elif _return == "book_selected":
        $ chosen_character = "im" # 임규  
        narrator '책을 집었다. 묵직한 무게가 손에 전해진다.'
        jump intro_mirror_im
    elif _return == "news_selected":
        $ chosen_character = "oh" # 오세창
        narrator '신문을 집었다. 바스락거리는 종이 소리가 난다.'
        jump intro_mirror_oh
    elif _return == "bandage_selected":
        $ chosen_character = "yeon" # 연미당
        narrator '붕대를 집었다. 붕대가 손에 전해진다.'
        jump intro_mirror_yeon
    
    return

# =============================================================================
# 거울 씬 (인트로 마지막 부분)
# =============================================================================
label intro_mirror_jang:
    narrator '주변을 둘러보니, 마침 거울이 보인다.'
    
    scene bg_mirror with fade

    narrator '거울을 살펴보자.'
    
    # Scene 3: 거울 - 장기영
    call screen interactive_mirror("jang_portrait")
    show jang_portrait:
        xalign 0.5
        yalign 0.0
    with dissolve
    play sound mirror_reveal  # 효과음 재생
    
    narrator '끝이 위를 향한 눈썹과 초롱초롱한 눈을 가진 남성의 모습이다.'
    
    m "이게 나라고? 일단 밖으로 나가보자"
    
    # 장기영 루트로 이동
    jump character_jang

label intro_mirror_im:
    narrator '주변을 둘러보니, 마침 거울이 보인다.'

    scene bg_mirror with fade

    narrator '거울을 살펴보자.'
    
    # Scene 3: 거울 - 임규
    call screen interactive_mirror("im_portrait")
    show im_portrait:
        xalign 0.5
        yalign 0.0
    with dissolve
    play sound mirror_reveal  # 효과음 재생
    
    narrator '짧게 자른 머리와 수염이 눈에 띄는 남성의 모습이다.'
    
    m "이게 나라고? 일단 밖으로 나가보자"
    
    # 임규 루트로 이동
    jump character_im

label intro_mirror_oh:
    narrator '주변을 둘러보니, 마침 거울이 보인다.'

    scene bg_mirror with fade

    narrator '거울을 살펴보자.'

    # Scene 3: 거울 - 오세창
    call screen interactive_mirror("oh_portrait")
    show oh_portrait:
        zoom 1.25
        xalign 0.5
        yalign 0.0
    with dissolve
    play sound mirror_reveal  # 효과음 재생
    
    narrator '강인한 턱선과 날카로운 눈빛의 근엄한 인상을 가진 남성의 모습이다.'
    
    m "이게 나라고? 일단 밖으로 나가보자"
    
    # 오세창 루트로 이동
    jump character_oh

label intro_mirror_yeon:
    narrator '주변을 둘러보니, 마침 거울이 보인다.'
    
    scene bg_mirror with fade
    
    narrator '거울을 살펴보자.'
    
    # Scene 3: 거울 - 연미당
    call screen interactive_mirror("yeon_portrait")
    show yeon_portrait:
        zoom 1.25
        xalign 0.5
        yalign 0.75
    with dissolve
    play sound mirror_reveal  # 효과음 재생
    
    narrator '선의의 미소를 짓고 있는 여성의 모습이다.' # 임의로 채워 넣음.
    
    m "이게 나라고? 일단 밖으로 나가보자"
    
    # 연미당 루트로 이동
    jump character_yeon

# =============================================================================
# 캐릭터별 분기 - 각각의 파일에서 처리
# =============================================================================
# character_jang: script_jang.rpy에서 정의
# character_im: script_im.rpy에서 정의  
# character_oh: script_oh.rpy에서 정의
