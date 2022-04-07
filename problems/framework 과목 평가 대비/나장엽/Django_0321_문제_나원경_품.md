
1. 정적 웹페이지에 대한 설명으로 옳지 않은 것을 모두 고르시오.
 
    1) 서버에 미리 저장된 파일이 사용자에게 그대로 전달되는 웹 페이지
    2) 서버는 추가적인 처리 과정 이후 클라이언트에게 응답을 보냄
    3) 모든 상황에서 모든 사용자에게 동일하지 않은 정보를 표시한다
    4) 일반적으로 HTML, Python, java가 사용된다.
-> 2,3



2.framework를 사용할때의 장점과 단점을 각각 1개 답하라.
	* 장점 : 노력을 덜 들이고 웹페이지를 만들 수 있다.
	* 단점 : 다소 독선적이라 사용할 수 있는 변수명이나, 암묵적인 규칙 등을 지켜야 한다.




3. MTV패턴에서 m에 해당하는 단어는 무엇이고, 그것이 하는 역할을 아래의 지문에서 찾으세요.

    1) 파일의 구조나 레이아웃을 정의
    2) 실제 내용을 보여주는데 사용한다
    3) 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리한다
    4) HTTP 요청을 수신하고 HTTP 응답을 반환한다.
-> model, 3




4.django의 프로젝트 생성 후 프로젝트의 구조에서 애플리케이션의 모든 설정을 포함하는 .py파일의 이름은 무엇인가요?
-> settings.py




5. django에서 프로젝트의 특징에 대해 옳지 않은 것을 모두 고르세요.
    
    1) application의 집합이다.
    2) 하나의 프로젝트는 하나의 앱만 가질 수 있다. 
    3) 실제 요청을 처리하고 페이지를 보여주고 하는 등의 역할을 담당한다.
    4) 하나의 역할 및 기능 단위로 작성한다.
    5) 프로젝트에서 app을 사용하기 위해서는 urls.py에서 INSTALLED_APPS에 등록을 해야한다.
-> 2, 5




6. views.py에서 posts 라는 변수를 render()를 사용하여 템플릿에 넘겨주었다. 
	 이제 넘겨진 posts 변수를 받아HTML에서 나타나게 해야한다. 
	 이 변수를 HTML에 표현하기 위한 코드는 무엇인가?
-> {{posts}}





7. 
모든 model 객체는 models.py 파일에 선언하여 모델을 만든다. 
만든 후 데이터베이스에 모델을 위한 테이블을 만들기 위해, 
모델에 몇 가지 변화가 생겼다는 것을 알게 해줘야 한다.
이때 사용하는 명령어는 무엇인가? 
-> python manage.py makemigrations
그리고 실제 데이터베이스에 반영하기 위해 실행해야 하는 명령어는 무엇인가? 
-> python manage.py migrate

 


8. 
폴더 templates 안에 base.html과 nav.html 파일이 있다. 
base.html에 nav.html을 포함시키려고 한다. 
이때 사용해야하는 템플릿 코드를 작성해라.



<!-- base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
--> {% include '_nav.html' %}

{% block content %}
{% endblock %}
</body>
</html>



9. 
하나의 프로젝트는 여러개의 app을 가질 수 있다. 
여러개의 app이 존재할 때, 프로젝트 폴더 내의 urls.py는 매우 복잡하게 되고, 오류가 발생하기 쉽다.
이런 상황을 방지하기 위해 각각의 애플리케이션 안에 urls.py를 생성하고, 
프로젝트 urls.py에서 각 앱의 urls.py로 url 매핑을 위탁하게 된다. 
이 때 작성해야 하는 코드는?

프로젝트 폴더 이름은 pjt, 애플리케이션의 폴더 이름은 application 이다. 

pjt/urls.py
_____________________________________
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('application/', include('application.urls'))
         

application/urls.py
_______________________________________
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
]





10. view가 하는 역할이 무엇인가 ? 
-> url을 통해 요청이 들어오면, 그 요청에 따라 view 함수는 model에서 데이터베이스를 가져오거나 template에 요청을 보내 화면을 출력할 수 있게 한다.