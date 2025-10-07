# 정현 담당
# 장기영 루트 스크립트
# script.rpy의 정의들을 모두 사용 가능

# =============================================================================
# 이미지 정의
# =============================================================================
# 챕터1 배경 이미지
image bg_room = At("bg/main_jang/ch1/room.png", custom_size)
image bg_passport_doc = At("bg/main_jang/ch1/passport_doc.png", custom_size)
image bg_passport_doc-hover = At("bg/main_jang/ch1/passport_doc-hover.png", custom_size)
image bg_harbor = At("bg/main_jang/ch1/harbor.png", custom_size)
image bg_shanghai_gov = At("bg/main_jang/ch1/shanghai_gov.png", custom_size)

# 챕터1 캐릭터 이미지
image kim = Transform("ch/kim.png", zoom=0.8)
image ahn = Transform("ch/ahn.png", zoom=0.8)

# 기억구슬
image memory_orb = "bg/memory_orb.png"

# 챕터2 배경 이미지
image bg_usa_street = At("bg/main_jang/ch2/usa_street.png", custom_size)
image bg_usa_street-dark = At("bg/main_jang/ch2/usa_street-dark.png", custom_size)
image bg_usa_street-letter = At("bg/main_jang/ch2/usa_street-letter.png", custom_size)
image bg_office = At("bg/main_jang/ch2/office.png", custom_size)

# 챕터2 오브젝트 이미지
image envelop = "bg/main_jang/ch2/envelop.png"
image envelop_hover = "bg/main_jang/ch2/envelop_hover.png"
image money-1 = At("bg/main_jang/ch2/money-1.png", custom_size)
image money-2 = At("bg/main_jang/ch2/money-2.png", custom_size)
image money-3 = At("bg/main_jang/ch2/money-3.png", custom_size)
image bubble-1 = At("bg/main_jang/ch2/bubble-1.png", custom_size)
image bubble-2 = At("bg/main_jang/ch2/bubble-2.png", custom_size)
image bubble-3 = At("bg/main_jang/ch2/bubble-3.png", custom_size)

# 챕터2 캐릭터 이미지
image lee = Transform("ch/lee.png", zoom=0.8)

# =============================================================================
# 오디오 정의
# =============================================================================
define audio.boat_horn = "audio/sfx/boat_horn.mp3"

# =============================================================================
# 캐릭터 정의 (장기영 전용)
# =============================================================================
# 장기영의 속마음 (회색 텍스트)
define jang_thought = Character(None, what_color="#888888", what_italic=True)

# ch1 김구, 안창호 선생님 
define kim = Character("김구", color="#ffd700")
define ahn = Character("안창호", color="#4dcf7f")
define kim_ahn = Character("김구, 안창호", color="#37c2f5")

# ch2 이승만
define lee = Character("이승만", color="#ff6b9d", what_line_spacing = 14)

# =============================================================================
# 챕터1로 이동
# =============================================================================
label character_jang:
    # 챕터1로 진입
    jump jang_ch1

# =============================================================================
# 챕터1: 주오대학 졸업 후 안창호, 김구의 권유를 받고 미국으로 건너가 학업을 계속함
# =============================================================================
label jang_ch1:
    # Scene 1: 일본 대학생의 방
    
    # 검은 배경에서 페이드인
    scene bg_black
    pause 1.0
    
    scene bg_room with fade_very_slow
    
    jang_thought "일본과 싸우려면 먼저 일본을 알아야 한다는 생각으로 건너왔건만, 일본 관헌의 감시는 여전하구나"
    
    # 화면 전환
    scene bg_black with fade_fast
    pause 0.5
    scene bg_room with fade_slow
    
    m "지금 이게 무슨 소리지? 밖에서 나는 소리는 아닌 것 같은데…일본과 싸워? 관헌의 감시는 또 무슨 말이야."
    
    narrator "속에서 울리는 소리에 나는 지금까지 일어난 이상한 일이 꿈이라는 것을 깨닫고 눈을 떴지만, 여전히 낯선 공간이다."
    
    m "이 책은 뭐지? 경제학 공부하는 학생인가? 이건 여권 신청서?"
    
    # 여권 신청서 인터랙티브 화면
    call screen interactive_passport_doc
    
    # 여권 신청서를 클릭한 후
    jump jang_ch1_passport_choice

label jang_ch1_passport_choice:

    show bg_passport_doc with dissolve

    pause 1.5

    menu:
        "여권 신청":
            # '신청 거절' 텍스트 표시
            show text "{size=80}{color=#ff0000}신청 거절{/color}{/size}" at truecenter with dissolve
            pause 2.0
            hide text with dissolve
            jump jang_ch1_passport_choice
        
        "여권 신청 ":  # 공백으로 구분하여 두 번째 선택지
            # '신청 거절' 텍스트 표시

            show text "{size=80}{color=#ff0000}신청 거절{/color}{/size}" at truecenter with dissolve
            pause 2.0
            hide text with dissolve
            
            m "뭐지? 버그인가?"
            
            hide bg_passport_doc with dissolve
            scene bg_room with fade_fast
            
            narrator "미국으로 가야 한다. 미국으로 가야 한다. 같은 소리가 머릿속에서 반복되어서 들린다."
            
            jump jang_ch1_destination_choice

label jang_ch1_destination_choice:
    menu:
        "미국으로 가기":
            # '여권 없음' 텍스트 표시
            show text "{size=80}{color=#ff0000}여권 없음{/color}{/size}" at truecenter with dissolve
            pause 2.0
            hide text with dissolve
            jump jang_ch1_destination_choice
        
        "상해로 가기":
            narrator "중국인으로 속이고 우선 상해에 무사히 도착했다."
            jump jang_ch1_scene2

# =============================================================================
# Scene 2: 항구 → 상해임시정부
# =============================================================================
label jang_ch1_scene2:
    # 항구 배경
    scene bg_harbor with fade_slow
    
    # 뱃고동 소리 효과음
    play sound boat_horn
    pause 2.0
    
    narrator "이곳이 상해구나."
    
    jang_thought "상해에 왔으니, 임시정부에 있는 위원들을 찾아가 보자. 미국으로 갈 수 있는 방법을 찾을 수 있을 거야"
    
    m "상해임시정부? 아, 나 설마 지금 일제강점기에 와 있는 거야?"
    
    narrator "아직 꿈인가 봐. 원래 이 몸의 주인 목소리인 것 같으니 따라보자."
    
    # 상해임시정부 건물 앞으로 전환
    scene bg_shanghai_gov with dissolve
    
    # 김구, 안창호 선생님 등장
    show kim at left with dissolve
    show ahn at right with dissolve
    
    kim_ahn "상해에서 함께 활동해 주어서 고맙네. 전한군사위원회(全韓軍事委員會)의 위원으로도 활약한 자네였기에 더욱 든든했어. 미국 땅으로 가서 하던 공부를 이어서 하고 조국의 광복을 위해 힘써주게나."
    
    narrator "이분들은 김구 선생님과 안창호 선생님? 교과서에서 봤어! 나는 독립운동가의 몸에 들어왔나 봐!"

label jang_ch1_final_choice:
    menu:
        "저는 여기가 좋아요.":
            narrator "내가 지금 정확히 누구 몸에 들어왔는지는 모르겠지만 이 사람이 원하는 대로 해보자"
            jump jang_ch1_final_choice
        
        "가겠습니다.":
            hide kim
            hide ahn
            with dissolve
            
            # 기억구슬 등장
            show memory_orb with dissolve
            pause 1.0
            
            # 화면 중앙에 텍스트 표시 (프레임 배경 포함)
            show screen framed_message("++챕터1 기억구슬 획득++", text_size=60)
            with dissolve

            pause 3.0
            hide screen framed_message with dissolve
            
            # 블랙아웃
            scene bg_black with fade_slow
            pause 2.0
            
            # 챕터2로 이어짐
            jump jang_ch2

# =============================================================================
# 챕터2: 구미위원부 위원으로 임명된 후 독립자금 및 교민 독립사상 고취 활동
# =============================================================================
label jang_ch2:
    # Scene 1: 1930년대 미국 길거리
    
    # 블랙아웃 유지 (챕터1의 블랙아웃에서 이어짐)
    scene bg_black
    pause 1.0
    
    scene bg_usa_street with fade_very_slow
    
    narrator "이상한 구슬을 손에 쥐자, 미국 본토에 도착했다."
    
    # 화면 전환
    scene bg_black with fade_fast
    pause 0.5
    scene bg_usa_street with fade_slow
    
    jang_thought "호놀룰루의 교회에서 뵈었던 이박사님께서는 언제 본토에 들어오시는 것인가?"
    
    jang_thought "1, 2년 뒤면 올 것이라 하셨는데 벌써 5년이나 지났다."
    
    jang_thought "어서 연락이 닿아서 내가 이 땅에서 할 수 있는 일을 하고 싶어."
    
    m "뭐? 5년? 미국 본토로 바로 올 수 있었던 것이 아니구나. 이분은 어떤 독립운동을 하셨던 걸까?"
    
    jang_thought "나는 지금 내가 당장 할 수 있는 일에 집중해야겠어."
    
    jang_thought "인디애나 대학에서의 국제법 공부는 일본과 맞서 싸우는 것에 도움이 될 것이야."
    
    m "어라? 이 편지봉투는 뭐지?"
    
    # 전보 인터랙티브 화면
    call screen interactive_envelope
    
    # 전보를 클릭한 후 - 편지 내용 표시
    scene bg_usa_street-letter with dissolve
    pause 2.0
    
    m "상의할 것이 있으니, 워싱턴에 있는 구미위원부로 와달라고? 누가 보낸 거야? 이승만이라면!"
    
    m "아까 그 이박사가 이승만 선생님이었구나!"
    
    # 블랙아웃
    scene bg_black with fade_slow
    pause 1.0
    
    narrator "나는 조국의 독립을 위하여 곧장 달려갔다."
    
    jump jang_ch2_scene2

# =============================================================================
# Scene 2: 구미위원부 사무실
# =============================================================================
label jang_ch2_scene2:
    # 블랙아웃에서 시작
    scene bg_black
    pause 1.0
    
    jang_thought "나는 조국의 독립을 위하여 곧장 달려갔다."
    
    # 구미위원부 사무실로 전환
    scene bg_office with fade_slow
    
    # 이승만 등장
    show lee with dissolve
    
    lee "기다리던 중 빨리 와주어 고맙소."
    
    lee "국제연맹에 가 항의할 것이 있어 그런데…"
    
    lee "석정이 구미위원부 위원이 되어 이곳 사무실을 지켜줄 수 있겠는가?"

label jang_ch2_gumi_choice:
    menu:
        "워싱턴과 뉴욕에 있는, 저보다 선배인 이들에게 맡기는 것이 좋지 않겠습니까?":
            lee "일본대학을 졸업한 사람이 일본 사람의 심부름이 싫어 미국으로 온 줄 알았는데 일본 사람에게 협조하러 이곳에 온 것이로군"
            jump jang_ch2_gumi_choice
        
        "알겠습니다. 여기에 남아 일하겠습니다. 내일이라도 곧 떠나십시오.":
            lee "우리 구미위원부에서는 일본의 만행을 세계에 알리고, \n독립 자금을 모집하고, 교민들의 독립사상을 고취하는 일을 하고 있다네."
            
            hide lee with dissolve
            
            narrator "독립운동을 하기 위한 돈을 모으고, 해외에 거주하고 있는 우리나라 사람에게 독립의 중요성을 알린다는 뜻이구나!"
            
            narrator "열심히 해보자!"
            
            # 블랙아웃
            scene bg_black with fade_slow
            pause 2.0
            
            # Scene3로 이어짐
            jump jang_ch2_scene3

# =============================================================================
# Scene 3: 1930년대 미국 길거리 - 독립자금 모금 활동
# =============================================================================
label jang_ch2_scene3:
    # 블랙아웃에서 시작
    scene bg_black
    pause 1.0
    
    # 1930년대 미국 길거리 배경
    scene bg_usa_street with fade_slow
    pause 1.0
    
    narrator "거리에서 독립자금 모금 활동을 시작했다."
    
    narrator "하지만 많은 사람들이 의구심과 회의적인 반응을 보였다."
    
    # 인터랙티브 스크린 호출
    call screen interactive_fundraising
    
    # 모든 말풍선을 클릭한 후
    jump jang_ch2_finale

label jang_ch2_finale:
    # 블랙아웃
    scene bg_black with fade_slow
    pause 1.5

    # 기억구슬 등장
    scene bg_usa_street with dissolve
    show memory_orb with dissolve
    pause 1.0
    
    # 화면 중앙에 텍스트 표시
    show screen framed_message("++챕터2 기억구슬 획득++", text_size=60)
    pause 3.0
    hide screen framed_message with dissolve
    
    hide memory_orb with dissolve
    
    # 블랙아웃
    scene bg_black with fade_slow
    pause 2.0
    
    # 챕터3로 이어짐 (나중에 구현)
    jump jang_ch3_placeholder

label jang_ch3_placeholder:
    narrator "챕터2가 완료되었습니다. 챕터3은 준비 중입니다."
    return

# =============================================================================
# 인터랙티브 스크린
# =============================================================================

# Scene 3 인터랙티브 스크린 변수
init python:
    clicked_bubble1 = False
    clicked_bubble2 = False
    clicked_bubble3 = False
    clicked_money1 = False
    clicked_money2 = False
    clicked_money3 = False
    show_jang_response = False
    current_jang_text = ""

screen interactive_fundraising():
    
    add "bg_usa_street-dark" at custom_size
    
    # 화폐 이미지들
    if not clicked_money1:
        add "money-1"
    
    if not clicked_money2:
        add "money-2"
    
    if not clicked_money3:
        add "money-3"
    
    # 말풍선 1
    if not clicked_bubble1:
        imagebutton:
            idle "bubble-1"
            hover Transform("bubble-1", alpha=0.8)
            focus_mask True
            action [
                SetVariable("clicked_bubble1", True),
                SetVariable("clicked_money1", True),
                SetVariable("show_jang_response", True),
                SetVariable("current_jang_text", "작은 외침이 모여야 큰 목소리가 되고, 그제야 세계가 우리를 들을 수 있습니다."),
                Hide("interactive_fundraising"),
                Show("interactive_fundraising")
            ]
    
    # 말풍선 2
    if not clicked_bubble2:
        imagebutton:
            idle "bubble-2"
            hover Transform("bubble-2", alpha=0.8)
            focus_mask True
            action [
                SetVariable("clicked_bubble2", True),
                SetVariable("clicked_money2", True),
                SetVariable("show_jang_response", True),
                SetVariable("current_jang_text", "조국 없는 삶은 결국 뿌리 없는 삶이니, 우리 후손에게는 반드시 독립된 나라를 물려주어야 합니다."),
                Hide("interactive_fundraising"),
                Show("interactive_fundraising")
            ]
    
    # 말풍선 3
    if not clicked_bubble3:
        imagebutton:
            idle "bubble-3"
            hover Transform("bubble-3", alpha=0.8)
            focus_mask True
            action [
                SetVariable("clicked_bubble3", True),
                SetVariable("clicked_money3", True),
                SetVariable("show_jang_response", True),
                SetVariable("current_jang_text", "당신의 작은 헌신이 모여 독립군의 총알이 되고, 세계에 조국의 목소리를 이어줍니다."),
                Hide("interactive_fundraising"),
                Show("interactive_fundraising")
            ]
    
    # 장기영의 응답 표시 (화면 하단)
    if show_jang_response and current_jang_text:
        frame:
            xalign 0.5
            ypos 800
            xsize 1050
            background Frame(Solid("#333333DD"), 20, 20)
            padding (40, 30)
            
            vbox:
                text "장기영" size 32 color "#ff6b6b"xalign 0.0
                text " " size 20
                text current_jang_text size 30 color "#FFFFFF" line_spacing 13
                
                textbutton "▶ 계속":
                    xalign 0.5
                    ypos 10
                    text_size 28
                    text_color "#FFD700"
                    text_hover_color "#FFA500"
                    action [
                        SetVariable("show_jang_response", False),
                        SetVariable("current_jang_text", ""),
                        Hide("interactive_fundraising"),
                        Show("interactive_fundraising")
                    ]
    
    # 모든 말풍선을 클릭했는지 확인
    if clicked_bubble1 and clicked_bubble2 and clicked_bubble3 and not show_jang_response:
        frame:
            xalign 0.5
            yalign 0.9
            background Frame(Solid("#00CC00DD"), 20, 20)
            padding (30, 20)
            
            textbutton "✓ 모든 응답 완료 - 클릭하여 계속":
                text_size 36
                text_color "#FFFFFF"
                text_hover_color "#FFFF00"
                action Return("all_bubbles_clicked")

screen interactive_passport_doc():
    
    # 클릭 가능한 여권 신청서 영역
    imagemap:
        ground "bg_room"
        hover "bg_passport_doc-hover"  # hover 이미지
        alpha True
        at custom_size

        hotspot (0, 0, 1920, 1080):  # 전체 화면 클릭 가능
            action Return("passport_clicked")

screen interactive_envelope():
    
    # 기본 배경
    add "bg_usa_street" at custom_size
    
    # 클릭 가능한 전보 봉투 영역
    imagebutton:
        idle "envelop"
        hover "envelop_hover"
        focus_mask True
        at truecenter
        action Return("envelope_clicked")