import json

platforms = ["PS5", "Xbox Series X", "PC"]
actions = [
    ("money", "бесконечные деньги и миллионы на счет", "Трейнеры и конфиги"),
    ("tank", "вызов военного танка Rhino", "Моды и скрипты"),
    ("invincibility", "режим бессмертия и неуязвимости", "Чит-конфиги"),
    ("police", "полный сброс уровня розыска полицией", "Команды"),
    ("supercar", "спавн эксклюзивных спорткаров", "Моды"),
    ("weapons", "полный арсенал оружия и патронов", "Чит-коды"),
    ("helicopter", "вызов боевого вертолета", "Моды"),
    ("speed", "ускорение времени и бега", "Конфиги"),
    ("weather", "управление погодой и штормом", "Скрипты"),
    ("gravity", "отключение гравитации", "Фан-моды")
]

cheats = []
counter = 1

for platform in platforms:
    for action_id, action_desc, category in actions:
        slug = f"gta-6-{action_id}-{platform.lower().replace(' ', '-')}"
        title = f"Чит на {action_desc} в GTA 6 для {platform}"
        keyword = f"читы на {action_desc} гта 6 {platform.lower()}"
        
        cheat = {
            "slug": slug,
            "title": title,
            "keyword": keyword,
            "category": category,
            "size": f"1.{counter} МБ",
            "downloads": f"{10000 + counter * 145}",
            "rating": "4.9",
            "date": "Ноябрь 2026",
            "image": "https://images.unsplash.com/photo-1514565131-fce0801e5785?auto=format&fit=crop&w=1000&q=80",
            "text": f"Актуальный конфигурационный файл и внутриигровые комбинации для активации функции: {action_desc} в одиночном режиме Grand Theft Auto VI на платформе {platform}. Проверено на безопасность, не блокирует сохранения."
        }
        cheats.append(cheat)
        counter += 1

with open("src/cheats.json", "w", encoding="utf-8") as f:
    json.dump(cheats, f, ensure_ascii=False, indent=2)

print(f"Успешно сгенерировано {len(cheats)} уникальных SEO-страниц в src/cheats.json!")
