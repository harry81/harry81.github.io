---
layout: post
title: "Elasticbeans talk"
date: 2017-9-13 17:44:50 +0900
comments: true
categories: elasticbeanstalk
---

#### Elasticbeanstalk health check
EB에서는 Health check 하는 기능을 기본적으로 포함하고 있다. 이것을 위해서는 Django에서 health check 요청을 허락하는 설정이 필요하다.
Route53에서 설정된 Domain으로 요청은 한다고 잘못생각해서 오랫동안 고민했다.

![/images/elasticbeans-health-check-0913.png](/images/elasticbeans-health-check-0913.png)

https://gist.github.com/dryan/8271687

    try:
        EC2_IP = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4').text
        ALLOWED_HOSTS.append(EC2_IP)
    except requests.exceptions.RequestException:
        pass

해결 : 위의 설정은 settings.py에 추가하자


#### 헤더에 Authorization 값 전달이 기본 설정이 아니다.
request에 호함된 모든 헤더값(사용자 토큰값)이 서버에 자동으로 전달이 되는 것이 기본인줄 알았는데, 그렇지 않더라. 

``` bash [wsgi_enabled_pass.config]
container_commands:
  01_wsgipass:
    command: 'echo "WSGIPassAuthorization On" >> ../wsgi.conf'
```
http://mattharris.org/2015/11/30/setting-aws-elasticbeanstalk-environment-wsgi-authorization/
