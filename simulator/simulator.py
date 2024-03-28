import logging
from pymongo import MongoClient
from datetime import datetime
import random
import time  # 導入time模塊
import os 


# 配置日誌
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# 从环境变量获取MongoDB URI
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/your_database')

# MongoDB連接設定
try:
    client = MongoClient(MONGO_URI)
    # 如果数据库名称可能也是动态的，可以像URI一样从环境变量中获取
    db = client['your_database']
    collection = db['iot_data_collection']
    logging.info("Connected to MongoDB.")
except Exception as e:
    logging.error(f"Error connecting to MongoDB: {e}")

# 模擬IoT數據插入
def simulate_iot_data_insert():
    try:
        data = {
            "device_id": f"device_{random.randint(1, 10)}",  # 設備ID
            "sensor_type": random.choice(['temperature', 'humidity', 'pressure']),  # 傳感器類型
            "value": random.uniform(10, 100),  # 傳感器讀數值
            "timestamp": datetime.now()  # 當前時間戳
        }
        collection.insert_one(data)
        logging.info(f"Inserted data: {data}")
    except Exception as e:
        logging.error(f"Error inserting data into MongoDB: {e}")

# 模擬數據插入操作
if __name__ == "__main__":
    while True:
        simulate_iot_data_insert()
        # 間隔時間（例如5秒），可以根據需要調整
        time.sleep(5)
