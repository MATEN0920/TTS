## 합성 음성과 실제 음성의 스펙트럼 차이를 수치로 계산
## 값이 낮을수록 품질이 좋음을 의미

## pip install pymcd

from pymcd.mcd import Calculate_MCD

## pymcd 모듈에서 Calculate_MCD 클래스를 import
## pymcd는 Mel Cepstral Distortion 계산을 위해 mel-cepstral coefficient(MCC)를 추출하고, 이를 바탕으로 두 음성 간의 유사도를 수치화

# 'plain', 'dtw', 'dtw_sl' 중 선택 가능
mcd_toolbox = Calculate_MCD(MCD_mode="plain")  # Calculate_MCD 객체를 생성하며, MCD_mode라는 파라미터를 통해 어떤 방식으로 MCD를 계산할지 선택 가능
mcd_value = mcd_toolbox.calculate_mcd("reference.wav", "synthesized.wav")  # 실제로 두 개의 음성 파일 (reference.wav와 synthesized.wav) 사이의 MCD를 계산
print("MCD:", mcd_value)  # 최종적으로 계산된 MCD 값을 출력