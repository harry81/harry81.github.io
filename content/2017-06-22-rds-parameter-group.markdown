---
layout: post
title: "rds-parameter-group"
date: 2017-06-22 11:51:34 +0900
comments: true
categories: 
---

### 문제 ###

-------------------------------------------------------------------------------
postgres에 SELECT 문장을 요청할 경우 발생, 일반적인 요청은 문제가 없으나 `order by` 이후에 들어오는 컬럼이 한글값을 가진 경우가 문제.

정렬이 되는 듯하나 유심히 순서를 확인해보면 맞지가 않다.
그래서 구글링해보니 같은 문제를 겪은 사람들이 있었다.
- postgresql 에서 한글 정렬 문제 해결하기 <https://ansuchan.com/postgresql-korean-order/>

- PostgreSQL 한글 정렬 <http://tech.jinto.pe.kr/165>


### 해결책 ###

-------------------------------------------------------------------------------
해결책은 다행히도 간단하다. db 생성시에 `LC_COLLATE 'C'` 옵션을 주면 되는 것.
단 이미 사용중인 db인 경우는 재생성해야 하는 번거로움이 있다.

- postgres의 한글 정렬
https://jupiny.com/2016/12/12/sort-korean-in-postgresql/

아래는 rds에서 collate 값을 변경이 필요한 경우
![/images/rds-parameter-groups.png](/images/rds-parameter-groups.png)



