"""
csv로 저장된 데이터 파일들을 모두 database에 올리는 파일
"""
import pandas as pd
from sqlalchemy import create_engine
import param as pa

# PostgreSQL 연결 정보
host = pa.HOST        
port = pa.PORT
dbname = pa.DBNAME
user = pa.USER
password = pa.PASSWORD

# SQLAlchemy를 이용한 엔진 생성
engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}")

#데이터 베이스에 데이터 올리는 함수
def create_database(Gen, datatype):
    df = pd.read_csv(f"{Gen}_{datatype}.csv")

    # 'your_table'이라는 이름의 테이블에 저장
    df.to_sql(f"{Gen}_{datatype}", engine, index=False, if_exists='replace')


if __name__ == "__main__":
    #날씨 데이터
    create_database(pa.GEN_DICT["동산 태양광"], "WeatherData")
    create_database(pa.GEN_DICT["솔라숲1호"], "WeatherData")

    #예보 데이터
    create_database(pa.GEN_DICT["동산 태양광"], "ForecastData")
    create_database(pa.GEN_DICT["솔라숲1호"], "ForecastData")

    #발전량 데이터
    create_database(pa.GEN_DICT["동산 태양광"], "Solar")
    create_database(pa.GEN_DICT["솔라숲1호"], "Solar")
    
    #예측 데이터
    create_database(pa.GEN_DICT["동산 태양광"], "Predict")
    create_database(pa.GEN_DICT["솔라숲1호"], "Predict")
    print("기본 데이터베이스 생성 완료")
 
 