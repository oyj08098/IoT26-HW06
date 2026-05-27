# IoT26-HW06
Car Recognition System with Raspberry Pi and Node-RED

- **전체 진행 흐름**
    1. **카메라 연결 및 Node-RED 설치 및 실행**
        
        ```python
        #터미널에서 Node-Red 실행 명령어
        node-red-start
        ```
        
    2. **Node-Red를 사용한 사진 촬용**
        1. Block 구조랑 실행 화면 사진에 첨부
    3. **Yolo 모델 설치** 
        1. Raspberry Pi의 저장공간과 성능을 고려해서 아주 가벼운 모델인
        **YOLOv3-tiny**를 사용 → 어떤 환경인지에 따라서 예측이 완벽하지 않은 문제가 발생할 수 있음.
    4. **차량 인식 Python 코드 작성**
        1. Cord에 첨부
    5. **Node-Red와 YOLO 코드 통합**
    6. **실행**
        1. 최종 결과물 사진에 첨부

1. Node-Red 블록 구조(Butten-exec-debug)
   <img width="1253" height="670" alt="image" src="https://github.com/user-attachments/assets/23fba9fc-cc46-4d2a-b666-2663d5cb8fff" />

2. 배포하기 누른 후에, http://연결IP/dashboard 접속 화면
   <img width="1176" height="548" alt="image" src="https://github.com/user-attachments/assets/1d6e8f48-550f-41a5-b27f-38d58f4cb76a" />

3. Take Photo 클릭해서 사진 찍기
   <img width="1050" height="476" alt="image" src="https://github.com/user-attachments/assets/b85e8195-f0a4-4a86-a7e1-bd5704e92ae4" />

4. 사진 확인
   <img width="2214" height="1385" alt="image" src="https://github.com/user-attachments/assets/4f05b255-3752-4fd4-9a92-ce3acaddc39f" />

5. Yolo모델하고 연동까지 마친 후, 인터넷에 있는 차량 사진 찾아서 라즈베리 카메라로 사진 촬영 → 차량 예측하는 모습 확인 가능(모델 성능과 여러 제약 조건 때문에 완벽하게 예측하기 하지는 못함 )
   <img width="1990" height="1119" alt="image" src="https://github.com/user-attachments/assets/29e3d253-12ee-43c8-a940-522511ccaa1c" />
