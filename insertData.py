from database.useConnection import useConnection

class insertData(useConnection):

    countries = "INSERT INTO countries(name, continent_name) VALUES(%s,%s)"
    countries_list = ([
        ('Bulgaria', 'Europe'),
        ('Netherlands', 'Europe'),
        ('England', 'Europe'),
        ('Japan', 'Asia')
    ])

    cities = "INSERT INTO cities(name, country_code) VALUES(%s,%s)"
    cities_list = ([
        ('Dupnica', 1),
        ('Pernik' , 1),
        ('Varna'  ,  1),
        ('Amsterdam', 2),
        ('London', 3),
        ('Manchester', 3),
        ('Tokio', 4)
    ])

    users = "INSERT INTO users(full_name, email, gender, city_id) VALUES(%s,%s,%s,%s)"
    users_list = ([
        ('Ivan Ivanov', 'VankataBate@abv.bg', 'male', 1),
        ('Iordan Velichkov', 'Iordan_123@gmail.com', 'male', 2),
        ('Ivana Nikolova', 'i_nikolova@abv.bg', 'female', 3),
        ('Adam James', 'adam_james@hotmail.com', 'male', 4),
        ('Jeff Hrady', 'jeff_dude@abv.bg', 'male', 5),
        ('Brie Bella', 'bella_brie@hotmail.com', 'female', 6),
        ('Zinch Zun', 'zun_zun@gmail.com', 'female', 7),
    ])

    orders = "INSERT INTO orders(user_id, status) VALUES(%s,%s)"
    orders_list = ([
        (1, 'In progress'),
        (2, 'Sent'),
        (3, 'Sent'),
        (4, 'Delivered'),
        (5, 'Delivered'),
        (6, 'Not confirmed yet'),
        (7, 'Wating for sending'),
    ])

    merchants = "INSERT INTO merchants(merchant_name, city_id, admin_id) VALUES(%s,%s,%s)"
    merchants_list = ([
        ('Optim-al', 1, 1),
        ('Squanto', 2, 2),
        ('Bradford', 3, 3),
        ('MyTurkey', 4, 4),
        ('HotYams', 5, 5),
        ('AGobbler', 6, 6),
        ('Mayflowa', 7, 7),
    ])

    categories = "INSERT INTO categories(id, name) VALUES(%s,%s)"
    categories_list = ([
        (1, 'Box'),
        (2, 'Plastic bag'),
        (3, 'Big box'),
        (4, 'Plastic bottle'),
        (5, 'Glass bottle'),
        (6, 'Envelope'),
        (7, 'Transparent cardboard'),
    ])

    products = "INSERT INTO products(name, merchant_id, category_id, price, status) VALUES(%s,%s,%s,%s,%s)"
    products_list = ([
        ('Vino', 1, 1, 50, 'On stock'),
        ('Clothes', 2, 2, 2, 2),
        ('PC', 3, 3, 3, 122) ,
        ('Coca-cola', 4, 4, 4, 10),
        ('Vodka', 5, 5, 5, 150),
        ('Gift-card', 6, 6, 6, 3),
        ('Flowers', 7, 7, 7, 500),
    ])

    order_items = "INSERT INTO order_items(order_id, product_id, quantity) VALUES(%s,%s,%s)"
    order_items_list = ([
        (1, 1, 800),
        (2, 2, 250),
        (3, 3, 10),
        (4, 4, 2500),
        (5, 5, 3000),
        (6, 6, 5000),
        (7, 7, 10000),
    ])

    useConnection.cursor.executemany(countries, countries_list)
    useConnection.cursor.executemany(cities, cities_list)
    useConnection.cursor.executemany(users , users_list)
    useConnection.cursor.executemany(orders, orders_list)
    useConnection.cursor.executemany(merchants, merchants_list)
    useConnection.cursor.executemany(categories, categories_list)
    useConnection.cursor.executemany(products, products_list)
    useConnection.cursor.executemany(order_items, order_items_list)
    useConnection.connection.commit()
