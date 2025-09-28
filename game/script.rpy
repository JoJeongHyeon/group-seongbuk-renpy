# 이 파일에 게임 스크립트를 입력합니다.

# =============================================================================
# 이미지 정의
# =============================================================================
# Transform 정의 - 화면에 맞춤
transform fit_screen:
    fit "cover"  # 화면을 완전히 채움 (일부 잘릴 수 있음)
    # 또는 다른 옵션들:
    # fit "contain"    # 화면을 완전히 채움 (일부 잘릴 수 있음)
    # fit "fill"     # 화면을 완전히 채움 (비율 무시)

transform custom_size:
    size (1920, 1080)

# 어떤 캐릭터의 초상화를 보여줄지 (character_portrait)를 파라미터로 받는 스크린
screen interactive_mirror(character_portrait):

    # imagemap을 사용합니다.
    imagemap:
        ground "bg_mirror"
        hover "bg_mirror_hover"
        alpha True

        at custom_size

        hotspot (0, 0, 1920, 1080):
            action Return("mirror_hovered")

# 배경 이미지
image bg_desk_book = "bgs/desk_book.png"
image bg_ceiling = "bgs/blurry_ceiling.png"     # 천장 배경

## 거울 호버 시험용
image bg_mirror = "bgs/mirror.png"              # 거울 배경
image bg_mirror_hover = "bgs/mirror_hover.png"
image bg_mirror_map = "bgs/mirror_map.png"

image bg_black = "#000000"                   # 블랙아웃용

# 캐릭터 일러스트
image jgy_portrait = "chs/jgy_mock-up.png"   # 장기영 초상화
image lg_portrait = "chs/lg_mock-up.png"  # 임규 초상화 (lg = 임규로 추정)
image osc_portrait = "chs/osc_mock-up.png"   # 오세창 초상화

# =============================================================================
# 오디오 정의
# =============================================================================
# 배경음악 (BGM) - 하나만!
define audio.main_bgm = "audio/bgm/main_bgm.mp3"  # 메인 배경음악

# 효과음 (SE)
define audio.mirror_reveal = "audio/se/mirror_reveal.mp3"  # 거울 속 인물 등장 효과음

# =============================================================================
# 캐릭터 정의
# =============================================================================
# 나레이터 (생각)
define narrator = Character(None, what_color="#ffffff")

# 주인공 (대사)
define mc = Character("나", color="#ffffff")

# 역사 인물들 (나중에 사용)
define jgy = Character("장기영", color="#ff6b6b")
define lg = Character("임규", color="#4ecdc4")
define osc = Character("오세창", color="#45b7d1")

# =============================================================================
# 게임 시작
# =============================================================================
label start:
    # BGM 시작 - 게임 내내 계속 재생
    play music main_bgm loop
    
    # Scene 1: 책상 위 역사책
    scene bg_desk_book at custom_size with fade
    
    '어젯밤, 나는 역사 시험을 위해 벼락치기로 공부하다 새벽쯤에 그대로 잠이 들었다.'
    
    # 화면 블랙아웃
    scene bg_black with fade
    
    '잠결에 어렴풋이 들려오는 대화 소리…'
    
    mc "아 시끄러워…"
    
    '더 이상 잠들기 어려워 눈을 떠보려 한다.'
    
    # Scene 2: 천장
    scene bg_ceiling at custom_size with fade
    
    '눈을 뜨자, 낯선 천장이 보인다.'
    
    '처음 보는 공간, 그리고 들려오는 일본어 소리…'
    
    mc "웬 일본어? 여긴 어디고, 왜 나는 여기 있지?"
    
    '손을 뻗자 무언가 잡힌다. 이건 뭐지?'
    
    # 분기점 등장
    menu:
        "무엇을 잡았을까?"
        
        "총":
            $ chosen_character = "jgy" # 장기영
            jump character_jgy
            
        "책":
            $ chosen_character = "lg" # 임규
            jump character_lg
            
        "신문":
            $ chosen_character = "osc" # 오세창
            jump character_osc
    
    return

# =============================================================================
# 캐릭터별 분기
# =============================================================================
label character_jgy:
    '주변을 둘러보니, 마침 거울이 보인다.'
    
    '거울을 살펴보자.'
    
    scene bg_mirror at custom_size with fade
    
    # Scene 3: 거울 - 장기영
    call screen interactive_mirror("jgy_portrait")
    show jgy_portrait with dissolve
    play sound mirror_reveal  # 효과음 재생
    
    '끝이 위를 향한 눈썹과 초롱초롱한 눈을 가진 남성의 모습이다.'
    
    mc "이게 나라고? 일단 밖으로 나가보자"
    
    # 메인스토리로 연결 (추후 구현)
    "장기영 루트가 시작됩니다..."
    return

label character_lg:
    '주변을 둘러보니, 마침 거울이 보인다.'
    
    '거울을 살펴보자.'

    scene bg_mirror at custom_size with fade
    
    # Scene 3: 거울 - 임규
    call screen interactive_mirror("lg_portrait")
    show lg_portrait with dissolve
    play sound mirror_reveal  # 효과음 재생
    
    '짧게 자른 머리와 수염이 눈에 띄는 남성의 모습이다.'
    
    mc "이게 나라고? 일단 밖으로 나가보자"
    
    # 메인스토리로 연결 (추후 구현)
    "임규 루트가 시작됩니다..."
    return

label character_osc:
    '주변을 둘러보니, 마침 거울이 보인다.'
    
    '거울을 살펴보자.'

    scene bg_mirror at custom_size with fade
    
    # Scene 3: 거울 - 오세창
    call screen interactive_mirror("osc_portrait")
    show osc_portrait with dissolve
    play sound mirror_reveal  # 효과음 재생
    
    '강인한 턱선과 날카로운 눈빛의 근엄한 인상을 가진 남성의 모습이다.'
    
    mc "이게 나라고? 일단 밖으로 나가보자"
    
    # 메인스토리로 연결 (추후 구현)
    "오세창 루트가 시작됩니다..."
    return
