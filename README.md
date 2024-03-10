# Спсок статей
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

# Статья
/api/articles/statya-1/
{
    "id": 1,
    "title": "статья 1",
    "content": "<p><img alt=\"\" src=\"/media/uploads/2024/03/06/image-105.jpg\" style=\"height:197px; width:352px\" />аывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыы</p>\r\n\r\n<p>аывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыыаывыаываыы</p>",
    "date": "2024-03-06"
}

# Спсок продукции с пагинацией
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
            "alloy_type": "Д16",
            "standard": "ГОСТ 21631-76",
            "thickness": "0.5-5.0",
            "width": "1000-1200",
            "length": "2000-4000"
        },
        {
            "id": 2,
            "product_category": "Лист",
            "supply_condition": "Н2",
            "alloy_type": "2017А",
            "standard": "ТУ 1-2-546-2000",
            "thickness": "0.2-5.0",
            "width": "1000-1200",
            "length": "4000-5000"
        },
        {
            "id": 3,
            "product_category": "Лист",
            "supply_condition": "М",
            "alloy_type": "В95",
            "standard": "ГОСТ 21631-76",
            "thickness": "0.4-0.7",
            "width": "6-6",
            "length": "3-5"
        }
    ]
}

# Два варианта api для продукции разбитой по группам на главной странице
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
                "alloy_type": "Д16",
                "standard": "ГОСТ 21631-76",
                "thickness": "0.5-5.0",
                "width": "1000-1200",
                "length": "2000-4000"
            },
            {
                "id": 2,
                "product_category": "Лист",
                "supply_condition": "Н2",
                "alloy_type": "2017А",
                "standard": "ТУ 1-2-546-2000",
                "thickness": "0.2-5.0",
                "width": "1000-1200",
                "length": "4000-5000"
            },
            {
                "id": 3,
                "product_category": "Лист",
                "supply_condition": "М",
                "alloy_type": "В95",
                "standard": "ГОСТ 21631-76",
                "thickness": "0.4-0.7",
                "width": "6-6",
                "length": "3-5"
            },
            {
                "id": 4,
                "product_category": "Лист",
                "supply_condition": "Т1",
                "alloy_type": "1105",
                "standard": "ОСТ 1.92073-82",
                "thickness": "0.1-0.3",
                "width": "7-10",
                "length": "12-14"
            },
            {
                "id": 5,
                "product_category": "Лист",
                "supply_condition": "Н2",
                "alloy_type": "1105",
                "standard": "ТУ 1-2-546-2000",
                "thickness": "0.2-5.0",
                "width": "15-16",
                "length": "12-15"
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
                "standard": "ГОСТ 21631-76"
            },
            {
                "id": 2,
                "product_category": "Лист",
                "alloy_type": "2017А",
                "standard": "ТУ 1-2-546-2000"
            },
            {
                "id": 3,
                "product_category": "Лист",
                "alloy_type": "В95",
                "standard": "ГОСТ 21631-76"
            },
            {
                "id": 4,
                "product_category": "Лист",
                "alloy_type": "1105",
                "standard": "ОСТ 1.92073-82"
            },
            {
                "id": 5,
                "product_category": "Лист",
                "alloy_type": "1105",
                "standard": "ТУ 1-2-546-2000"
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


# Список (сплав и тип продукции) для фильтрации продукции
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
    ]
}


# Фильтрация продукции
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


# Второй блок раздела "О компании"
/api/company/about/1/
{
    "id": 1,
    "text": "<h2>...</h2>"
}


# Контакты отделов и адрес компании
/api/contacts/
{
    "departments": [
        {
            "id": 1,
            "telephone_number": "+7 (3439) 399-409",
            "name": "Приемная"
        },
        {
            "id": 2,
            "telephone_number": "+7 (3439) 399-440",
            "name": "Отдел продаж"
        },
        {
            "id": 3,
            "telephone_number": "+7 (3439) 399-404",
            "name": "Цветные металлы"
        },
        {
            "id": 4,
            "telephone_number": "+7 (3439) 399-448",
            "name": "Бухгалтерия"
        }
    ],
    "address": {
        "region": "Свердловская область",
        "city": "Каменск-Уральский",
        "address": "ул. Заводская, 9/8",
        "map": "<script type=\"text/javascript\" charset=\"utf-8\" async src=\"https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3Af23f57325491a287d30a1709cc1f8a6c2d76590225bf8488c72fa86d75a442f5&amp;width=100%25&amp;height=100%&amp;lang=ru_RU&amp;scroll=true\"></script>"
    }
}