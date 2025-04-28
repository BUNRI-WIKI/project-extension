# 분리위키 모델 서빙 API 서버 구축

## 1. 프로젝트 개요

- **프로젝트명**: 분리위키 모델 서빙 API 서버 구축
- **프로젝트 기간**: 2025.03 ~ 2025.05
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



## 4. 시스템 아키텍처

(🔔 **여기에 시스템 구조도 삽입**)

**구성 설명:**
- 모델 파일 저장소는 AWS S3를 사용
- 서버 기동 시 S3에서 최신 모델을 다운로드하여 메모리에 로드
- TensorBoard를 통해 S3 모델 경로 기반으로 학습 이력 조회 가능
- FastAPI 서버와 TensorBoard는 Docker Compose로 통합 관리



## 5. 상세 기능 설명

### 5.1 모델 로딩
- 서버 시작 시 S3로부터 `latest_model.yaml`을 통해 최신 모델 경로 확인
- YOLO 모델 (이미지 분리배출 분류) 및 KcBERT 모델 (문장 혐오 표현 분류) 파일을 다운로드 및 메모리에 로드
- 모델 로드 실패 시 로컬 fallback 모델 경로 사용

### 5.2 API 제공

| API Endpoint | Method | 설명 |
|:---|:---|:---|
| `/kcbert/prediction` | POST | 혐오 표현 분류 |
| `/yolo/prediction` | POST | 재활용품 이미지 탐지 및 분류 |

### 5.3 로깅 시스템
- loguru를 활용하여 통합 로깅
- 로그 포맷: `[시간] - [호스트명:IP] | [레벨] | [메시지]`
- 로그 파일은 `logfile.log`에 저장, 3일 주기로 롤링



## 6. 문제 해결 경험

| 이슈 | 해결 방법 |
|:---|:---|
| Logger 초기화 시점 오류 | lifespan 시작 시 Logger.initialize() 추가 |
| 모델 로딩 실패 가능성 대비 | try-except로 실패 시 fallback 경로 로드 처리 |
| Docker 이미지 최적화 | Python slim 이미지 사용, 필요 최소 패키지 설치 |
| API 설계 | GET 요청으로 body 받던 문제 발견 → POST로 설계 변경 계획 |



## 7. 추후 개선 계획

- `/reload_model` API 추가 개발
  - 서버 재시작 없이 실시간으로 모델 리로드 가능하게 개선
- AWS SQS 메시지를 FastAPI 백그라운드 task로 수신
  - 새로운 모델 업로드 감지 시 자동 reload
- API 인증 및 보안 강화
  - `/reload_model` 같은 민감한 엔드포인트에 Token 인증 추가
- 모델 버전 관리 체계 수립
  - S3 모델 폴더를 버전별로 관리하고 rollback 지원

---

## 8. 마무리 및 느낀 점

- 이번 프로젝트를 통해 FastAPI 기반 서버 아키텍처 구축 경험을 얻었고,
- AWS S3, SQS 등 클라우드 서비스를 연동하는 경험을 실습할 수 있었다.
- 운영/배포를 고려한 Docker Compose 환경 구성, Logging 설계 등 실무에 가까운 경험을 할 수 있었다.
- "분리위키" 서비스처럼 실제 사용자에게 제공되는 모델 서빙 시스템을 직접 구축해보며,
  현업 환경에서 서버 운영 및 자동화 관점의 중요성을 체감할 수 있었다.
- 향후에는 자동화 및 모니터링(모델 성능 추적, 에러 트래킹)까지 추가하여 프로젝트를 더욱 고도화할 계획이다.
