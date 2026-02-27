import json
import sys
import re

# Читаем JSON
data = json.loads(sys.stdin.readline().strip())

# Количество запросов
q = int(sys.stdin.readline().strip())

for _ in range(q):
    query = sys.stdin.readline().strip()
    current = data
    found = True

    # Разбиваем по точкам (object keys)
    parts = query.split('.')

    for part in parts:
        # Находим имя ключа и все индексы в []
        tokens = re.findall(r'([a-zA-Z_]\w*)|\[(\d+)\]', part)

        for key, index in tokens:
            if key:  # доступ к объекту
                if isinstance(current, dict) and key in current:
                    current = current[key]
                else:
                    found = False
                    break
            elif index:  # доступ к массиву
                idx = int(index)
                if isinstance(current, list) and 0 <= idx < len(current):
                    current = current[idx]
                else:
                    found = False
                    break

        if not found:
            break

    if found:
        print(json.dumps(current, separators=(',', ':')))
    else:
        print("NOT_FOUND")