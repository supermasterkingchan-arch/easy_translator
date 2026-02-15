# Easy Translator

간편한 영한/한영 번역기 애플리케이션입니다. PyQt6와 Google Translate API를 사용하여 제작되었습니다.

## 주요 기능
- **자동 언어 감지**: 영어는 한국어로, 한국어는 영어로 자동 번역합니다.
- **항상 위에 표시**: 다른 창들보다 항상 위에 있어 작업 중 사용하기 편리합니다.
- **미니멀 디자인**: 테두리가 없는 깔끔한 디자인과 반투명 배경을 지원합니다.

## 설치 및 실행 가이드 (Linux)

터미널을 열고 아래 명령어들을 순서대로 입력하면 누구나 쉽게 설치할 수 있습니다.

### 1. 프로젝트 다운로드 (Git Clone)
먼저 소스 코드를 컴퓨터로 다운로드합니다.

```bash
git clone https://github.com/YOUR_USERNAME/Easy_Translator.git
cd Easy_Translator
```
*(참고: `YOUR_USERNAME` 부분은 실제 깃허브 사용자명으로 변경해주세요)*

### 2. 간편 설치 (스크립트 사용)
포함된 설치 스크립트를 실행하면 필요한 패키지와 가상 환경이 자동으로 설정됩니다.

```bash
# 설치 스크립트에 실행 권한 부여
chmod +x install.sh

# 설치 시작
./install.sh
```

### 3. 프로그램 실행
설치가 완료되면 아래 명령어로 프로그램을 실행하세요.

```bash
./run.sh
```

---

## 수동 설치 (Windows / Mac / 기타)

1. Python 3가 설치되어 있어야 합니다.
2. 터미널(또는 CMD)에서 프로젝트 폴더로 이동합니다.
3. 필요한 라이브러리를 설치합니다: `pip install -r requirements.txt`
4. 프로그램을 실행합니다: `python main.py`