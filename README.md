
# Abstract Base Classes in Python

### 1) Abstract Base class nima o'zi, shu haqida tushunchaga ega bo'lamiz,keyin code yozib yanada to'liqroq tushunib olamiz.
#### GitHubda Follow bo'ling [ ![My](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white) ](https://github.com/fayzullohblog)

<p align="center">
<img alt="Types-of-OOPS-2" height="500" src="https://media.geeksforgeeks.org/wp-content/uploads/20230818181616/Types-of-OOPS-2.gif" width="500">
</p>


> [!NOTE]
Abstract classni tushunish uchun, sizga hayotiy mosil keltiraman. Abstract class degani mavxum class degani, ammo  bu class mavxum bo'lsada bizga foydalanayotgan  codning  interfice tomondan chiroyli ko'rsatish va tartibli holatda yozish uchundir. Diqqatli bo'ling ! siz
Mexmon xonadan online xona booking qildingiz, sizga mexmona xona xodimlari tomonidan xonaning raqami, xonaga kirish uchun maxsus parol, internet uchun passwordni ham berdi, xullas kalom siz uchun maxsus kerak bo'lgan ma'lumotlarni berdi,
endi shu xizmatni sizga kabi boshqa  klintlar uchun ham qiladi, albatda ularning talabidan kelib chiqib. Shu yerda mexmon xonaning ichki ish holati qanday bo'layotganligi, sizga xona uchun raqam, kirish paroli va boshqa xizmatlarni qanday qilayotganligi
siz uchun mavxum, ammo bu xizmatlar sizga kerak, xuddi shunday Abstact class va method xosil qilishn uchun abc modulidan ABC va @abstractmethod-larni import qilib mavxum Abstract class xosil qilamiz, va bu  classdan boshqa bir subclasslar vorislik oladi,
va vorislik olgan class bu guyoki Mexmon xoandan online joy booking qilgan klintga uxshaydi, Subclass, Abstract classning barcha methodlarini o'zgartirib(override) qilib , o'zi uchun foydalanadi.
endi code yozamiz



### 2) main.py faylga birinchi Abstract classdan foydalanmasdan oddiy vorsilkdan foydalanib ko'ramiz.

```sh
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        pass

class User(Person):
    def display_info(self):
        print(f"User: {self.name}, Age: {self.age}")

class Admin(Person):
    def display_info(self):
        print(f"Admin: {self.name}, Age: {self.age}")\

person=Person('fayzulloh',23)
user = User("John Doe", 25)
admin = Admin("Admin Name", 30)


person.display_info()
user.display_info()
admin.display_info()
```
***Etibor bering, Person classidan , Admin va User classlari vorslik oldi va Person classining display_info() methoodini override qildi, va har bir class uchun alohida object yaratdi,
natija esa quyidagicha chiqadi.***

#### Natija
```sh
User: John Doe, Age: 25
User: Admin Name, Age: 30
```


> [!NOTE]
Abstract Classdan hechqachon object yaratib bo'lmaydi va Abstract classda mavjuda bo'lgan methodla, Abstract classdan voris olgan classlar, Abstract classning methodlarini o'zgartirib foydalanadi.
> 

### 3) main.py faylga birinchi Abstract classdan foydalanib ko'ramiz. Buning uchun abc modulidan ABC class uchun , @abstractmethod decoratirini,  methodlar  uchun import qilib olamiz


```sh
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def display_info(self):
        pass

class User(Person):
    def display_info(self):
        print(f"User: {self.name}, Age: {self.age}")

class Admin(Person):
    def display_info(self):
        print(f"User: {self.name}, Age: {self.age}")


user = User("John Doe", 25)
admin = Admin("Admin Name", 30)
person=Person('Fayzulloh',23)

user.display_info()
admin.display_info()

```
***Etibor bering, Person classidan , Admin va User classlari vorslik oldi va Person classining display_info() methoodini override qildi, va faqat voris classlar  uchun alohida object yaratdildi,
Abstract class uchun object yarata olmadek. va Natija quyidagicha***

#### Natija
```sh
User: John Doe, Age: 25
User: Admin Name, Age: 30
```

***`@abstractmethod` - bu decoratirni Abstract classning harqanday methodida foydalanishlik shart bo'ladi, 
sababi boshqa classlarda ya'ni subclasslarda aynan shu methodlar override qilinadi. Abstract classdagi methodalar nima uchun kerak, aynan subclasslarning interficelarini yaxshilash va codeni sodda ko'rinishga olib kelish uchun***



#### Vedio orqali ko'rish
[ ![My](https://user-images.githubusercontent.com/57800056/245666234-e0c3afd8-9ca1-44fd-8595-47ec0f6c4cfc.png) ](https://www.youtube.com/@webmaster_py)   

#### quyidagi social tarmoqlarda kuzating
[ ![My](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white) ](https://github.com/fayzullohblog) [ ![My](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white) ](https://www.linkedin.com/in/fayzullohblog/)  [ ![My](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white) ](https://www.instagram.com/fayzullohblog/)   [ ![My](https://patrolavia.github.io/telegram-badge/chat.png) ](https://t.me/webmasterpy)  [ ![](https://patrolavia.github.io/telegram-badge/follow.png) ](https://t.me/suniy_intelekt_uzb) [ ![My](https://github.com/paulrobertlloyd/socialmediaicons/blob/main/facebook-48x48.png) ](https://www.facebook.com/fayzullohblog/)  [ ![My](https://github.com/paulrobertlloyd/socialmediaicons/blob/main/youtube-48x48.png) ](https://www.youtube.com/@webmaster_py) 



#### My Skill

[![My Skills](https://skillicons.dev/icons?i=python,django,postgresql,git,aws,html,css)](https://skillicons.dev)

