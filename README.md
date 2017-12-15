# trading-bot

Course Work Project, 2017 Fall @ Data Science, Seoultech.

### RTS Stack = Real Time Streaming ?
다양한 실시간 데이터 처리 기술 존재 (Ex) Streamsets, Apache Nifi, Flume 등등  
하지만 ELK stack 이용해 pipeline 구축 실습함
#### >> ELK Stack: elasticsearch + logstash + kibana
- elasticsearch: 데이터 저장소, DB와 같은 역활
- logstash: 데이터 수집(pipeline 입구)
- kibana: 웹서버, UI 차트 등 시각화 목적

## Proposal for RTS Stack Practice
- 목적: 데이터 분석을 위한 **데이터 pipeline** 프로젝트 기획
- 분석 데이터: **실시간 가상화폐 시세 정보**
- 주제선정 배경: realtime data handling & realtime decision making
- 데이터 출처: [Bithumb API](https://www.bithumb.com/u1/US127), [Sample Code](./SampleCode_bithumb)
  - Public API: bithumb 거래소 공개정보
  - Private API: bithumb 회원 개인정보 (API Key 발급 필요)
- 진행 계획
  - 1차적으로 Public API 이용해 pipeline 구축
  - (기회가 된다면) 실시간 의사결정 알고리즘 구현  

## Visualization Result

<iframe src="http://35.201.174.105:5601/app/kibana#/dashboard?embed=true&_g=(refreshInterval:(display:'10%20seconds',pause:!f,section:1,value:10000),time:(from:'2017-12-15T01:28:25.263Z',mode:absolute,to:'2017-12-15T09:16:18.659Z'))&_a=(filters:!(),options:(darkTheme:!t),panels:!((col:1,id:price_median,panelIndex:1,row:1,size_x:6,size_y:3,type:visualization),(col:7,id:min-max,panelIndex:2,row:1,size_x:6,size_y:3,type:visualization),(col:1,id:count_read,panelIndex:3,row:4,size_x:12,size_y:2,type:visualization),(col:1,id:data-group-by-10min,panelIndex:8,row:6,size_x:12,size_y:2,type:visualization)),query:(query_string:(analyze_wildcard:!t,query:'*')),title:'New%20Dashboard',uiState:())" height="600" width="800"></iframe>
