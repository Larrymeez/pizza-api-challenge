from server.app import create_app, db
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    pizza1 = Pizza(name='Margherita', ingredients='Tomato, Mozzarella, Basil')
    pizza2 = Pizza(name='Pepperoni', ingredients='Tomato, Mozzarella, Pepperoni')

    restaurant1 = Restaurant(name='Pizza Palace', address='123 Main Street')
    restaurant2 = Restaurant(name='Slice House', address='456 Market Street')

    db.session.add_all([pizza1, pizza2, restaurant1, restaurant2])
    db.session.commit()

    rp1 = RestaurantPizza(price=10, pizza_id=pizza1.id, restaurant_id=restaurant1.id)
    rp2 = RestaurantPizza(price=12, pizza_id=pizza2.id, restaurant_id=restaurant2.id)

    db.session.add_all([rp1, rp2])
    db.session.commit()
