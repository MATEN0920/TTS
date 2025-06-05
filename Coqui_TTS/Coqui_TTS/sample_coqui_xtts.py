from TTS.api import TTS

# 모델 로드
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2").to("cpu")

# 한국어 텍스트
text = "안녕하세요. 지금은 다국어 모델로 한국어를 합성하고 있습니다. 만나서 반갑습니다. 어떤 작업을 도와드릴까요?"

# 스피커 WAV 파일 경로
speaker_wav = "speaker.wav"

# 합성 및 저장
tts.tts_to_file(
    text=text,
    file_path="output.wav",
    speaker_wav=speaker_wav,
    language="ko",
)
print("완료: output.wav 파일 생성됨!")
