import psycopg2

with psycopg2.connect(user="postgres",
                      password="Hun$917&305TpS",
                      port="5432",
                      database="ur_db") as conn:
    def create_db():
        """
        Функция, создающая структуру БД (таблицы)
        :return: Таблица создана
        """
        with conn.cursor() as cur:
            create_query = """ CREATE TABLE IF NOT EXISTS customer_profile(
                                customer_id SERIAL PRIMARY KEY,
                                name VARCHAR(30) NOT NULL,
                                Last_name VARCHAR(40)NOT NULL,
                                telephone VARCHAR(30) NOT NULL,
                                topic VARCHAR(200) NOT NULL,
                                description TEXT NOT NULL,
                                date VARCHAR(30) NOT NULL
                                )"""
            cur.execute(create_query)
            return 'Таблица создана'


    # print(create_db())
    conn.commit()


    def delete_db():
        """
        Функция, удаляющая таблицы базы данных
        :return: Таблица удалена
        """
        with conn.cursor() as cur:
            delete_query = """DROP TABLE customer_profile;"""
            cur.execute(delete_query)
            return 'Таблица удалена'


    # print(delete_db())
    conn.commit()