# 가빈 담당
# 오세창 루트 스크립트  
# script.rpy의 정의들을 모두 사용 가능

# =========================================
# 오세창 루트:
# =========================================
# -------- 배경/오브젝트 이미지 정의 --------
#chap1
image bg_appointment = At("images/bg/main_oh/ch1/appointment.png", custom_size)
image bg_bakmunguk = At("images/bg/main_oh/ch1/bakmunguk.png", custom_size)
image bg_bakmunguk_shutdown = At("images/bg/main_oh/ch1/bakmunguk_shutdown.png", custom_size)
image bg_harbor = At("images/bg/main_oh/ch1/harbor.png", custom_size)
image bg_tradeoff_1 = At("images/bg/main_oh/ch1/tradeoff/1.png", custom_size)
image bg_tradeoff_2 = At("images/bg/main_oh/ch1/tradeoff/2.png", custom_size)
image bg_tradeoff_3 = At("images/bg/main_oh/ch1/tradeoff/3.png", custom_size)
image bg_tradeoff_4 = At("images/bg/main_oh/ch1/tradeoff/4.png", custom_size)
image bg_tradeoff_5 = At("images/bg/main_oh/ch1/tradeoff/5.png", custom_size)
image bg_ink_1 = At("images/bg/main_oh/ch1/ink/1.png", custom_size)
image bg_ink_2 = At("images/bg/main_oh/ch1/ink/2.png", custom_size)
image bg_ink_3 = At("images/bg/main_oh/ch1/ink/3.png", custom_size)
image bg_ink_4 = At("images/bg/main_oh/ch1/ink/4.png", custom_size)
image bg_ink_5 = At("images/bg/main_oh/ch1/ink/5.png", custom_size)
image bg_ink_6 = At("images/bg/main_oh/ch1/ink/6.png", custom_size)
image bg_ink_7 = At("images/bg/main_oh/ch1/ink/7.png", custom_size)
image bg_ink_8 = At("images/bg/main_oh/ch1/ink/8.png", custom_size)

#chap2
image bg_talk = At("images/bg/main_oh/ch2/talk.png", custom_size)
image bg_news_machine = At("images/bg/main_oh/ch2/news_machine.png", custom_size)
image bg_clock_12 = At("images/bg/main_oh/ch2/clock/12.png", custom_size)
image bg_clock_3 = At("images/bg/main_oh/ch2/clock/3.png", custom_size)
image bg_clock_6 = At("images/bg/main_oh/ch2/clock/6.png", custom_size)
image bg_clock_9 = At("images/bg/main_oh/ch2/clock/9.png", custom_size)
image bg_critique_ijh = At("images/bg/main_oh/ch2/critique/ijh.png", custom_size)
image bg_critique_lgt = At("images/bg/main_oh/ch2/critique/lgt.png", custom_size)
image bg_critique_ljy = At("images/bg/main_oh/ch2/critique/ljy.png", custom_size)
image ijh_critique = "images/bg/main_oh/ch2/jokja/igh_critique.png"
image education = "images/bg/main_oh/ch2/jokja/education.png"
image daehan = "images/bg/main_oh/ch2/jokja/daehan.png"
image taegeuk_box = "images/bg/main_oh/ch2/taegeuk_box.png"

# -------- BGM/효과음 --------
define audio.oh_main_bgm = "audio/bgm/oh_main_bgm.mp3"
define audio.oh_ch1 = "audio/bgm/oh_ch1.mp3"
define audio.oh_ch2 = "audio/bgm/oh_ch2.mp3"

# 캐릭터 설정
define wife = Character("부인", color="#6bffba")

# =========================================
# 라벨: 오세창 루트 
# =========================================
label character_oh:
    jump oh_chap1

# =========================================
# Ch1. 박문국 주사 → 신문 발행 → 폐지 → 망명
# =========================================
label oh_chap1:
    play music oh_main_bgm fadein 1.0 loop
    
    scene bg_appointment with fade_slow
    m "오케이! 빨리 기억 구슬을 찾고 돌아가야겠어!"
    m "뭐야. 내가 조선시대의 관복을 입고 있잖아?"
    m "관직 임명장? 내가 신문, 잡지 등을 만드는 조선시대 국가 기관인 박문국의 팀장이라고?"
    wife "당신, 출근 안 해요? 얼른 다녀와요."
    m "출근? 내가? 일단 아무것도 모르겠지만 일단 내가 대신 출근해 보자…"
    
    "박문국에 출근했다. 우리나라 최초의 주간 신문인 <한성주보>를 발행하는 것이 내 업무라고 한다."
    m "오, 그럼 신문을 만들어 볼까?"
    scene bg_bakmunguk with fade_fast
    # 신문 발행 시퀀스 
    menu:
        "신문 발행하기":
            #동전 -> 신문 트레이드오프 애니메이션
            scene bg_tradeoff_1
            pause 0.90
            scene bg_tradeoff_2
            pause 0.90
            scene bg_tradeoff_3
            pause 0.90
            scene bg_tradeoff_4
            pause 0.90
            scene bg_tradeoff_5
            pause 0.90

    stop music fadeout 1.0
    "박문국의 돈이 다 떨어져 더 이상 신문을 만들 수 없게 되었다."
    
    scene bg_bakmunguk_shutdown with fade_fast
    play music oh_ch1 fadein 1.0
    
    "후에 나는 몸의 주인을 대신해서 여러 곳에서 관직 생활을 했지만, 곧 역모에 휘말리게 되었다..."

    # ----- 잉크 번짐 전환 (bg_bakmunguk_shutdown 위) -----
    scene bg_bakmunguk_shutdown with fade_fast

    python:
    # (이미 bg_bakmunguk_shutdown이 아래에서 보이는 상태)
        ink_frames = [
            ("bg_ink_1", 0.80),
            ("bg_ink_2", 0.70),
            ("bg_ink_3", 0.60),
            ("bg_ink_4", 0.50),
            ("bg_ink_5", 0.40),
            ("bg_ink_6", 0.35),
            ("bg_ink_7", 0.30),
            ("bg_ink_8", 0.25),
        ]
    
    # 순차적으로 먹물 이미지 겹치기
        for name, delay in ink_frames:
            renpy.show(name, at_list=[], layer="overlay")  # bg_bakmunguk_shutdown 위에 겹치게 표시
            renpy.pause(delay, hard=True)
    

    
    # 먹물 애니메이션 (overlay 레이어 사용)
    #python:
        #for i in range(1, 9):
            #name = f"bg_ink_{i}"
            #renpy.show(name, at_list=[], layer="overlay")
            #renpy.pause(0.70, hard=True)
        # 마지막 프레임 유지하면서 배경 교체
        #renpy.scene()  # 기존 배경 제거
        #renpy.show("bg_black")
        #renpy.pause(0.4, hard=True)
        # overlay 레이어 정리
        #for i in range(1, 9):
            #renpy.hide(f"bg_ink_{i}", layer="overlay")

    

        
    scene bg_black
    m "어떡하지? 이러다가는 목숨을 잃고 말 거야….어디로든 도망가야 해!"
    
    # 망명 선택
    call exile_menu_loop
    
    # 망명 후 항구 장면
    scene bg_harbor with fade_fast
    m "어쩔 수 없다. 일본으로 망명해야겠다."
    m "어? 저 빛나는 건 뭔지? 눌러봐야겠다."
    m "기억 구슬이 맞나 보구나!"
    
    stop music fadeout 1.0
    # Ch1 종료, Ch2로 이어짐
    jump oh_chap2

# =========================================
# 망명 결정 루프
# =========================================
label exile_menu_loop:
    menu:
        "어떻게 할까?"
        
        "일본으로 망명하기":
            return
        
        "그대로 살기":
            "이건 아닌 것 같다. 까딱하면 내가 죽을 수도 있어!"
            jump exile_menu_loop

# =========================================
# Ch2. 
# =========================================
label oh_chap2:
    scene bg_black with fade_slow
    play music oh_main_bgm fadein 1.0 loop
    m "휴, 일본으로 도망쳐서 겨우 살았네."
    "일본으로 망명해서 다카지마 류조로 살던 도중, 천도교 교주인 손병희를 만났다."
    
    scene bg_talk with fade_fast
    

    scene bg_clock_12 
    pause 0.60
    scene bg_clock_3
    pause 0.50
    scene bg_clock_6
    pause 0.40
    scene bg_clock_9
    pause 0.35
    scene bg_clock_12
    pause 0.30
    scene bg_clock_3
    pause 0.20
    scene bg_clock_6
    pause 0.15
    scene bg_clock_9
    pause 0.10
    scene bg_clock_12
    pause 0.10
    scene bg_clock_3
    pause 0.05
    scene bg_clock_6
    pause 0.90

    m "시간이 흘러 드디어 귀국했다. 너무 그리웠어……."

    scene bg_black with fade_fast

    "나도 뭔가 사람들에게 도움이 되고 싶어."
    "대신해서 관직 업무를 하던 경험을 살려 할 수 있는 게 없을까?"
    m "아, 박문국 주사였던 경험이 있지!"
    "사람들의 교육을 위해 천도교 기관지를 만들자."
    "이름은 <만세보>가 좋겠는데?"
    stop music fadeout 1.0
    play music oh_ch2 fadein 1.0
    scene bg_news_machine with fade_fast

    m "민족 정신을 위해 친일파를 비판해야 하는 것이 옳아."
    m "일단 가장 먼저 친일 단체인 일진회의 문제점을 널리 알려야겠어!" 

    call menu_loop_ijh
    call menu_loop_ljy
    call menu_loop_lgt

    scene bg_news_machine with fade_fast
    m "친일파의 만행에 대해서 내가 직접 알리다니!"
    m "역사 시간에서 배우던 독립 운동을 직접 해 볼 수 있다는 게 너무 뿌듯하다."
    m "근데 하다 보니 일진회의 문제점이 너무 많잖아? 일진회를 막을 더 확실한 방법이 없을까?"
    m "하는 김에 민족 정신에 대한 교육도 더 집중적으로 할 수 있는 협회가 있었으면 좋겠어."
    "출근? 내가? 일단 아무것도 모르겠지만 일단 내가 대신 출근해 보자…"

    # 드래그 앤 드롭 미니게임
    call daehan_association_minigame

    # 드래그 앤 드롭 완료 후
    scene bg_news_machine with fade_fast
    "대한협회 결성!"
    m "이제 더 체계적으로 민족 정신을 지킬 수 있겠어!"
    "신문 찍는 기계 앞에서 기억구슬을 주웠다."
    stop music fadeout 1.0
    return

# =========================================
# 일진회 비판 메뉴
# =========================================
label menu_loop_ijh:
    menu:
        "일진회를 비판하는 글을 <만세보>에 싣자."
        
        "비판하기":
            scene bg_critique_ijh with fade_fast
            show screen info_tooltip("일진회: 일본이 우리나라를 차지하는 데에 앞장섰던 단체로, 처음에는 나라를 발전시키자고 했지만 나중에는 일본에 나라를 넘겨주는 데 도움을 준 친일단체")
            pause 1.5
            "아! 일진회 역적 무리들이 왜적과 결탁하여 을사늑약을 찬성하고 합병을 청원하니,"
            "이 어찌 동포를 배반하고 조종의 강토를 팔아먹는 천추의 역적 행위가 아니겠는가!"
            hide screen info_tooltip
            #일진회: 일본이 우리나라를 차지하는 데에 앞장섰던 단체로, 
            #처음에는 나라를 발전시키자고 했지만 나중에는 일본에 나라를 넘겨주는 데 도움을 준 친일단체
            return
        
        "비판하지 않기":
            m "우리나라를 일본에게 넘기는 것을 보고도 가만히 있는 게 맞을까?"
            jump menu_loop_ijh

# =========================================
# 이지용 비판 메뉴
# =========================================
label menu_loop_ljy:
    menu:
        "친일파인 내부대신 이지용 비판하기"
        
        "비판하기":
            scene bg_critique_ljy with fade_fast
            show screen info_tooltip("이지용: 조선 시대 말기에 살았던 왕족 출신의 관료로, 1905년에 일본이 우리나라의 외교권을 빼앗는 을사조약에 찬성한 '을사오적' 중 한 명")
            pause 1.5
            "내부대신 이지용은 대역무도한 역적으로, 왜놈의 협박에 굴복하여 을사늑약에 도장을 찍고"
            "삼천리 강토를 적에게 넘기니, 백성들의 원성이 하늘을 찌르도다!"
            hide screen info_tooltip
            #이지용: 조선 시대 말기에 살았던 왕족 출신의 관료로, 
            #1905년에 일본이 우리나라의 외교권을 빼앗는 을사조약에 찬성한 '을사오적' 중 한 명
            return
        
        "비판하지 않기":
            m "우리나라를 일본에게 넘기는 것을 보고도 가만히 있는 게 맞을까?"
            jump menu_loop_ljy

# =========================================
# 이근택 비판 메뉴
# =========================================
label menu_loop_lgt:
    menu:
        "친일파인 군부대신 이근택 비판하기"
        
        "비판하기":
            scene bg_critique_lgt with fade_fast
            show screen info_tooltip("이근택: 1905년 군부대신으로서 일본과 맺은 을사조약에 찬성해 우리나라 주권을 빼앗기는 데 앞장섰고, 이후 일본이 나라를 다스릴 때 중요한 자리를 맡아 친일 행위를 한 일제 강점기 대표적인 친일파")
            pause 1.5
            "군부대신 이근택은 나라의 군권을 지켜야 할 자리에 있으면서도"
            "왜적의 칼날 앞에 무릎 꿇고 을사늑약에 서명하여 국권을 도적질하였으니, 이 무슨 염치없는 배신인가!"
            hide screen info_tooltip
            #이근택: 1905년 군부대신으로서 일본과 맺은 을사조약에 찬성해 우리나라 주권을 빼앗기는 데 앞장섰고, 
            #이후 일본이 나라를 다스릴 때 중요한 자리를 맡아 친일 행위를 한 일제 강점기 대표적인 친일파
            return
        
        "비판하지 않기":
            m "우리나라를 일본에게 넘기는 것을 보고도 가만히 있는 게 맞을까?"
            jump menu_loop_lgt

# =========================================
# 대한협회 결성 드래그 앤 드롭 미니게임
# =========================================
label daehan_association_minigame:
    # 미니게임 변수 초기화
    $ items_placed = {"ijh_critique": False, "education": False}
    
    # 미니게임 화면 표시 - 루프로 변경
    label minigame_loop:
        call screen drag_drop_game
        
        # 두 개 모두 True가 될 때까지 반복
        if items_placed["ijh_critique"] and items_placed["education"]:
            return
        else:
            jump minigame_loop

screen drag_drop_game():
    modal True
    
    # 배경
    add "bg_news_machine"
    
    # 타이틀
    text "일진회 비판과 민족 정신에 대한 교육을 태극기 상자에 모두 올려주세요":
        xalign 0.5 
        ypos 50 
        size 40
        color "#000000"
    
    # ✅ 완료 체크: 둘 다 True면 자동 종료(문구 없이)
    if items_placed["ijh_critique"] and items_placed["education"]:
        key "dismiss" action Return()
    
    # --- (A) 태극기 상자 ---
    fixed:
        xpos 750
        ypos 500
        xysize (450, 450)
        add "taegeuk_box" zoom 0.3 xalign 0.5 yalign 0.5

        # ✅ 완료 시 단일 이미지 하나만 표시(daehan)
        if items_placed["ijh_critique"] and items_placed["education"]:
            add "daehan" zoom 0.3 xalign 0.5 yalign 0.70
    
    # --- (B) 드래그 그룹 및 드롭 영역 ---
    draggroup:
        # 투명 드롭 존(태극기 상자 히트박스)
        drag:
            drag_name "taegeuk_box"
            draggable False
            droppable True
            drag_raise False
            xpos 700
            ypos 800
            child Solid("#00000000", xysize=(550, 100))
        
        # 일진회 비판 카드
        if not items_placed["ijh_critique"]:
            drag:
                drag_name "ijh_critique"
                droppable False
                dragged drag_callback
                xpos 150
                ypos 200
                add "ijh_critique" zoom 0.08 

        # 민족 정신 교육 카드
        if not items_placed["education"]:
            drag:
                drag_name "education"
                droppable False
                dragged drag_callback
                xpos 1350
                ypos 200
                add "education" zoom 0.08
    

# 드래그 콜백 함수
init python:
    def drag_callback(drags, drop):
        # drop이 없으면 (태극기 상자 밖에 놓으면) 실패
        if drop is None:
            return False
        
        drag = drags[0]
        
        # 태극기 상자에 놓였을 때만 처리
        if drop.drag_name == "taegeuk_box":
            # 일진회 비판을 태극기 상자에 올렸을 때
            if drag.drag_name == "ijh_critique":
                store.items_placed["ijh_critique"] = True
                renpy.restart_interaction()
                return True
            # 민족 정신 교육을 태극기 상자에 올렸을 때
            elif drag.drag_name == "education":
                store.items_placed["education"] = True
                renpy.restart_interaction()
                return True
        
        # 태극기 상자가 아닌 곳에 놓거나, 잘못된 아이템이면 실패
        return False


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
screen tooltip_box(info):
    zorder 101
    
    frame:
        xalign 0.75
        yalign 0.05
        xmaximum 500
        background "#2C3E50"
        padding (20, 20)
        
        text info:
            size 20
            color "#FFFFFF"
            line_spacing 5
            text_align 0.0