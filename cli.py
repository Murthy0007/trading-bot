import argparse
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

def main():
    setup_logger()

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        # 🔹 Validate input
        validate_order(args.symbol, args.side, args.type, args.quantity, args.price)

        print("\n📊 Order Request Summary:")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        if args.price:
            print(f"Price: {args.price}")

        print("\n⏳ Placing order...")

        # 🔹 Place order
        order = place_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        # 🔹 FIXED SUCCESS / ERROR LOGIC
        if order and "error" not in order:
            print("\n✅ Order Successful!")
            print("Order ID:", order.get("orderId"))
            print("Status:", order.get("status"))
            print("Executed Qty:", order.get("executedQty"))
            print("Avg Price:", order.get("avgPrice"))
        else:
            print("\n❌ Order Failed!")
            if order and "error" in order:
                print("Error:", order["error"])

    except Exception as e:
        print("\n❌ Error:", str(e))


if __name__ == "__main__":
    main()