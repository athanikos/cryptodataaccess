from datetime import datetime
from jsonpickle import encode, decode
import json
import mock
from bson import ObjectId
from cryptomodel.coinmarket import prices
from cryptomodel.cryptomodel import user_transaction, exchange_rates
import json
from cryptodataaccess.Rates.RatesMongoStore import RatesMongoStore
from cryptodataaccess.Rates.RatesRepository import RatesRepository
from cryptodataaccess.config import configure_app
import pytest
from cryptodataaccess.helpers import do_local_connect, convert_to_int_timestamp
from cryptodataaccess.tests.helpers import insert_prices_record, insert_exchange_record, insert_prices_record_with_method, \
    get_prices20200812039_record, get_prices20200801T2139_record
import jsonpickle
from cryptomodel.coinmarket import prices, EUR, EURQuote
DATE_FORMAT = '%Y-%m-%d %H:%M:%S.%f'


@pytest.fixture(scope='module')
def mock_log():
    with mock.patch("cryptodataaccess.helpers.log_error"
                    ) as _mock:
        _mock.return_value = True
        yield _mock


def test_fetch_symbol_rates_for_date_pass_str_or_dt():
    config = configure_app()
    do_local_connect(config)
    user_transaction.objects.all().delete()
    exchange_rates.objects.all().delete()
    prices.objects.all().delete()
    insert_prices_record()
    insert_exchange_record()
    config = configure_app()
    store = RatesMongoStore(config, mock_log)
    rates_repo = RatesRepository(store)
    do_local_connect(config)
    rates_repo.fetch_symbol_rates_for_date(convert_to_int_timestamp(datetime.today()))
    dt = datetime(year=2040, month=1, day=1)
    rates_repo.fetch_symbol_rates_for_date(convert_to_int_timestamp(dt))
    assert (len(prices.objects) == 1)


def test_fetch_symbol_rates_for_dat_with_two_entries_within_two_hours():
    config = configure_app()
    users_store = RatesMongoStore(config, mock_log)
    rates_repo = RatesRepository(users_store)
    do_local_connect(config)
    dt_now = convert_to_int_timestamp(datetime.today())
    user_transaction.objects.all().delete()
    prices.objects.all().delete()
    insert_exchange_record()
    insert_prices_record_with_method(get_prices20200812039_record)
    insert_prices_record_with_method(get_prices20200801T2139_record)
    rts = rates_repo.fetch_symbol_rates_for_date(convert_to_int_timestamp(datetime.today()))
    dt = datetime(year=2020, month=8, day=1, hour=21, minute=0) #1596304800
    print(dt.timestamp())


def test_delete_symbol_rates():
    config = configure_app()
    users_store = RatesMongoStore(config, mock_log)
    rates_repo = RatesRepository(users_store)
    do_local_connect(config)
    prices.objects.all().delete()
    new_price = prices()
    new_price.source_id = ObjectId('666f6f2d6261722d71757578')
    rates_repo.insert_prices(new_price)
    dt = convert_to_int_timestamp(datetime(year=2025, month=7, day=3))
    theprices =  prices.objects.all()
    assert (len(    prices.objects) == 1 )
    rates_repo.delete_prices(new_price.source_id)
    theprices2 =  rates_repo.fetch_latest_prices_to_date(convert_to_int_timestamp(datetime.today()))
    assert (len(    prices.objects) == 0 )



import jsonpickle
import jsonpickle.tags as tags
import jsonpickle.unpickler as unpickler
import jsonpickle.util as util


def test_jsonpickle_decode2():
    from pathlib import Path
    txt = Path("cryptodataaccess/tests/sample_records/from_kafka.json").read_text()
    dct =    jsonpickle.decode(txt)
    dct[tags.OBJECT] = util.importable_name(prices)
    dct['name'] = 'prices'

    obj = unpickler.Unpickler().restore(dct, classes=prices)
    assert isinstance(obj, prices)
    assert obj.name == 'prices'

