## 합성 음성이 얼마나 잘 들리는지(명료성)를 0~100%로 수치화

## pip install pystoi

import soundfile as sf  # WAV 등 오디오 파일을 읽고 쓰기 위한 라이브러리
from pystoi import stoi  # STOI 알고리즘의 Python 구현 라이브러리

clean, fs = sf.read("reference.wav")  # 원본 음성
denoised, fs = sf.read("synthesized.wav")  # 합성된 음성
score = stoi(clean, denoised, fs, extended=False)
print("STOI:", score)