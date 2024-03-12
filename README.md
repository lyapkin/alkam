# Спсок статей
```
/api/articles/
{
    "articles": [
        {
            "id": 10,
            "title": "оборудование",
            "slug": "oborudovanie",
            "content_concise": "Descriptionываыва",
            "image_url": "/media/images/image_105_cnrgKV9.jpg",
            "date": "2024-03-07",
            "categories": [
                1(id)
            ]
        },
        {
            "id": 4,
            "title": "статья 4",
            "slug": "statya-4",
            "content_concise": "Description",
            "image_url": "/media/images/image_105_ehqaNJp.jpg",
            "date": "2024-03-06",
            "categories": [
                1(id),
                5(id)
            ]
        }
    ],
    "categories": [
        {
            "id": 1,
            "name": "Алюминиевый прокат"
        },
        {
            "id": 2,
            "name": "Оборудование"
        },
        {
            "id": 3,
            "name": "Продукция"
        },
        {
            "id": 4,
            "name": "Новости АЛКАМ"
        },
        {
            "id": 5,
            "name": "Металлургия"
        }
    ]
}
```


# Статья
```
/api/articles/statya-1/
{
    "id": 1,
    "title": "статья 1",
    "content": "<p><img alt=\"\" src=\"/media/uploads/2024/03/06/image-105.jpg\" style=\"height:197px; width:352px\" />аывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыы</p>\r\n\r\n<p>аывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыы</p>",
    "date": "2024-03-06"
}
```


# Спсок продукции с пагинацией
```
/api/products/
{
    "count": 7,
    "next": "http://127.0.0.1:8000/api/products/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "product_category": "Лист",
            "supply_condition": "Т1",
            "standard": "ГОСТ 21631-76",
            "thickness": "0.5-5.0",
            "width": "1000-1200",
            "length": "2000-4000",
            "material": "Алюминий"
        },
        {
            "id": 2,
            "product_category": "Лист",
            "supply_condition": "Н2",
            "standard": "ТУ 1-2-546-2000",
            "thickness": "0.2-5.0",
            "width": "1000-1200",
            "length": "4000-5000",
            "material": "Алюминий"
        },
        {
            "id": 3,
            "product_category": "Лист",
            "supply_condition": "М",
            "standard": "ГОСТ 21631-76",
            "thickness": "0.4-0.7",
            "width": "6-6",
            "length": "3-5",
            "material": "Алюминий"
        }
    ]
}
```


# Два варианта api для продукции разбитой по группам на главной странице
```
/api/products/?grouped
[
    {
        "typeSlug": "list",
        "typeName": "Лист",
        "products": [
            {
                "id": 1,
                "product_category": "Лист",
                "supply_condition": "Т1",
                "standard": "ГОСТ 21631-76",
                "thickness": "0.5-5.0",
                "width": "1000-1200",
                "length": "2000-4000",
                "material": "Алюминий"
            },
            {
                "id": 2,
                "product_category": "Лист",
                "supply_condition": "Н2",
                "standard": "ТУ 1-2-546-2000",
                "thickness": "0.2-5.0",
                "width": "1000-1200",
                "length": "4000-5000",
                "material": "Алюминий"
            },
            {
                "id": 3,
                "product_category": "Лист",
                "supply_condition": "М",
                "standard": "ГОСТ 21631-76",
                "thickness": "0.4-0.7",
                "width": "6-6",
                "length": "3-5",
                "material": "Алюминий"
            },
            {
                "id": 4,
                "product_category": "Лист",
                "supply_condition": "Т1",
                "standard": "ОСТ 1.92073-82",
                "thickness": "0.1-0.3",
                "width": "7-10",
                "length": "12-14",
                "material": "Алюминий"
            },
            {
                "id": 5,
                "product_category": "Лист",
                "supply_condition": "Н2",
                "standard": "ТУ 1-2-546-2000",
                "thickness": "0.2-5.0",
                "width": "15-16",
                "length": "12-15",
                "material": "Алюминий"
            },
            {
                "id": 6,
                "product_category": "Лист",
                "supply_condition": "Т1",
                "standard": "ТУ 1-2-546-2000",
                "thickness": "1.0-2.0",
                "width": "1-2",
                "length": "1-2",
                "material": "Алюминий"
            },
            {
                "id": 7,
                "product_category": "Лист",
                "supply_condition": "Н2",
                "standard": "ТУ 1-2-607-2005",
                "thickness": "1.0-2.0",
                "width": "1-2",
                "length": "12-13",
                "material": "Алюминий"
            }
        ]
    },
    {
        "typeSlug": "listy-riflenye",
        "typeName": "Листы рифленые",
        "products": []
    },
    {
        "typeSlug": "plita",
        "typeName": "Плита",
        "products": []
    },
    {
        "typeSlug": "profil-press",
        "typeName": "Профиль пресс",
        "products": []
    }
]
```

```
/api/products/preview/
[
    {
        "typeSlug": "list",
        "typeName": "Лист",
        "products": [
            {
                "id": 1,
                "product_category": "Лист",
                "alloy_type": "Д16",
                "standard": "ГОСТ 21631-76",
                "material": "Алюминий"
            },
            {
                "id": 2,
                "product_category": "Лист",
                "alloy_type": "2017А",
                "standard": "ТУ 1-2-546-2000",
                "material": "Алюминий"
            },
            {
                "id": 3,
                "product_category": "Лист",
                "alloy_type": "В95",
                "standard": "ГОСТ 21631-76",
                "material": "Алюминий"
            },
            {
                "id": 4,
                "product_category": "Лист",
                "alloy_type": "1105",
                "standard": "ОСТ 1.92073-82",
                "material": "Алюминий"
            },
            {
                "id": 5,
                "product_category": "Лист",
                "alloy_type": "1105",
                "standard": "ТУ 1-2-546-2000",
                "material": "Алюминий"
            }
        ]
    },
    {
        "typeSlug": "listy-riflenye",
        "typeName": "Листы рифленые",
        "products": []
    },
    {
        "typeSlug": "plita",
        "typeName": "Плита",
        "products": []
    },
    {
        "typeSlug": "profil-press",
        "typeName": "Профиль пресс",
        "products": []
    }
]
```


# Список (сплав и тип продукции) для фильтрации продукции
```
/api/products/filters_list
{
    "alloys": [
        {
            "id": 1,
            "name": "Д16",
            "slug": "d16"
        },
        {
            "id": 2,
            "name": "ВД1",
            "slug": "vd1"
        },
        {
            "id": 3,
            "name": "В95",
            "slug": "v95"
        },
        {
            "id": 4,
            "name": "1105",
            "slug": "1105"
        },
        {
            "id": 5,
            "name": "2024",
            "slug": "2024"
        },
        {
            "id": 6,
            "name": "2017А",
            "slug": "2017a"
        }
    ],
    "categories": [
        {
            "id": 1,
            "name": "Лист",
            "slug": "list"
        },
        {
            "id": 2,
            "name": "Листы рифленые",
            "slug": "listy-riflenye"
        },
        {
            "id": 3,
            "name": "Плита",
            "slug": "plita"
        },
        {
            "id": 4,
            "name": "Профиль пресс",
            "slug": "profil-press"
        }
    ],
    "materials": [
        {
            "id": 1,
            "name": "Алюминий",
            "slug": "alyuminiy"
        }
    ]
}
```


# Фильтрация продукции
```
/api/products/?alloy=d16&category=list
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "product_category": "Лист",
            "supply_condition": "Т1",
            "alloy_type": "Д16",
            "standard": "ГОСТ 21631-76",
            "thickness": "0.5-5.0",
            "width": "1000-1200",
            "length": "2000-4000"
        }
    ]
}
```


# Второй блок раздела "О компании"
```
/api/company/about/1/
{
    "id": 1,
    "text": "<h2>...</h2>"
}
```


# Проекты
```
/api/company/projects/
[
    {
        "id": 1,
        "preview": "НачалПараграф Параграф Параграф Параграф Параграф Параграф Параграф Параграф Параграф Параграф Параграф Параграф2 Параграф2 Параграф2 Параграф2 Параграф2   fdsfsdfsdfsdfs sdfsdfsfsdfssdfsdfsdfsd",
        "preview_image": "http://127.0.0.1:8000/media/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2024-03-11_154143.png"
    },
    {
        "id": 2,
        "preview": "параграффффпараграффффпараграфф...",
        "preview_image": "http://127.0.0.1:8000/media/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2024-03-11_154143_bvGQGui.png"
    }
]
```

```
/api/company/projects/1/
{
    "id": 1,
    "content": "<h1>Заголовок</h1>\r\n\r\n<p>НачалПараграф&nbsp;Параграф&nbsp;Параграф&nbsp;Параграф&nbsp;Параграф&nbsp;Параграф&nbsp;Параграф&nbsp;Параграф&nbsp;Параграф&nbsp;Параграф&nbsp;Параграф&nbsp;</p>\r\n\r\n<p><img alt=\"\" src=\"http://localhost:8000/media/uploads/2024/03/06/image-105.jpg\" style=\"height:197px; width:352px\" /></p>\r\n\r\n<p>Параграф2&nbsp;Параграф2&nbsp;<img alt=\"\" src=\"http://localhost:8000/media/uploads/2024/03/06/image-105.jpg\" style=\"height:197px; width:352px\" />Параграф2&nbsp;Параграф2&nbsp;Параграф2&nbsp;</p>\r\n\r\n<hr />\r\n<h2>Заголовок 2</h2>\r\n\r\n<p>fdsfsdfsdfsdfs</p>\r\n\r\n<p>sdfsdfsfsdfssdfsdfsdfsd</p>\r\n\r\n<p><img alt=\"\" src=\"http://localhost:8000/media/uploads/2024/03/06/image-105.jpg\" style=\"height:197px; width:352px\" /></p>\r\n\r\n<p>&nbsp;</p>"
}
```


# Форма запроса звонка
```
/api/requests/calls/
Body: (заполненые поля обязательные, номер телефона валидируется на бэке)
{
    "name": "Андрей",
    "number": "+79876543210",
    "comment": ""
}
```


# Форма запроса коммерческого предложения
```
/api/requests/commercials/
Body: (заполненые поля обязательные, номер телефона валидируется на бэке)
{
    "name": "Андрей",
    "number": "+79876543210",
    "comment": "",
    "product_details": "test",
    "activity_type": "",
    "company_name": "test"
}
```