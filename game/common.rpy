# 공동 사용 코드 정의

# =============================================================================
# 트랜지션 정의
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
# 변수 정의
# =============================================================================

# =============================================================================
# 이미지 정의
# =============================================================================

# 임무창
image ui_mission_guide = At("ui_screen/ui_mission_guide.png", custom_size)

# 기억구슬
image memory_orb-1 = "bg/memory_orb-1.png"
image memory_orb-2 = "bg/memory_orb-2.png"
image memory_orb-3 = "bg/memory_orb-3.png"
image memory_orb-4 = "bg/memory_orb-4.png"
image memory_orb-1_hover = "bg/memory_orb-1_hover.png"
image memory_orb-2_hover = "bg/memory_orb-2_hover.png"
image memory_orb-3_hover = "bg/memory_orb-3_hover.png"
image memory_orb-4_hover = "bg/memory_orb-4_hover.png"

# 상태창
image ui_ch1 = At("ui_screen/ui_ch1.png", custom_size)
image ui_ch2 = At("ui_screen/ui_ch2.png", custom_size)
image ui_ch3 = At("ui_screen/ui_ch3.png", custom_size)
image ui_ch4 = At("ui_screen/ui_ch4.png", custom_size)
image ui_orb_found_ch1 = At("ui_screen/ui_orb_found_ch1.png", custom_size)
image ui_orb_found_ch2 = At("ui_screen/ui_orb_found_ch2.png", custom_size)
image ui_orb_found_ch3 = At("ui_screen/ui_orb_found_ch3.png", custom_size)
image ui_orb_found_ch4 = At("ui_screen/ui_orb_found_ch4.png", custom_size)

# =============================================================================
# 사운드 정의
# =============================================================================

# 배경음
define audio.main_bgm = "audio/bgm/guk-ak_bgm.mp3"

# 기억구슬 효과음
define audio.memory_orb_appear = "audio/sfx/memory_orb_appear.mp3"
define audio.memory_orb_get = "audio/sfx/memory_orb_get.wav"

# =============================================================================
# 캐릭터 정의
# =============================================================================
define m = Character("나", color="#ffffff")
define m_thought = Character("나", color="#ffffff", what_italic=True)

define jang = Character("장기영", color="#ff6b6b")
define im = Character("임규", color="#4ecdc4")
define oh = Character("오세창", color="#45b7d1")

define jang_thought = Character("???", color="#ff6b6b", what_color="#888888", what_italic=True)
define im_thought = Character("???", color="#4ecdc4", what_color="#888888", what_italic=True)
define oh_thought = Character("???", color="#45b7d1", what_color="#888888", what_italic=True)

# =============================================================================
# 스크린 정의
# =============================================================================

# =========================================
# 정보 툴팁 스크린
# =========================================
screen info_tooltip(info_text):
    zorder 100
    
    # 물음표 아이콘 버튼
    frame:
        xalign 0.95
        yalign 0.05
        xysize (50, 50)
        background "#4169E1"
        padding (0, 0)
        
        button:
            xysize (50, 50)
            background None
            action NullAction()
            
            text "?":
                align (0.5, 0.5)
                size 35
                color "#FFFFFF"
                bold True
            
            # 마우스 호버 시 툴팁 표시
            hovered Show("tooltip_box", info=info_text)
            unhovered Hide("tooltip_box")

# 툴팁 박스 스크린
screen tooltip_box(info, xalign=0.75, yalign=0.05):
    zorder 101
    
    frame:
        xalign xalign
        yalign yalign
        xmaximum 500
        background "#2C3E50"
        padding (20, 20)
        
        text info:
            size 20
            color "#FFFFFF"
            line_spacing 5
            text_align 0.0

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