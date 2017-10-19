# trading-bot

Course Work Project, 2017 Fall @ Data Science, Seoultech.

### RTS Stack = Real Time Streaming ?
다양한 실시간 데이터 처리 기술 존재 (Ex) Streamsets, Apache Nifi, Flume 등등  
하지만 ELK stack 이용해 pipeline 구축 실습함
##### ELK Stack: elasticsearch + logstash + kibana
- elasticsearch: 데이터 저장소, DB와 같은 역활
- logstash: 데이터 수집(pipeline 입구)
- kibana: 웹서버, UI 차트 등 시각화 목적

## Proposal for RTS Stack Practice
- 목적: 데이터 분석을 위한 **데이터 pipeline** 프로젝트 기획
- 분석 데이터: 실시간 가상화폐 시세 정보
- 데이터 출처: [Bithumb API](https://www.bithumb.com/u1/US127), [Sample Code](https://github.com/5eo1ab/trading-bot/tree/master/SampleCode_bithumb)
- 주제선정 배경: realtime data handling & realtime decision making
