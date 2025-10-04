# 게임에서 사용할 캐릭터를 정의합니다.
define im = Character('임규', color="#4ecdc4")
define narrator = Character(None)
define p = Character('나', color="#ffffff")  # 주인공 (이름 미상)


# 이미지 정의
image bg table_im = "table_im.png"
image bg table_im_suc = "table_im_suc.png"
image bg mirror = "mirror.png"       # 거울 배경
image mirror im = "im_mr.png"       # 거울 속 임규
image char im = "im.png"           # 임규 캐릭터  
image black = "#000000"                 # 검은 화면

# 화면 전환 효과 정의
define fade = Fade(0.75, 0.25, 0.75)
define dissolve_slow = Dissolve(1.0)

# Drag and drop
screen declaration_dragdrop():

    modal True
    default placed = {"s1": None, "s2": None, "s3": None, "s4": None, "s5": None}

    $ slots = {
        "s1": (384, 270),   # 독
        "s2": (614, 486),   # 립
        "s3": (902, 270),   # 선
        "s4": (1094, 486),  # 언
        "s5": (1382, 270),  # 서
    }

    for sid, (xp, yp) in slots.items():
        drag:
            draggable False
            droppable True
            drag_name sid
            xpos xp ypos yp
            xanchor 0.5 yanchor 0.5
            xysize (140, 140)   # ← 드롭 판정 조금 넉넉하게

            fixed:
                xysize (120, 120)  # 테두리는 그대로 120
                xpos 10 ypos 10     # 외곽 판정(140) 안쪽에 테두리(120) 위치
                add Solid("#0000")
                add Solid("#333") xpos 0   ypos 0   xsize 120 ysize 2
                add Solid("#333") xpos 0   ypos 118 xsize 120 ysize 2
                add Solid("#333") xpos 0   ypos 0   xsize 2   ysize 120
                add Solid("#333") xpos 118 ypos 0   xsize 2   ysize 120

            # ★★ 여기! Function 제거하고 콜백 직접 넘김 ★★
            dropped _on_drop(sid)

    draggroup:
        use letter_piece("독", 200, 900)
        use letter_piece("립", 500, 900)
        use letter_piece("선", 800, 900)
        use letter_piece("언", 1100, 900)
        use letter_piece("서", 1400, 900)

    textbutton "완료":
        xpos 960 ypos 1000 xanchor 0.5
        action Function(_check_solution, placed)


# 글자 조각 (픽셀 기준)
screen letter_piece(ch, xp, yp):
    drag:
        draggable True
        drag_name ch
        drag_raise True
        xpos xp ypos yp
        xanchor 0.5 yanchor 0.5
        child Text(ch, size=60, color="#111", outlines=[(2, "#000", 0, 0)])


# ── 드롭 처리 & 정답 검사
init python:
    # dropped 콜백: (dragged, dropped) 인자를 자동으로 받는다.
    def _on_drop(slot_id):
        def _cb(dragged, dropped):
            scr = renpy.current_screen()
            if scr:
                scr.scope["placed"][slot_id] = dragged.drag_name
            # 슬롯 중앙으로 스냅
            try:
                dragged.snap(dropped)
            except Exception:
                dragged.snap(dropped.xpos, dropped.ypos)
        return _cb

    def _check_solution(placed):
        target = ["독", "립", "선", "언", "서"]
        now = [placed["s1"], placed["s2"], placed["s3"], placed["s4"], placed["s5"]]

        if None in now:
            renpy.notify("아직 빈 슬롯이 있어!")
            return

        if now == target:
            renpy.say(None, "독립선언서 완성!")
            renpy.jump("next_scene")
        else:
            renpy.notify("순서가 달라. 다시 맞춰봐!")


# 여기에서부터 게임이 시작합니다.
label start:   #label route_im:
    show mirror im at left with dissolve_slow
    
    narrator "거울 속에는... 낯선 남성이 서 있다."
    narrator "단정하게 자른 짧은 머리와 지적인 인상을 주는 수염."
    narrator "온화하면서도 굳건한 의지가 느껴지는 눈빛."
    
    p "이 사람은... 누구지? 그런데 왜 내가 이 모습으로..."
    
    # 기억 각성 연출
    $ renpy.pause(0.5)
    scene black with Fade(0.3, 0.5, 0.3)
    
    narrator "머릿속에 무수한 기억들이 스며든다."
    narrator "교육... 계몽... 민족의식... 조선어학회..."
    
    scene bg mirror with dissolve_slow  
    show char im at left
    
    im "나는... 임규다."
    im "조선의 교육자이자 언어학자 임규."
    
    $ awakening_complete = True
    narrator "이제 이해했다."
    narrator "나는 일제강점기 조선어 보존과 민족교육에 힘쓰던 임규가 되어 있다."
    
    scene black with fade
    pause 1.0

    im "그래 우린 독립을 위해 싸우고 있어."

    im "독립선언서을 작성하자"



    #[Scene2] Drag and drop
    scene bg table_im with fade

    narrator "글자를 끼워 넣어 독립선언문을 완성하자."

    call screen declaration_dragdrop

    return

label next_scene:
    scene table_im_suc

    im "드디어 완성했다. 우리의 독립선언문이...!"

    return
