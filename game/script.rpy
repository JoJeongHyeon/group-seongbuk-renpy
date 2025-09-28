# ========== 이미지 ==========
# 배경 
image bg desk_book       = im.Scale("images/bg/desk_book.png", 1920, 1080)
image bg blurry_ceiling  = im.Scale("images/bg/blurry_ceiling.png", 1920, 1080)
image bg mirror          = im.Scale("images/bg/mirror.png", 1920, 1080)

# 캐릭터 
image ch jgy  = "images/sprites/jgy_mock-up.png"    # 장기영
image ch lg   = "images/sprites/lg_mock-up.png"     # 임규
image ch osc  = "images/sprites/osc_mock-up.png"    # 오세창

# 효과용
image blackout = Solid("#000")

# ========== 트랜지션 ==========
define fade_slow = Fade(0.5, 1.0, 0.5)
define fade_fast = Fade(0.2, 0.4, 0.2)

# ========== 위치/스케일 트랜스폼 ==========
# 거울 앞 좌표 
transform in_mirror_pos:
    xpos 880       # x 픽셀
    ypos 750       # y 픽셀
    xanchor 0.5
    yanchor 0.78
    zoom 0.8

# ========== 변수 ==========
default route = None  # "jgy" / "lg" / "osc"

# ========== 캐릭터 ==========
define m = Character("나", color="#c8ffc8", what_font="font/RIDIBatang.otf")

# ========== 음악 ==========
define audio.main_bgm = "audio/bgm/main_bgm.mp3"
define audio.mirror_reveal = "audio/sfx/mirror_reveal.mp3"

# ========== 시작 ==========
label start:

    # ---------------- Scene 1 ----------------
    scene bg desk_book with fade_slow
    play music main_bgm fadein 1.0 loop
    "어젯밤, 나는 역사 시험을 위해 벼락치기로 공부하다 새벽쯤에 그대로 잠이 들었다."

    scene blackout with fade_fast
    "잠결에 어렴풋이 들려오는 대화 소리…"
    m "아 시끄러워…"
    "더 이상 잠들기 어려워 눈을 떠보려 한다."

    # ---------------- Scene 2 ----------------
    scene bg blurry_ceiling with fade_slow
    "눈을 뜨자, 낯선 천장이 보인다."
    "처음 보는 공간, 그리고 들려오는 일본어 소리…"
    m "웬 일본어? 여긴 어디고, 왜 나는 여기 있지?"
    "손을 뻗자 무언가 잡힌다. 이건 뭐지?"

    # [분기점] 루트 선택
    menu:
        "무엇을 집어들까?"

        "총을 집어든다":
            $ route = "jgy"
        "책을 집어든다":
            $ route = "lg"
        "신문을 집어든다":
            $ route = "osc"

    jump scene3


label scene3:
    scene bg mirror with fade_slow
    "주변을 둘러보니, 마침 거울이 보인다."
    "거울을 살펴보자."

    play sound mirror_reveal

    
    if route == "jgy":
        show ch jgy at in_mirror_pos with fade_slow
        "끝이 위를 향한 눈썹과 초롱초롱한 눈을 가진 남성의 모습이다."
    elif route == "lg":
        show ch lg at in_mirror_pos with fade_slow
        "짧게 자른 머리와 수염이 눈에 띄는 남성의 모습이다."
    elif route == "osc":
        show ch osc at in_mirror_pos with fade_slow
        "강인한 턱선과 날카로운 눈빛의 근엄한 인상을 가진 남성의 모습이다."

    m "이게 나라고? 일단 밖으로 나가보자"

    jump main_story


# ========== 메인 스토리 진입 ==========
label main_story:
    if route == "jgy":
        jump chapter_jgy
    elif route == "lg":
        jump chapter_lg
    elif route == "osc":
        jump chapter_osc
    else:
        "문을 열고 밖으로 나선다…"
        return

label chapter_jgy:
    # 장기영 루트
    return

label chapter_lg:
    # 임규 루트
    return

label chapter_osc:
    # 오세창 루트
    return
