from DB import conn


def add_customer(name, last_name, telephone, topic, description, date):
    with conn.cursor() as cur:
        select_query = """INSERT INTO customer_profile (name, last_name, telephone, topic, description, date)
                       VALUES (%s, %s, %s, %s, %s, %s)"""
        cur.execute(select_query, (name, last_name, telephone, topic, description, date))
        return 'Клиент добавлен'


us_name = 'Михаил'
us_last_name = 'Воронин'
us_telephone = '+7(999)999-99-99'
us_topic = 'бытовуха'
us_description = 'бухает с другом'
us_date = '25.10.2023'
# print(add_customer(us_name, us_last_name, us_telephone, us_topic, us_description, us_date))
conn.commit()
