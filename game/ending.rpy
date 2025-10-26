# 엔딩과 결과 페이지 스크립트

# =============================================================================
# 엔딩 분기 시스템
# =============================================================================

# 캐릭터별 엔딩으로 분기하는 메인 엔딩 라벨
label ending_dispatcher(character_ending):
    if character_ending == "im_ending":
        jump im_ending
    elif character_ending == "jang_ending":
        jump jang_ending
    elif character_ending == "oh_ending":
        jump oh_ending
    else:
        # 기본 엔딩
        jump default_ending

# =============================================================================
# 캐릭터별 개별 엔딩
# =============================================================================

#음악
define audio.outro = "audio/bgm/outro_bgm.mp3"
define audio.outro_scene3 = "audio/bgm/outro_scene3.mp3"

#이미지
image memory_orb-0 = "bg/memory_orb-0.png"
image bg_bookback = At("bg/outro/book_back.png", custom_size)
image im_ending = At("bg/outro/im_ending.png", custom_size)
image oh_ending = At("bg/outro/oh_ending.png", custom_size)
image jang_ending = At("bg/outro/jang_ending.png", custom_size)
image book2 = "bg/outro/book2.png"
image book2_hover = "bg/outro/book2_hover.png"
image bg_desk_bk = "bg/outro/desk_bk.png"
image bg_sign = At("bg/outro/sign_2.png", custom_size)
image bg_end = "bg/outro/end.png"

# === 토글용 변수 기본값  ===
default end2_show_a = False
default end2_show_b = False
default end2_show_c = False


default persistent.common_ending_finale = []

# 임규 엔딩
label im_ending:
    play music audio.outro
    scene bg_desk_bk with dissolve
    

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
        jump im_ending_scene2

    return

# 장기영 엔딩
label jang_ending:
    play music audio.outro
    scene bg_desk_bk with dissolve
    
    m "마지막 기억 구슬을 찾고 현실 세계로 복귀했다."
    m "하도 생생해서 꿈인지 현실인지 모르겠다."

    m "아 맞다. 시험 공부! 빨리 책상에 앉아서 공부해야겠다."

    m "이게 뭐지? 처음 보는 책인데..?"
    
    # 장기영 전용 책 표시
    show screen mission_guide("책을 펴보자.", icon="🔍")
    call screen interactive_jang_desk
    hide screen mission_guide
    
    if _return == "jang_book_selected":
        jump jang_ending_scene2
    
    return

# 오세창 엔딩
label oh_ending:
    play music audio.outro
    scene bg_desk_bk with dissolve
    
    m "마지막 기억 구슬을 찾고 현실 세계로 복귀했다."
    m "하도 생생해서 꿈인지 현실인지 모르겠다."

    m "아 맞다. 시험 공부! 빨리 책상에 앉아서 공부해야겠다."

    m "이게 뭐지? 처음 보는 책인데..?"
    
    # 오세창 전용 책 표시
    show screen mission_guide("책을 펴보자.", icon="🔍")
    call screen interactive_oh_desk
    hide screen mission_guide
    
    if _return == "oh_book_selected":
        jump oh_ending_scene2
    
    return

# 임규 엔딩 씬 2
label im_ending_scene2:
    scene im_ending with fade_fast
    
    
    pause
    
    jump im_sign
    return

# 장기영 엔딩 씬 2
label jang_ending_scene2:
    scene jang_ending with fade_fast

    pause
    
    jump im_sign
    return

# 오세창 엔딩 씬 2
label oh_ending_scene2:
    scene oh_ending with fade_fast

    pause
    
    jump im_sign
    return

return

# 공동 엔딩 씬 3
label im_sign:
    
    scene black with fade
    
    narrator "오늘 함께한, 독립 투사분들의 이름을 기억해 주세요."
    narrator "그리고, 당신의 이름도 남겨 의지를 이어나가 주세요."
    
    # 서명 스크린 호출
    show screen mission_guide("오른쪽 페이지에 서명을 작성해주세요.", icon="🖊")
    call screen signature_screen
    hide screen mission_guide
    
    return

# 공통 엔딩 피날레
label common_ending_finale:
    jump ending_scene3

label ending_scene3:
    scene bg_desk_bk with fade_slow
    jump ending_scene4

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

    jump end_credits
    
# 최종 크레딧
label end_credits:
    scene bg_end
    with dissolve

    # show screen exit_button  # 나가기 버튼 표시

    pause
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
    # 임규 전용 책 인터랙션
    use interactive_books("book2", return_value="book2_selected")

# 장기영 전용 책 스크린
screen interactive_jang_desk():
    # 장기영 전용 책 인터랙션 (book2 대신 장기영 관련 이미지 사용 가능)
    use interactive_books("book2", return_value="jang_book_selected")

# 오세창 전용 책 스크린
screen interactive_oh_desk():
    # 오세창 전용 책 인터랙션
    use interactive_books("book2", return_value="oh_book_selected")

# =============================================================================
# 서명 스크린
# =============================================================================

screen signature_screen():
    modal True

    # 전체 배경
    add "bg_sign" xalign 0.5 yalign 0.5

    # 오른쪽 절반에 서명 영역 (투명 캔버스)
    frame:
        background Solid((0, 0, 0, 0))
        xalign 1.0
        yalign 0.5
        xsize 960
        ysize 1080

        add DrawSignature(signature_canvas):
            xsize 960
            ysize 1080

    # UI 요소들 (서명 영역 위에 표시)
    frame:
        background Solid((0, 0, 0, 0))
        xalign 1.0
        yalign 0.5
        xsize 960
        ysize 1080

        vbox:
            spacing 30
            xalign 0.5
            ypos 50

            # 안내 문구
            text "":
                size 30
                color "#ffffff"
                outlines [(2, "#000", 0, 0)]
                xalign 0.5
                text_align 0.5

    # 하단 버튼들
    frame:
        background Solid((0, 0, 0, 0))
        xalign 1.0
        yalign 1.0
        xsize 960
        ysize 150

        hbox:
            spacing 30
            xalign 0.3
            yalign -0.5

            textbutton "다시 쓰기":
                action Function(signature_canvas.clear)
                xsize 160
                ysize 55
                text_color "#000000"

            textbutton "서명 완료":
                action Function(complete_signature)
                xsize 160
                ysize 55
                text_color "#000000"


init python:
    import pygame
    import os
    import random
    
    # 서명 저장 경로
    GAMEDIR = config.gamedir.replace("\\", "/")
    SIGNATURE_DIR = GAMEDIR + "/signatures"
    MEMORIAL_IMAGE = GAMEDIR + "/images/bg/memorial_flag.png"
    BASE_FLAG_IMAGE = GAMEDIR + "/images/bg/ending/태극기.jpg"
    
    SIGNATURE_SIZE_RATIO = 8
    
    # 디렉토리 생성
    if not os.path.exists(SIGNATURE_DIR):
        os.makedirs(SIGNATURE_DIR)
    
    class SignatureCanvas:
        """손글씨 서명을 그릴 수 있는 캔버스"""
        def __init__(self, width=960, height=1080):
            self.width = width
            self.height = height
            self.drawing = False
            self.last_pos = None
            self.lines = []
            
        def start_drawing(self, pos):
            self.drawing = True
            self.last_pos = pos
            
        def draw(self, pos):
            if self.drawing and self.last_pos:
                self.lines.append((self.last_pos, pos))
                self.last_pos = pos
                
        def stop_drawing(self):
            self.drawing = False
            self.last_pos = None
            
        def clear(self):
            self.lines = []
            self.drawing = False
            self.last_pos = None
            renpy.restart_interaction()  # 화면 갱신
            
        def save_to_image(self, filepath):
            """서명을 투명 배경 이미지로 저장"""
            surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            surface.fill((0, 0, 0, 0))  # 투명 배경
            
            for start, end in self.lines:
                pygame.draw.line(surface, (0, 0, 0, 255), start, end, 3)
            
            pygame.image.save(surface, filepath)
            return filepath
    
    def merge_signature_to_flag(signature_path):
        """서명을 태극기에 합성"""
        try:
            # 베이스 이미지 로드
            if os.path.exists(MEMORIAL_IMAGE):
                base = pygame.image.load(MEMORIAL_IMAGE)
            elif os.path.exists(BASE_FLAG_IMAGE):
                base = pygame.image.load(BASE_FLAG_IMAGE)
            else:
                base = pygame.Surface((1200, 800))
                base.fill((255, 255, 255))
            
            base = base.convert_alpha()
            
            # 서명 이미지 로드
            signature = pygame.image.load(signature_path)
            signature = signature.convert_alpha()
            
            # 서명 크기 조정
            sig_width = base.get_width() // SIGNATURE_SIZE_RATIO
            sig_height = int(signature.get_height() * (sig_width / signature.get_width()))
            signature = pygame.transform.smoothscale(signature, (sig_width, sig_height))
            
            # 랜덤 위치 계산
            margin = 50
            max_x = base.get_width() - sig_width - margin
            max_y = base.get_height() - sig_height - margin
            
            x = random.randint(margin, max(margin, max_x))
            y = random.randint(margin, max(margin, max_y))
            
            # 서명 합성
            base.blit(signature, (x, y))
            
            # 결과 저장
            pygame.image.save(base, MEMORIAL_IMAGE)
            
            return True
        except Exception as e:
            renpy.notify("이미지 합성 중 오류: {}".format(str(e)))
            return False
    
    # 전역 캔버스 객체
    signature_canvas = SignatureCanvas()
    
    def complete_signature():
        """서명 저장 및 태극기에 합성"""
        if not signature_canvas.lines:
            renpy.notify("서명을 작성해주세요!")
            return
        
        import time
        timestamp = int(time.time() * 1000)
        sig_path = SIGNATURE_DIR + "/sig_{}.png".format(timestamp)
        
        # 서명 이미지 저장
        signature_canvas.save_to_image(sig_path)
        
        # 태극기에 합성
        success = merge_signature_to_flag(sig_path)
        
        if success:
            # persistent 초기화 확인
            if not hasattr(persistent, 'common_ending_finale'):
                persistent.common_ending_finale = []
            
            persistent.common_ending_finale.append({
                'timestamp': timestamp,
                'filename': os.path.basename(sig_path)
            })
            
            renpy.notify("서명이 등록되었습니다!")
            signature_canvas.clear()
            renpy.jump("common_ending_finale")
        else:
            renpy.notify("서명 등록에 실패했습니다.")
    
    class DrawSignature(renpy.Displayable):
        """서명을 그리는 디스플레이어블"""
        def __init__(self, canvas, **kwargs):
            super(DrawSignature, self).__init__(**kwargs)
            self.canvas = canvas
        
        def render(self, width, height, st, at):
            render = renpy.Render(self.canvas.width, self.canvas.height)
            
            # 투명 배경 (아무것도 그리지 않음)
            
            # 선 그리기
            if self.canvas.lines:
                canvas_obj = render.canvas()
                for start, end in self.canvas.lines:
                    canvas_obj.line((0, 0, 0, 255), start, end, 5)
            
            return render
        
        def event(self, ev, x, y, st):
            import pygame
            
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.canvas.start_drawing((x, y))
                renpy.redraw(self, 0)
                return None
            
            elif ev.type == pygame.MOUSEMOTION:
                if self.canvas.drawing:
                    self.canvas.draw((x, y))
                    renpy.redraw(self, 0)
                return None
            
            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                self.canvas.stop_drawing()
                renpy.redraw(self, 0)
                return None
            
            return None