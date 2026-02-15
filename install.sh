#!/bin/bash

# 에러 발생 시 스크립트 실행 중단
set -e

echo "=========================================="
echo "   Easy Translator 설치 스크립트"
echo "=========================================="

# 스크립트가 있는 디렉토리로 이동
cd "$(dirname "$0")"

# 1. 시스템 패키지 설치 (Ubuntu/Debian 계열 기준)
echo "[1/4] 시스템 패키지 업데이트 및 필수 요소 설치..."
if [ -f /etc/debian_version ]; then
    sudo apt-get update
    # PyQt6 실행에 필요한 시스템 라이브러리(libxcb-cursor0 등)도 함께 설치
    sudo apt-get install -y python3 python3-venv python3-pip git libxcb-cursor0
elif [ -f /etc/redhat-release ]; then
    # Fedora/RedHat 계열
    sudo dnf install -y python3 python3-pip git
else
    echo "[알림] Debian/Ubuntu 계열이 아닙니다. Python 3와 venv가 설치되어 있는지 확인해주세요."
fi

# 2. 가상 환경(venv) 생성
echo "[2/4] Python 가상 환경(venv) 생성 중..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "  -> 가상 환경이 생성되었습니다."
else
    echo "  -> 가상 환경이 이미 존재합니다."
fi

# 3. Python 라이브러리 설치
echo "[3/4] 필요한 Python 라이브러리 설치 중..."
if [ -f "requirements.txt" ]; then
    ./venv/bin/pip install --upgrade pip
    ./venv/bin/pip install -r requirements.txt
else
    echo "  [오류] requirements.txt 파일이 없습니다. 설치를 중단합니다."
    exit 1
fi

# 4. 실행 스크립트(run.sh) 생성
echo "[4/4] 실행용 스크립트(run.sh) 생성 중..."
cat > run.sh <<EOL
#!/bin/bash
cd "\$(dirname "\$0")"
./venv/bin/python main.py
EOL
chmod +x run.sh

echo "=========================================="
echo "   설치가 완료되었습니다!"
echo "   이제 './run.sh' 명령어로 프로그램을 실행하세요."
echo "=========================================="