# Point-v0.1

Суть: є дерево технологій, користувачі-студенти і користувачі-освітні сервіси. На основі дерева технологій викладачі будують свої курси,
а студенти - відслідковують прогрес у навчанні.

Є код написаний не програмістом на Django, закладені моделі, частина обробки, виведена частина сторінок.

Функціонал:

2. UI:
- авторизація
	- реєстрація +
	- логін +
	- логаут +

- паспорт листочка
	- назва +
	- опис +
	- key points +
	- parent leaves +
	- children leaves +
	- status ( unique for every student) +

- дерево: граф, генерується на основі зв'язків між листками:
	- можливість відцентрувати по конкретному листку (відобразити його в основі дерева і рівень вище)
	- можливість відкривати/закривати додаткові рівні по кліку 
	- зміну кольорів залежно від статусу листка (unique for every student)

- паспорт курсу, можливість з паспорту курсу згенерувати контракт
	- назва +
	- опис +
	- освітній сервіс +
	- ціна +
	- листочки, які входять до курсу +
	- кнопка "записатись на курс", яка змінюється на "підписано", а потім на "завершено" ( unique for every student)

- портфоліо студента ( unique for every student )
	- таблиця з колонками "назва листочка" "статус" "освіт. сервіс, який підтвердив" +
		- можливість змінювати статуси ручками самостійно
	- таблиця з колонками "назва курсу" "статус" "освітній сервіс, що надає послуги"
- сторінка контрактів студента ( unique for every student )
	- таблиця з колонками "назва курсу" "останній статус" "освітній сервіс"
	- можливість розірвати контракт
- сторінка контрактів освітнього сервісу ( unique for every student )
	- згрупована по курсах таблиця з колонками "назва курсу" "студент" "останній статус"
	- можливість розірвати контракт
	- можливість завершити контракт (успішно або ні)
	- можливість підтвердити запис студента на курс

можна написати код з нуля, можна підхопити і доробити функціонал