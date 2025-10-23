# 엔딩과 결과 페이지 스크립트

# 1. 이미지 최신화
# 2. 사인을 직접?

#음악
define audio.outro = "audio/bgm/outro_bgm.mp3"
define audio.outro_scene3 = "audio/bgm/outro_scene3.mp3"

#이미지
image memory_orb-0 = "bg/memory_orb-0.png"
image bg_bookback = At("bg/outro/book_back.png", custom_size)
image im_ending = At("bg/outro/im_ending.png", custom_size)
image oh_ending = "bg/outro/oh_ending.png"
image jang_ending = "bg/outro/jang_ending.png"
image book2 = "bg/outro/book2.png"
image book2_hover = "bg/outro/book2_hover.png"

# === 토글용 변수 기본값  ===
default end2_show_a = False
default end2_show_b = False
default end2_show_c = False


label im_ending_placeholder:
    play music audio.outro
    scene bg_desk with dissolve
    

    m "마지막 기억 구슬을 찾고 현실 세계로 복귀했다."
    m "하도 생생해서 꿈인지 현실인지 모르겠다."

    m "아 맞다. 시험 공부! 빨리 책상에 앉아서 공부해야겠다."

    m "이게 뭐지? 처음 보는 책인데..?"
    
    # 인터랙티브 테이블 사용
    show screen mission_guide("책을 펴보자.", icon="🔍")
    call screen interactive_desk
    hide screen mission_guide


    # 선택에 따른 분기
    if _return == "book2_selected":
        jump ending_scene2
    
    return

label ending_scene2:
    scene im_ending with fade_fast

    # 미션 가이드는 잠깐 보여주고(0.8초 예시) 숨김
    show screen mission_guide("더 알고싶은 사건에 마우스를 올려보자..", icon="🔍")
    $ renpy.pause(0.8)
    hide screen mission_guide

    # 토글용 변수 초기화 (매번 동일 상태에서 시작)
    $ end2_show_a = end2_show_b = end2_show_c = False

    # 토글 화면 + 우하단 네비 표시
    show screen ending_scene2_ui
    show screen next_nav_to("ending_scene3")

    # 유저가 버튼 누를 때까지 대기
    $ renpy.pause(hard=True)
    return
label ending_scene3:
    scene bg_desk with fade_slow

    jump ending_scene4

return


label ending_scene4:
    scene bg_bookback with fade_fast

    
# 기억구슬 등장

    play sound audio.outro_scene3

    show memory_orb-0 with dissolve
    play sound memory_orb_appear fadein 0.5 fadeout 3.0
    pause 1.0
    
    # 클릭 후 사라짐
    show screen mission_guide("기억구슬을 눌러보세요.", icon="🔮")
    call screen interactive_objects("memory_orb-0")
    hide screen mission_guide

    hide memory_orb-0 with dissolve
    pause 0.5
    
    # 블랙아웃
    scene bg_black with fade_slow
    pause 2.0


    narrator "이 순간도 기억 구슬에 담겼습니다."
    narrator "오늘 독립운동가와 함께 획득한 기억 구슬들을\n앞으로도 떠올려주세요."


    jump end
    
    # 챕터3로 이어짐
label end:
    scene bg_desk
    with dissolve
    
    show screen exit_button  # 나가기 버튼 표시
    
    narrator "제작 : 고려대학교 HUSS  고연우, 강지온, 길유진, 안지원, 양예진, \n이민욱, 정정비, 정채연, 조정현, 최가빈"

#--------------------------------------------------------------
# 호버 > 책
screen interactive_books(idle_image, hover_image=None, use_alpha=False, return_value="clicked"):
    
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

screen interactive_desk():
    
    
    # 분기를 위해 return_value를 사용. 일반적인 인터랙티브에는 필요 없음.
    use interactive_books("book2", return_value="book2_selected")





#-----------------------------------------

# === ending_scene2 본문 UI (토글 영역) ===
screen ending_scene2_ui():
    
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

# === 우하단 네비 버튼 (오버레이) ===
screen next_nav_to(label_name):
    zorder 200
    modal False
    textbutton "뒷 페이지 넘기기":
        anchor (1.0, 1.0)
        pos (0.97, 0.95)     # 1920x1080 기준 오른쪽 하단(비율 좌표)
        # 픽셀로 고정하고 싶으면: xpos 1840 ypos 1015
        action [
            Hide("ending_scene2_ui"),
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