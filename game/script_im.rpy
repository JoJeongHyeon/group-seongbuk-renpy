# 민욱 담당
# 임규 루트 스크립트

# =============================================================================
# 오디오 정의
# =============================================================================
# 기억구슬 효과음
define audio.memory_orb_appear = "audio/sfx/memory_orb_appear.mp3"
define audio.memory_orb_get = "audio/sfx/memory_orb_get.wav"

#똑똑
define audio.im_ch1 = "audio/bgm/im_ch1.wav"

# === 책 정보 (전역) ===
screen interactive_table_im():
    # 기본 테이블 이미지
    add "ch1_table_ex" at custom_size
    
    #  성호사설 영역 (중간 하단)
    imagemap:
        ground Null(1920, 1080)  # 투명한 배경
        hover "bk1_hover"
        alpha True
        at custom_size
        hotspot (0, 0, 1920, 1080):
            action Return ("next_ch")
            
    # 용비어천가 영역 (우측 상단)        
    imagemap:
        ground Null(1920, 1080)  # 투명한 배경
        hover "bk2_hover"
        alpha True
        at custom_size
        hotspot (0, 0, 1920, 1080):
            action Return("next_ch")

    # 지봉유설 영역 (좌측 상단)
    imagemap:
        ground Null(1920, 1080)  # 투명한 배경
        hover "bk3_hover"
        alpha True
        at custom_size
        hotspot (0, 0, 1920, 1080):
            action Return("next_ch")

    # 역사 인물들
define choi = Character("최남선", image = "choi",color="#49b9bf")
define w = Character("낯선 사람", image = "choi0",color="#b28080")
define hara = Character("하라 다카시", image = "hara",color="#ff3030") 
define w1 = Character("???", image = "hara0",color="#aa7c7c")
define im_t = Character("???", color="#ff6b6b", what_color="#888888", what_italic=True)

# 기억구슬
image memory_orb-1 = "bg/memory_orb-1.png"
image memory_orb-2 = "bg/memory_orb-2.png"
image memory_orb-3 = "bg/memory_orb-3.png"
image memory_orb-4 = "bg/memory_orb-4.png"
image memory_orb-1_hover = "bg/memory_orb-1_hover.png"
image memory_orb-2_hover = "bg/memory_orb-2_hover.png"
image memory_orb-3_hover = "bg/memory_orb-3_hover.png"
image memory_orb-4_hover = "bg/memory_orb-4_hover.png"

# UI 스크린 - 챕터 및 구슬 발견창
image ui_ch1 = At("ui_screen/ui_ch1.png", custom_size)
image ui_ch2 = At("ui_screen/ui_ch2.png", custom_size)
image ui_ch3 = At("ui_screen/ui_ch3.png", custom_size)
image ui_ch4 = At("ui_screen/ui_ch4.png", custom_size)
image ui_orb_found_ch1 = At("ui_screen/ui_orb_found_ch1.png", custom_size)
image ui_orb_found_ch2 = At("ui_screen/ui_orb_found_ch2.png", custom_size)
image ui_orb_found_ch3 = At("ui_screen/ui_orb_found_ch3.png", custom_size)
image ui_orb_found_ch4 = At("ui_screen/ui_orb_found_ch4.png", custom_size)


#chapter1
image bk-1               = At("bg/main_im/ch1/bk-1.png", custom_size)
image bk-2               = At("bg/main_im/ch1/bk-2.png", custom_size)             
image bk-3               = At("bg/main_im/ch1/bk-3.png", custom_size)
image imbubble-1         = At("bg/main_im/ch1/imbubble-1.png", custom_size)
image imbubble-2         = At("bg/main_im/ch1/imbubble-2.png", custom_size)             
image imbubble-3         = At("bg/main_im/ch1/imbubble-3.png", custom_size)
image bg_table_empty     = At("bg/table_empty.png", custom_size)   
image ch1_table          = At("bg/main_im/ch1/bg_im_table.png", custom_size)             
image ch1_table_ex       = At("bg/main_im/ch1/table_ex.png", custom_size)   

#chapter2          
image bg_darkroom        = At("bg/main_im/ch2/darkroom.png", custom_size)
image ch2_door           = At("bg/main_im/ch2/door.png", custom_size)
#chapter3
image imch3_bg = At("bg/main_im/ch3/bg_chapter3.png", custom_size)
image imch3_bg_dokrip = At("bg/main_im/ch3/bg_dokrip.png", custom_size)
image word_dok = "bg/main_im/ch3/dok.png"
image word_rip = "bg/main_im/ch3/rip.png"
image word_seon = "bg/main_im/ch3/seon.png"
image word_eon = "bg/main_im/ch3/eon.png"
image word_seo = "bg/main_im/ch3/seo.png"

#chapter4
image imch4_bg = At("bg/main_im/ch4/bg_chapter4.png", custom_size)
image imch4_bgp = At("bg/main_im/ch4/bg_chapter4p.png", custom_size)
image imch4_bgpc = At("bg/main_im/ch4/bg_chapter4pc.png")

image p1 = "bg/main_im/ch4/puzzle1.png"
image p2 = "bg/main_im/ch4/puzzle2.png"
image p3 = "bg/main_im/ch4/puzzle3.png"
image p4 = "bg/main_im/ch4/puzzle4.png"
image p5 = "bg/main_im/ch4/puzzle5.png"
image p6 = "bg/main_im/ch4/puzzle6.png"
image p7 = "bg/main_im/ch4/puzzle7.png"
image p8 = "bg/main_im/ch4/puzzle8.png"
image pf = "bg/main_im/ch4/puzzle_frame.png"   
image pf = "bg/main_im/ch4/frame0.png"         


define mt = Character("나", color="#ffffff", what_italic=True)

# 게임 시작
#===========================================================================
# 챕터 1 일본어에 능통하고, 조선광문회에서 고전 발간 편집을 진행한 것.
#===========================================================================
label character_im:   
    play music im_main_bgm fadein 1.0 loop
    scene ch1_table_ex with fade_slow   #책들이 놓여있는 이미지, 이미지 축소해야함.
    show ui_ch1 with dissolve

    m "구슬을 찾으려면 어떻게 해야 하지?"
    hide ui_ch1 with dissolve
    mt "그리고 여긴 또 어디야…"
    mt "얼굴은 한국인 같았는데, 한국이려나?"
    mt "책상에는 일본어책도 여러 권 있고, \n원래 이분은 일본어를 상당히 잘하셨나?"
    m "그리고 이건 한국 고전인가?"
    
    show screen mission_guide("책을 눌러 정보를 확인하세요.", icon="📄")
    m "책상 위에 책들이 이리저리 놓여 있네."

    hide screen mission_guide
    
    call screen interactive_table_im


    # 선택에 따른 분기
    if _return == "next_ch":
        # $ chosen_character = "jang" # 장기영
        im_t '우리 민족 전통은 이어져야 하지.'
        im_t '그러기 위해선 고전을 잊어선 안돼.'
        m "머릿속에서 들리는 말이나" 
        m "여기 책들을 보면 고전을 연구하던 분이셨구나."
        m "밖에서 쓰는 말이나" 
        m "보이는 풍경으로 봐서는 일제강점기 같은데..."
        m "이런 시기에 우리의 고전을 연구하셨다면, 대단하신 분이네."
        
        jump next
        return
label next:
    show memory_orb-1 with dissolve
    play sound memory_orb_appear fadein 0.5 fadeout 3.0
    pause 1.0
    
    
    mt "이게 뭐지? 갑자기 웬 구슬?"
            
    mt "왜 자꾸 둥둥 떠 있는 거야.."
    mt "잡아야 하는 건가?"

    show screen mission_guide("기억구슬을 눌러보세요.", icon="🔮")
    call screen interactive_objects("memory_orb-1")
    hide memory_orb-1
    hide screen mission_guide
            


    hide memory_orb-1 with dissolve

    mt "아, 이런 구슬을 찾으라는 이야기였구나!"
            
    # 챕터1 표시
    window hide
    # show screen framed_message("챕터1 | 기억구슬 획득", text_size=60) with dissolve

    play sound memory_orb_get
    pause 2.0
            
    # 구슬 발견창 표시 (챕터1 숨기면서 동시에 표시)

    show ui_orb_found_ch1 with dissolve
    pause 2.0
    hide ui_orb_found_ch1 with dissolve
            
    # 블랙아웃
    scene bg_black with fade_slow
    pause 2.0
            
    # 챕터2로 이어짐
    jump chapter2

return

#===========================================================================
# 챕터 2 최남선이 독립선언서를 작성하도록 돕다
#===========================================================================

label chapter2:

    scene bg_darkroom with Dissolve(3) # 교차 디졸브

    show ui_ch2 with dissolve

    mt "뭔가 시간대가 바뀐 거 같은데.."
    hide ui_ch2 with dissolve
    mt "음? 밖에 누가 왔나?"
    jump chapter2_scene2

label chapter2_scene2:
    
    scene ch2_door with fade_slow

    play sound im_ch1 fadein 1.0
    narrator "똑똑"

    w "우정 선생님, 안에 계신가요?" ##낯선 사람!!!!

    m "누가 찾아온 듯하다."
    m "누굴까? 함께 고전 연구를 함께하는 사람인가?"
    m "나는 아무 생각 없이 문을 열려다가 멈칫했다."
    m "잠깐만, 누군지도 모르는데 문을 열어줘도 되나?"

    menu:

        "열어 준다.":
            jump say_choi

        "열어 주지 않는다.":
            show screen info_tooltip("최남선\n독립선언서의 기초를 작성한 계몽사상가이자 언론인으로, 《소년》 잡지를 창간해 청년 계몽운동을 주도했다.")
            
            choi "선생님 접니다, 최남선."
            m "최남선? 들어본 것 같은데.."
            m "누군가 속삭이는 소리가 들린다"
            im_t "이 사람은 믿을 수 있다. 함께 일하는 동지 최남선이다."

            m "나는 홀린 듯이 문을 열었다."
            hide screen info_tooltip
            jump say_choi
return

label say_choi:
    show screen info_tooltip("최남선\n독립선언서의 기초를 작성한 계몽사상가이자 언론인으로, 《소년》 잡지를 창간해 청년 계몽운동을 주도했다.")
    choi "사실, 오늘은 긴히 드릴 말씀이 있어 이리 찾아오게 되었습니다."
            
    jump chapter2_scene3
return

label chapter2_scene3:

    scene bg_darkroom with fade_slow

    choi "우정 선생님, 우리는 만세 운동을 시행하려고 합니다."
    show screen info_tooltip("최남선\n독립선언서의 기초를 작성한 계몽사상가이자 언론인으로, 《소년》 잡지를 창간해 청년 계몽운동을 주도했다.")
            
    mt '만세 운동? 3.1운동을 말하는 건가?'
    mt '그럼 지금은 3.1운동 직전 시기인가 보네.'

    choi "저는 독립선언서를 작성하기로 했습니다."
    choi "그래서, 선생님께 이 일에 대한 조언을 구하고자 합니다"
    hide screen info_tooltip
    m "뭐라고 대답하지..?"
    menu:
        "말린다":
            jump stop_choi

        "지지한다":
            jump support_choi


label stop_choi:
    im "너무 위험한 일이네."
    choi "하지만 선생님, 이 일은 반드시 해야만 합니다."
    choi "지금이 아니면 안됩니다!"

    m "선택의 여지가 없다.."


    menu:
        "지지한다":
            jump support_choi

label support_choi:
    m "그래, 누군가는 반드시 해야할 일이지."
    m "그리고, 작성하려면 안전한 장소도 필요하겠지."
    m "우리 집을 내어줄 테니, 여기서 독립선언서를 작성하시게."
    m "그리고, 일본으로도 전달해야 하겠지? 그 임무를 내가 맡겠네."
    m "도와주겠다는 마음을 먹자, 저절로 입이 열렸다."
    m "이분은 큰 위험을 감수하고도 \n만세 운동을 돕고자 하는 사람이었던 것 같다."

    # 기억구슬 등장

    show memory_orb-2 with dissolve
    play sound memory_orb_appear fadein 0.5 fadeout 3.0
    pause 1.0
    
    m "어.. 또 구슬이다."

    # 클릭 후 사라짐
    show screen mission_guide("기억구슬을 눌러보세요.", icon="🔮")
    call screen interactive_objects("memory_orb-2")
    hide screen mission_guide

    hide memory_orb-2 with dissolve
    pause 0.5
    
    m "이번에도 구슬을 만지니, 사라졌다."

    # 챕터2 표시
    window hide
    play sound memory_orb_get
    pause 2.0
    
    # 구슬 발견창 표시 (챕터2 숨기면서 동시에 표시)
    show ui_orb_found_ch2 with dissolve
    pause 2.0
    hide ui_orb_found_ch2 with dissolve
    
    # 블랙아웃
    scene bg_black with fade_slow
    pause 2.0

    m "그런데 이번에는 아까와 다르게"
    m "공간이 바뀌는 기분이 들었다."
    m "뮈지? 순간이동?"

    jump chapter3

#===========================================================================
# 챕터 3 일본으로 건너가서 독립선언서를 전달하고, 선언하다
#===========================================================================

label chapter3:
    scene imch3_bg with fade_slow

    m "아까 있던 곳과는 확연히 다르다."
    m "여기는....?"

    im_t "일본이다."
    im_t "나는 일본에 독립선언서를 우송하고자 왔다."
    
    m "아까 말한대로 정말 일본으로 전달하는 임무를 하고 계시다니."
    m "나는 괜히 떨리는 마음에 침을 꿀꺽 삼켰다."

    im_t "일본 수상과 의회에 독립선언서를 보내야 한다. 그러기 위해서는...."

# ======드래그 앤 드롭==================

    window hide

    $ _reset_dokrip_state_rail()

 

    while True:
        $ result = renpy.call_screen("dokrip_rail")
        if result == "success":
            "좋아! 순서를 맞췄다."
            m "머릿속에서 말해주는 대로, 독립선언서를 차례로 우송했다."
            m "하는 동안 손이 덜덜 떨렸지만, \n무사히 마치고 나니 뿌듯한 감정도 들었다."
            m "그러고 숙소로 돌아오는 길에 한 일본인을 마주쳤다."
            jump next_ch1   # ← 성공 후 이동할 라벨명으로 바꿔줘
        else:
            "다시, <독립선언서> 순서로 배치 해보자."

    return

label next_ch1:


    m "나는 본능적으로 걸음을 멈추고 노려보았다."
    m "가슴 속에서 무언가 끓어오르는 감정이 전해져 왔다."

    w1 "그대는 누구이길래 나를 노려보는가?"

    im_t "저 사람은 일본 총리, 하라 다카시다."
    show screen info_tooltip("하라 다카시\n일본 제19대 총리로, 조선 식민통치를 총독부 중심의 ‘문화통치’로 전환시킨 인물이다.")
    
    hara "가만, 조선놈인가?"
    
    menu:
        
        "나는 조선의 임규요. 조선의 독립을 선포하려 이곳에 왔소!":
            jump next_ch2
        "민족자결주의에 따라 조선인의 일은 조선인이 담당해야 하는 법!":
            jump next_ch2
        "속히 총독부의 문을 닫고 조선엔 있는 일본군을 철수하시오!":
            jump next_ch2
    

label next_ch2:
    hide screen info_tooltip
    scene imch3_bg with fade_slow

    show ui_ch3 with dissolve
    m "우리 조선은 반드시 자주 독립을 이룰 것이다."
    hide ui_ch3 with dissolve
    m "국무총리는 나의 당당한 태도에 놀랐는지, 그대로 굳었다."
    
    im_t "여기에 오래 있으면, 얼마 안 가 현장에서 체포될 것이다."
    
    m "나는 그를 노려보다가 자리를 피했다."

    # 기억구슬 등장
    scene bg_black with dissolve
    show memory_orb-3 with dissolve
    play sound memory_orb_appear fadein 0.5 fadeout 3.0
    pause 1.0

    mt "구슬을 하나 더 찾았네."
    # 클릭 후 사라짐
    show screen mission_guide("기억구슬을 눌러보세요.", icon="🔮")
    call screen interactive_objects("memory_orb-3")
    hide screen mission_guide
    hide memory_orb-3 with dissolve
    pause 0.5
    
    # 챕터3 표시
    window hide
    play sound memory_orb_get
    pause 2.0
    
    # 구슬 발견창 표시 (챕터3 숨기면서 동시에 표시)
    show ui_orb_found_ch3 with dissolve
    pause 2.0
    hide ui_orb_found_ch3 with dissolve

    # 블랙아웃
    scene bg_black with fade_slow
    pause 2.0

    mt "그리고, 또 다른 곳으로 이동하려는 것 같다."
    
    # 챕터4로 이어짐
    jump chapter4

return

#===========================================================================
# 챕터 4
#===========================================================================

label chapter4:
    scene imch4_bg with fade_slow
    show ui_ch4 with dissolve

    m "여기는 또 어디지? 연구실 같은데..."
    hide ui_ch4 with dissolve
    m "가장 가까이에 있는 책상을 살펴보았다."

    m "와, 자료가 엄청 많네"
    m "우리 말과 관련된 자료들이 널려있고, \n사전의 일부 같은 종이들도 눈에 띈다."
    m "사전이라도 만들려는 것일까?"
    m "어? 이건..."


    $ setup_puzzle()
    call screen reassemble_puzzle

    return

label reassemble_complete:

    scene imch4_bgpc with fade_fast

    m "표음주의 철자법을 따를 필요가 있다?"
    m "이분은 소리가 나는 대로 쓰는 철자법을 주장하셨구나."
    m "그리고 여기 자료들을 보면 사전을 만드려고 하셨던 것 같은데..."
    m "이런 분들의 노력이 있었어서 정말 다행이야."
    m "그런데, 내가 빙의한 이분은 대체 누구시지..? 들어본 적이 없는데.."

    # 기억구슬 등장
    show memory_orb-4 with dissolve
    play sound memory_orb_appear fadein 0.5 fadeout 3.0
    pause 1.0
    
    show screen mission_guide("기억구슬을 눌러보세요.", icon="🔮")
    call screen interactive_objects("memory_orb-4")
    hide screen mission_guide
    hide memory_orb-4 with dissolve
    
    mt "아, 찾았다."
    mt "이게 마지막인 것 같은데.."
    mt "이제 현실로 돌아가는 거겠지?"
    
    # 챕터4 표시
    window hide
    play sound jang_last_orb_get
    pause 2.0
    
    # 구슬 발견창 표시 (챕터4 숨기면서 동시에 표시)
    
    show ui_orb_found_ch4 with dissolve
    pause 2.0
    hide ui_orb_found_ch4 with dissolve
    
    # 블랙아웃
    scene bg_black with fade_slow
    pause 2.0
    
    # 임규 엔딩으로 이어짐
    jump im_ending

return

#===========================================================================
# 챕터 N
#===========================================================================





# 1. 수정 보충 사항 정리
# -말하는 주체 수정
# -최남선 말풍선 가림
# -호버, 다음으로 버튼을 통해 스토리 진행 :: 지금 상태 보고 기획에서 괜찮으면 굳이 안 바꿔도 될듯
# 구슬, bgm 삽입

# =========================================
# 퍼즐 미니게임
# =========================================


default page_pieces = 8
default full_page_size = (813, 736)
default piece_coordinates = [(157, 157), (289, 157), (628, 155), (158, 373), (458, 325), (803, 374), (160, 594), (435, 669)]
default initial_piece_coordinates = []
default finished_pieces = 0


default puzzle_complete = False

init python:
    def setup_puzzle():
        for i in range(page_pieces):
            start_x = 1200
            start_y = 200
            end_x = 1700
            end_y = 800
            rand_loc = (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_piece_coordinates.append(rand_loc)

    def piece_drop(dropped_on, dragged_piece):
        global finished_pieces, puzzle_complete

        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y)
            dragged_piece[0].draggable = False
            finished_pieces += 1

            if finished_pieces == page_pieces:
                puzzle_complete = True
                renpy.restart_interaction()  # 화면 즉시 갱신


screen reassemble_puzzle:
    image "imch4_bgp"

    frame:
        background "bg/main_im/ch4/puzzle_frame.png"
        xysize full_page_size
        anchor(0, 0)
        pos(161, 154)
    
    draggroup:
        for i in range(page_pieces):
            drag:
                drag_name i
                pos initial_piece_coordinates[i]
                anchor(0.5, 0.5)
                focus_mask True
                drag_raise True
                image "bg/main_im/ch4/puzzle%s.png" % (i + 1)

        for i in range(page_pieces):
            drag:
                drag_name i
                draggable False
                droppable True
                dropped piece_drop
                pos piece_coordinates[i]
                focus_mask True
                image "bg/main_im/ch4/puzzle%s.png" % (i + 1) alpha 0.0

                if puzzle_complete:
                    timer 2.0 action [Hide("reassemble_puzzle"), Jump("reassemble_complete")]





# =============================================================================
# 인터랙티브 스크린
# =============================================================================

screen interactive_table_im():


    default clicked_imbubble1 = False
    default clicked_imbubble2 = False
    default clicked_imbubble3 = False

    add "ch1_table_ex" at custom_size
    
    # bk-1
    imagemap:
        ground Null(1920, 1080)  # 투명한 배경
        hover "bk-1"
        alpha True
        at custom_size
        hotspot (0, 0, 1920, 1080):
            action SetScreenVariable("clicked_imbubble1", True)

            
    # bk-2
    imagemap:
        ground Null(1920, 1080)  # 투명한 배경
        hover "bk-2"
        alpha True
        at custom_size
        hotspot (0, 0, 1920, 1080):
            action SetScreenVariable("clicked_imbubble2", True)

    
    # bk-3
    imagemap:
        ground Null(1920, 1080)  # 투명한 배경
        hover "bk-3"
        alpha True
        at custom_size
        hotspot (0, 0, 1920, 1080):
            action SetScreenVariable("clicked_imbubble3", True)
    
    # === 클릭한 오브젝트의 말풍선 표시 ===
    if clicked_imbubble1:
        add "imbubble-1" at custom_size
    if clicked_imbubble2:
        add "imbubble-2" at custom_size
    if clicked_imbubble3:
        add "imbubble-3" at custom_size

    # === 세 말풍선 모두 확인했을 때 다음 버튼 등장 ===
    if clicked_imbubble1 and clicked_imbubble2 and clicked_imbubble3:
        frame:
            xalign 0.5
            yalign 0.9
            background Frame(Solid("#1E293BDD"), 20, 20)
            padding (30, 20)
            textbutton "모든 오브젝트를 확인했습니다 - 다음으로 이동":
                text_size 24
                text_color "#E0E7FF"
                text_hover_color "#93C5FD"
                action Return("next_ch")





# =========================
# [레일 낱말 퍼즐 — 완전 통합본]
# =========================

# --- 이미지 선언(네가 준 경로 기준) ---
image imch3_bg_dokrip = "bg/main_im/ch3/bg_dokrip.png"
image word_dok       = "bg/main_im/ch3/dok.png"
image word_rip       = "bg/main_im/ch3/rip.png"
image word_seon      = "bg/main_im/ch3/seon.png"
image word_eon       = "bg/main_im/ch3/eon.png"
image word_seo       = "bg/main_im/ch3/seo.png"

# --- 느린 디졸브(없어서 에러나는 것 방지) ---
init python:
    dissolve_slow = Dissolve(0.8)

# --- 퍼즐 로직/상태 ---
init python:
    import random

    # 정답 순서(왼->오): 독/립/선/언/서
    CORRECT_ORDER = ["dok", "rip", "seon", "eon", "seo"]

    # drag_name -> 이미지이름 매핑
    WORD_IMG = {
        "dok":  "word_dok",
        "rip":  "word_rip",
        "seon": "word_seon",
        "eon":  "word_eon",
        "seo":  "word_seo",
    }

    # 레일 Y좌표와 가로 범위(1920x1080 기준, 필요시 조정)
    RAIL_Y     = 400
    RAIL_MIN_X = 260
    RAIL_MAX_X = 1660

    # 시작 x 후보(대략 균등하게 배치되는 기준점)
    START_XS = [320, 640, 960, 1280, 1600]

    # 화면 변수 초기화(셔플해서 레일 위에 올리기)
    def _reset_dokrip_state_rail():
        renpy.store.dokrip_words = CORRECT_ORDER[:]  # 키 집합 고정
        random.shuffle(renpy.store.dokrip_words)     # 출현 순서 셔플
        xs = START_XS[:]
        random.shuffle(xs)
        renpy.store.word_xy = {}
        for i, key in enumerate(renpy.store.dokrip_words):
            renpy.store.word_xy[key] = [xs[i], RAIL_Y]

    # 가로만 움직이도록 고정(드래그 콜백)
    def clamp_horizontal(drags, drop):
        d = drags[0]
        # y는 항상 레일로
        d.y = RAIL_Y
        # x는 범위 제한
        if d.x < RAIL_MIN_X: d.x = RAIL_MIN_X
        if d.x > RAIL_MAX_X: d.x = RAIL_MAX_X
        # 현재 좌표 저장
        renpy.store.word_xy[d.drag_name] = [d.x, d.y]
        return None

    # 현재 x좌표 기준 왼->오 순서가 정답인지 확인
    def check_order_by_x():
        items = []
        for key in renpy.store.dokrip_words:
            x, y = renpy.store.word_xy[key]
            items.append((x, key))
        items.sort()  # x 오름차순
        ordered = [k for _, k in items]
        return ordered == CORRECT_ORDER

    # 보기 좋게 균등 슬롯으로 스냅(선택 기능)
    def _snap_to_even_slots():
        items = []
        for key in renpy.store.dokrip_words:
            x, y = renpy.store.word_xy[key]
            items.append((x, key))
        items.sort()
        for i, (_, key) in enumerate(items):
            renpy.store.word_xy[key] = [START_XS[i], RAIL_Y]
        renpy.restart_interaction()

    # 확인 버튼 액션

    def _rail_check_then_return():
        if check_order_by_x():
            renpy.end_interaction("success")  # ← 여기!
        else:
            renpy.end_interaction("retry")    # ← 여기!
    # def _rail_check_then_return():
    #     if check_order_by_x():
    #         renpy.return_("success")
    #     else:
    #         renpy.return_("retry")

# --- 화면(Screen) ---
screen dokrip_rail():
    tag dokrip_rail
    modal True

    # 배경
    add "imch3_bg_dokrip" at custom_size

    # 레일 가이드(얇은 선)
    add Solid("#FFFFFF30") at Transform(xysize=(1440, 6)) xpos 240 ypos RAIL_Y

    # 드래그 가능한 단어들
    draggroup:
        for key in dokrip_words:
            $ x, y = word_xy[key]
            drag:
                drag_name key
                child WORD_IMG[key]      # ← 여기서 이미지가 들어간다!
                draggable True
                droppable False
                xpos x
                ypos y
                anchor (0.5, 0.5)
                dragged clamp_horizontal

    # 안내문
    frame:
        align (0.5, 0.08)
        padding (16, 12)
        text "글자를 움직여 ‘독립선언서’ 작성을 시작하자." size 34

    # 하단 버튼
    hbox:
        align (0.5, 0.92)
        spacing 20
        textbutton "확인"     action Function(_rail_check_then_return)


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