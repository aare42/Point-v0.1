# Point-v0.1

Суть: є дерево технологій, користувачі-студенти і користувачі-освітні сервіси. На основі дерева технологій викладачі будують свої курси,
а студенти - відслідковують прогрес у навчанні.


Функціонал:

1. Класова структура, сутності:

https://drive.google.com/file/d/1682SUNQv8Xxi0SAY9iLmtTkMXw6MpQs0/view?usp=share_link - посилання на останню версію БД
по суті:

Користувач django.auth_user:

![image](https://user-images.githubusercontent.com/126251095/230977584-2dafdb4d-5a48-4ee8-91e9-c88d07259ccf.png)

Листок (тема):

![image](https://user-images.githubusercontent.com/126251095/230978616-ab01848c-67f1-455c-8cd4-a0415bb0a24c.png)

Тип листка: (теорія, практика, проект)

![image](https://user-images.githubusercontent.com/126251095/230978834-1dd29a8d-a103-4581-bda5-f9d79dc2c9ad.png)

Key_point (контрольне питання):

![image](https://user-images.githubusercontent.com/126251095/230978697-b5116165-5cf2-481d-ab9f-429abc9ab860.png)

Зв'язки між листками (ребра графа, ManyToMany Leaf-Leaf):

![image](https://user-images.githubusercontent.com/126251095/230979086-b6d21682-dceb-4866-bb0d-89e2ac466c28.png)

Студент: (OneToOne з User)

![image](https://user-images.githubusercontent.com/126251095/230978342-bfa017aa-76dc-4198-a409-e4b2015b87f3.png)

Студентський листок: (копія листка для кожного з студентів, зберігає в собі статус вивчення, поєднує дерево і студента)

![image](https://user-images.githubusercontent.com/126251095/230979556-eb54db95-5560-448d-93e1-9b61956442c7.png)

Статус студентського листка: ("not interested", "interested", "learning", "learned", "validated") 

![image](https://user-images.githubusercontent.com/126251095/230979632-8749930b-4d3a-4621-bd43-c922c69c2d70.png)

тут потрібна ще одна сутність, поки не заклав - статус validated свідчить про те що тему вивчено і підтверджено якимось освітнім сервісом. Інформацію про те хто підтвердив потрібно якось зберігати. це може бути щось типу:

Диплом:
- id
- студентський листок (з якого можна потім витягнути студента)
- курс, в процесі проходження якого тема була вивченою (з якого можна витягнути освітній сервіс, який підтвердив вивчення)

Освітній сервіс:

![image](https://user-images.githubusercontent.com/126251095/230980540-adf2a617-1519-43bd-bde3-d5bd08e2e9ea.png)

Курс:

![image](https://user-images.githubusercontent.com/126251095/230980630-03ad2088-2c0d-464b-b65e-c05ecabc4e4c.png)

Листки, що входять до курсу: (сутність, що зв'язує курс і листки, ManyToMany Leaf-Course)

![image](https://user-images.githubusercontent.com/126251095/230980707-0566e462-766d-49ed-88f9-6da53d83f65f.png)

Контракт: (сутність, що зв'язує курс і студента)

![image](https://user-images.githubusercontent.com/126251095/230981109-865bfa43-9fd1-41cd-a06a-07d70110c470.png)

Статус контракту: (requested, rejected, active, fail, success, terminated)

![image](https://user-images.githubusercontent.com/126251095/230981334-f70bf94e-d7df-48d7-a31f-823ef71db5b8.png)

Зміна статусу контракту: (сутність, яка генерується щоразу коли статус змінюється. зберігає контракт, дату зміни, новий статус, ініціатора (user). знайшовши по даті останню можна знайти актуальний статус)

![image](https://user-images.githubusercontent.com/126251095/230981437-5d55376d-8f48-4883-bc88-92d97501cbde.png)

2. UI use-cases:
- стартова для авторизованого: перенаправлення на дешборд студента і кнопка-логаут. для не авторизованого: кнопки реєстрація і логін. з всіх сторінок можливість перейти на стартову (наприклад клікнувши на лого в header). Contacts в footer - статична інфа. 
- авторизація:
	- реєстрація (username, e-mail, пароль), якщо не складно - OAuth
	якщо дані коректні - створює користувача, перекидає на логін, якщо ні - перезапускає форму і попереджає що щось не так
	- логін
	якщо дані коректні - перенаправляє на дешборд, якщо ні - перезапускає форму і попереджає що щось не так
	- логаут - перенаправляє на стартову
- паспорт листочка (відкривається прямим лінком)
	для будь-якого користувача
	- назва листка
	- тип листка
	- опис листка
	- key points (контрольні питання)
	- parent leaves (попередні листки) гіперлінки на паспорт відповідного листка
	- children leaves (подальші листки) гіперлінки на паспорт відповідного листка
	для авторизованого користувача
	- status StudentLeaf (можна кольором, можна текстом)
	- можливість зміни статусу (якщо статус не "validated" - то вільна зміна між статусами, якщо "validated" - заблоковано)

- дерево: направлений граф. Кожна вершина - листок, має бути вказана назва. Вершина є гіперлінком на паспорт відповідного листка (можливо хорошим рішенням буде розділити екран і в одній частині відобразити дерево, а в іншій - паспорт "активного" листка, тобто останнього, на який клікали лівою кнопкою).
Ребра генеруються на основі зв'язків між листками: (зв'язок зараз в БД задається з допомогою ManyToManyField Edge", по суті зв'язок іде від теми, яку необхідно знати до теми, для вивчення якої потрібно знати попередню. ми це візуалізуємо і зберігаємо зв'язки, але не блокуємо можливість вивчати теми, не вивчивши попередні). 
	для будь-якого користувача
	- власне відображення дерева
	- можливість відцентрувати по конкретному листку (відобразити його в основі дерева і рівень вище (попередні теми) ) 	https://drive.google.com/file/d/1Zwhazwx35quP2xpCl7Z_p0SYDJDoNhlI/view?usp=share_link  центрування викликається переходом по лінку з дешборду або клік правою кнопкою по листку на самому дереві
	- можливість відкривати/закривати додаткові рівні вверх чи вниз по кліку. якщо попереднього чи наступного рівня немає - кнопка блокується
https://drive.google.com/file/d/1M9qPFyHeu7Mv0mS8ayty2u_-Bh873S_r/view?usp=share_link
https://drive.google.com/file/d/1khfrsOEiYcl152tGHMKKr0QdbQvf1q2X/view?usp=share_link
https://drive.google.com/file/d/1jHouhSXI6VLWtov1788Ebw-4zPszx6H9/view?usp=share_link
	якщо користувач авторизований
	- зміну кольорів залежно від статусу листка: "not intersted" - сірий, "interested" - жовтий, "learning" - синій, "learned" - зелений, "validated" - темно-зелений 
https://drive.google.com/file/d/1ES3FylfZLO1IaRCWyj9zywEEBvAdXaK8/view?usp=share_link

- паспорт курсу, можливість з паспорту курсу згенерувати контракт
	для будь-якого користувача
	- назва курсу
	- опис курсу
	- освітній сервіс, що є автором курсу
	- ціна курсу
	- листочки-теми, які входять до курсу
	для авторизованого користувача
	- якщо немає контракту з статусом "active" чи "requested" по цьому курсу - кнопка "записатись на курс", якщо є контракт - то відображення останнього статусу. по кліку на кнопку створюється контракт між студентом і курсом зі статусом "requested"

- дешборд студента (відкривається лише для авторизованого користувача)
	- список листків, в яких будь-який статус, окрім "not interested". запис в списку складається з назви листка, останнього статусу, якщо "validated" - поруч 		назва 	  освітнього сервісу, який підтвердив і кнопки, яка дає можливість зміни статусу (якщо статус не "validated" - то вільна зміна між статусами, якщо 		"validated" 		- заблоковано). по кліку на назву листка - перехід на дерево, відцентроване по цьому листку
	- список курсів, в яких з студентом є контракт. запис в списку містить назву курсу, останній статус курсу, освітній сервіс, що є автором курсу. по кліку на 		назву курсу - перехід на паспорт курсу
	- перенаправлення на сторінку контрактів студента
	- якщо авторизований юзер має під собою Educator - посилання на контракти його як викладача
	
- сторінка контрактів студента (відкривається лише для авторизованого користувача)
	- список контрактів студента. кожен запис складається з назви курсу, останнього статусу контракту і назви освітньго сервісу що є автором курсу. а також з 	  кнопки, що дає можливість відхилити заявку (якщо статус "requested" або "active" перетворити його на "terminated")
	
- сторінка контрактів освітнього сервісу (відкривається за умови що до авторизованого user-а прив'язаний освітній сервіс)
	- згрупована по курсах таблиця, де рядком є контракт, а колонки:
		- студент
		- колонка на кожен з листків, що входять до складу курсу.
		якщо статус контракту "active" 
		  на перетині рядка-студента і колонки-листка булівська галочка "вивчено-не вивчено"
		- кнопка "зберегти зміни" (якщо вони автоматично не синхронізуються). при натисканні змінює статуси листків студента між "learning" i "learned"
		- кнопка "успішно завершити курс" - змінює статус всіх листків, що входять до курсу на "validated", а статус контракту на "success"
		- кнопка "неуспішно завершити курс" - змінює статус всіх листків, які в даний момент відмічені як вивчені на "validated", а статус контракту на "fail"
		- кнопка "розірвати контракт" - повертає статус всіх листків, які входять до курсу на "interested", а статус контракту на "terminated"
		
		якщо статус контракту "requested" - кнопки "прийняти" - змінює статус на "active", і "відхилити" - змінює статус на "rejected"
		
		якщо статус контракту "rejected", "terminated", "success", "failed" чи "validated" - просто ім'я студента і цей статус, без можливості змін. подібні 		контракти бажано перемістити вниз списку

