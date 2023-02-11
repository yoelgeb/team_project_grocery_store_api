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

def y(text):
    return text

def max_price():
    dict_list = []
    query = f"""SELECT product_name, MAX(product_price) as Max_Price
    FROM products
    GROUP BY product_name
    ORDER BY Max_Price DESC"""
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    for row in result: 
        row_dict = {
            "product_name" : row[0],
            "Max_price" : row[1]
        }
        dict_list.append(row_dict)
    return dict_list

def product_category():
    dict_list=[]
    query="""SELECT  product_name, category_name
    from products
    JOIN product_categories
    ON products.category_id = product_categories.category_id
    ORDER BY category_name"""
    db_cursor.execute(query)
    result = db_cursor.fetchall()
    for row in result: 
        row_dict = {
            "product_name" : row[0],
            "category_name" : row[1]
        }
        dict_list.append(row_dict)
    return dict_list


