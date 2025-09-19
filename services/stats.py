from collections import defaultdict


def default_stats():
    return {"wins": 0, "total": 0}

statistics = defaultdict(default_stats)

def get_stat(user_id):
    data = statistics[user_id]
    wins = data["wins"]
    total = data["total"]
    percentage = (wins / total) * 100 if total > 0 else 0
    text = f"Ты выиграл {wins} из {total}. Процент побед: {percentage:.2f}%"
    return text

def update_stats(user_id, winner):
    statistics[user_id]["total"] += 1
    if winner:
        statistics[user_id]["wins"] += 1