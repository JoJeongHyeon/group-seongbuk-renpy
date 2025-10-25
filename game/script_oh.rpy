# 가빈 담당
# 오세창 루트 스크립트  
# script.rpy의 정의들을 모두 사용 가능

# =========================================
# 오세창 루트:
# =========================================
# -------- 배경/오브젝트 이미지 정의 --------

# 구슬/상태창
image bead = "images/bg/main_oh/ch3/bead/memory_bead.png"
image bead_hover = "images/bg/main_oh/ch3/bead/bead_hover.png"
image bg_ch1 = At("images/bg/main_oh/all/ch1.png", custom_size)
image bg_ch2 = At("images/bg/main_oh/all/ch2.png", custom_size)
image bg_ch3 = At("images/bg/main_oh/all/ch3.png", custom_size)
image bg_ch4 = At("images/bg/main_oh/all/ch4.png", custom_size)
image bg_ch1_status = At("images/bg/main_oh/all/ch1_status.png", custom_size)
image bg_ch2_status = At("images/bg/main_oh/all/ch2_status.png", custom_size)
image bg_ch3_status = At("images/bg/main_oh/all/ch3_status.png", custom_size)
image bg_ch4_status = At("images/bg/main_oh/all/ch4_status.png", custom_size)

# chap1
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

# chap2
image bg_talk = At("images/bg/main_oh/ch2/talk.png", custom_size)
image bg_speech = At("images/bg/main_oh/ch2/speech.png", custom_size)
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

# chap3
image bg_oh_desk = At("images/bg/main_oh/ch3/oh_desk.png", custom_size)
image bg_crowd_news_1 = At("images/bg/main_oh/ch3/crowd_news/1.png", custom_size)
image bg_crowd_news_2 = At("images/bg/main_oh/ch3/crowd_news/2.png", custom_size)
image bg_crowd_news_3 = At("images/bg/main_oh/ch3/crowd_news/3.png", custom_size)
image bg_crowd_news_4 = At("images/bg/main_oh/ch3/crowd_news/4.png", custom_size)
image bg_crowd_news_5 = At("images/bg/main_oh/ch3/crowd_news/5.png", custom_size)
image bg_crowd_news_6 = At("images/bg/main_oh/ch3/crowd_news/6.png", custom_size)
image bg_crowd_news_7 = At("images/bg/main_oh/ch3/crowd_news/7.png", custom_size)
image bg_crowd_novel_1 = At("images/bg/main_oh/ch3/crowd_novel/1.png", custom_size)
image bg_crowd_novel_2 = At("images/bg/main_oh/ch3/crowd_novel/2.png", custom_size)
image bg_crowd_novel_3 = At("images/bg/main_oh/ch3/crowd_novel/3.png", custom_size)
image bg_crowd_novel_4 = At("images/bg/main_oh/ch3/crowd_novel/4.png", custom_size)
image bg_crowd_novel_5 = At("images/bg/main_oh/ch3/crowd_novel/5.png", custom_size)
image bg_crowd_novel_6 = At("images/bg/main_oh/ch3/crowd_novel/6.png", custom_size)
image bg_crowd_novel_7 = At("images/bg/main_oh/ch3/crowd_novel/7.png", custom_size)
image bg_bead_1 = At("images/bg/main_oh/ch3/bead/1.png", custom_size)
image bg_bead_2 = At("images/bg/main_oh/ch3/bead/2.png", custom_size)
image bg_bead_3 = At("images/bg/main_oh/ch3/bead/3.png", custom_size)
image bg_bead_4 = At("images/bg/main_oh/ch3/bead/4.png", custom_size)
image bg_bead_5 = At("images/bg/main_oh/ch3/bead/5.png", custom_size)

image cartoon = "images/bg/main_oh/ch3/cartoon.png"
image essay = "images/bg/main_oh/ch3/essay.png"
image news_cylinder = "images/bg/main_oh/ch3/news_cylinder.png"
image colleague = "images/bg/main_oh/ch3/colleague.png"

# chap4
image bg_doknip_1 = At("images/bg/main_oh/ch4/doknip/1.png", custom_size)
image bg_doknip_2 = At("images/bg/main_oh/ch4/doknip/2.png", custom_size)
image bg_doknip_3 = At("images/bg/main_oh/ch4/doknip/3.png", custom_size)
image bg_doknip_4 = At("images/bg/main_oh/ch4/doknip/4.png", custom_size)
image bg_taegeuk_draw_1 = At("images/bg/main_oh/ch4/taegeuk_draw/1.png", custom_size)
image bg_taegeuk_draw_2 = At("images/bg/main_oh/ch4/taegeuk_draw/2.png", custom_size)
image bg_taegeuk_draw_3 = At("images/bg/main_oh/ch4/taegeuk_draw/3.png", custom_size)
image bg_taegeuk_draw_4 = At("images/bg/main_oh/ch4/taegeuk_draw/4.png", custom_size)
image bg_gather = At("images/bg/main_oh/ch4/gather.png", custom_size)
image bg_manse = At("images/bg/main_oh/ch4/manse.png", custom_size)
image bg_paper_machine = At("images/bg/main_oh/ch4/paper_machine.png", custom_size)
image bg_police = At("images/bg/main_oh/ch4/police.png", custom_size)
image chundogyo = "images/bg/main_oh/ch4/chundogyo.png"
image taegeuk = "images/bg/main_oh/ch4/taegeuk.png"
image black_brush = "images/bg/main_oh/ch4/taegeuk_draw/black.png"
image black_high = "images/bg/main_oh/ch4/taegeuk_draw/black_high.png"
image blue_brush = "images/bg/main_oh/ch4/taegeuk_draw/blue.png"
image blue_high = "images/bg/main_oh/ch4/taegeuk_draw/blue_high.png"
image red_brush = "images/bg/main_oh/ch4/taegeuk_draw/red.png"
image red_high = "images/bg/main_oh/ch4/taegeuk_draw/red_high.png"

# -------- BGM/효과음 --------
define audio.oh_main_bgm = "audio/bgm/oh_main_bgm.mp3"
define audio.oh_ch1 = "audio/bgm/oh_ch1.mp3"
define audio.oh_ch2 = "audio/bgm/oh_ch2.mp3"
define audio.memory_orb_get = "audio/sfx/memory_orb_get.wav"

# 캐릭터 설정
define wife = Character("부인", color="#6bffba")
define coll = Character("동료", color="#6bffba")
define son = Character("손병희", color="#d36bff")
define reader_1 = Character("독자1", color="#6bffba")
define reader_2 = Character("독자2", color="#6bffba")
define reader_3 = Character("독자3", color="#6bffba")
define chondo = Character("천도교도", color="#6bffba")
define voice = Character("???", color="#ffffff")

# ================================
# 공용: 클릭해서 넘어가는 오버레이 스크린
# ================================
screen overlay_wait(img_name):
    modal True
    add img_name
    # 화면 어디든 클릭/탭 시 종료
    key "dismiss" action Return()
    imagebutton:
        idle Solid("#00000000", xysize=(config.screen_width, config.screen_height))
        hover Solid("#00000000", xysize=(config.screen_width, config.screen_height))
        action Return()

# ================================
# Ch1 말미: 구슬 클릭 스크린 (배경 위 오버레이)
# ================================
screen bead_click_event(xpos, ypos, zoom):
    modal True
    # 구슬 안내 텍스트(옵션)
    text "빛나는 구슬을 클릭하세요":
        xalign 0.5
        ypos 80
        size 36
        color "#ffffff"
        outlines [(2, "#000000", 0, 0)]
    # 구슬 버튼 (클릭하면 Return)
    imagebutton:
        idle Transform("bead", zoom=zoom)
        hover Transform("bead_hover", zoom=zoom)
        focus_mask True
        xpos xpos
        ypos ypos
        xanchor 0.5
        yanchor 0.5
        action Return()

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

    # ▶ 챕터 1 시작 오버레이 (클릭해야 넘어감)
    
    scene bg_appointment with fade_slow
    call screen overlay_wait("bg_ch1")
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

    # ----- 잉크 번짐 전환 (파이썬 블록) -----
    scene bg_bakmunguk_shutdown with fade_fast

    python:
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
        for name, delay in ink_frames:
            renpy.show(name, at_list=[], layer="overlay")
            renpy.pause(delay, hard=True)
        renpy.scene()
        renpy.show("bg_black")
        renpy.pause(0.4, hard=True)
        for i in range(1, 9):
            renpy.hide(f"bg_ink_{i}", layer="overlay")

    scene bg_black
    m "어떡하지? 이러다가는 목숨을 잃고 말 거야….어디로든 도망가야 해!"
    
    # 망명 선택
    call exile_menu_loop
    
    # 망명 후 항구 장면
    scene bg_harbor with fade_fast
    m "어쩔 수 없다. 일본으로 망명해야겠다."
    stop music fadeout 1.0
    m "어? 저 빛나는 건 뭔지? 눌러봐야겠다."

    # ✅ 구슬 클릭 이벤트(클릭해야 진행)
    call screen bead_click_event(0.9, 0.8, 0.35)
    play sound memory_orb_get

    # ▶ 챕터 1 종료 오버레이 (클릭해야 넘어감)
    call screen overlay_wait("bg_ch1_status")
    m "기억 구슬이 맞나 보구나!"

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
# Ch2. 천도교 입교 → 만세보 발행 → 대한협회 결성
# =========================================
label oh_chap2:
    # ▶ 챕터 2 시작 오버레이
    scene bg_black with fade_slow
    call screen overlay_wait("bg_ch2")
    play music oh_main_bgm fadein 1.0 loop
    m "휴, 일본으로 도망쳐서 겨우 살았네. 모르는 곳에서 그냥 죽을 뻔..."
    "일본으로 망명해서 살던 도중, 천도교 교주인 손병희를 만났다."
    
    scene bg_speech with fade_fast
    son "천도교는 1860년 1대 교주인 최제우 교주님께서 창시하신 민족 종교입니다. 사람 마음속의 하늘인 한울님과 연결되어 서로를 존중하며 세상을 더 좋게 만들자는 가르침을 전하는 종교입니다."
    son "비록 우리 천도교는 원래 개화를 싫어하지만, 3대 교주인 저는 문명 개화에 찬성하는 입장입니다."
    son "뜻이 같은 자, 천도교로 오시오!"

    m "지금 1860년이 넘었다고? 심지어 1대 교주도 아니고 3대 교주? 완전 조선시대 말이잖아!"
    coll "자네, 어떤가? 자네도 같이 입교하는 게 좋을 것 같네! 완전 좋은 기회야! 무조건 같이 입교하는 걸세!"
    "천도교에 입교하게 되었다."

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
    coll "자네, 나랑 같이 사람들의 교육을 위해 천도교 기관지를 같이 만듭시다. 경험 있으니까 잘할 수 있지 않겠습니까? 이름은 <만세보>가 좋겠습니다."
    stop music fadeout 1.0
    play music oh_ch2 fadein 1.0
    scene bg_news_machine with fade_fast

    coll "민족 정신을 위해 친일파를 비판해야 하는 것이 옳습니다. 누구를 비판하는 게 좋을 것 같습니까?"
   
    call menu_loop_critique

    scene bg_news_machine with fade_fast
    m "친일파의 만행에 대해서 내가 직접 알리다니. 역사 책에서 보던 독립 운동을 직접 해 볼 수 있다는 게 너무 뿌듯하다!"
    coll "근데 아무리 생각해도 일진회를 더 견제해야 됩니다. 민족 정신에 대한 교육의 필요성이 더 중요해졌지 않습니까? 협회를 만들어야 하지 않을까 생각합니다."

    # 드래그 앤 드롭 미니게임
    call daehan_association_minigame

    # 드래그 앤 드롭 완료 후
    scene bg_news_machine with fade_fast
    "대한협회 결성!"
    

    "신문 찍는 기계 앞에서 구슬을 발견했다."
    call screen bead_click_event(0.9, 0.8, 0.35)
    play sound memory_orb_get

    # ▶ 챕터 2 종료 오버레이
    call screen overlay_wait("bg_ch2_status")
    m "벌써 두 번째 구슬이다! 이 속도면 집에 빨리 갈 수 있겠지?"

    stop music fadeout 1.0
    jump oh_chap3
    
# =========================================
# Ch3. 대한민보 편찬 → 연재만화 → 풍자소설
# =========================================
label oh_chap3:
    # ▶ 챕터 3 시작 오버레이

    scene bg_black with fade_fast
    call screen overlay_wait("bg_ch3")
    show colleague at Transform(zoom=0.35, xalign=0.5, yalign=0.5)
    play music oh_main_bgm fadein 1.0 loop

    coll "하, 근데 이것만으로도 아직 너무 부족한 것 같습니다."
    coll "일본의 만행이 너무 심해지고 있습니다…. 우리나라를 하나의 뜻으로 모아야 합니다!"
    coll "이번에는 기관지가 아닌 신문도 같이 발행해 보는 것은 어떱니까?"
    
    scene bg_oh_desk with fade_fast
    "대한민보를 편찬하게 되었다."
    m "근데 나도 긴 글 읽고 공부하는 것을 싫어하는데……. 맨날 벼락치기만 하고"
    m "단순히 글 말고도 쉽게 사람들에게 지식을 전파할 수 있는 방법이 없을까?"
    
    call menu_loop_news
    call mission_news
    
    scene bg_crowd_news_4
    pause 1.0
    scene bg_crowd_news_5
    pause 1.0
    scene bg_crowd_news_6
    pause 1.0
    scene bg_crowd_news_7
    pause 1.0

    reader_1 "오, 신문에 만화라니 신선하고 재미있는데?"
    reader_2 "이건 어떤 신문이야? 나도 구매해야겠다. 나도 신문 한 부 주시오!"
    m "만화 말고도 사람들이 신문을 좀 더 재미있게 읽을 수 있는 방법은 없을까? 아, 소설 같은 것도 신문에 넣으면 좋을 것 같은데."

    call menu_loop_novel
    call mission_novel

    scene bg_crowd_novel_4
    pause 1.0
    scene bg_crowd_novel_5
    pause 1.0
    scene bg_crowd_novel_6
    pause 1.0
    scene bg_crowd_novel_7
    pause 1.0

    reader_1 "아, 이젠 풍자소설도 신문으로 볼 수 있어?"
    reader_2 "그렇다니까. 한글로 되어 있어서 읽기도 얼마나 쉬운데?"
    reader_3 "뭐?! 그럼 나 같은 사람도 읽을 수 있겠네!"
    
    scene bg_oh_desk with fade_fast
    call screen bead_click_event(0.1, 0.7, 0.4)
    play sound memory_orb_get

    # ▶ 챕터 3 종료 오버레이
    call screen overlay_wait("bg_ch3_status")
    "책상에서 기억 구슬을 획득했다."
    m "이제 다음이 마지막 구슬인가? 벌써 마지막 구슬이라니 약간은 아쉽네…."

    stop music fadeout 1.0
    jump oh_chap4

# =========================================
# Ch4. 독립선언서 준비 → 3.1 만세운동 → 체포
# =========================================
label oh_chap4:
    # ▶ 챕터 4 시작 오버레이

    scene bg_gather with fade_slow
    call screen overlay_wait("bg_ch4")
    play music oh_main_bgm fadein 1.0 loop
    
    chondo "아, 그러고 보니 우리가 독립선언서를 준비해야 하네. 만세 운동도 같이 준비하기로 했어! 자네 기억하고 있지?"
    m "뭐? 내가 언제? 다른 사람들과 만세 운동을 준비해야 된다고 한다. 어떡해?"
    m "처음부터 성공할 것 같지는 않아…. 책에서 본 독립운동가분들도 다 이렇게 생각했겠지? 그래! 해 보자!"
    
    "독립만세운동과 독립선언서를 준비하는 움직임에 힘을 보태야 한다."
    "먼저 독립선언서를 인쇄할 준비를 해 놓자."
    
    scene bg_paper_machine with fade_fast
    
    m "일본 몰래 준비하다가 일찍 들켜 독립선언서를 뺏겨 만세 운동을 못하게 될지도 모른다. 어떻게 해야 할까?"
    
    call declaration_backup_loop
    
    "이제 안심이 조금 된다. 독립선언서를 인쇄했다."
    
    m "3.1 만세운동을 위한 태극기도 그려야 한다."
    
    # 태극기 그리기 미니게임
    #call draw_taegeuk_minigame
    
    "태극기를 그렸다!"
    
    m "내가 천도교 대표로 대한독립선언서에 서명도 해야 된대…!"
    
    call sign_declaration_loop
    
    scene bg_gather with fade_fast
    #play music manse_effect fadein 1.0
    
    "대한독립선언서에 서명하고, 3.1 만세운동을 시작한다!"
    
    # 독립선언서 뿌리기 인터랙션
    #call screen spread_declaration
    
    scene bg_manse with fade_fast
    
    "대한독립만세!"
    "대한독립만세!"
    "대한독립만세!"
    
    voice "오세창은 민족 대표 33인 중 1인으로 독립선언서에 참여하고 만세운동을 벌였다."
    
    scene bg_police with fade_fast
    
    "결국 일본에게 붙잡혀 체포되었다."
    m "직접 해 보니 독립운동가분들에게 감사한 마음을 가져야겠어."
    
    scene bg_manse with fade_fast
    
    "대한독립만세!"
    
    call screen bead_click_event(960, 540, 0.35)
    play sound memory_orb_get
    call screen overlay_wait("bg_ch4_status")
    "태극기와 함께 기억 구슬을 얻었다."
    m "드디어 구슬을 다 모았다! 이제 집에 돌아갈 수 있겠다!"  
    stop music fadeout 1.0
    
    jump oh_ending
    
    return

# =========================================
# 독립선언서 백업 선택 루프
# =========================================
label declaration_backup_loop:
    menu:
        "원본만 가지고 있기":
            "만세 운동을 아예 할 수 없게 될지도 모른다. 그래도 원본만 가지고 있을까?"
            jump declaration_backup_loop
        
        "혹시 모르니 다른 곳에 베껴 써 놓았다가 만세 운동까지 대비하기":
            return

# =========================================
# 독립선언서 서명 선택 루프
# =========================================
label sign_declaration_loop:
    menu:
        "대한독립선언서에 서명하고, 3.1 만세운동을 진행하시겠습니까?"
            
        "네":
            return
        
        "넵":
            return
        
        "정말 결의에 찬 마음으로 예":
            return
        
        "당연하지":
            return

# =========================================
# 독립선언서 뿌리기 인터랙션
# =========================================
screen spread_declaration():
    modal True
    add "bg_gather"
    text "독립선언서를 클릭하여 만세운동을 시작하세요":
        xalign 0.5 
        ypos 50 
        size 40
        color "#ffffff"
        outlines [(2, "#000000", 0, 0)]
    imagebutton:
        idle "declaration_paper"
        hover "declaration_paper"
        xalign 0.5
        yalign 0.5
        action Return()

# =========================================
# 비판 메뉴 루프
# =========================================
label menu_loop_critique:
    menu:
        "친일 단체인 일진회의 문제점을 널리 알려야겠어!":
            scene bg_critique_ijh with fade_fast
            pause 1.5
            "아! 일진회 역적 무리들이 왜적과 결탁하여 을사늑약을 찬성하고 합병을 청원하니,"
            "이 어찌 동포를 배반하고 조종의 강토를 팔아먹는 천추의 역적 행위가 아니겠는가!"
            return
        
        "친일파, 을사조약에 찬성한 '을사오적' 중 한 명인 내부대신 이지용을 비판하자!":
            scene bg_critique_ljy with fade_fast
            pause 1.5
            "내부대신 이지용은 대역무도한 역적으로, 왜놈의 협박에 굴복하여 을사늑약에 도장을 찍고"
            "삼천리 강토를 적에게 넘기니, 백성들의 원성이 하늘을 찌르도다!"
            return

        "친일파, 을사조약에 찬성한 '을사오적' 중 한 명인 군부대신 이근택을 비판하자!":
            scene bg_critique_lgt with fade_fast
            pause 1.5
            "군부대신 이근택은 나라의 군권을 지켜야 할 자리에 있으면서도"
            "왜적의 칼날 앞에 무릎 꿇고 을사늑약에 서명하여 국권을 도적질하였으니, 이 무슨 염치없는 배신인가!"
            return

        "그냥 비판하지 말자!":
            "진짜 우리나라가 일본에게 팔리는 것을 보고도 가만히 있을 건가?"
            jump menu_loop_critique

# =========================================
# 신문 콘텐츠 선택 메뉴 루프
# =========================================
label menu_loop_news:
    menu:
        "연재 만화를 싣기":
            show cartoon at Transform(zoom=0.55, xalign=0.5, yalign=0.5)
            pause 1.0
            "우리나라 최초의 신문 연재 만화가 되었다!"
            return

        "엄청 긴 글을 싣기":
            show essay
            pause 1.0
            "사람들이 재미없어 할 것 같다."
            hide essay
            jump menu_loop_news

# =========================================
# 소설 콘텐츠 선택 메뉴 루프
# =========================================
label menu_loop_novel:
    menu:
        "풍자 소설과 설명을 돕는 그림 싣기":
            show novel at Transform(zoom=0.8, xalign=0.5, yalign=0.5)
            pause 1.0
            "순한글로 되어 있는 풍자소설 <금수재판>이 연재되어 많은 독자들을 얻게 되었다!"
            return

        "긴 글만 싣기":
            show essay 
            pause 1.0
            "아… 글로만 되어 있는 신문은 너무 어려운 것 같은데?"
            hide essay
            jump menu_loop_novel

# =========================================
# 신문 배포 미션 (Reader 1 → Reader 2) 
# =========================================

# 전체 미션 진입
label mission_news:
    call mission_news_r1
    call mission_news_r2
    return

# ---------- Reader 1 ----------
label mission_news_r1:
    $ news_delivered_r1 = False
    
    label mission_news_r1_loop:
        call screen news_delivery_r1
        if news_delivered_r1:
            return
        else:
            jump mission_news_r1_loop

screen news_delivery_r1():
    modal True
    add "bg_crowd_news_2"
    text "신문을 새로운 독자에게 권유하기 (1/2)":
        xalign 0.5
        ypos 50
        size 40
        color "#ffffff"
        outlines [(2, "#000000", 0, 0)]
    if news_delivered_r1:
        timer 0.05 action Return()
    draggroup:
        drag:
            drag_name "reader_zone_r1"
            draggable False
            droppable True
            drag_raise False
            xpos 1100
            ypos 600
            child Solid("#dc6969a9", xysize=(150, 400))
        drag:
            drag_name "news_cylinder_r1"
            droppable False
            dragged news_drag_callback_r1
            xpos 150
            ypos 600
            add "news_cylinder" zoom 0.3

init python:
    def news_drag_callback_r1(drags, drop):
        if drop is None:
            return False
        drag = drags[0]
        if (drop.drag_name == "reader_zone_r1") and (drag.drag_name == "news_cylinder_r1"):
            if not store.news_delivered_r1:
                store.news_delivered_r1 = True
                renpy.restart_interaction()
                return True
        return False

# ---------- Reader 2 ----------
label mission_news_r2:
    $ news_delivered_r2 = False
    label mission_news_r2_loop:
        call screen news_delivery_r2
        if news_delivered_r2:
            return
        else:
            jump mission_news_r2_loop

screen news_delivery_r2():
    modal True
    add "bg_crowd_news_3"
    text "신문을 새로운 독자에게 권유하기 (2/2)":
        xalign 0.5
        ypos 50
        size 40
        color "#ffffff"
        outlines [(2, "#000000", 0, 0)]
    if news_delivered_r2:
        timer 0.05 action Return()
    draggroup:
        drag:
            drag_name "reader_zone_r2"
            draggable False
            droppable True
            drag_raise False
            xpos 730
            ypos 650
            child Solid("#dc6b6ba9", xysize=(150, 350))
        drag:
            drag_name "news_cylinder_r2"
            droppable False
            dragged news_drag_callback_r2
            xpos 150
            ypos 600
            add "news_cylinder" zoom 0.3

init python:
    def news_drag_callback_r2(drags, drop):
        if drop is None:
            return False
        drag = drags[0]
        if (drop.drag_name == "reader_zone_r2") and (drag.drag_name == "news_cylinder_r2"):
            if not store.news_delivered_r2:
                store.news_delivered_r2 = True
                renpy.restart_interaction()
                return True
        return False

# =========================================
# 소설 배포 미션 (Reader 1 → Reader 2) 
# =========================================

label mission_novel:
    call mission_novel_r1
    call mission_novel_r2
    return

# ---------- Reader 1 ----------
label mission_novel_r1:
    $ novel_delivered_r1 = False
    label mission_novel_r1_loop:
        call screen novel_delivery_r1
        if novel_delivered_r1:
            return
        else:
            jump mission_novel_r1_loop

screen novel_delivery_r1():
    modal True
    add "bg_crowd_novel_2"
    text "신문을 새로운 독자에게 권유하기 (1/2)":
        xalign 0.5
        ypos 50
        size 40
        color "#ffffff"
        outlines [(2, "#000000", 0, 0)]
    if novel_delivered_r1:
        timer 0.05 action Return()
    draggroup:
        drag:
            drag_name "reader_zone_novel_r1"
            draggable False
            droppable True
            drag_raise False
            xpos 850
            ypos 550
            child Solid("#e87e7eaa", xysize=(180, 500))
        drag:
            drag_name "news_cylinder_novel_r1"
            droppable False
            dragged novel_drag_callback_r1
            xpos 150
            ypos 600
            add "news_cylinder" zoom 0.3

init python:
    def novel_drag_callback_r1(drags, drop):
        if drop is None:
            return False
        drag = drags[0]
        if (drop.drag_name == "reader_zone_novel_r1") and (drag.drag_name == "news_cylinder_novel_r1"):
            if not store.novel_delivered_r1:
                store.novel_delivered_r1 = True
                renpy.restart_interaction()
                return True
        return False

# ---------- Reader 2 ----------
label mission_novel_r2:
    $ novel_delivered_r2 = False
    label mission_novel_r2_loop:
        call screen novel_delivery_r2
        if novel_delivered_r2:
            return
        else:
            jump mission_novel_r2_loop

screen novel_delivery_r2():
    modal True
    add "bg_crowd_novel_3"
    text "신문을 새로운 독자에게 권유하기(2/2)":
        xalign 0.5
        ypos 50
        size 40
        color "#ffffff"
        outlines [(2, "#000000", 0, 0)]
    if novel_delivered_r2:
        timer 0.05 action Return()
    draggroup:
        drag:
            drag_name "reader_zone_novel_r2"
            draggable False
            droppable True
            drag_raise False
            xpos 1200
            ypos 550
            child Solid("#f26a6aa1", xysize=(200, 450))
        drag:
            drag_name "news_cylinder_novel_r2"
            droppable False
            dragged novel_drag_callback_r2
            xpos 150
            ypos 600
            add "news_cylinder" zoom 0.3

init python:
    def novel_drag_callback_r2(drags, drop):
        if drop is None:
            return False
        drag = drags[0]
        if (drop.drag_name == "reader_zone_novel_r2") and (drag.drag_name == "news_cylinder_novel_r2"):
            if not store.novel_delivered_r2:
                store.novel_delivered_r2 = True
                renpy.restart_interaction()
                return True
        return False

# =========================================
# 대한협회 결성 드래그 앤 드롭 미니게임
# =========================================
label daehan_association_minigame:
    $ items_placed = {"ijh_critique": False, "education": False}
    label minigame_loop:
        call screen drag_drop_game
        if items_placed["ijh_critique"] and items_placed["education"]:
            return
        else:
            jump minigame_loop

screen drag_drop_game():
    modal True
    add "bg_news_machine"
    text "일진회 비판과 민족 정신에 대한 교육을 태극기 상자에 모두 올려주세요":
        xalign 0.5 
        ypos 50 
        size 40
        color "#000000"
    if items_placed["ijh_critique"] and items_placed["education"]:
        key "dismiss" action Return()
    fixed:
        xpos 750
        ypos 500
        xysize (450, 450)
        add "taegeuk_box" zoom 0.3 xalign 0.5 yalign 0.5
        if items_placed["ijh_critique"] and items_placed["education"]:
            add "daehan" zoom 0.3 xalign 0.5 yalign 0.70
    draggroup:
        drag:
            drag_name "taegeuk_box"
            draggable False
            droppable True
            drag_raise False
            xpos 700
            ypos 800
            child Solid("#00000000", xysize=(550, 100))
        if not items_placed["ijh_critique"]:
            drag:
                drag_name "ijh_critique"
                droppable False
                dragged drag_callback
                xpos 150
                ypos 200
                add "ijh_critique" zoom 0.08 
        if not items_placed["education"]:
            drag:
                drag_name "education"
                droppable False
                dragged drag_callback
                xpos 1350
                ypos 200
                add "education" zoom 0.08

init python:
    def drag_callback(drags, drop):
        if drop is None:
            return False
        drag = drags[0]
        if drop.drag_name == "taegeuk_box":
            if drag.drag_name == "ijh_critique":
                store.items_placed["ijh_critique"] = True
                renpy.restart_interaction()
                return True
            elif drag.drag_name == "education":
                store.items_placed["education"] = True
                renpy.restart_interaction()
                return True
        return False

# =========================================
# 태극기 그리기 미니게임 (3단계, 각 단계 클릭드롭 필수)
# =========================================
label draw_taegeuk_minigame:
    call taegeuk_stage_1
    call taegeuk_stage_2
    call taegeuk_stage_3
    scene bg_taegeuk_draw_4 with fade_fast
    $ renpy.pause(1.0, hard=True)
    return

# ---------- Stage 1 : 빨간 붓 성공 ----------
label taegeuk_stage_1:
    $ tae_s1_done = False
    call screen taegeuk_draw_s1
    return

screen taegeuk_draw_s1():
    modal True
    if tae_s1_done:
        timer 0.05 action Return()
    fixed:
        add "bg_taegeuk_draw_1"
        add Solid("#ffff0080", xysize=(640, 360)) xpos 640 ypos 300
        draggroup:
            drag:
                drag_name "paper_zone_s1"
                draggable False
                droppable True
                drag_raise False
                xpos 640
                ypos 300
                child Solid("#00000000", xysize=(640, 360))
            drag:
                drag_name "black_move_s1"
                droppable False
                dragged taegeuk_drag_cb_s1
                xpos 400
                ypos 620
                child "black_brush" at Transform(zoom=0.85)
            drag:
                drag_name "blue_move_s1"
                droppable False
                dragged taegeuk_drag_cb_s1
                xpos 600
                ypos 650
                child "blue_brush" at Transform(zoom=0.85)
            drag:
                drag_name "red_move_s1"
                droppable False
                dragged taegeuk_drag_cb_s1
                xpos 820
                ypos 610
                child "red_high" at Transform(zoom=0.85)

init python:
    def taegeuk_drag_cb_s1(drags, drop):
        if drop is None:
            return False
        drag = drags[0]
        if drop.drag_name == "paper_zone_s1" and drag.drag_name == "red_move_s1":
            store.tae_s1_done = True
            renpy.restart_interaction()
            return True
        if drop.drag_name == "paper_zone_s1":
            return True
        return False

# ---------- Stage 2 : 파란 붓 성공 ----------
label taegeuk_stage_2:
    $ tae_s2_done = False
    call screen taegeuk_draw_s2
    return

screen taegeuk_draw_s2():
    modal True
    if tae_s2_done:
        timer 0.05 action Return()
    fixed:
        add "bg_taegeuk_draw_2"
        add Solid("#ffff0080", xysize=(640, 360)) xpos 640 ypos 300
        draggroup:
            drag:
                drag_name "paper_zone_s2"
                draggable False
                droppable True
                drag_raise False
                xpos 640
                ypos 300
                child Solid("#00000000", xysize=(640, 360))
            drag:
                drag_name "black_move_s2"
                droppable False
                dragged taegeuk_drag_cb_s2
                xpos 400
                ypos 620
                child "black_brush" at Transform(zoom=0.85)
            drag:
                drag_name "red_move_s2"
                droppable False
                dragged taegeuk_drag_cb_s2
                xpos 820
                ypos 610
                child "red_brush" at Transform(zoom=0.85)
            drag:
                drag_name "blue_move_s2"
                droppable False
                dragged taegeuk_drag_cb_s2
                xpos 600
                ypos 650
                child "blue_high" at Transform(zoom=0.85)

init python:
    def taegeuk_drag_cb_s2(drags, drop):
        if drop is None:
            return False
        drag = drags[0]
        if drop.drag_name == "paper_zone_s2" and drag.drag_name == "blue_move_s2":
            store.tae_s2_done = True
            renpy.restart_interaction()
            return True
        if drop.drag_name == "paper_zone_s2":
            return True
        return False

# ---------- Stage 3 : 검은 붓 성공 ----------
label taegeuk_stage_3:
    $ tae_s3_done = False
    call screen taegeuk_draw_s3
    return

screen taegeuk_draw_s3():
    modal True
    if tae_s3_done:
        timer 0.05 action Return()
    fixed:
        add "bg_taegeuk_draw_3"
        add Solid("#ffff0080", xysize=(640, 360)) xpos 640 ypos 300
        draggroup:
            drag:
                drag_name "paper_zone_s3"
                draggable False
                droppable True
                drag_raise False
                xpos 640
                ypos 300
                child Solid("#00000000", xysize=(640, 360))
            drag:
                drag_name "red_move_s3"
                droppable False
                dragged taegeuk_drag_cb_s3
                xpos 820
                ypos 610
                child "red_brush" at Transform(zoom=0.85)
            drag:
                drag_name "blue_move_s3"
                droppable False
                dragged taegeuk_drag_cb_s3
                xpos 600
                ypos 650
                child "blue_brush" at Transform(zoom=0.85)
            drag:
                drag_name "black_move_s3"
                droppable False
                dragged taegeuk_drag_cb_s3
                xpos 400
                ypos 620
                child "black_high" at Transform(zoom=0.85)

init python:
    def taegeuk_drag_cb_s3(drags, drop):
        if drop is None:
            return False
        drag = drags[0]
        if drop.drag_name == "paper_zone_s3" and drag.drag_name == "black_move_s3":
            store.tae_s3_done = True
            renpy.restart_interaction()
            return True
        if drop.drag_name == "paper_zone_s3":
            return True
        return False