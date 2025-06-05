from pydub import AudioSegment

# mp3 파일을 로드
audio = AudioSegment.from_mp3("input.mp3")

# wav로 변환 (16kHz, 16bit PCM)
audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)
audio.export("speaker.wav", format="wav")
print("변환 완료: speaker.wav 생성!")
