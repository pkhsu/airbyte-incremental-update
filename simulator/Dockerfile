# 使用官方Python鏡像作為基礎鏡像
FROM python:3.9-slim

# 設置工作目錄
WORKDIR /app

# 複製Python腳本到容器內
COPY simulator.py /app/

# 安裝pymongo和apscheduler
RUN pip install pymongo apscheduler

# 運行模擬器腳本
CMD ["python", "./simulator.py"]
