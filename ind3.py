if __name__ == '__main__':
    # Начальная дистанция
    daily_distance = 10.0  # км
    total_distance = 0.0

    print("Расчет дистанции за 7 дней:")
    print(f"День 1: {daily_distance:.2f} км")

    total_distance += daily_distance

    # Расчет для дней 2-7
    for day in range(2, 8):
        daily_distance = daily_distance * 1.10  # Увеличение на 10%
        total_distance += daily_distance
        print(f"День {day}: {daily_distance:.2f} км")

    print(f"\nСуммарный путь за 7 дней: {total_distance:.2f} км")