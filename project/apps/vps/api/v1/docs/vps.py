from drf_spectacular.utils import extend_schema

vps_schema = {
    "list": extend_schema(
        **{"summary": "Виртуальный выделенный сервер - Список объектов",}
    ),
    "retrieve": extend_schema(
        **{"summary": "Виртуальный выделенный сервер - Данные объекта",}
    ),
    "create": extend_schema(
        **{"summary": "Виртуальный выделенный сервер - Создание объекта",}
    ),
    "change_status": extend_schema(
        **{"summary": "Виртуальный выделенный сервер - Изменение статуса объекта",}
    ),
}
