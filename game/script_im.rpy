# 민욱 담당
# 임규 루트 스크립트



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
define choi = Character("최남선", image = "choi",color="#4a2222")


image bk1_hover         = At("main_im/bk1_hover.png", custom_size)
image bk2_hover         = At("main_im/bk2_hover.png", custom_size)
image bg_table_empty           = At("bg/table_empty.png", custom_size)             
image bk3_hover         = At("main_im/bk3_hover.png", custom_size)           
image side choi  = "ch/choi.png"         
image bead  = "main_im/bead.png"
image ch1_door         = At("main_im/door.png", custom_size)             
image ch1_table         = At("main_im/table.png", custom_size)             
image ch1_table_ex        = At("main_im/table_ex.png", custom_size)             
image bg_darkroom        = At("main_im/darkroom.png", custom_size)


# 게임 시작
label character_im:
    scene ch1_table_ex with fade_slow   #책들이 놓여있는 이미지, 이미지 축소해야함.

    m "얼굴을 보면 분명히 한국인일 텐데…"
    m "일본어책도 여러 권 있고, 원래 이분은 일본어를 상당히 잘하셨나 본데?"
    m "그리고 이건 한국 고전인가?"
    m "책상 위에 책들이 이리저리 놓여 있네."

    # 인터랙티브 테이블 사용
    call screen interactive_table_im
    
    # 선택에 따른 분기
    if _return == "next_ch":
        $ chosen_character = "jang" # 장기영
        narrator '우리 민족 전통은 이어져야 하지. 그러기 위해선 고전을 잊어선 안돼.'
        m "머릿속에서 들리는 말이나, 여기 책들을 보면 고전을 연구하던 분이셨구나."
        m "밖에서 쓰는 말이나, 보이는 풍경으로 봐서는 일제강점기 같은데..."
        m "이런 시기에 우리의 고전을 연구하셧따면, 대단하신 분일 거야."
        jump chapter1
return

#구슬 등장
label chapter1:
    scene ch1_table with fade_fast

    show bead with fade_slow   #구슬 등장
    m "이게 뭐지? 갑자기 웬 구슬"
    m "이건...."

    ##########브금 넣어야 함.##########
    
    hide bead with fade_slow #구슬 사라짐

    m '구슬을 보고 있던 차에, 누군가 문을 두드렸다.'

    scene ch1_door with Dissolve(5) # 교차 디졸브

    narrator "우정 선생님, 안에 계신가요?"

    m "누가 찾아온 듯하다."
    m "누굴까? 함께 고전 연구를 함께하는 사람인가?"
    m "나는 아무 생각 없이 문을 열려다가 멈칫했다."
    m "잠깐만, 누군지도 모르는데 문을 열어줘도 되나?"

    menu:

        "열어 준다.":
            jump say_choi

        "열어 주지 않는다.":
            jump say_no

label say_no:
    m "최남선? 들어본 것 같은데.."
    m "누군가 속사이는 소리가 들린다"
    narrator "이 사람은 믿을 수 있다. 함께 일하는 동지 최남선이다."

    m "나는 홀린 듯이 문을 열었다."
    jump say_choi
return

label say_choi:
    choi "사실, 전 오늘은 긴히 드릴 말씀이 있어 이리 찾아오게 되었습니다."
    
    jump chapter2

return

label chapter2:
    scene bg_darkroom with fade_slow

    choi "우정 선생님, 우리는 만세 운동을 시행하려고 합니다."

    m '만세 운동? 3.1운동을 만하는 건가?'
    m '그럼 지금은 3.1운동 직전 시기인가 보네.'

    choi "저는 독립선언서를 작성하기로 했습니다."
    choi "그래서, 선생님께 이 일에 대한 조언을 구하고자 합니다"

    #선택에 따른 분기

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
    m "’도와주겠다는 마음을 먹자, 저절로 입이 열렸다.’"
    m "’이분은 큰 위험을 감수하고도 만세 운동을 돕고자 하는 사람이었던 것 같다.’"

    show bead with fade_slow

    m "또 구슬이 나타났다."
    m "이 구슬은 뭘까...."
    m "그런데 아까와 다르게 갑자기 주변이 변화하는 것 같다."
    m "ㅁ...무..뭐지? 순간이동?"

    hide bead with fade_slow

    jump chater3

label chapter3:



#1. 수정 보충 사항 정리
# -말하는 주체 수정
# -최남선 말풍선 가림
# -호버, 다음으로 버튼을 통해 스토리 진행 :: 지금 상태 보고 기획에서 괜찮으면 굳이 안 바꿔도 될듯
# 구슬, bgm 삽입