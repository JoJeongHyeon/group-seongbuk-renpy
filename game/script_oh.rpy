# 가빈 담당
# 오세창 루트 스크립트  
# script.rpy의 정의들을 모두 사용 가능

# 드래그 앤 드롭 함수 정의
init python:
    def drag_placed(drags, drop):
        if not drop:
            return False
        
        draggable = drags[0].drag_name
        droppable = drop.drag_name
        
        # 올바른 매칭 확인
        mapping = {"gun": "gun_zone", "book": "book_zone", "news": "news_zone"}
        
        if mapping.get(draggable) == droppable:
            # 올바른 zone에 놓였을 때만
            if draggable == "gun":
                store.gun_placed = True
            elif draggable == "book":
                store.book_placed = True
            elif draggable == "news":
                store.news_placed = True
            
            # 디버깅: 현재 상태 출력
            renpy.notify("배치됨: gun={}, book={}, news={}".format(
                store.gun_placed, store.book_placed, store.news_placed))
            
            # 화면 강제 갱신
            renpy.restart_interaction()
            return True
        else:
            # 잘못된 zone에 놓였을 때
            renpy.notify("잘못된 위치입니다!")
            return False

# 기본 변수 정의
default gun_placed = False
default book_placed = False
default news_placed = False

# 이미지 정의
# 배경
image bg_table_empty = At("bg/table_empty.png", custom_size)
image bg_table = At("bg/table.png", custom_size)
# 오브젝트
image asset_gun = "images/assets/asset_gun.png"
image asset_book = "images/assets/asset_book.png"
image asset_news = "images/assets/asset_news.png"

label character_oh:
    # 간단한 테스트 코드
    scene bg_table_empty with fade_fast
    narrator "✅ script_oh.rpy 파일이 정상적으로 로드되었습니다!"
    oh "안녕하세요! 저는 오세창입니다."
    oh "드래그 앤 드롭 테스트 시작"
    
    # 변수 강제 초기화
    $ gun_placed = False
    $ book_placed = False
    $ news_placed = False
    
    # 세 개 모두 True가 될 때까지 무한 반복
    label drag_loop:
        call screen drag_drop_screen
        
        # screen에서 돌아왔을 때 세 개 모두 True인지 확인
        if gun_placed and book_placed and news_placed:
            jump drag_complete
        else:
            # 아직 완료 안 됨, 다시 반복
            jump drag_loop

label drag_complete:
    scene bg_table with fade_fast
    "드래그 앤 드롭 테스트 성공"
    return

screen drag_drop_screen():
    # modal True로 설정하여 다른 입력 차단
    modal True
    
    add "bg_table_empty"
    
    draggroup:
        # Zone들을 먼저 배치 (아래쪽 레이어)
        # Gun Zone
        drag:
            drag_name "gun_zone"
            child Solid("#faf4c06c", xysize=(250, 200))
            draggable False
            droppable True
            xpos 540
            ypos 390
        
        # Book Zone
        drag:
            drag_name "book_zone"
            child Solid("#cefbc977", xysize=(250, 200))
            draggable False
            droppable True
            xpos 1020
            ypos 325
        
        # News Zone
        drag:
            drag_name "news_zone"
            child Solid("#cbeaf064", xysize=(250, 200))
            draggable False
            droppable True
            xpos 890
            ypos 580
        
        # 드래그 아이템들 (위쪽 레이어)
        # Gun 드래그 아이템
        if not gun_placed:
            drag:
                drag_name "gun"
                child "asset_gun"
                draggable True
                droppable False
                dragged drag_placed
                drag_raise True
                xpos 210
                ypos 820
        
        # Book 드래그 아이템
        if not book_placed:
            drag:
                drag_name "book"
                child "asset_book"
                draggable True
                droppable False
                dragged drag_placed
                drag_raise True
                xpos 1400
                ypos 800
        
        # News 드래그 아이템
        if not news_placed:
            drag:
                drag_name "news"
                child "asset_news"
                draggable True
                droppable False
                dragged drag_placed
                drag_raise True
                xpos 800
                ypos 820
    
    # 배치된 아이템들을 zone 위에 표시
    if gun_placed:
        add "asset_gun":
            xpos 565
            ypos 440
    if book_placed:
        add "asset_book":
            xpos 1045
            ypos 375
    if news_placed:
        add "asset_news":
            xpos 850
            ypos 580
    
    # 모든 아이템이 배치되면 자동으로 다음으로
    if gun_placed and book_placed and news_placed:
        timer 0.3 action Return()