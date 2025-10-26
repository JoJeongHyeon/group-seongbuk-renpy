# 공동 사용 코드 정의

# =============================================================================
# 변수 정의
# =============================================================================

# =============================================================================
# 이미지 정의
# =============================================================================

# =============================================================================
# 음악 정의
# =============================================================================





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
# =============================================================================
# 네비 버튼 스크린
# =============================================================================
# === 우하단 네비 버튼 (오버레이) ===
screen next_nav_to(label_name):
    zorder 200
    modal False
    textbutton "뒷 페이지 넘기기":
        anchor (1.0, 1.0)
        pos (0.97, 0.95)     # 1920x1080 기준 오른쪽 하단(비율 좌표)
        # 픽셀로 고정하고 싶으면: xpos 1840 ypos 1015
        action [
            Hide("im_ending_scene2_ui"),
            Hide("jang_ending_scene2_ui"),
            Hide("oh_ending_scene2_ui"),
            Hide("next_nav_to"),
            Jump(label_name)
        ]

# === 우하단 나가기 버튼 ===
screen exit_button():
    zorder 200
    modal False
    textbutton "나가기":
        anchor (1.0, 1.0)
        pos (0.97, 0.95)     # 1920x1080 기준 오른쪽 하단(비율 좌표)
        # 픽셀로 고정하고 싶으면: xpos 1840 ypos 1015
        action [
            Hide("exit_button"),
            Jump("start")  # 또는 MainMenu() - 메인 메뉴로 돌아가기
        ]