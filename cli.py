import argparse
import logging
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_inputs
from bot.logging_config import setup_logger

def main():

    setup_logger()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_inputs(args.symbol, args.side, args.type, args.quantity, args.price)

        client = get_client()

        order = place_order(
            client=client,
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\n=== ORDER SUCCESS ===")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Qty: {order.get('executedQty')}")
        print(f"Avg Price: {order.get('avgPrice', 'N/A')}")

    except Exception as e:
        print("\n=== ORDER FAILED ===")
        print(str(e))
        logging.error(str(e))


if __name__ == "__main__":
    main()