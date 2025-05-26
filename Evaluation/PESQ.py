## 음성 신호의 왜곡 정도를 평가하여 MOS와 유사한 점수로 환산

## pip install https://github.com/serser/python-pesq/archive/master.zip

from scipy.io import wavfile  # scipy.io.wavfile: WAV 파일을 로드하기 위한 라이브러리
from pypesq import pypesq  # pypesq: Python에서 PESQ 알고리즘을 실행할 수 있게 해주는 래퍼 라이브러리 (C기반 ITU PESQ 구현을 감쌈)

rate, ref = wavfile.read("reference.wav")  # 두 파일을 샘플링 레이트(rate)와 음성 신호 배열(ref, deg)로 읽어dha
rate, deg = wavfile.read("synthesized.wav")  # 두 파일은 샘플링 레이트가 동일해야 하며, 길이도 비슷해야 정확한 PESQ 평가가 가능
lqo = pypesq(rate, ref, deg, 'wb')  # 'wb'는 wide-band, 'nb'는 narrow-band
print("PESQ MOS-LQO:", lqo)
