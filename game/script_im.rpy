# 민욱 담당
# 임규 루트 스크립트



# # === 책 정보 (전역) ===
# screen interactive_table_im():
#     # 기본 테이블 이미지
#     add "ch1_table_ex" at custom_size
    
#     # 신문 영역 (중간 하단)
#     imagemap:
#         ground Null(1920, 1080)  # 투명한 배경
#         hover "im_bk1_hover"
#         alpha True
#         at custom_size
#         hotspot (0, 0, 1920, 1080):
#             action Return("bk1_selected")
            
#     # 책 영역 (우측 상단)        
#     imagemap:
#         ground Null(1920, 1080)  # 투명한 배경
#         hover "im_bk2_hover"
#         alpha True
#         at custom_size
#         hotspot (0, 0, 1920, 1080):
#             action Return("bk2_selected")
    
#     # 총 영역 (좌측 상단)
#     imagemap:
#         ground Null(1920, 1080)  # 투명한 배경
#         hover "im_bk3_hover"
#         alpha True
#         at custom_size
#         hotspot (0, 0, 1920, 1080):
#             action Return("bk3_selected")

# script.rpy의 정의들을 모두 사용 가능

image ch1_bk1         = At("im/bk1_hover.png", custom_size)
image ch1_bk2         = At("im/bk2_hover.png", custom_size)
image bg_table_empty           = At("bg/table_empty.png", custom_size)             
image ch1_bk3         = At("im/bk3_hover.png", custom_size)
image bg_asset_book         = At("assets/asset_book.png")
image bg_asset_gun         = At("assets/asset_gun.png")
image bg_asset_news         = At("assets/asset_news.png")             
image ch1_choi         = At("im/choi.png", custom_size)             
image ch1_door         = At("im/door.png", custom_size)             
image ch1_table         = At("im/table.png", custom_size)             
image ch1_table_ex         = At("im/table_ex.png", custom_size)

# 변수 초기화
default gun_placed = False
default book_placed = False
default news_placed = False

# 드래그 앤 드롭 처리 함수
init python:
    def drag_placed(drags, drop):
        if not drop:
            return False
        
        drag_name = drags[0].drag_name
        drop_name = drop.drag_name
        
        # 올바른 슬롯에 드롭되었는지 확인
        if drag_name == "gun" and drop_name == "slot_red":
            store.gun_placed = True
            return True
        elif drag_name == "book" and drop_name == "slot_green":
            store.book_placed = True
            return True
        elif drag_name == "news" and drop_name == "slot_purple":
            store.news_placed = True
            return True
        
        # 잘못된 위치면 원래 자리로 돌아감
        return False
    
    def check_all_placed():
        """모든 아이템이 배치되었는지 확인"""
        return gun_placed and book_placed and news_placed

# 게임 시작
label character_im:
    $ gun_placed = False
    $ book_placed = False
    $ news_placed = False
    
    call drag_drop_scene
    
    return

# 드래그 앤 드롭 씬 (재귀 사용)
label drag_drop_scene:
    scene bg_table_empty
    
    show screen drag_drop_screen
    
    # 사용자 입력 대기
    pause
    
    # 모든 아이템이 배치되지 않았다면 재귀 호출
    if not check_all_placed():
        call drag_drop_scene
    
    return

# 완료 후 다음 씬
label complete_scene:
    hide screen drag_drop_screen
    
    scene bg_table
    centered "Complete! All items placed correctly."
    
    # 다음 씬으로 이동
    "Proceeding to next scene..."
    
    return

# 드래그 앤 드롭 스크린
screen drag_drop_screen():
    
    # 상태 표시 (디버깅용 - 원하면 제거 가능)
    frame:
        xalign 1.0
        yalign 0.0
        xpadding 20
        ypadding 20
        background "#000000cc"
        
        vbox:
            text "Gun = [gun_placed]" size 20 color "#ffffff"
            text "Book = [book_placed]" size 20 color "#ffffff"
            text "News = [news_placed]" size 20 color "#ffffff"
    
    # 배치된 아이템 표시 (draggroup 밖에서)
    if gun_placed:
        add "asset_gun" xpos 400 ypos 250
    
    if book_placed:
        add "asset_book" xpos 800 ypos 250
    
    if news_placed:
        add "asset_news" xpos 600 ypos 500
    
    # 드래그 앤 드롭 그룹
    draggroup:
        
        # 슬롯 1: 빨간색 영역 (테이블 왼쪽 위) - Gun
        drag:
            drag_name "slot_red"
            droppable True
            draggable False
            xpos 400
            ypos 250
            xysize (200, 200)
            
            # 디버깅용 - 실제로는 투명하게 하려면 주석 처리
            # add Solid("#ff000033")
        
        # 슬롯 2: 초록색 영역 (테이블 오른쪽 위) - Book
        drag:
            drag_name "slot_green"
            droppable True
            draggable False
            xpos 800
            ypos 250
            xysize (200, 200)
            
            # 디버깅용 - 실제로는 투명하게 하려면 주석 처리
            # add Solid("#00ff0033")
        
        # 슬롯 3: 보라색 영역 (테이블 아래 중앙) - News
        drag:
            drag_name "slot_purple"
            droppable True
            draggable False
            xpos 600
            ypos 500
            xysize (200, 200)
            
            # 디버깅용 - 실제로는 투명하게 하려면 주석 처리
            # add Solid("#ff00ff33")
        
        # 총 (아직 배치되지 않았을 때만 표시)
        if not gun_placed:
            drag:
                drag_name "gun"
                draggable True
                droppable False
                drag_raise True
                
                xpos 100
                ypos 800
                
                add "asset_gun"
                
                dragged drag_placed
        
        # 책 (아직 배치되지 않았을 때만 표시)
        if not book_placed:
            drag:
                drag_name "book"
                draggable True
                droppable False
                drag_raise True
                
                xpos 1500
                ypos 800
                
                add "asset_book"
                
                dragged drag_placed
        
        # 신문 (아직 배치되지 않았을 때만 표시)
        if not news_placed:
            drag:
                drag_name "news"
                draggable True
                droppable False
                drag_raise True
                
                xpos 750
                ypos 650
                
                add "asset_news"
                
                dragged drag_placed
    
    # Complete 버튼 (모든 아이템이 배치되었을 때만 표시)
    if check_all_placed():
        imagebutton:
            xalign 0.5
            yalign 0.9
            idle Text("Complete", size=40, color="#ffffff", outlines=[(2, "#000000")])
            hover Text("Complete", size=40, color="#ffff00", outlines=[(2, "#000000")])
            action Jump("complete_scene")

    # scene ch1_table_ex with fade_slow   #책들이 놓여있는 이미지, 이미지 축소해야함.
    # show im_portrait at left
    # m "얼굴을 보면 분명히 한국인일 텐데…"
    # m "일본어책도 여러 권 있고, 원래 이분은 일본어를 상당히 잘하셨나 본데?"
    # m "그리고 이건 한국 고전인가?"
    # m "책상 위에 책들이 이리저리 놓여 있네."

    # # 인터랙티브 테이블 사용
    # call screen interactive_table_im
    
    # # 선택에 따른 분기
    # if _return == "bk1_selected":
    #     $ chosen_character = "jang" # 장기영
    #     narrator '총을 집었다. 차가운 금속의 감촉이 느껴진다.'
    #     jump intro_mirror_jang
    # elif _return == "bk2_selected":
    #     $ chosen_character = "im" # 임규  
    #     narrator '책을 집었다. 묵직한 무게가 손에 전해진다.'
    #     jump intro_mirror_im
    # elif _return == "bk3_selected":
    #     $ chosen_character = "oh" # 오세창
    #     narrator '신문을 집었다. 바스락거리는 종이 소리가 난다.'
    #     jump intro_mirror_oh

return