# 정현 담당
# 장기영 루트 스크립트
# script.rpy의 정의들을 모두 사용 가능

# =============================================================================
# 이미지 정의
# =============================================================================
image asset_gun = "images/assets/asset_gun.png"
image asset_book = "images/assets/asset_book.png"
image asset_news = "images/assets/asset_news.png"

image bg_table_empty = At("images/bg/table_empty.png", custom_size)

# =============================================================================
# 드래그 앤 드롭 처리 함수
# =============================================================================
init python:
    def drag_placed(drags, drop):
        if not drop:
            return
        
        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name
        return True

label character_jang:

    narrator "✅ script_jang.rpy 파일이 정상적으로 로드되었습니다!"
    
    jang "안녕하세요! 저는 장기영입니다."
    jang "오늘은 드래그 앤 드롭 실습을 해보겠습니다."
    # 변수
    default gun_placed  = False
    default book_placed = False
    default news_placed = False

    scene bg_table_empty
    "물건들을 테이블의 올바른 위치에 배치하세요"

    call placing_object

    return

label placing_object:

    call screen drag_drop_practice

    if draggable == "gun_item" and droppable == "gun":
        $ gun_placed = True
    elif draggable == "book_item" and droppable == "book":
        $ book_placed = True
    elif draggable == "news_item" and droppable == "news":
        $ news_placed = True

    if gun_placed and book_placed and news_placed:
        jump success
    else:
        jump placing_object

    return

label success:

    scene bg_table

    narrator "모든 물건을 올바르게 배치했습니다!"
    
    jang "잘 하셨습니다! 드래그 앤 드롭 실습을 완료했어요."
    
    jang "이제 다음 단계로 넘어가볼까요?"

    return

# =============================================================================
# 드래그 앤 드롭 스크린
# =============================================================================
screen drag_drop_practice():
    
    # 테이블 배경
    add "bg_table_empty"

    text "총 = [gun_placed]":
        pos(1600, 600)
    text "책 = [book_placed]":
        pos(1600, 650)
    text "신문 = [news_placed]":
        pos(1600, 700)
    
    # 드래그 그룹
    draggroup:
        # ===== 총 =====
        # 드래그 가능한 총
        drag:
            drag_name "gun_item"
            child "asset_gun"
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
            xpos 200
            ypos 800
        
        # 총 드롭 영역 (좌측 상단)
        drag:
            drag_name "gun"
            child Solid("#ff000030", xysize=(250, 200))  # 반투명 빨강
            draggable False
            droppable True
            xpos 540
            ypos 390
        
        # ===== 책 =====
        # 드래그 가능한 책
        drag:
            drag_name "book_item"
            child "asset_book"
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
            xpos 1400
            ypos 800
        
        # 책 드롭 영역 (우측 상단)
        drag:
            drag_name "book"
            child Solid("#00ff0030", xysize=(250, 200))  # 반투명 초록
            draggable False
            droppable True
            xpos 1020
            ypos 325
        
        # ===== 신문 =====
        # 드래그 가능한 신문
        drag:
            drag_name "news_item"
            child "asset_news"
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
            xpos 800
            ypos 800
        
        # 신문 드롭 영역 (중간 하단)
        drag:
            drag_name "news"
            child Solid("#0000ff30", xysize=(250, 200))  # 반투명 파랑
            draggable False
            droppable True
            xpos 890
            ypos 580