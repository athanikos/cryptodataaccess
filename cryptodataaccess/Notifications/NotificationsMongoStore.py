from datetime import datetime
from cryptomodel.coinmarket import prices
from cryptomodel.fixer import exchange_rates, Q
from cryptomodel.readonly import SymbolRates

from cryptodataaccess.Notifications.NotificationsStore import NotificationsStore
from cryptodataaccess.Rates.RatesStore import RatesStore
from cryptodataaccess.helpers import server_time_out_wrapper, do_connect, convert_to_int_timestamp

DATE_FORMAT = '%Y-%m-%d %H:%M:%S.%f'


class NotificationsMongoStore(NotificationsStore):

    def __init__(self, config, log_error):
        self.configuration = config
        self.log_error = log_error

    def fetch_unsent_notifications(self):
        symbols = {}
        latest_prices = self.fetch_latest_prices_to_date( convert_to_int_timestamp(datetime.today()))
        for coin in latest_prices[0].coins:
            symbols.update({coin.symbol: coin.name})
        return symbols

    def update_to_sent(self):
        dt_now = convert_to_int_timestamp(datetime.today())
        return self.fetch_symbol_rates_for_date(dt_now)

