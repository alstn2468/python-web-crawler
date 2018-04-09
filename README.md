간단한 파이썬 웹 크롤러<br/>
Simple Python Web Crawler
======================
개발자 : 김민수<br/>
Developer : Kim Min Su
---------------------
## ■ 사용법(instructions)

### 1. 깃 클론(Git Clone)
- - -
### 2. 크롤링할 웹 주소 설정(Set URL to Crawling)
- - -
parser.py의 10번째 줄(parser.py, Line 10)
```
request =  requests.get('https://github.com/alstn2468?tab=repositories')
                         ▲     여기에 주소를 설정(Set URL here)      ▲
```
### 3. 크롤링할 웹페이지에서 요소 검사(Scanning for elements in the web)
- - -
parser.py의 20번째 줄(parser.py, Line 10)
```
repo_titles = soup.select('#user-repositories-list > ul > li > div.d-inline-block.mb-1 > h3 > a')
                            ▲                    여기에 CSS 요소를 설정                      ▲
```
