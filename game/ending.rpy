# 엔딩과 결과 페이지 스크립트

# =============================================================================
# 초기화 및 변수 설정
# =============================================================================

# Persistent 변수 초기화
default persistent.memorial_signatures = []

# =============================================================================
# 이미지 정의
# =============================================================================

# =============================================================================
# 이미지 효과 정의
# =============================================================================

# 기억 구슬 깜빡임 효과
image memory_orb_blink:
    "memory_orb-4" # 이미 정의됨. script_jang.rpy에서
    alpha 0.3
    linear 0.8 alpha 1.0
    linear 0.8 alpha 0.3
    repeat

# =============================================================================
# 오디오 정의
# =============================================================================
define audio.ending_bgm = "audio/bgm/ending_bgm.mp3"

# =============================================================================
# 캐릭터 정의
# =============================================================================
define narrator = Character()


# =============================================================================
# 엔딩 라벨
# =============================================================================
label ending_scene:
    scene bg_black with fade_fast
    play music ending_bgm fadein 1.0 loop

    m_thought '마지막 기억 구슬을 찾고 현실 세계로 복귀했다.'
    m_thought '하도 생생해서 꿈인지 현실인지 모르겠다.'

    scene bg_desk with fade_slow

    m "맞다! 시험 공부! 빨리 책상 앞에 앉아서 공부해야지."

    m_thought '책상 위에 처음 보는 책 한 권이 놓여져 있네. 확인해보자.'

    jump ending_book

label ending_book:

    narrator "책을 확인해보세요."
    narrator "책을 전부 확인했습니다."

    jump ending_memorial

label ending_memorial:
    
    scene black with fade
    
    narrator "오늘 함께한, 독립 투사분들의 이름을 기억해 주세요."
    narrator "그리고, 당신의 이름도 남겨 의지를 이어나가 주세요."
    
    # 서명 스크린 호출
    call screen signature_screen
    
    return

label ending_memorial_complete:
    
    scene black with fade
    
    # 기억 구슬 로딩 화면
    show memory_orb_blink at truecenter:
        zoom 1.5
    with dissolve
    
    show screen framed_message("기억구슬이 이름을 적는 중입니다.")
    pause 3.0
    
    hide memory_orb_blink with dissolve
    hide screen framed_message with dissolve

    # 완성된 태극기 보여주기 (커스텀 사이즈 적용)
    if os.path.exists(MEMORIAL_IMAGE):
        show expression MEMORIAL_IMAGE at custom_size with dissolve
        pause 3.0
    
    narrator "당신의 이름이 역사에 새겨졌습니다."
    narrator "오늘 성북의 독립운동가와 함께한 기억을 앞으로도 떠올려 주세요..."
    
    pause 3.0

    scene black with fade_very_slow
    
    return

# =============================================================================
# 이름 서명 캔버스 정의
# =============================================================================

init python:
    import pygame
    import os
    import random
    
    # 서명 저장 경로 (Ren'Py는 슬래시 사용)
    GAMEDIR = config.gamedir.replace("\\", "/")
    SIGNATURE_DIR = GAMEDIR + "/signatures"
    MEMORIAL_IMAGE = GAMEDIR + "/images/bg/memorial_flag.png"
    BASE_FLAG_IMAGE = GAMEDIR + "/images/bg/ending/태극기.jpg"
    
    # 서명 크기 설정 (태극기 너비의 1/N)
    SIGNATURE_SIZE_RATIO = 8  # 숫자가 클수록 서명이 작아짐 (4=큼, 8=중간, 12=작음)
    
    # 디렉토리 생성
    if not os.path.exists(SIGNATURE_DIR):
        os.makedirs(SIGNATURE_DIR)
    
    class SignatureCanvas:
        """손글씨 서명을 그릴 수 있는 캔버스"""
        def __init__(self, width=800, height=400):
            self.width = width
            self.height = height
            self.drawing = False
            self.last_pos = None
            self.lines = []  # 그린 선들을 저장
            
        def start_drawing(self, pos):
            """그리기 시작"""
            self.drawing = True
            self.last_pos = pos
            
        def draw(self, pos):
            """선 그리기"""
            if self.drawing and self.last_pos:
                self.lines.append((self.last_pos, pos))
                self.last_pos = pos
                
        def stop_drawing(self):
            """그리기 종료"""
            self.drawing = False
            self.last_pos = None
            
        def clear(self):
            """캔버스 초기화"""
            self.lines = []
            self.drawing = False
            self.last_pos = None
            
        def save_to_image(self, filepath):
            """그린 내용을 이미지로 저장"""
            surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            surface.fill((0, 0, 0, 0))  # 투명 배경
            
            # 선 그리기
            for start, end in self.lines:
                pygame.draw.line(surface, (0, 0, 0, 255), start, end, 3)
            
            pygame.image.save(surface, filepath)
            return filepath
    
    def merge_signature_to_flag(signature_path):
        """서명을 태극기에 합성"""
        try:
            # 베이스 이미지 로드 (기존 memorial_flag가 있으면 그걸 사용, 없으면 원본 태극기)
            if os.path.exists(MEMORIAL_IMAGE):
                base = pygame.image.load(MEMORIAL_IMAGE)
            elif os.path.exists(BASE_FLAG_IMAGE):
                base = pygame.image.load(BASE_FLAG_IMAGE)
            else:
                # 태극기가 없으면 기본 흰색 배경 생성
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
            
            # 랜덤한 위치 계산 (여백을 두고)
            margin = 50
            max_x = base.get_width() - sig_width - margin
            max_y = base.get_height() - sig_height - margin
            
            x = random.randint(margin, max(margin, max_x))
            y = random.randint(margin, max(margin, max_y))
            
            # 서명을 태극기에 합성
            base.blit(signature, (x, y))
            
            # 결과 저장
            pygame.image.save(base, MEMORIAL_IMAGE)
            
            return True
        except Exception as e:
            renpy.notify("이미지 합성 중 오류 발생: {}".format(str(e)))
            return False
    
    # 전역 캔버스 객체
    signature_canvas = SignatureCanvas()

# =============================================================================
# 서명 스크린
# =============================================================================

screen signature_screen():
    modal True
    
    # 배경
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 600
        background "#f5f5dc"
        
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            
            # 안내 텍스트
            text "독립을 위해 싸운 선열들을 기리며\n당신의 이름을 서명해주세요":
                size 30
                xalign 0.5
                text_align 0.5
                color "#333"
            
            # 캔버스 영역
            frame:
                xsize 820
                ysize 420
                background "#ffffff"
                xalign 0.5
                
                # 드로잉 영역 - Displayable 사용
                add DrawSignature(signature_canvas):
                    xalign 0.5
                    yalign 0.5
            
            # 버튼들
            hbox:
                spacing 20
                xalign 0.5
                
                textbutton "다시 쓰기":
                    action Function(signature_canvas.clear)
                    xsize 150
                    ysize 50
                
                textbutton "서명 완료":
                    action Function(complete_signature)
                    xsize 150
                    ysize 50

init python:
    def complete_signature():
        """서명 저장 및 태극기에 합성"""
        if not signature_canvas.lines:
            renpy.notify("서명을 작성해주세요!")
            return
        
        # 고유한 파일명 생성
        import time
        timestamp = int(time.time() * 1000)
        sig_path = SIGNATURE_DIR + "/sig_{}.png".format(timestamp)
        
        # 서명 이미지 저장
        signature_canvas.save_to_image(sig_path)
        
        # 태극기에 합성
        success = merge_signature_to_flag(sig_path)
        
        if success:
            # persistent에 기록
            persistent.memorial_signatures.append({
                'timestamp': timestamp,
                'filename': os.path.basename(sig_path)
            })
            
            renpy.notify("서명이 등록되었습니다!")
            signature_canvas.clear()
            renpy.jump("ending_memorial_complete")
        else:
            renpy.notify("서명 등록에 실패했습니다.")
    
    class DrawSignature(renpy.Displayable):
        """서명을 그리는 디스플레이어블"""
        def __init__(self, canvas, **kwargs):
            super(DrawSignature, self).__init__(**kwargs)
            self.canvas = canvas
        
        def render(self, width, height, st, at):
            render = renpy.Render(800, 400)
            
            # 배경 그리기
            render.canvas().rect((255, 255, 255, 255), (0, 0, 800, 400))
            
            # 선 그리기
            if self.canvas.lines:
                canvas = render.canvas()
                for start, end in self.canvas.lines:
                    canvas.line((0, 0, 0, 255), start, end, 3)
            
            return render
        
        def event(self, ev, x, y, st):
            import pygame
            
            # 마우스 왼쪽 버튼을 누를 때
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.canvas.start_drawing((x, y))
                renpy.redraw(self, 0)
            
            # 마우스를 움직일 때 (버튼이 눌린 상태)
            elif ev.type == pygame.MOUSEMOTION:
                if self.canvas.drawing:
                    self.canvas.draw((x, y))
                    renpy.redraw(self, 0)
            
            # 마우스 버튼을 뗄 때
            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                self.canvas.stop_drawing()
                renpy.redraw(self, 0)
            
            # 항상 None을 반환 (이벤트를 다른 곳에서도 처리할 수 있게)
            return None