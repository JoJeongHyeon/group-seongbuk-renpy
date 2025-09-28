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

# =============================================================================
# 이미지 정의
# =============================================================================
# 배경 
image bg_desk_book = At("bgs/desk_book.png", custom_size)
image bg_ceiling = At("bgs/blurry_ceiling.png", custom_size)     
image bg_mirror = At("bgs/mirror.png", custom_size)              
image bg_mirror_hover = At("bgs/mirror_hover.png", custom_size)  # 거울 호버 이미지

# 캐릭터 
image jang_portrait = "chs/jang_mock-up.png"    # 장기영 초상화
image im_portrait = "chs/im_mock-up.png"        # 임규 초상화
image oh_portrait = "chs/oh_mock-up.png"        # 오세창 초상화

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

# =============================================================================
# 게임 시작
# =============================================================================
label start:
    # BGM 시작 - 게임 내내 계속 재생
    play music main_bgm fadein 1.0 loop
    
    # Scene 1: 책상 위 역사책
    scene bg_desk_book with fade_slow
    
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
    
    # 분기점 등장
    menu:
        "무엇을 잡았을까?"
        
        "총":
            $ chosen_character = "jang" # 장기영
            jump character_jang
            
        "책":
            $ chosen_character = "im" # 임규
            jump character_im
            
        "신문":
            $ chosen_character = "oh" # 오세창
            jump character_oh
    
    return

# =============================================================================
# 캐릭터별 분기
# =============================================================================
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
    
    # 메인스토리로 연결 (추후 구현)
    "장기영 루트가 시작됩니다..."
    return

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
    
    # 메인스토리로 연결 (추후 구현)
    "임규 루트가 시작됩니다..."
    return

label character_oh:
    narrator '주변을 둘러보니, 마침 거울이 보인다.'

    scene bg_mirror with fade
    
    narrator '거울을 살펴보자.'

    # Scene 3: 거울 - 오세창
    call screen interactive_mirror("oh_portrait")
    show oh_portrait with dissolve
    play sound mirror_reveal  # 효과음 재생
    
    narrator '강인한 턱선과 날카로운 눈빛의 근엄한 인상을 가진 남성의 모습이다.'
    
    m "이게 나라고? 일단 밖으로 나가보자"
    
    # 메인스토리로 연결 (추후 구현)
    "오세창 루트가 시작됩니다..."
    return
