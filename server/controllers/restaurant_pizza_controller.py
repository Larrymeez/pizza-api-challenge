from flask import Blueprint, jsonify, request
from server.app import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    try:
        data = request.get_json()
        price = data['price']
        pizza_id = data['pizza_id']
        restaurant_id = data['restaurant_id']

        rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(rp)
        db.session.commit()

        return jsonify({
            "id": rp.id,
            "price": rp.price,
            "pizza_id": rp.pizza.id,
            "restaurant_id": rp.restaurant.id,
            "pizza": {
                "id": rp.pizza.id,
                "name": rp.pizza.name,
                "ingredients": rp.pizza.ingredients
            },
            "restaurant": {
                "id": rp.restaurant.id,
                "name": rp.restaurant.name,
                "address": rp.restaurant.address
            }
        }), 201

    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400
    except Exception:
        return jsonify({"errors": ["Invalid input or foreign keys not found"]}), 400
