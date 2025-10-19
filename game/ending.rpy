# 엔딩과 결과 페이지 스크립트

# =============================================================================
# 캐릭터별 개별 엔딩
# =============================================================================

#음악
define audio.outro = "audio/bgm/outro_bgm.mp3"
define audio.outro_scene3 = "audio/bgm/outro_scene3.mp3"

#이미지
# bg desk는 intro에서 정의됨.
image outro_memory_orb = At("bg/outro/outro_memory_orb.png", custom_size)
image outro_memory_orb_hover = At("bg/outro/outro_memory_orb_hover.png", custom_size)
image outro_book = At("bg/outro/outro_book.png", custom_size)
image bg_bookback = At("bg/outro/book_back.png", custom_size)
image im_ending = At("bg/outro/im_ending.png", custom_size)
image oh_ending = At("bg/outro/oh_ending.png", custom_size)
image jang_ending = At("bg/outro/jang_ending.png", custom_size)

# === 토글용 변수 기본값  ===
default end2_show_a = False
default end2_show_b = False
default end2_show_c = False

# =========================================
# 엔딩 씬
# =========================================

# 엔딩 시작
label ending_start:
    play music audio.outro
    scene bg_desk with dissolve
    
    m "마지막 기억 구슬을 찾고 현실 세계로 복귀했다."
    m "하도 생생해서 꿈인지 현실인지 모르겠다."
    
    m "아 맞다. 시험 공부! 빨리 책상에 앉아서 공부해야겠다."

    m "이게 뭐지? 처음 보는 책인데..?"
    
    # 장기영 전용 책 표시
    show screen mission_guide("책을 펴보자.", icon="🔍")
    call screen interactive_objects("outro_book", use_alpha=True)
    hide screen mission_guide
    
    jump ending_scene2

    return

# 장기영 엔딩
label ending_scene2:
    if character_ending == "jang_ending":
        scene jang_ending with fade_fast
    elif character_ending == "oh_ending":
        scene oh_ending with fade_fast
    else:
        scene im_ending with fade_fast

    # 미션 가이드는 잠깐 보여주고(0.8초 예시) 숨김
    show screen mission_guide("더 알고싶은 사건에 마우스를 올려보자..", icon="🔍")
    pause 0.8

    # 장기영 전용 토글 변수 초기화
    $ end2_show_a = end2_show_b = end2_show_c = False

    # 토글 화면 + 우하단 네비 표시
    if character_ending == "jang_ending":
        show screen jang_ending_scene2_ui
    elif character_ending == "oh_ending":
        show screen oh_ending_scene2_ui
    else:
        show screen im_ending_scene2_ui
    show screen next_nav_to("ending_scene3")

    # 유저가 버튼 누를 때까지 대기
    $ renpy.pause(hard=True)
    
    return

label ending_scene3:
    scene bg_black with dissolve
    pause 1.0
    show screen outro_book_screen()
    pause 1.0
    hide screen outro_book_screen with dissolve
    jump ending_scene4

label ending_scene4:
    scene bg_bookback with fade_very_slow

    # 기억구슬 등장
    play sound audio.outro_scene3

    play sound memory_orb_appear fadein 0.5 fadeout 3.0
    pause 1.0
    
    # 클릭 후 사라짐
    show screen mission_guide("기억구슬을 눌러보세요.", icon="🔮")
    call screen interactive_objects("outro_memory_orb") with dissolve
    hide screen mission_guide

    pause 0.5
    
    # 블랙아웃
    scene bg_black with fade_slow
    pause 2.0

    narrator "이 순간도 기억 구슬에 담겼습니다."
    narrator "오늘 독립운동가와 함께 획득한 기억 구슬들을\n앞으로도 떠올려주세요."

    jump end_credits
    
# 최종 크레딧
label end_credits:
    show screen outro_book_screen()
    pause 1.0
    
    show screen exit_button  # 나가기 버튼 표시
    
    narrator "제작 : 고려대학교 HUSS  고연우, 강지온, 길유진, 안지원, 양예진, \n이민욱, 정정비, 정채연, 조정현, 최가빈"

# =========================================
# 스크린 정의
# =========================================

# === 책 화면 스크린 ===
screen outro_book_screen():
    add "bg_desk"
    add "outro_book"

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
            Hide("mission_guide"),
            Hide("next_nav_to"),
            Dissolve(1.0),
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
            Hide("outro_book_screen"),
            Jump("start")  # 또는 MainMenu() - 메인 메뉴로 돌아가기
        ]

# === 임규 엔딩 씬2 본문 UI (토글 영역) ===
screen im_ending_scene2_ui(): # 파라미터를 리스트로 하면 text를 여러 개 넣을 수 있을 듯?
    
    # 토글 A
    vbox:
        pos (980, 215)
        
        textbutton "✅" action ToggleVariable("end2_show_a")
        if end2_show_a:
            vbox:
                xoffset 30
                spacing 4
                text "1895년 - 게이오의숙 중학교 특별과, 1900년 - 센슈학교 경제과, \n1907년 도쿄 청년학원 교사 (조선인 유학생에게 일본어 가르침)" color "#000000"

    # 토글 B
    vbox:
        pos (980, 520)  # 여기 y값 조정하세요
        
        textbutton "✅" action ToggleVariable("end2_show_b")
        if end2_show_b:
            vbox:
                xoffset 30
                spacing 4
                text "천도교 측의 대표로, 개신교 측 안세환과 함께 일본 정부, 귀족원,\n중의원에 독립선언서 3통과 의견서 및 기타 첨부 문서를 전달"

    # 토글 C
    vbox:
        pos (980, 715)  # 여기 y값 조정하세요
        
        textbutton "✅" action ToggleVariable("end2_show_c")
        if end2_show_c:
            vbox:
                xoffset 30
                spacing 4
                text "미륵암에서 한용운, 정인보, 오세창 등과 모여 시를 지었다.\n<북산선고>는 최규동의  권유로 한시 24편을 모은 것"

# === 장기영 엔딩 씬2 본문 UI (토글 영역) ===
screen jang_ending_scene2_ui():
    
    # 토글 A - 축구 관련
    vbox:
        pos (980, 215)
        
        textbutton "✅" action ToggleVariable("end2_show_a")
        if end2_show_a:
            vbox:
                xoffset 30
                spacing 4
                text "1905년 - 대한축구협회 창립 멤버\n조선 최초의 축구팀 '대한축구단' 창단에 참여" color "#000000"

    # 토글 B - 교육 관련
    vbox:
        pos (980, 520)
        
        textbutton "✅" action ToggleVariable("end2_show_b")
        if end2_show_b:
            vbox:
                xoffset 30
                spacing 4
                text "보성전문학교에서 체육 교육을 통해 청년들에게\n민족 정신과 체력 단련의 중요성을 가르쳤다." color "#000000"

    # 토글 C - 독립운동 관련
    vbox:
        pos (980, 715)
        
        textbutton "✅" action ToggleVariable("end2_show_c")
        if end2_show_c:
            vbox:
                xoffset 30
                spacing 4
                text "체육을 통한 민족 의식 고취와 청년 계몽 운동에 헌신\n스포츠를 통해 일제강점기 조선인들에게 희망을 전했다." color "#000000"

# === 오세창 엔딩 씬2 본문 UI (토글 영역) ===
screen oh_ending_scene2_ui():
    
    # 토글 A - 서예와 문화 관련
    vbox:
        pos (980, 215)
        
        textbutton "✅" action ToggleVariable("end2_show_a")
        if end2_show_a:
            vbox:
                xoffset 30
                spacing 4
                text "조선 후기 서예가로 전통 서예 문화를 보존하고 발전시켰다.\n한국 서예사에 큰 족적을 남긴 대표적인 서예가 중 한 명이다." color "#000000"

    # 토글 B - 신문과 출판 관련
    vbox:
        pos (980, 520)
        
        textbutton "✅" action ToggleVariable("end2_show_b")
        if end2_show_b:
            vbox:
                xoffset 30
                spacing 4
                text "박문국에서 <한성주보> 발행, <만세보> 창간, <대한민보> 편찬\n우리나라 최초의 신문 연재 만화와 풍자소설 <금수재판> 게재" color "#000000"

    # 토글 C - 독립운동 관련
    vbox:
        pos (980, 715)
        
        textbutton "✅" action ToggleVariable("end2_show_c")
        if end2_show_c:
            vbox:
                xoffset 30
                spacing 4
                text "3.1 만세운동 민족 대표 33인 중 1인으로 독립선언서에 서명\n천도교 대표로 대한독립선언서 작성과 만세운동 준비에 참여" color "#000000"