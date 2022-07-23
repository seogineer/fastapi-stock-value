# fastapi-stock-value

### 개발 환경
python 3.10.5  
pycharm professional

### 패키지
pip3 install uvicorn  
pip3 install fastapi  
pip3 install pandas_datareader  
pip3 install yfinance  
pip3 install pydantic   

### 실행 방법
````shell
uvicorn main:app --reload
````

### API
POST /stock

Request Body  
````json
{  
  "ticker":"string",   
  "start":"string",  
  "end": "string"  
}
````

ex)  
````json
{  
  "ticker":"QQQ",   
  "start":"2022-07-22",  
  "end": "2022-07-22"  
}
````

### 새로 알게된 지식
- python
  - MacOS는 기본적으로 python2 버전을 탑재하고 있다.
  - 하지만 개발은 python3 버전을 사용했다.
- FastAPI
  - 웹 프레임워크이다.
  - Spring의 maven, gradle 처럼 pip로 패키지를 관리한다.
  - /docs 경로에 swagger를 이용해 api 문서를 자동으로 생성해준다.
- pydantic
  - spring jackson 라이브러리 역할을 한다.
  - 요청으로 받은 json을 클래스에 매핑시켜준다.
- yfinance
  - 야후 파이낸스로부터 주식 정보를 가져올 수 있다.