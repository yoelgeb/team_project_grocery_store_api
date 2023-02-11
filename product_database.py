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
# Return all the category names
def get_product_categories():
    cat_list = []
    stmt = "Select * from product_categories"
    db_cursor.execute(stmt)
    result_set = db_cursor.fetchall()
    for row in result_set:
        cat_list.append(row)
    return cat_list

def buy_product(email, product_name):
    stmt = f'''
    INSERT INTO customer_products(customer_id, product_id)
    VALUES ((Select customer_id from Customers where email = "{email}"), 
		Select product_id from Products where product_name = "{product_name}"))
    '''
    db_cursor.execute(stmt)
    my_connection.commit()

def create_user(email, first_name, password):
    stmt = f'''
    INSERT into customers(email, first_name, customer_pass)
        values("{email}", "{first_name}", "{password}")
    '''
    db_cursor.execute(stmt)
    my_connection.commit()

def view_owned_products(email):
    own_list = []
    stmt = f'''
        SELECT DISTINCT product_name 
        FROM customer_products
        JOIN products ON products.product_id = customer_products.product_id
        WHERE customer_id = (SELECT customer_id FROM customers WHERE email = "{email}")
    '''
    db_cursor.execute(stmt)
    result_set = db_cursor.fetchall()
    for row in result_set:
        own_list.append(row[0])
    return own_list

def create_user_review(email, product, star_num):
    pass

def update_quantity():
    pass

def delete_user():
    pass

def get_product_by_price():
    pass

def get_review_by_pop():
    pass

def get_all_products():
    pass

print(view_owned_products("yoel@gmail.com"))

