# TTS 모델 비교
## Google TTS(gTTS)
- 간단하고 사용 방법이 비교적 간단함
- 하지만 조정 가능한 옵션이 매우 적어서 프로젝트에 사용하기는 어려울 듯
## Tortoise TTS
- 오픈소스 기반의 고품질 TTS 시스템
- 하지만 기본적으로 영어 데이터셋에 최적화되어 있음
- 한국어 음성을 자연스럽게 합성하려면, 대량의 한국어 음성 데이터(예: 50시간 이상)를 확보해 Tortoise TTS 모델을 재학습(fine-tuning)해야 할듯
- https://github.com/neonbjb/tortoise-tts
## TensorFlow TTS
- TensorFlow 기반의 TTS 라이브러리
- 한국어 TTS를 위한 사전 학습된 모델도 존재하며, 이를 활용해 간단하게 한국어 텍스트를 음성으로 변환할 수 있음
- https://github.com/TensorSpeech/TensorFlowTTS
## Coqui TTS
- 오픈소스 딥러닝 기반의 TTS 툴킷
- 다양한 언어(한국어 포함)와 목소리로 텍스트를 자연스러운 음성으로 변환할 수 있는 라이브러리
- 1100개 이상의 언어에 대한 사전학습(pretrained) 모델을 제공하며, 음성 합성, 음성 클로닝(voice cloning), 커스텀 음성 생성 등 고급 기능을 지원
- https://github.com/coqui-ai/TTS
## Dia
- 대화형 음성 합성, 감정 표현, 음성 클로닝, 비언어 사운드를 통합한 최신 오픈소스 TTS 모델
- 여러 명의 화자가 등장하는 대화체 음성을 자연스럽게 합성 가능
- 텍스트 입력만으로도 다양한 감정과 억양을 음성에 반영 가능
- 한국 개발자들이 만든 모델로, 한국어 데이터셋 기반으로 학습된 모델
- https://github.com/nari-labs/dia
## 모델별 성능비교
- 추가 예정
