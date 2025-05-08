# 분리위키 모델 서빙 API 서버 구축

## 1. 프로젝트 개요

- **프로젝트명**: 분리위키 모델 서빙 API 서버 구축
- **프로젝트 기간**: 2024.03 ~ 2024.11
- **목적 및 배경**:
  - 분리배출 가이드 제공 서비스인 "분리위키"를 지원하기 위해,
  - 재활용 분리수거 이미지 및 문장을 분류하는 모델을 안정적으로 서빙하는 API 서버를 구축
  - S3에 저장된 최신 모델을 자동 로드하여 예측 성능을 지속적으로 유지하는 것을 목표로 함



## 2. 기술 스택

| 구분 | 사용 기술 |
|:---|:---|
| Language | Python 3.10 |
| Web Framework | FastAPI |
| Cloud Storage | AWS S3 |
| Visualization | TensorBoard |
| Containerization | Docker, Docker Compose |
| 기타 | boto3, loguru, transformers, ultralytics (YOLO) |



## 3. 주요 기능 및 흐름

- FastAPI Lifespan 사용하여 서버 시작 시 모델 로드
- S3에서 최신 모델(state_dict) 자동 다운로드 및 초기화
- Logger를 통한 서버 로그 관리 및 에러 기록
- TensorBoard를 통해 모델 학습 결과 시각화
- Docker Compose를 통한 서버 및 TensorBoard 통합 실행

## 4. 상세 기능 설명

### 4.1 모델 로딩
- 서버 시작 시 S3로부터 `latest_model.yaml`을 통해 최신 모델 경로 확인
- YOLO 모델 (이미지 분리배출 분류) 및 KcBERT 모델 (문장 혐오 표현 분류) 파일을 다운로드 및 메모리에 로드
- 모델 로드 실패 시 로컬 fallback 모델 경로 사용

### 4.2 API 제공

| API Endpoint | Method | 설명 |
|:---|:---|:---|
| `/kcbert/prediction` | POST | 혐오 표현 분류 |
| `/yolo/prediction` | POST | 재활용품 이미지 탐지 및 분류 |

### 4.3 로깅 시스템
- loguru를 활용하여 통합 로깅
- 로그 포맷: `[시간] - [호스트명:IP] | [레벨] | [메시지]`
- 로그 파일은 `logfile.log`에 저장, 3일 주기로 롤링


## 5. 문제 해결 경험

* **서버 재기동 없이 모델을 갱신하는 구조 설계**   
  초기에는 FastAPI 서버가 시작될 때 `latest_model.yaml`을 통해 S3에서 최신 모델을 불러오는 구조로 설계했지만, 새로운 모델이 업로드된 경우 서버를 **재시작하지 않으면 반영되지 않는 문제**가 있었습니다.
  → 이를 해결하기 위해 `/reload_model` API를 설계하고, 런타임 중에도 모델을 S3에서 불러와 **동적으로 교체할 수 있는 구조**로 개선을 준비하였습니다.



