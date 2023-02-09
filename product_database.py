from mysql import connector

my_connection = connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "grocery"
)

db_cursor = my_connection.cursor()


def get_products(category):
    dict_list = []
    stmt = f'''Select product_name, product_quantity, product_price, category_name
                    from products
	                    join product_categories on products.category_id = product_categories.category_id
                where category_name = "{category}"'''
    db_cursor.execute(stmt)
    result_set = db_cursor.fetchall()
    for row in result_set: 
        row_dict = {
            "name" : row[0],
            "quantity" : row[1],
            "price" : row[2],
            "category" : row[3]
        }
        dict_list.append(row_dict)
    return dict_list

# print(get_products("Fruits"))
