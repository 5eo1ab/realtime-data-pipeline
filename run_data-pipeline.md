# Run data-pipeline
데이터 파이프라인 설치(레퍼런스 참고) 및 실행방법 기록

## 0. set software
#### install - logstash, elasticsearch & kibana
reference: [freepsw's stage 1](https://github.com/freepsw/demo-spark-analytics/tree/master/00.stage1)

#### install - kafka, apache spark (미작업)
reference: [freepsw's stage 2](https://github.com/freepsw/demo-spark-analytics/tree/master/00.stage2)

## 1. run elasticsearch  
```
$ cd ~/trading-bot/sw/elasticsearch-2.4.0    
$ run/elasticsearch
```

## 2. run kibana
```
$ cd ~/trading-bot/sw/kibana-4.6.2-linux-x86_64
$ bin/kibana
```

## 3. run logstash
