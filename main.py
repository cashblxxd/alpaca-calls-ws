from alpaca.trading.client import TradingClient
from alpaca.trading.requests import LimitOrderRequest, MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from config import settings
import logging

logger = logging.getLogger(__name__)


client = TradingClient(settings.ALPACA_API_KEY, settings.ALPACA_API_SECRET, paper=True)

spy_stock_limit_buy_order = client.submit_order(
    order_data=MarketOrderRequest(
        symbol="SPY", 
        qty=100, 
        side=OrderSide.BUY, 
        time_in_force=TimeInForce.DAY
    )
)

spy_options_limit_sell_order = client.submit_order(
    order_data=LimitOrderRequest(
        symbol="SPY240705C00540000", 
        limit_price=4.11,
        qty=1, 
        side=OrderSide.SELL, 
        time_in_force=TimeInForce.DAY
    )
)

logger.info(f"Submitted SPY stock limit buy order: {spy_stock_limit_buy_order}")
logger.info(f"Submitted SPY options limit sell order: {spy_options_limit_sell_order}")
logger.info("Current trades:")
logger.info(client.get_all_positions())
