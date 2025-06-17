from flask import Blueprint, request, jsonify
from server.app import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def add_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    errors = []
    if price is None or not (1 <= price <= 30):
        errors.append('Price must be between 1 and 30.')
    if not pizza_id:
        errors.append('pizza_id is required.')
    if not restaurant_id:
        errors.append('restaurant_id is required.')

    if errors:
        return jsonify({'errors': errors}), 400

    rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(rp)
    db.session.commit()

    pizza = Pizza.query.get(pizza_id)
    return jsonify({'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients}), 201
