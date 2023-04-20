# 패키지는 '.'를 사용하여 파이썬 모듈을 계층적으로 관리하게 해줌

# import 패키지~모듈 포함
# -> 패키지의 디렉토리들과 monitor.py 작성

import framework.graphic.monitor

framework.graphic.monitor.display()

# 모듈 포함
from framework.graphic import monitor

monitor.display()

# 부분 포함
from framework.graphic.monitor import display
display()

# __init__
# 원래는 패키지에 인식시키기 위해서 반드시 필요했지만 3.3 부턴 자동인식.
# *로 원하는 모듈만 선택해서 import 시킬 수 있다.

# -> __init__.py, volume.py 작성
from framework.sound import *
volume.volumeUp()

# relative 패키지
# -> render.py 작성
from .framework.graphic.render import rendering
rendering()