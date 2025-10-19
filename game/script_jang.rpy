# 정현 담당
# 장기영 루트 스크립트
# script.rpy의 정의들을 모두 사용 가능

# =============================================================================
# 애니메이션 정의
# =============================================================================

transform slide_backwards:
    zoom 0.7
    xalign 0.5
    yalign -0.5
    easein 1.0 yalign 1.0

# =============================================================================
# 변수 정의
# =============================================================================
default draggable = ""
default droppable = ""

# =============================================================================
# 이미지 정의
# =============================================================================

# 챕터1 배경 이미지
image bg_room = At("bg/main_jang/ch1/room.png", custom_size)
image bg_passport_doc = "bg/main_jang/ch1/passport_doc.png" # At custom_size 애니메이션 안됨.
image bg_shanghai_harbor = At("bg/main_jang/ch1/harbor.png", custom_size)
image bg_shanghai_gov = At("bg/main_jang/ch1/shanghai_gov.png", custom_size)

# 챕터1 오브젝트 이미지
image table_passport_doc = At("bg/main_jang/ch1/table_passport_doc.png", custom_size)
image table_passport_doc_hover = At("bg/main_jang/ch1/table_passport_doc_hover.png", custom_size)

# 챕터1 캐릭터 이미지
image kim = Transform("ch/kim.png", zoom=0.8)
image ahn = Transform("ch/ahn.png", zoom=0.8)

# 챕터2 배경 이미지
image bg_usa_street = At("bg/main_jang/ch2/usa_street.png", custom_size)
image bg_usa_street_dark = At(Transform("bg/main_jang/ch2/usa_street.png", matrixcolor=BrightnessMatrix(-0.3)), custom_size)
image bg_office = At("bg/main_jang/ch2/office.png", custom_size)

# 챕터2 오브젝트 이미지
image envelop = "bg/main_jang/ch2/envelop.png"
image envelop_hover = "bg/main_jang/ch2/envelop_hover.png"
image letter_from_lee = "bg/main_jang/ch2/letter.png"
image money-1 = At("bg/main_jang/ch2/money-1.png", custom_size)
image money-2 = At("bg/main_jang/ch2/money-2.png", custom_size)
image money-3 = At("bg/main_jang/ch2/money-3.png", custom_size)
image bubble-1 = At("bg/main_jang/ch2/bubble-1.png", custom_size)
image bubble-2 = At("bg/main_jang/ch2/bubble-2.png", custom_size)
image bubble-3 = At("bg/main_jang/ch2/bubble-3.png", custom_size)

# 챕터2 캐릭터 이미지
image lee = Transform("ch/lee.png", zoom=0.8)

# 챕터3 배경 이미지
image bg_usa_phone = At("bg/main_jang/ch3/bg_phone.png", custom_size)

# 챕터3 오브젝트 이미지
image usa_newspaper = "bg/main_jang/ch3/newspaper.png"
image usa_newspaper_hover = "bg/main_jang/ch3/newspaper_hover.png"
image usa_newspaper_open = "bg/main_jang/ch3/newspaper_open.png"
image usa_phone = At("bg/main_jang/ch3/phone.png", custom_size)
image usa_phone_hover = At("bg/main_jang/ch3/phone_hover.png", custom_size)

# 챕터4 배경 이미지
image bg_pacific_map = At("bg/main_jang/ch4/pacific_map.png", custom_size)
image bg_chungking_gov = At("bg/main_jang/ch4/chungking_gov.png", custom_size)
image bg_radio_dark = At("bg/main_jang/ch4/radio_dark.png", custom_size)
image bg_radio = At("bg/main_jang/ch4/bg_radio.png", custom_size)

# 챕터4 오브젝트 이미지
image radio = At("bg/main_jang/ch4/radio.png", custom_size)
image radio_hover = At("bg/main_jang/ch4/radio_hover.png", custom_size)
image red_circle = Transform("bg/main_jang/ch4/red_circle.png", zoom=0.66)
image walkie_talkie = "bg/main_jang/ch4/walkie_talkie.png"
image translate_icon = "bg/main_jang/ch4/translate_icon.png"
image secret_doc = "bg/main_jang/ch4/secret_doc.png"
image old_map = "bg/main_jang/ch4/old_map.png"

# =============================================================================
# 오디오 정의
# =============================================================================

# ch1
define audio.jang_refusal = "audio/sfx/jang_refusal.mp3"
define audio.boat_horn = "audio/sfx/boat_horn.mp3"

# ch2
define audio.jang_letter_get = "audio/sfx/jang_letter_get.mp3"
define audio.jang_money_get = "audio/sfx/jang_money_get.mp3"

# ch3
define audio.jang_pick_up_phone = "audio/sfx/jang_pick_up_phone.wav"
define audio.jang_newspaper_appear = "audio/sfx/jang_newspaper_appear.mp3"

# ch4
define audio.jang_ch4_independence = "audio/bgm/jang_ch4_independence.mp3"
define audio.jang_ch4_liberation = "audio/bgm/jang_ch4_liberation.mp3"
define audio.jang_goal_in = "audio/sfx/jang_goal_in.mp3"
define audio.jang_fighter_jet = "audio/sfx/jang_fighter_jet.wav"
define audio.jang_radio_change = "audio/sfx/jang_radio_change.mp3"
define audio.jang_last_orb_get = "audio/sfx/jang_last_orb_get.mp3"

# =============================================================================
# 캐릭터 정의 (장기영 전용)
# =============================================================================

# ch1 김구, 안창호 선생님 
define kim_ahn = Character("김구, 안창호", color="#37c2f5")

# ch2 이승만
define lee = Character("이승만", color="#ff6b9d")

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
    scene bg_black with dissolve
    pause 1.0

    show ui_ch1 with dissolve
    pause 2.0
    hide ui_ch1 with dissolve
    
    jang_thought "일본과 싸우려면 먼저 일본을 알아야 한다는 생각으로 건너왔건만, \n일본 관헌의 감시는 여전하구나."
    
    scene bg_room with fade_slow

    m "밖에서 들리는 소리는 아니고…원래 몸 주인의 마음속 소리인가보구나."
    m "이 책은 뭐지? 경제학 공부하는 학생인가? \n책상 오른쪽에 이건 여권 신청서?"
    
    # 여권 신청서 인터랙티브 화면
    show screen mission_guide("책상 위의 여권 신청서를 눌러보세요.", icon="📄")
    call screen interactive_objects("table_passport_doc")
    hide screen mission_guide
    
    # 여권 신청서를 클릭한 후
    jump jang_ch1_passport_choice

label jang_ch1_passport_choice:

    python:
        renpy.show("bg_passport_doc", at_list=[slide_backwards])
        renpy.with_statement(dissolve)
        renpy.pause(1.5)

        for attempt in range(2):
            
            # 메뉴 선택
            choice = renpy.display_menu([("여권 신청", True)])
            
            if choice:
                # '신청 거절' 텍스트 표시
                renpy.show("reject_text", what=Text("{size=80}{color=#ff0000}신청 거절{/color}{/size}", xalign=0.5, yalign=0.5))
                renpy.play("audio/sfx/jang_refusal.mp3")
                renpy.with_statement(dissolve)
                renpy.pause(2.0)
                renpy.hide("reject_text")
                renpy.with_statement(dissolve)
            
        renpy.hide("bg_passport_doc") # 여기서는 다시 슬라이드 못하나?  
        renpy.with_statement(dissolve)
                
    m "뭐지? 왜 신청을 안 받아주는 거야?"

    jang_thought "미국으로 가야 한다... 미국으로 가야 한다..." 

    m_thought "미국으로 가야 한다는 소리가 머릿속에서 반복되어서 들린다."
            
    jump jang_ch1_destination_choice

label jang_ch1_destination_choice:
    menu:
        "미국으로 가기":
            # '여권 없음' 텍스트 표시
            show text "{size=80}{color=#ff0000}여권 없음{/color}{/size}" at truecenter with dissolve
            play sound jang_refusal
            pause 1.0
            hide text with dissolve
            
            m "아, 여권이 없어서 미국으로 바로 갈 수는 없구나. \n다른 곳에 가서 방법을 찾아봐야 하나…"
            
            # 상해로 가기만 표시
            jump jang_ch1_destination_choice_shanghai_only
        
        "상해로 가기":
            m "마음속 소리대로 따라가야 나도 내가 가고 싶은 집으로 갈 수 있을거야."
            
            # 미국으로 가기만 표시
            jump jang_ch1_destination_choice_usa_only

label jang_ch1_destination_choice_shanghai_only:
    menu:
        "상해로 가기":
            jang_thought "여권은 없었지만 중국인으로 속여서 우선 상해에 도착할 수 있었다."
            jump jang_ch1_scene2

label jang_ch1_destination_choice_usa_only:
    menu:
        "미국으로 가기":
            # '여권 없음' 텍스트 표시
            show text "{size=80}{color=#ff0000}여권 없음{/color}{/size}" at truecenter with dissolve
            play sound jang_refusal
            pause 1.0
            hide text with dissolve
            
            m "아, 여권이 없어서 미국으로 바로 갈 수는 없구나. \n다른 곳에 가서 방법을 찾아봐야 하나…"
            
            # 상해로 가기로 이동
            jump jang_ch1_destination_choice_shanghai_only

# =============================================================================
# Scene 2: 항구 → 상해임시정부
# =============================================================================
label jang_ch1_scene2:
    # 항구 배경
    scene bg_shanghai_harbor with fade_slow
    
    # 뱃고동 소리 효과음
    play sound boat_horn
    pause 2.0
    
    m_thought "이곳이 상해구나."

    jang_thought "상해에 왔으니, 임시정부에 있는 위원들을 찾아가 보자. \n미국으로 갈 수 있는 방법을 찾을 수 있을 거야."
    
    m "상해임시정부? 공부하면서 봤던 거야! \n그럼 여기는 아마 1920년대 이후겠구나."
    m "기억 구슬 찾아서 집에 돌아가려면 이 마음의 소리대로 해야겠어."

    scene bg_black with fade_slow

    m "어? 갑자기 잠이 쏟아지네. 이러면 안되는데."

    jang_thought "나는 상해임시정부에서 잠시 활동하였다. \n어느 날 김구 선생님과 안창호 선생님께서 나를 부르셨다."
    
    # 상해임시정부 건물 앞으로 전환
    scene bg_shanghai_gov with dissolve
    
    # 김구, 안창호 선생님 등장
    show kim at left with dissolve
    show ahn at right with dissolve
    
    kim_ahn "상해에서 함께 활동해 주어서 고맙네. 어린 나이 때부터 러시아의 \n전한군사위원회{font=SourceHanSansLite.ttf}{size=30}(全韓軍事委員會){/size}{/font}의 위원으로도 활약한 자네였기에 \n더욱 든든했어."
    kim_ahn "이제는 미국 땅으로 가서 하던 공부를 이어서 하고 조국의 광복을 위해 \n힘써주게나."
    
    m_thought "이분들은 김구 선생님과 안창호 선생님? 교과서에서 봤어! \n나는 독립운동가의 몸에 들어왔나 봐!"

label jang_ch1_final_choice:
    menu:
        "저는 여기가 좋아요.":
            m_thought "내가 지금 정확히 누구 몸에 들어왔는지는 모르겠지만 이 사람이 원하는 대로 해보자. 미국으로 가고 싶다는 말을 몇 번이나 들었는지 모르겠어."
            jump jang_ch1_final_choice
        
        "가겠습니다.":
            hide kim
            hide ahn
            with dissolve
            
            # 기억구슬 등장 및 클릭 대기
            play sound memory_orb_appear fadein 0.5 fadeout 3.0
            pause 1.0
            show memory_orb-1 with dissolve
            pause 1.0
            
            show screen mission_guide("기억구슬을 눌러보세요.", icon="🔮")
            call screen interactive_objects("memory_orb-1")
            hide screen mission_guide
            
            m "중력의 영향을 받지 않고 떠있는 걸 보니 이게 기억 구슬이구나!"
            
            hide memory_orb-1 with dissolve

            m "어라? 분명히 쥐었는데 바로 사라졌어. 뭐지?"
            
            # 구슬 발견창 표시
            window hide
            show ui_orb_found_ch1 with dissolve
            play sound memory_orb_get
            pause 2.0
            hide ui_orb_found_ch1 with dissolve
            
            # 블랙아웃
            scene bg_black with fade_slow
            
            # 챕터2로 이어짐
            jump jang_ch2

# =============================================================================
# 챕터2: 구미위원부 위원으로 임명된 후 독립자금 및 교민 독립사상 고취 활동
# =============================================================================
label jang_ch2:
    # Scene 1: 1930년대 미국 길거리
    
    # 블랙아웃 유지 (챕터1의 블랙아웃에서 이어짐)
    scene bg_black
    show ui_ch2 with dissolve
    pause 2.0
    hide ui_ch2 with dissolve
    
    scene bg_usa_street with fade_very_slow
    
    jang_thought "호놀룰루의 교회에서 뵈었던 이박사님께서는 언제 본토에 들어오시는 \n것인가?"
    jang_thought "1, 2년 뒤면 올 것이라 하셨는데 벌써 5년이나 지났다."
    jang_thought "어서 연락이 닿아서 내가 이 땅에서 할 수 있는 일을 하고 싶어."
    
    m "뭐? 5년이나 지났어? 호놀룰루라면 하와이인데…미국 본토로 바로 \n올 수 있었던 것이 아니구나. 이분은 어떤 독립운동을 하셨던 걸까?"
    
    jang_thought "나는 지금 내가 당장 할 수 있는 일에 집중해야겠어."
    jang_thought "인디애나 대학에서의 국제법 공부는 일본과 맞서 싸우는 것에 도움이 \n될 것이야."
    
    m "어라? 이 편지봉투는 뭐지?"
    
    # 전보 인터랙티브 화면
    show screen mission_guide("편지봉투를 눌러보세요.", icon="✉️")
    call screen interactive_objects("envelop")
    play sound jang_letter_get
    hide screen mission_guide
    
    # 전보를 클릭한 후 - 편지 내용 표시
    scene bg_usa_street_dark
    show letter_from_lee at slide_backwards
    with dissolve

    pause 2.0
    
    m "상의할 것이 있으니, 워싱턴에 있는 구미위원부로 와달라고? \n누가 보낸 거야? 이승만이라면!"
    m "아까 그 이박사가 이승만 선생님이었구나!"
    
    # 블랙아웃
    scene bg_black with fade_slow
    pause 1.0
    
    jump jang_ch2_scene2

# =============================================================================
# Scene 2: 구미위원부 사무실
# =============================================================================
label jang_ch2_scene2:
    # 블랙아웃에서 시작
    
    m "조국의 독립을 위하여 곧장 달려가야 한다는 마음의 소리를 듣고서, \n나는 당장 실행에 옮겼다."
    
    # 구미위원부 사무실로 전환
    scene bg_office with fade_slow
    
    # 이승만 등장
    show lee with dissolve
    
    lee "기다리던 중 빨리 와주어 고맙소."
    lee "국제연맹에 가 항의할 것이 있어 그런데…"
    lee "석정이 구미위원부 위원이 되어 이곳 사무실을 지켜줄 수 있겠는가?"

label jang_ch2_gumi_choice:
    menu:
        "다른 선배님들께 맡기는 것이 좋지 않겠습니까?":
            lee "일본 사람의 심부름이 싫어 미국으로 온 줄 알았는데 일본 사람에게 \n협조하러 이곳에 온 것이로군."
            jump jang_ch2_gumi_choice
        
        "이곳에 남아 일할테니, 내일이라도 곧 떠나십시오.":
            lee "우리 구미위원부에서는 일본의 만행을 세계에 알리고, 독립 자금을 \n모집하고, 교민들의 독립사상을 고취하는 일을 하고 있다네."
            
            hide lee with dissolve
            
            m_thought "독립운동을 하기 위한 돈을 모으고, 해외에 거주하고 있는 우리나라 \n사람에게 독립의 중요성을 알린다는 뜻이구나!"
            m_thought "열심히 해보자!"
            
            # 블랙아웃
            scene bg_black with fade_slow
            pause 1.0
            
            # Scene3로 이어짐
            jump jang_ch2_scene3

# =============================================================================
# Scene 3: 1930년대 미국 길거리 - 독립자금 모금 활동
# =============================================================================
label jang_ch2_scene3:
    
    # 1930년대 미국 길거리 배경
    scene bg_usa_street with fade_slow
    pause 1.0
    
    jang_thought "거리에서 독립자금 모금 활동을 시작했다."
    jang_thought "하지만 많은 사람들이 의구심과 회의적인 반응을 보였다."
    jang_thought "교민들의 반응을 듣고 설득해보자."

    # 인터랙티브 스크린 호출
    scene bg_usa_street_dark with dissolve
    show screen mission_guide("교민들의 말풍선을 모두 눌러보세요.", icon="💰")
    call screen interactive_fundraising
    hide screen mission_guide
    
    # 모든 말풍선을 클릭한 후
    jump jang_ch2_finale

label jang_ch2_finale:

    # 기억구슬 등장
    scene bg_usa_street with dissolve

    show memory_orb-2 with dissolve
    play sound memory_orb_appear fadein 0.5 fadeout 3.0
    pause 1.0
    
    # 클릭 후 사라짐
    show screen mission_guide("기억구슬을 눌러보세요.", icon="🔮")
    call screen interactive_objects("memory_orb-2")
    hide screen mission_guide

    hide memory_orb-2 with dissolve
    pause 0.5
    
    # 구슬 획득창 표시
    window hide
    play sound memory_orb_get
    show ui_orb_found_ch2 with dissolve
    pause 2.0
    hide ui_orb_found_ch2 with dissolve
    
    # 블랙아웃
    scene bg_black with fade_slow
    pause 2.0
    
    # 챕터3로 이어짐
    jump jang_ch3

# =============================================================================
# 챕터3: 미국-일본 전쟁 확대로 한미 공동 전투 활동 필요성 통감한 후 미군에 자원입대
# =============================================================================
label jang_ch3:
    # Scene 1: 1930년대 미국 길거리
    
    # 블랙아웃에서 시작
    scene bg_black
    show ui_ch3 with dissolve
    pause 2.0
    hide ui_ch3 with dissolve
    
    # 1930년대 미국 길거리 배경
    scene bg_usa_street with fade_slow
    
    m_thought "구미위원부의 재정난으로 인디애나 대학으로 돌아가 다시 공부를 \n계속했다."
    
    # 신문이 아래에서 위로 올라오는 애니메이션
    play sound jang_newspaper_appear volume 2.0
    show usa_newspaper:
        xalign 0.5
        yalign 1.75
        easein 1.25 yalign 0.5
    pause 2.0
    hide usa_newspaper
    
    # 신문 클릭 대기
    show screen mission_guide("신문을 눌러보세요.", icon="📰")
    
    call screen interactive_objects("usa_newspaper")
    hide screen mission_guide
    
    # 신문을 클릭한 후
    jump jang_ch3_after_newspaper

label jang_ch3_after_newspaper:

    show usa_newspaper_open at slide_backwards
    with dissolve
    pause 1.0
    
    # 신문 속 텍스트 표시
    show screen framed_message("1941년 12월 8일 일본이 진주만을 기습", text_size=50)
    pause 2.0
    hide screen framed_message with dissolve
    
    jang_thought "일본이 드디어 잠자는 사자 미국을 깨워놓고 말았구나."
    jang_thought "드디어 우리나라가 독립할 때가 왔구나. 이제야 기회가 왔구나."
    jang_thought "워싱턴에 있는 이박사에게 당장 전화를 걸어야겠다."
    
    m_thought "전화라고요? 전화를 걸어보자."
    
    # 전화기 배경으로 전환
    scene bg_usa_phone with dissolve
    
    # 전화기 클릭 대기
    show screen mission_guide("전화기를 눌러보세요.", icon="📞")
    call screen interactive_objects("usa_phone")
    play sound jang_pick_up_phone volume 3.0
    hide screen mission_guide
    
    # 전화기를 클릭한 후
    jump jang_ch3_phone_menu

label jang_ch3_phone_menu:
    
    menu:
        "이박사님 저희 이제 어떡하면 좋은가요?":
            show text "{color=#000}{size=300}...{/size}{/color}" at Position(xalign=0.5, yalign=0.2) with dissolve
            pause 2.0
            hide text with dissolve
            
            m "음? 아직 연결이 안 되었구나."
            
            jump jang_ch3_phone_menu
        
        "조국의 해방을 위해 그곳으로 가겠습니다.":
            lee "아주 기쁘오. 곧 오기 바랍니다."
            
            jump jang_ch3_finale

label jang_ch3_finale:
    # 블랙아웃
    scene bg_black with fade_slow
    
    jang_thought "이박사와 상의 끝에 미군에 지원입대키로 결심했다. 미국은 35세 미만의 젊은 남성만을 뽑았기 때문에 40세인 나는 35세라고 속이고 지원병으로 들어갔다."
    
    m "네? 나이까지 속여서요? 이분 대체 뭐지?"
    
    jang_thought "이 기회를 놓치면 한국인으로서 독립운동에 참가할 기회가 없어지고 \n만다."
    
    m "잠깐! 그러면 나 이분의 몸으로 지금 미군에 입대하는 거야?"
    
    # 기억구슬 등장
    scene bg_black with dissolve
    play sound memory_orb_appear fadein 0.5 fadeout 3.0
    pause 1.5
    show memory_orb-3 with dissolve_slow
    pause 1.0

    # 클릭 후 사라짐
    show screen mission_guide("기억구슬을 눌러보세요.", icon="🔮")
    call screen interactive_objects("memory_orb-3")
    hide screen mission_guide
    hide memory_orb-3 with dissolve
    pause 0.5
    
    # 구슬 획득창 표시
    window hide
    play sound memory_orb_get
    show ui_orb_found_ch3 with dissolve
    pause 2.0
    hide ui_orb_found_ch3 with dissolve

    # 블랙아웃
    scene bg_black with fade_slow
    
    # 챕터4로 이어짐
    jump jang_ch4

# =============================================================================
# 챕터4: 미군으로 제 2차 세계 대전 참전 및 충칭 임시정부 연락원 활동
# =============================================================================
label jang_ch4:
    
    # Scene 1: 태평양 전쟁 및 충칭 임시정부 연락원
    # 태평양 지도 배경

    show ui_ch4 with dissolve
    pause 2.0
    hide ui_ch4 with dissolve

    play music jang_ch4_independence fadeout 2.0 fadein 2.0
    scene bg_pacific_map with fade_slow
    
    jang_thought "나는 미국 전략사무국인 OSS에 추천되어 정보, 통신 등의 특수교육을 받을 수 있었다."
    jang_thought "비밀리에 유격훈련을 받은 후 남태평양 지구에 투입되었고, 나는 조국의 광복을 위하여 위험한 일을 도맡아 했다."
    jang_thought "조국을 위하여 나의 목숨을 걸고 적군이 있는 근처의 지리와 군세에 \n관한 정보를 수집, 제공하는 일을 했다."
    jang_thought "나는 현재 육군 항공대 중령으로서 제2차 세계 대전에 참전하는 중이다."
    
    # 화면 전환 (디졸브) - 충칭 임시정부 청사
    scene bg_chungking_gov with dissolve
    pause 1.0
    
    jang_thought "충칭에 있는 임시정부의 연락원으로 활동하며 임시정부와의 협력을 다시 이어갔다."
    
    m_thought "어? 전에는 상해에 있었다며 이제는 충칭인가?"
    m_thought "연락원은 무슨 일을 하는 거지?"

    window hide
    
    # 드래그 앤 드롭 게임으로 전환
    $ walkie_placed = False
    $ translate_placed = False
    $ doc_placed = False
    $ map_placed = False
    
    jump placing_ch4_objects

label placing_ch4_objects:
    
    show screen mission_guide("흩어져 있는 정보들을 충칭 임정 청사로 보내세요.", icon="🔍")
    call screen drag_drop_ch4()
    hide screen mission_guide
    
    # 드래그 앤 드롭 결과 처리
    if draggable == "walkie_item" and droppable == "circle_drop":
        $ walkie_placed = True
        play sound jang_goal_in
        show screen after_drag_drop_ch4()
        jang_thought "연합군으로부터 작전 명령을 수신하고, 충칭의 임시정부와 다른 지역 간에 실시간으로 연락을 가능케 했어!"
    elif draggable == "translate_item" and droppable == "circle_drop":
        $ translate_placed = True
        play sound jang_goal_in
        show screen after_drag_drop_ch4()
        jang_thought "임시정부와 OSS의 합작을 위해 문서를 번역하고 연합국 측의 정보를 입수했어!"
    elif draggable == "doc_item" and droppable == "circle_drop":
        $ doc_placed = True
        play sound jang_goal_in
        show screen after_drag_drop_ch4()
        jang_thought "국내외 독립운동 조직 간의 정치적, 군사적, 행정적 정보를 은밀하게 \n전달했어!"
    elif draggable == "map_item" and droppable == "circle_drop":
        $ map_placed = True
        play sound jang_goal_in
        show screen after_drag_drop_ch4()
        jang_thought "지도를 전달해서 군사 작전을 계획하고 수행하는 것에 도움이 되었어!"
    
    # 모든 아이템이 배치되었는지 확인
    if walkie_placed and translate_placed and doc_placed and map_placed:
        hide screen mission_guide
        hide screen after_drag_drop_ch4
        jump ch4_all_items_placed
    else:
        jump placing_ch4_objects

label ch4_all_items_placed:

    scene bg_pacific_map:
        matrixcolor BrightnessMatrix(-0.3)
    with dissolve
    play sound jang_fighter_jet
    pause 1.0

    jang_thought "나는 다른 임무를 위해 다른 지역으로 비행하는 중 라디오 방송으로 \n일본의 항복 관련 소식을 들었다. 이는 종전을 의미한다. 그 비행기에 타고 있던 군인들이 모두 함성을 질렀다."
    
    jump jang_ch4_radio

label jang_ch4_radio:
    
    # 라디오가 있는 어두운 배경으로 전환
    scene bg_radio_dark with dissolve
    
    # 라디오 클릭 대기
    show screen mission_guide("라디오를 눌러보세요.", icon="📻")
    call screen interactive_objects("radio")
    play sound jang_radio_change
    hide screen mission_guide
    
    # 라디오 클릭 후
    jump jang_ch4_liberation

label jang_ch4_liberation:
    # 라디오 뉴스 텍스트 표시
    show screen framed_message("일본이 러시아를 중간에 내세워 항복을 교섭…", text_size=50)
    pause 2.0
    hide screen framed_message with dissolve
    
    # 배경음 전환
    play music jang_ch4_liberation fadeout 2.0 fadein 2.0
    
    m_thought "지금이 대체 몇 년도 몇 월 며칠이지?"
    m_thought "항복이라면 우리나라가 곧 독립된다는 것인가?"
    
    m "일제에 저항한 독립투사분들이 있고, 독립 의지를 세계에 얼마나 힘들게 끊임없이 알렸는데! 제발 해방이요!"
    
    jang_thought "갑작스럽기는 하지만 지금까지 조국의 광복을 위해 동지들과 함께 \n희생했고, 우리의 독립 정신을 전 세계에 알렸기에 분명히 독립할 수 있을 것이다."
    jang_thought "틀림없이 머지않아 우리나라가 독립되는구나."
    
    # 기억구슬 등장
    play sound memory_orb_appear fadein 0.5 fadeout 3.0
    pause 1.0
    show memory_orb-4 with dissolve_slow
    pause 1.0

    show screen mission_guide("기억구슬을 눌러보세요.", icon="🔮")
    call screen interactive_objects("memory_orb-4")
    hide screen mission_guide

    m "이게 마지막 구슬인가?"
    m "광복과 동시에 나는 현실 세계로 복귀하는구나."
    
    # 구슬 획득창 표시
    window hide
    hide memory_orb-4 with dissolve_slow
    pause 0.5
    show ui_orb_found_ch4 with dissolve
    play sound jang_last_orb_get
    pause 3.0
    hide ui_orb_found_ch4 with dissolve
    
    # 블랙아웃
    scene bg_black with fade_slow
    pause 2.0
    
    # 장기영 엔딩으로 이어짐

    $ character_ending = "jang_ending"
    jump ending_start
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
    
    # 화폐 이미지들
    if not clicked_money1:
        add "money-1"
    
    if not clicked_money2:
        add "money-2"
    
    if not clicked_money3:
        add "money-3"
    
    # 말풍선 1
    if not clicked_bubble1:
        if not show_jang_response:
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
        else:
            add "bubble-1"
    
    # 말풍선 2
    if not clicked_bubble2:
        if not show_jang_response:
            imagebutton:
                idle "bubble-2"
                hover Transform("bubble-2", alpha=0.8)
                focus_mask True
                action [
                    SetVariable("clicked_bubble2", True),
                    SetVariable("clicked_money2", True),
                    SetVariable("show_jang_response", True),
                    SetVariable("current_jang_text", "조국 없는 삶은 결국 뿌리 없는 삶이니, \n우리 후손에게는 반드시 독립된 나라를 물려주어야 합니다."),
                    Hide("interactive_fundraising"),
                    Show("interactive_fundraising")
                ]
        else:
            add "bubble-2"
    
    # 말풍선 3
    if not clicked_bubble3:
        if not show_jang_response:
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
        else:
            add "bubble-3"
    
    # 장기영의 응답 표시 (화면 하단)
    if show_jang_response and current_jang_text:
        window:
            id "jang_response_window"
            xalign 0.5
            xfill True
            yalign gui.textbox_yalign
            ysize gui.textbox_height
            background Image("gui/textbox.png", xalign=0.5, yalign=1.0)
            
            # 화자 이름박스 (screens.rpy의 namebox 스타일 참고)
            window:
                id "jang_namebox"
                xanchor 0.302
                xsize gui.namebox_width
                yalign 0.05
                ysize gui.namebox_height
                background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
                padding gui.namebox_borders.padding
                
                text "독립의 희망을 북돋기":
                    properties gui.text_properties("name", accent=True)
                    xalign gui.name_xalign
                    yalign 0.5
                    color "#ff5e5e"
            
            # 대사 내용 (screens.rpy의 say_dialogue 스타일 참고)
            vbox:
                xpos gui.dialogue_xpos
                xsize gui.dialogue_width
                ypos gui.dialogue_ypos
                
                text current_jang_text:
                    properties gui.text_properties("dialogue")
                    line_spacing gui.dialogue_line_spacing
                    color "#FFFFFF"
                
                text " " size 10  # 간격 조정
                
                textbutton "▷ 독립운동자금 받기":
                    xalign 0.5
                    text_size 28
                    text_color "#FFD700"
                    text_hover_color "#FFA500"
                    action [
                        Play("sound", "audio/sfx/jang_money_get.mp3"),
                        SetVariable("show_jang_response", False),
                        SetVariable("current_jang_text", ""),
                        Hide("interactive_fundraising"),
                        Show("interactive_fundraising")
                    ]
    
    # 모든 말풍선을 클릭했는지 확인
    if clicked_bubble1 and clicked_bubble2 and clicked_bubble3 and not show_jang_response:
        timer 0.5 action Return("all_bubbles_clicked")

# =============================================================================
# 챕터4 드래그 앤 드롭 스크린
# =============================================================================
init python:
    def drag_placed(drags, drop):
        if not drop:
            return
        
        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name
        return True

screen after_drag_drop_ch4():
    
    add "bg_pacific_map"
    if not walkie_placed:
        add "walkie_talkie":
            zoom 0.6 xalign 0.68 yalign 0.12
    if not translate_placed:
        add "translate_icon":
            zoom 0.6 xalign 0.88 yalign 0.86
    if not doc_placed:
        add "secret_doc":
            zoom 0.6 xalign 0.58 yalign 0.65
    if not map_placed:
        add "old_map":
            zoom 0.6 xalign 0.92 yalign 0.4

screen drag_drop_ch4():
    
    add "bg_pacific_map"

    # 드래그 그룹
    draggroup:
        # ===== 무전기 =====
        # 드래그 가능한 무전기
        if not walkie_placed:
            drag:
                drag_name "walkie_item"
                child Transform("walkie_talkie", zoom=0.6)
                droppable False
                dragged drag_placed
                drag_raise True
                xalign 0.68 
                yalign 0.12
        
        # ===== 번역 아이콘 =====
        # 드래그 가능한 번역 아이콘
        if not translate_placed:
            drag:
                drag_name "translate_item"
                child Transform("translate_icon", zoom=0.6)
                draggable True
                droppable False
                dragged drag_placed
                drag_raise True
                xalign 0.88 
                yalign 0.86
        
        # ===== 비밀 문서 =====
        # 드래그 가능한 비밀 문서
        if not doc_placed:
            drag:
                drag_name "doc_item"
                child Transform("secret_doc", zoom=0.6)
                draggable True
                droppable False
                dragged drag_placed
                drag_raise True
                xalign 0.58 
                yalign 0.65
        
        # ===== 낡은 지도 =====
        # 드래그 가능한 낡은 지도
        if not map_placed:
            drag:
                drag_name "map_item"
                child Transform("old_map", zoom=0.6)
                draggable True
                droppable False
                dragged drag_placed
                drag_raise True
                xalign 0.92
                yalign 0.4
        
        # ===== 붉은 원 드롭 영역 =====
        drag:
            drag_name "circle_drop"
            child "red_circle" # map_circle은 원 이미지 + 네모 영역 => drag를 어디에 해도 인식됨.
            draggable False
            droppable True
            xalign 0.23
            yalign 0.48