alter table products
Add constraint fk_categories_products
foreign key (category_id) references categories(id)