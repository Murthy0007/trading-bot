from bot.client import get_client
import logging
import time

def place_order(symbol, side, order_type, quantity, price=None):
    client = get_client()

    try:
        # 🔹 MARKET ORDER
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        # 🔹 LIMIT ORDER
        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logging.info(f"Order placed: {order}")
        return order

    except Exception as e:
        error_msg = str(e)
        logging.error(f"Error placing order: {error_msg}")

        # 🔹 Simulated response
        simulated_order = {
            "orderId": int(time.time()),
            "status": "FAILED (Simulated)",
            "executedQty": "0",
            "avgPrice": "0",
            "error": error_msg
        }

        return simulated_order