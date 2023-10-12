<h1>Описание Проекта Commercial_network</h1>

Commercial_network это django rest_framework проект для управления сетью по продаже электроники


<h1>Запуск проекта</h1>
<ul>
<li>1. Cклонируйте себе проект https://github.com/alexandr50/Project_certification.git</li>
<li>2. Перейдите в папку commercial_network</li>
<li>3. Установите зависимости из requirements.txt</li>
<li>4. Запустите проект python manage.py runserver</li>
<li>5. Документация доступна по 
<ol>
<li>swagger http://127.0.0.1:8000/docs/</li>
<li>redoc http://127.0.0.1:8000/redoc/</li>
</ol>
</li>
</ul>

<h1>Приложения и модели</h1>

<h4>CustomUser:</h4>
Кастомная модель юзера

<h4>ProductionPlant:</h4>
Модель завода у которой нет поставщика, он не имеет поставщика<br>
Связана с Product (ManyToMany)<br>
Связана с Contact (OneToOne)
<h4>RetailNetwork:</h4>
Модель розничной сети, имеет поставщика только одного<br>
Связана с Product (ManyToMany)<br>
Связана с Contact (OneToOne)<br>
Связана с Production Plant (ForeignKey)

<h4>SoloTrader:</h4>
Модель индивидульного предпринимателя имеет поставщика только одного<br>
Связана с Product (ManyToMany)<br>
Связана с Contact (OneToOne)<br>
Связана с Production Plant (ForeignKey)<br>
Связана с ReatilNetwork (ForeignKey)

<h1>Пагинация</h1>
<ol>
<li>Для всех моделей реализована пагинация с выводом 10 объектов на страницу.</li>
<li>Максимальное значение - 50 объектов на страницу.</li>
</ol>


<h1>Тестирование</h1>
<ol>
<li>Проведена проверка синтаксиса и соблюдения PEP с помощью flake8.</li>
</ol>