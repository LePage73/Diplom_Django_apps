﻿![Logotype](./docs/ru/Logo.jpg)

# Дипломная работа по теме:

## «Реализация веб-платформы для оказания дистанционных медицинских услуг в области диетологии»

## Автор: Круглов Игорь aka LePage

2024 г.

# 1\. Введение

## Обоснование выбора темы

1. В современном мире, мире пандемий и транспортного коллапса растет необходимость в предоставлении услуг на дистанционной основе.
2. Также существует растущая, стимулируемая государством, потребность оказания качественных услуг в труднодоступных и малонаселенных районах.
3. Работа в области разработки приложения позволит применить полученные знания на практике, создать основу для дальнейших разработок в области оказания дистанционных услуг.
4. Таким образом выбор темы «**Реализация веб-платформы для оказания дистанционных медицинских услуг в области диетологии**» обусловлен её актуальностью, потребностями рынка и её практической значимостью.

## Определение цели и задач исследования

Цель исследования:

Создать **веб-площадку** для оказания услуг в области диетологии и контроля веса.

Задачи исследования:

1. Обзор **фреймворков** для написания **веб-приложений**. Провести анализ существующих инструментов, выбрать наиболее подходящие под имеющуюся задачу.
2. Создание платформы в **формате веб-приложения** проведение тестирование её поведения при подключении и входе различных пользователей.
3. Составить **дипломную работу**, включающую в себя введение, обзор литературы, методологию и результаты исследования, анализ результатов, выводы и рекомендации.

Цели и задачи исследования направлены на получение практических результатов, которые позволят сформировать методы построения платформ для оказания удаленных услуг.

# 2\. Основные понятия и определения

1. **Фреймворк** (**Framework**): Программная платформа, которая предоставляет готовые компоненты и инструменты для разработки приложений. В контексте веб-приложений часто используются **Django**, **FastAPI** или **Flask**.
2. **Веб**\-**приложение** (**Web** **Application**): Программное приложение, которое работает на веб-сервере и доступно через браузер.
3. **База данных (БД) (DataBase) — это упорядоченный набор информации, который хранится в электронном виде**. Обычно он отражает характеристики какого-либо объекта или совокупности объектов, а также количественные показатели их взаимодействия друг с другом. Часто под БД понимаются **системы управления базами данных**. То есть не сам набор информационных сведений, а средства и инструменты для работы с ним. Для их обозначения часто используется аббревиатура **СУБД**.

# 3\. Методы и подходы к разработке

## Архитектура веб-приложения

**Frontend** и Backend: **фронтенд** (интерфейс пользователя) и **бэкенд** (серверная логика). **Фронтенд** может быть разработан с использованием **HTML**, **CSS** и **JavaScript**, а **бэкенд** может быть реализован на **Python** с использованием фреймворков, таких как **Flask** , **FastAPI** или **Django**.

## Обеспечение безопасности

**Аутентификация** и **авторизация**: Нужно настроить **авторизацию** пользователей, по возможности используя штатные средства, распределить их по группам/ролям для доступа и работы с соответствующим контентом.

# 4\. Обзор популярных инструментов для разработки веб-приложений на Python

## Django

Основные возможности:

**ORM (object-relational mapping)**: позволяет писать запросы к базам данных на **Python** вместо **SQL**. **ORM** абстрагирует взаимодействие с базами данных, автоматически генерирует схемы и упрощает разработку приложений.

**Система** **аутентификации**: обеспечивает комплексное управление учётными записями, группами и правами доступа. Она упрощает реализацию функций регистрации, входа и выхода пользователей, контролирует доступ к различным разделам сайта.

**Шаблонизатор**: инструмент для создания динамического **HTML**\-кода. Он позволяет внедрять переменные в шаблоны для динамического отображения данных на веб-страницах. С его помощью можно создать базовый шаблон с общей структурой сайта, а затем расширять его для отдельных страниц, добавляя уникальный контент: текст, изображения, информацию, комментарии и многое другое.

**Работа с формами**: встроенная библиотека для отображения и проверки форм. Она упрощает создание **форм ввода данных** и их **валидацию** по заданным критериям. Например, можно создать форму регистрации с полями для имени пользователя, электронной почты и пароля. Когда пользователь заполнит и отправит такую форму, **Django** проверит корректность заполнения всех полей.

**URL-маршрутизация**: удобная система для связывания **URL-адресов** с функциями обработки запросов. Она позволяет создавать понятные ссылки на страницы вашего веб-приложения.

**Встроенная административная панель:** автоматически генерируемый интерфейс для управления данными приложения. Она позволяет легко просматривать, добавлять, редактировать и удалять записи в базе данных без написания дополнительного кода.

**Интернационализация:** встроенная поддержка многоязычности и автоматическая локализация форматов даты, времени и чисел.

**Встроенная защита от распространённых уязвимостей**: **Django** обеспечивает защиту от **SQL-инъекций**, **межсайтового скриптинга (XSS)**, подделки межсайтовых запросов (**CSRF**), **кликджекинга** и **удалённого выполнения кода**.

Особенности:

Из описанных функций видно, что **Django** в первую очередь предназначен для разработки серверной части (**бэкенда**) веб-приложений. Фреймворк обрабатывает пользовательские запросы, управляет базами данных и отвечает за логику приложения.

Требует соблюдения жесткой структуры проекта.

## Flask

Основные возможности:

**Минимальный набор инструментов из коробки**. Причём они не навязывают какую-то архитектуру или жёсткую структуру проектов. Разработчики сами решают, как и что они будут создавать.

**Гибкость**. Работая с **Flask**, программист может выбирать только необходимые встроенные инструменты и подключать дополнительные внешние, не перегружая проект лишними модулями.

**Расширяемость**. У **Flask** много расширений и плагинов, которые помогают быстро добавить новую функциональность. Например, авторизацию, управление базами данных и работу с формами.

**Простота**. У **Flask** простой синтаксис, что делает изучение этого фреймворка более простым, а также позволяет быстрее создавать прототипы веб-приложений.

Особенности:

**Минималистичный подход**: только основные компоненты без лишних зависимостей.

**Высокая гибкость** для добавления нужных библиотек и модулей.

**Jinja2** для шаблонов и **Werkzeug** для маршрутизации и обработки запросов.

Подходит для небольших и средних проектов, где требуется большая гибкость.

## FastAPI

Основные возможности:

**Скорость работы**. Это достигается благодаря использованию асинхронного программирования (**asyncio**) и **Uvicorn** — высокопроизводительного **ASGI**\-сервера, который лежит в основе фреймворка. Согласно различным тестам производительности, **FastAPI** способен обрабатывать сотни тысяч запросов в секунду.

**Простота и интуитивность**. Использование аннотаций типов **Python** позволяет автоматически генерировать схемы данных, документацию и валидацию входных данных. Это уменьшает количество кода, который нужно писать вручную, и минимизирует вероятность ошибок.

**Асинхронность.** Встроенная поддержка асинхронных операций позволяет эффективно работать с большим количеством одновременных запросов, что особенно важно для приложений, работающих с **I/O** операциями, такими как работа с базами данных или **внешними API**.

**Поддержка стандартов OpenAPI** и **JSON Schema**. **FastAPI** полностью поддерживает спецификации **OpenAPI** и **JSON Schema**, что позволяет автоматически генерировать **документацию для API** и **схемы данных**. Это значительно упрощает процесс интеграции с другими системами и создания клиентских приложений.

**Совместимость и расширяемость**. **FastAPI** построен на основе **Starlette** и **Pydantic**, двух мощных библиотек, которые отвечают за маршрутизацию, асинхронность и валидацию данных соответственно.

Особенности:

Часто используется для создания **API** и **микросервисов**.

Кроме того, **FastAPI** позволяет быстро и эффективно создавать веб-приложения с чистым, **современным** **Python-кодом**, с подсказками типов.

# 5\. Проектирование приложения

## Планирование и анализ требований

Выбор фреймворка и инструментов:

Определение наиболее подходящего фреймворка (например, **Django**, **Flask** или **FastAPI**) и инструментов для разработки.

### При выборе фреймворка обращаем внимание на возможность

- гибко строить **Route**,
- работать **запросами**.

### Также стоит обратить внимание на то

- как организована работа с **PATH**;
- есть ли **CSRF**\-защита;
- есть ли защите от **SQL injection**;
- есть ли базовые инструменты для **авторизации**;
- есть ли базовые инструменты для **ролей** и **пользователей**;
- есть ли возможности **редиректов**;

Определение структуры приложения:

Разработка схемы архитектуры, включающей **фронтенд**, **бэкенд**, **базу** **данных**.

Разработка прототипа:

## Основные требования

**Реализация основного функционала**: Создание базовой версии приложения с минимально необходимым функционалом для тестирования и демонстрации.

## Технические требования

**Фронтенд**: использовать **HTML**, **CSS**, **JavaScript**, **Bootstrap**

**Бэкенд: Python** с использованием фреймворка

**База данных:** Использование базы данных (например, **SQLite**) для хранения данных о пользователях, их профилях, справочниках, назначений (рецептов).

# 6\. Разработка в соответствии с созданной документацией

## Планирование разработки

### Разработка делится на три основных этапа, в соответствии с архитектурным паттерном MVT

- Создание структуры БД.
- Разработка серверной логики, форм, представлений
- Создание и стилизация шаблонов HTML-страниц приложения

## Разработка

- 1. этап: разработана структура **БД** медицинского учреждения. См. Приложение №1
  2. этап: используя фрймворк **Django**, как наиболее подходящий под требования проекта, в соответствии с паттерном **MVT ,** создано веб-приложение **см.** Приложение №2 **и** Приложение №3  
        .
  3. этап: используя **HTML**, **CSS**, **JavaScript** и фреймворк **Bootstrap** стилизован пользовательский интерфейс

# 7\. Анализ и интерпретация результатов

При тестировании приложения создавалось несколько пользователей, которые авторизовались в разных группах, создавались и изменялись их профили, писались отчеты и назначения от разных пользователей адресованные различным пользователям, строились графики динамики лечения для различных пользователей.

Тестирование показало устойчивость системы, сбоев и искажений информации не наблюдалось.

# 8\. Заключение

Проектирование и разработка веб-приложения для удаленного оказания медицинских услуг были успешно завершены в соответствии с изначально заданной документацией.

Приложение включает функционал аутентификации и авторизации пользователей, хранения и обмена информацией, реализует удобное отображение информации, компактное.

## Вывод

Фреймворк Django позволяет быстро создать легко масштабируемую, администрируемую, надежную и защищенную веб-платформу для оказания дистанционных услуг.

# 9\. Список используемой литературы

## Django

<https://djangodoc.ru/3.2/contents/>

<https://djangodoc.ru/3.1/topics/db/models/?ysclid=m2043f1ve0188813609>

<https://djangodoc.ru/3.2/topics/forms/modelforms/?ysclid=m1z7lql5b8406659582>

<https://django.fun/docs/django/5.0/ref/forms/widgets/?ysclid=m24kdgc3b6406627716#numberinput>

<https://djangodoc.ru/3.2/topics/forms/?ysclid=m2a3lkkkhv595374666>

<https://fixmypc.ru/post/sozdanie-stranits-vkhoda-i-vykhoda-v-django-i-sozdanie-polzovatelei/?ysclid=m20f5zl2de178963768>

<https://proglib.io/p/kurs-django-chast-2-orm-i-osnovy-raboty-s-bazami-dannyh-2024-01-29?ysclid=m2043hsmfy985650264>

## QuerySet

<https://dropcode.ru/thread/kak-soedenit-dve-tablitsy-cherez-kliuch-v-django>

<https://metanit.com/python/django/5.8.php>

<https://stackoverflow.com/questions/50384564/manytomany-does-not-save-to-db-django>

<https://qna.habr.com/q/307975?ysclid=m2a512z1wh73673394>

<https://habr.com/ru/articles/752574/>

## Matplotlib

<https://skillbox.ru/media/code/biblioteka-matplotlib-dlya-postroeniya-grafikov/?ysclid=m2k5zb28s1162502486>

## Bootstrap

<https://webref.ru/layout/bootstrap5>

<https://getbootstrap.com/docs/5.3/components/modal/>

<https://getbootstrap.com/docs/5.0/components/popovers/>

## CSS

<https://siterost.net/post/background-image-html-css?ysclid=m24bicq4h7793652222>

<https://htmlacademy.ru/blog/css/background-image>

# ПРИЛОЖЕНИЕ №1. Структура БД

Для хранения данных о пациентах, врачах, назначений, отчетов и различных справочников и связей между ними, была разработана следующая структура **Базы** **Данных** (**БД**)

| 1   | **auth_user** | **пользователи (встроенная таблица Django)** |
| --- | --- | --- |

| 2   | **Pacient_Profile** | **профиль пациента** |
| --- | --- | --- |
| &nbsp; | Id  | &nbsp; |
| &nbsp; | User | _1 -2- 1 к auth_user_ |
| &nbsp; | Family | &nbsp; |
| &nbsp; | first_name | &nbsp; |
| &nbsp; | second_name | &nbsp; |
| &nbsp; | phone_number | &nbsp; |
| &nbsp; | Adress | &nbsp; |
| &nbsp; | birth_date | &nbsp; |
| &nbsp; | first_diagnos | &nbsp; |
| &nbsp; | start_weight | &nbsp; |
| &nbsp; | Gender | &nbsp; |
| &nbsp; | registration_date | &nbsp; |
| &nbsp; | Email | &nbsp; |
| &nbsp; | Doctor_Profile | _1-2-М к Doctor_Profile_ |

| 3   | **Doctor_Profile** | **профиль врача** |
| --- | --- | --- |
| &nbsp; | Id  | &nbsp; |
| &nbsp; | User | _1-2- 1 к auth_user_ |
| &nbsp; | Family | &nbsp; |
| &nbsp; | first_name | &nbsp; |
| &nbsp; | secondary_name | &nbsp; |
| &nbsp; | doc_stage | &nbsp; |
| &nbsp; | doc_specialty | _M-2-M к Specialty_list_ |
| &nbsp; | birth_date | &nbsp; |
| &nbsp; | Email | &nbsp; |
| &nbsp; | phone_number | &nbsp; |
| &nbsp; | registration_date | &nbsp; |
| &nbsp; | foto_file_path | &nbsp; |
| &nbsp; | Gender | &nbsp; |

| 4   | **Diets_List** | **список диет** |
| --- | --- | --- |
| &nbsp; | id  | &nbsp; |
| &nbsp; | title | &nbsp; |
| &nbsp; | description | &nbsp; |
| &nbsp; | foto_file_path | &nbsp; |

| 5   | **Preparats_List** | **список препаратов** |
| --- | --- | --- |
| &nbsp; | id  | &nbsp; |
| &nbsp; | title | &nbsp; |
| &nbsp; | description | &nbsp; |
| &nbsp; | foto_file_path | &nbsp; |

| 6   | **Assignment** | **назначения пациентам** |
| --- | --- | --- |
| &nbsp; | id  | &nbsp; |
| &nbsp; | assign_date | &nbsp; |
| &nbsp; | pacient_profile | _1-2-M к Pacient_Profile_ |
| &nbsp; | doctor_profile_id | _1-2-M к Doctor_Profile_ |
| &nbsp; | description | &nbsp; |
| &nbsp; | diets | _1-2-M к Diets_List_ |
| &nbsp; | preparats_list | _M-2-M к Preparats_List_ |

| 7   | **Pacient_reports** | **отчет пациента** |
| --- | --- | --- |
| &nbsp; | id  | &nbsp; |
| &nbsp; | report_date | &nbsp; |
| &nbsp; | weight_today | &nbsp; |
| &nbsp; | symptoms_list | _М-2-М к Symptoms_List_ |
| &nbsp; | patient_profile | _1-2-M к Pacient_Profile_ |

| 8   | **Specialty_list** | **специальности врачей** |
| --- | --- | --- |
| &nbsp; | id  | &nbsp; |
| &nbsp; | title | &nbsp; |
| &nbsp; | description | &nbsp; |

| 9   | **Symptoms_list** | **Список симптомов** |
| --- | --- | --- |
| &nbsp; | id  | &nbsp; |
| &nbsp; | title | &nbsp; |

# ПРИЛОЖЕНИЕ №2. Структура папок проекта

![Folders](./docs/ru/folders.jpg)

# ПРИЛОЖЕНИЕ №3. Веб-приложение на Django

### Легенда:

По заказу некоего абстрактного «Центра диетологии и контроля веса», далее «МедЦентр» создаем веб-платформу для удаленного оказания медицинских услуг для пациентов страдающих избыточным весом, дистрофией, анорексией и т.д. Т.З. от заказчика имеет следующий вид:

С площадкой все работают только удаленно.

Пользователи могут быть только в одной из трех ипостасей:

Группа «Врачи» - доктора

Группа «Администраторы» - суперпользователи

«Вне групп» - пациенты

Администратор имеет полный доступ в админпанель

Администратор через админпанель создает и редактирует справочник медицинских препаратов, справочник диет, справочник возможных побочных симптомов.

Администратор через админпанель прикрепляет к вновь зарегистрированному пациенту лечащего врача.

Администратор в админпанели сам создает логины и пароли пользователей-врачей и включает их в группу «Врачи»

Пользователь зашедший на сайт попадает на начальную страницу «О нас», где знакомится с услугами «МедЦентра», там же ему предлагают войти или зарегистрироваться.

На странице «Вход» пользователю предлагается ввести логин и пароль, если пользователь не регистрировался в системе ранее ему предлагается зарегистрироваться и перенаправляют на страницу регистрации. Если пользователь ввел правильную пару логин/пароль он входит в систему и авторизуется как врач или пациент в зависимости от принадлежности к группе «Врачи».

После входа и авторизации пользователь направляется в свой личный кабинет – страница «Личный кабинет».

При регистрации пользователь задает свою пару логин/пароль и создает свой профиль (Регистрационную карточку) . Которую впоследствии он может редактировать на странице «Профиль».

Доктор. как уже зарегистрированный Администраторм пользователь создает и редактирует свой профиль в меню «Профиль». Доктор не создавший профиль не может быть прикреплен к пациентам.

В «Личном кабинете» пациента пользователь может ознакомиться с назначениями от врача, посмотреть подробности о назначенных препаратах, диете, узнать частичную информацию о лечащем враче, его стаже, специальностях. А также отправить отчет (предполагается ежедневный) о своем состоянии, включающий: текущий вес, наблюдаемые возможные симптомы побочных эффектов, а также оставить любую другую информацию на свое усмотрение.

В «Личном кабинете доктора» врач видит список очереди прикрепленных пациентов, выбирает любого из них, видит краткую информацию из его профиля, видит графики изменения веса пациента и частоты проявления различных побочных симптомов созданные на основе (ежедневных) отчетов пациента. Так же он может ознакомиться с назначениями пациенту выданными ранее и создать новое назначение, если требуется.

### Проект:

На основании Т.З. во фреймворке Django были созданы соответствующие структуре БД (Приложение №1) модели, они были мигрированы во встроенную СУБД SQLite в корне проекта. Была создана структура папок проекта в соответствии с требованиями фреймворка Django (Приложение №2). Настроены маршруты. Также в Django были созданы формы для моделей с применением различных виджетов. В представлении, реализованном как в функциональном виде (FBV), так и основанном на Class-based View (CBV), была создана логика проекта, описывающая алгоритм Т.З. Для создания графических изображений, иллюстрирующих динамику процесса лечения, использовалась библиотека matplotlib.pyplot.

При обращении по HTTP адресу проекта пользователь попадает на страницу «О нас»

Рис. 1. Страница «О нас»![ris1](./docs/ru/ris1.jpg)

При нажатии на ссылку «войти» либо выбрав пункт меню «Вход» пользователь перенаправляется на страницу аутентификации.

Рис. 2. Страница «Вход»![ris2](./docs/ru/ris2.jpg)

Где он сможет войти в систему как авторизованный пользователь или перейти на страницу «Регистрация» по ссылке или пункту меню «Регистрация». Пользователи - врачи портала в системе уже зарегистрированы Администратором.

Рис. 3. Страница «Регистрация»![ris3](./docs/ru/ris3.jpg)

После регистрации либо входа, либо по кнопке меню «Личный кабинет» пользователь перенаправляется на страницу «Личного кабинета» вид которой зависит от «ипостаси» (так в Т.З.) пользователя - врач или пациент.

В «Личном кабинете» пациента пользователь может отправить врачу отчет о своем текущем состоянии:

Рис. 4. Страница «Личного кабинета» пациента. Основной вид.![ris4](./docs/ru/ris4.jpg)

Либо ознакомиться с текущим или прошлыми назначениями.

Рис. 5. Страница «Личного кабинета» пациента. Дополнительный вид.![ris5](./docs/ru/ris5.jpg)

При желании авторизованный пользователь может отредактировать, а пользователь-врач ещё и создать свой профиль выбрав пункт меню «Профиль»

Рис. 6. Страница редактирования профиля пациента.![ris6](./docs/ru/ris6.jpg)

Рис. 7. Страница редактирования профиля врача.![ris7](./docs/ru/ris7.jpg)

Также пользователь, авторизованный как врач, после входа или выбрав пункт меню «Личный кабинет» попадает на страницу личного кабинета врача. Где выбрав пациента из списка ожидающих приема, может ознакомиться с карточкой пациента, динамикой лечения, создать новое назначение, ознакомиться с предыдущими назначениями.

Рис. 8. Личный кабинет врача.![ris8](./docs/ru/ris8.jpg)

Рис. 9. Личный кабинет врача. Предыдущие назначения.![ris9](./docs/ru/ris9.jpg)

Рис. 10. Личный кабинет врача. Предыдущие назначения. Расширенный вид.

![ris10](./docs/ru/ris10.jpg)

Так же по пункту меню «Профиль» авторизованный пользователь-врач может создать/отредактировать свой профиль.

Рис. 11. Профиль доктора.![ris11](./docs/ru/ris11.jpg)