# Dockerfile

FROM python:3.10



# 소스코드 복사
COPY . /etc/hangul_hill

#작업 폴더 설정
WORKDIR /etc/hangul_hill

## Install packages
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

## Run the application on the port 8080
EXPOSE 18000
WORKDIR /etc/hangul_hill/src
CMD ["uvicorn", "app.hangul_hill.main:app" ,"--host","0.0.0.0","--port","18000"]
