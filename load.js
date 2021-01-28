db.main_employee.insertMany(
    [
        {"surname": "Бульдяев", "name": "Сергей", "secname": "Александрович"},
        {"surname": "Ляховец", "name": "Дмитрий", "secname": "Сергеевич"},
        {"surname": "Гудов", "name": "Алексей", "secname": "Владимирович"},
        {"surname": "Черепанов", "name": "Сергей", "secname": "Александрович"},
        {"surname": "Клейменов", "name": "Виктор", "secname": "Семенович"}
    ]);

db.main_item.insertMany(
    [{
        "name": "Мат. ценность 1",
        "user": "",
        "responsible": "",
        "components": [],
        "inventory_n": "",
        "otss_category": "",
        "condition": "",
        "unit_from": "",
        "in_operation": "",
        "fault_document_requisites": "",
        "date_of_receipt": null,
        "number_of_receipt": "",
        "requisites": "",
        "transfer_date": null,
        "otss_requisites": "",
        "spsi_requisites": "",
        "transfer_requisites": "",
        "comment": "",
        "last_check": null
    }, {
            "name": "Мат. ценность 2",
            "user": "",
            "responsible": "",
            "components": [
                {
                    "id": 0,
                    "name": "Компонент 1",
                    "serial_n": "",
                    "type": "",
                    "view": "",
                    "category": "",
                    "year": "",
                    "cost": "",
                    "location": {
                        "object": "",
                        "corpus": "",
                        "unit": "",
                        "cabinet": ""
                    }
                },
                {
                    "id": 1,
                    "name": "Компонент 2",
                    "serial_n": "",
                    "type": "",
                    "view": "",
                    "category": "",
                    "year": "",
                    "cost": "",
                    "location": {
                        "object": "",
                        "corpus": "",
                        "unit": "",
                        "cabinet": ""
                    }
                },
                {
                    "id": 2,
                    "name": "Компонент 3",
                    "serial_n": "",
                    "type": "",
                    "view": "",
                    "category": "",
                    "year": "",
                    "cost": "",
                    "location": {
                        "object": "",
                        "corpus": "",
                        "unit": "",
                        "cabinet": ""
                    }
                }
            ],
            "inventory_n": "",
            "otss_category": "",
            "condition": "",
        "unit_from": "",
        "in_operation": "",
        "fault_document_requisites": "",
        "date_of_receipt": null,
        "number_of_receipt": "",
        "requisites": "",
        "transfer_date": null,
        "otss_requisites": "",
        "spsi_requisites": "",
        "transfer_requisites": "",
        "comment": "",
        "last_check": null
    }
    ]
);

db.main_otss.insertMany(
    [
        {"category": "1"},
        {"category": "2"},
        {"category": "3"},
        {"category": "Не секретно"}
    ]
);

db.main_location.insertMany(
    [
        {
            "object": "Академия",
            "corpus": "3",
            "cabinet": "113",
            "unit": "к732"
        },
        {
            "object": "Академия",
            "corpus": "3",
            "cabinet": "136",
            "unit": "к732"
        },
        {
            "object": "Академия",
            "corpus": "3",
            "cabinet": "103",
            "unit": "к732"
        }
    ]
);

db.main_unit.insert(
    {"unit": "к732"}
)