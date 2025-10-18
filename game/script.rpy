
# =============================================================================
# 커스텀 효과 정의
# =============================================================================

# 트랜지션
define fade_very_slow = Fade(0.7, 1.5, 2.0)
define fade_slow = Fade(0.5, 1.0, 0.5)
define fade_fast = Fade(0.2, 0.4, 0.2)

# 디졸브 효과
define dissolve_fast = Dissolve(0.2)
define dissolve_slow = Dissolve(1.0)

# 이미지를 1920x1080 크기에 맞추는 설정
transform custom_size:
    size (1920, 1080)
    # fit "cover" 이런 애도 있다고 함. 자세한 건 문서 ㄱ

# 미션 가이드 슬라이드 인 애니메이션 (왼쪽에서 오른쪽으로)
transform slide_in_left:
    xoffset -300  # 화면 왼쪽 밖에서 시작
    alpha 0.0
    easein 0.5 xoffset 0 alpha 1.0  # 0.5초 동안 원래 위치로 이동하며 페이드 인

# =============================================================================
# 이미지 정의
# =============================================================================
# UI 스크린 이미지
image ui_mission_guide = At("ui_screen/ui_mission_guide.png", custom_size)
image ui_intro_mission = At("ui_screen/ui_intro_mission.png", custom_size)

# 배경 
image bg_desk    = At("bg/intro/desk.png", custom_size)
image bg_ceiling = At("bg/intro/ceiling.png", custom_size)

# 테이블
image bg_table = At("bg/intro/table_empty.png", custom_size) 

# 거울
image bg_mirror         = At("bg/intro/bg_mirror.png", custom_size)             
image bg_mirror_jang    = At("bg/intro/mirror_jang.png", custom_size)   # 장기영 거울 이미지
image bg_mirror_im      = At("bg/intro/mirror_im.png", custom_size)     # 임규 거울 이미지
image bg_mirror_oh      = At("bg/intro/mirror_oh.png", custom_size)     # 오세창 거울 이미지

# 오브젝트
image gun = At("bg/intro/table_gun.png", custom_size)
image gun_hover = At("bg/intro/table_gun_hover.png", custom_size)
image book = At("bg/intro/table_book.png", custom_size)
image book_hover = At("bg/intro/table_book_hover.png", custom_size)
image news = At("bg/intro/table_news.png", custom_size)
image news_hover = At("bg/intro/table_news_hover.png", custom_size)
image mirror = At("bg/intro/mirror.png", custom_size)
image mirror_hover = At("bg/intro/mirror_hover.png", custom_size)

# 캐릭터 
image jang_portrait = "ch/jang.png"    # 장기영 초상화
image im_portrait = "ch/im.png"        # 임규 초상화
image oh_portrait = "ch/oh.png"        # 오세창 초상화

# 효과용
image bg_black = "#000000"          # 블랙아웃용 이미지

# =============================================================================
# 오디오 정의
# =============================================================================
# 배경음
define audio.main_bgm = "audio/bgm/guk-ak_bgm.mp3"

# 효과음
define audio.mirror_reveal = "audio/sfx/mirror_reveal.mp3"  # 거울 속 인물 등장

# =============================================================================
# 캐릭터 정의
# =============================================================================
# 주인공 (대사)
define m = Character("나", color="#ffffff")

# 주인공 (생각)
define m_thought = Character("나", color="#ffffff", what_italic=True)

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
    pause 2.0
    
    scene bg_desk with fade_very_slow
    
    m_thought '어젯밤, 나는 역사 시험을 위해 벼락치기로 공부하다 새벽쯤에 그대로 잠이 들었다.'
    
    # 화면 블랙아웃
    scene bg_black with fade_fast
    
    m_thought '잠결에 어렴풋이 들려오는 대화 소리…'
    
    m "아 시끄러워…"
    
    m_thought '더 이상 잠들기 어려워 눈을 떠보려 한다.'
    
    # Scene 2: 천장
    scene bg_ceiling with fade_slow
    
    m_thought '눈을 뜨자, 낯선 천장이 보인다.'
    m_thought '처음 보는 공간, 그리고 들려오는 일본어 소리…'
    
    m "웬 일본어? 여긴 어디고, 왜 나는 여기 있지?"
    
    m_thought '손을 뻗자 무언가 잡힌다. 이건 뭐지?'
        
    # 인터랙티브 테이블 사용
    show screen mission_guide("테이블에 있는 물건 하나를 선택하세요.", icon="🔍")
    call screen interactive_table with dissolve
    hide screen mission_guide

    show screen full_table

    # 선택에 따른 분기
    if _return == "gun_selected":
        $ chosen_character = "jang" # 장기영
        m_thought '총을 집었다.'
        
        jump intro_mirror_jang
    elif _return == "book_selected":
        $ chosen_character = "im" # 임규  
        m_thought '책을 집었다.'
        jump intro_mirror_im
    elif _return == "news_selected":
        $ chosen_character = "oh" # 오세창
        m_thought '신문을 집었다.'
        jump intro_mirror_oh
    
    return

# =============================================================================
# 거울 씬 (인트로 마지막 부분)
# =============================================================================
label intro_mirror_jang:

    scene bg_mirror
    m_thought '주변을 둘러보니, 마침 거울이 보인다.'
    hide screen full_table with dissolve
    
    m_thought '거울을 살펴보자.'
    
    # Scene 3: 거울 - 장기영
    show screen mission_guide("거울을 눌러보세요.", icon="🔍")
    call screen interactive_objects("mirror")
    hide screen mission_guide
    
    # 거울 클릭 시 장기영 거울 이미지 표시
    scene bg_mirror_jang with dissolve
    # play sound mirror_reveal  # 효과음 재생
    
    m_thought '반짝이는 눈과 근엄한 인상을 가진 남성의 모습이다. '
    
    m "이게 나라고? 일단 밖으로 나가보자"
    
    # 임무창 표시
    window hide
    show ui_intro_mission with dissolve
    pause 2.0
    
    m "어? 이건 뭐지? 이게 말로만 듣던 퀘스트창?"
    m "큰일이네. 빨리 기억 구슬을 찾아서 집으로 가야겠어!"
    
    hide ui_intro_mission with dissolve
    
    # 장기영 루트로 이동
    jump character_jang

label intro_mirror_im:

    scene bg_mirror
    m_thought '주변을 둘러보니, 마침 거울이 보인다.'
    hide screen full_table with dissolve

    m_thought '거울을 살펴보자.'
    
    # Scene 3: 거울 - 임규
    show screen mission_guide("거울을 눌러보세요.", icon="🔍")
    call screen interactive_objects("mirror")
    hide screen mission_guide    
    # 거울 클릭 시 임규 거울 이미지 표시
    scene bg_mirror_im with dissolve
    # play sound mirror_reveal  # 효과음 재생
    
    m_thought '짧게 자른 머리와 수염이 눈에 띄는 남성의 모습이다.'
    
    m "이게 나라고? 일단 밖으로 나가보자"
    
    # 임무창 표시
    window hide
    show ui_intro_mission with dissolve
    pause 2.0
    
    m "어? 이건 뭐지? 이게 말로만 듣던 퀘스트창?"
    m "큰일이네. 빨리 기억 구슬을 찾아서 집으로 가야겠어!"
    
    hide ui_intro_mission with dissolve
    
    # 임규 루트로 이동
    jump character_im

label intro_mirror_oh:

    scene bg_mirror
    m_thought '주변을 둘러보니, 마침 거울이 보인다.'
    hide screen full_table with dissolve

    m_thought '거울을 살펴보자.'

    # Scene 3: 거울 - 오세창
    show screen mission_guide("거울을 눌러보세요.", icon="🔍")
    call screen interactive_objects("mirror")
    hide screen mission_guide
    
    # 거울 클릭 시 오세창 거울 이미지 표시
    scene bg_mirror_oh with dissolve
    # play sound mirror_reveal  # 효과음 재생
    
    m_thought '강인한 턱선과 날카로운 눈빛의 차분한 인상을 가진 남성의 모습이다.'
    
    m "이게 나라고? 일단 밖으로 나가보자"
    
    # 임무창 표시
    window hide
    show ui_intro_mission with dissolve
    pause 2.0
    
    m "어? 이건 뭐지? 이게 말로만 듣던 퀘스트창?"
    m "큰일이네. 빨리 기억 구슬을 찾아서 집으로 가야겠어!"
    
    hide ui_intro_mission with dissolve
    
    # 오세창 루트로 이동
    jump character_oh

# =============================================================================
# 캐릭터별 분기 - 각각의 파일에서 처리
# =============================================================================
# character_jang: script_jang.rpy에서 정의
# character_im: script_im.rpy에서 정의  
# character_oh: script_oh.rpy에서 정의

# =============================================================================
# 인터랙티브 스크린
# =============================================================================

# 범용 오브젝트 인터랙션 스크린 (script_jang.rpy 스타일)
screen interactive_objects(idle_image, hover_image=None, use_alpha=False, return_value="clicked"):
    
    # 클릭 가능한 오브젝트 영역
    imagebutton:
        idle idle_image
        if hover_image:
            hover hover_image
        elif use_alpha:
            hover Transform(idle_image, alpha=0.8)
        else:
            hover idle_image + "_hover"
        focus_mask True
        at truecenter
        action Return(return_value)

screen interactive_table():
    
    add "bg_table"
    # 분기를 위해 return_value를 사용. 일반적인 인터랙티브에는 필요 없음.
    use interactive_objects("news", return_value="news_selected")
    use interactive_objects("book", return_value="book_selected")
    use interactive_objects("gun", return_value="gun_selected")

screen full_table():
    add "bg_table"
    add "news"
    add "book"
    add "gun"

# =============================================================================
# 미션 가이드 스크린 (이미지 배경 버전)
# =============================================================================
screen mission_guide(mission_text, icon="📍"):
    # 다른 화면과 비교해서 최상단에 위치하도록 설정
    # 0-100 사이의 값으로 설정
    zorder 100
    
    # 미션창 배경 이미지 (슬라이드 인 애니메이션 적용)
    add "ui_mission_guide" at slide_in_left
    
    # 텍스트 컨테이너 (슬라이드 인 애니메이션 적용)
    frame:
        at slide_in_left
        xalign 0.03
        yalign 0.165
        xmaximum 480
        background None  # 배경 이미지를 사용하므로 투명하게
        padding (30, 30)
        
        vbox:            
            # 임무 내용
            text mission_text:
                font "fonts/HeirofLightRegular.ttf"
                size 24
                color "#FFFFFF"
                line_spacing 8 # 줄 간격
                text_align 0.0 # 왼쪽 정렬 0.0 중앙 정렬 0.5 오른쪽 정렬 1.0

# =============================================================================
# 화면 중앙 메시지 스크린 (챕터 획득 등)
# =============================================================================
screen framed_message(message_text, text_size=60):
    zorder 200
    
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 80
        ypadding 40
        background Frame(Solid("#000000CC"), 20, 20)
        
        text message_text:
            font "fonts/HeirofLightRegular.ttf"
            size text_size
            color "#FFD700"
            text_align 0.5

