Drop database grocery;

CREATE DATABASE IF NOT EXISTS grocery;
use grocery;

create table Product_categories
(
	category_id int primary key,
    category_name varchar(50) not null
);

create table Products
(
	product_id int primary key auto_increment,
    product_name varchar(50) Not NULL,
    product_quantity int NOT NULL,
    product_price float,
    category_id int,
    
    foreign key (category_id) references Product_categories(category_id)
);

create table Product_reviews
(
	product_review_id int primary key auto_increment,
    num_stars int not null,
    product_id int,
    
    foreign key (product_id) references Products(product_id)
);

create table customers
(
	customer_id int primary key auto_increment,
	email VARCHAR (50) NOT NULL,
	first_name VARCHAR (50) NOT NULL,
	password VARCHAR (50) NOT NULL,
    product_review_id int,
    
    foreign key (product_review_id) references Product_reviews(product_review_id)
);