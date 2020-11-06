# bakery_management
Django Backend that supports the use case of Bakery Management

- Python Supported Version: 3.7.x

# API Documentation

API Documentation is done using drf-yasg.
Link: https://drf-yasg.readthedocs.io/en/stable/readme.html


# Database Schema

                     Entities
    _____________________|__________________________
    |           |            |           |           |
    User        Bakery      Product     Ingredient    ProductIngredient
        - owner fk(user)    - name      - name          - product fk(product)
        - name              - bakery    - bakery        - ingredient fk(ingredient)
        - address           - is_veg                    - quantity
                            - cost                      - percentage
                            - selling_price         unique (prodoct, ingredient)
                        unique(name, bakery)

# Supported Features

## Bakery Shop Admin Features
- Add Ingredients like Milk, Eggs etc
- Create Product from a list of ingredients
- Get the detail of Product (ingredients with quantity percentage, cost price, selling price etc)


## End User (Customer) Features
- Get a list of available products
