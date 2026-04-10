import init_django_orm


from db.models import Genre, Actor


def main():
    # --- СТВОРЕННЯ (Create) ---
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Action")
    Genre.objects.create(name="Dramma")  # Спеціально з помилкою для подальшого оновлення

    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reeves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    # --- ОНОВЛЕННЯ (Update) ---
    # Виправляємо помилку в назві жанру
    Genre.objects.filter(name="Dramma").update(name="Drama")

    # Оновлюємо прізвище Джорджа
    Actor.objects.filter(last_name="Klooney").update(last_name="Clooney")

    # Оновлюємо ім'я та прізвище Кіану (виправляємо Kianu на Keanu)
    Actor.objects.filter(first_name="Kianu").update(
        first_name="Keanu",
        last_name="Reeves"
    )

    # --- ВИДАЛЕННЯ (Delete) ---
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # --- ПОВЕРНЕННЯ (Read + Sort) ---
    # Знаходимо всіх Смітів та сортуємо за ім'ям
    return Actor.objects.filter(last_name="Smith").order_by("first_name")


if __name__ == "__main__":
    print(main())