# TTS Model
## Google TTS(gTTS)
- 간단하고 사용 방법이 비교적 간단함
- 하지만 조정 가능한 옵션(목소리, 속도, 말하는 방식 등)이 매우 적어서 프로젝트에 사용하기는 어려울 듯
## TensorFlow TTS
- TensorFlow 기반의 TTS 라이브러리
- 한국어 TTS를 위한 사전 학습된 모델도 존재하며, 이를 활용해 간단하게 한국어 텍스트를 음성으로 변환할 수 있음
- https://github.com/TensorSpeech/TensorFlowTTS
## Coqui TTS
- 오픈소스 딥러닝 기반의 TTS 툴킷
- 다양한 언어와 목소리로 텍스트를 자연스러운 음성으로 변환할 수 있는 라이브러리
- 1100개 이상의 언어에 대한 사전학습(pretrained) 모델을 제공하며, 음성 합성, 음성 클로닝(voice cloning), 커스텀 음성 생성 등 고급 기능을 지원
- https://github.com/coqui-ai/TTS
## Dia
- 대화형 음성 합성, 감정 표현, 음성 클로닝, 비언어 사운드를 통합한 최신 오픈소스 TTS 모델
- 여러 명의 화자가 등장하는 대화체 음성을 자연스럽게 합성 가능
- 텍스트 입력만으로도 다양한 감정과 억양을 음성에 반영 가능
- 한국 개발자들이 만든 모델로, 한국어 데이터셋 기반으로 학습된 모델
- https://github.com/nari-labs/dia
## Tacotron
- 구글이 2018년에 발표한 자연스러운 음성 합성을 위한 딥러닝 기반 텍스트-투-스피치(Text-to-Speech, TTS) 모델
- 현재 한국어 언어로 사전학습된 모델이 오픈소스에 존재하지 않아 Korean Single Speaker Speech Dataset로 한국어 학습 중
- epoch = 50으로 학습한 결과, 음성이 제대로 출력되지 않아 epoch=100으로 설정하고 학습할 예정
## Glow-TTS
# 모델별 성능비교
## TTS 모델 성능 평가 기준
### 주관적 평가
1. MOS(Mean Opinion Score)
- 사람이 직접 합성된 음성을 듣고 1점에서부터 5점(혹은 4점) 척도로 자연스러움, 명료성, 전반적 품질을 평가
- MOS 평가는 실제 사용자의 인식을 반영하지만, 많은 인력과 시간이 소요되는 단점이 존재
### 객관적 평가
1. MCD(Mel-Cepstral Distortion)
- 합성 음성과 실제 음성의 스펙트럼 차이를 수치로 계산
- 값이 낮을수록 품질이 좋음을 의미
2. PESQ(Perceptual Evaluation of Speech Quality)
- 음성 신호의 왜곡 정도를 평가하여 MOS와 유사한 점수로 환산
3. STOI(Short-Time Objective Intelligibility)
- 합성 음성이 얼마나 잘 들리는지(명료성)를 0~100%로 수치화
4. CER(Character Error Rate)
- 합성 음성을 음성 인식기로 텍스트로 변환한 뒤, 원래 입력 텍스트와 비교하여 문자 단위 오류율을 측정
- 낮을수록 텍스트 전달력이 좋음을 의미
