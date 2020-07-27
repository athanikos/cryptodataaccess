import mock
from bson import ObjectId
from cryptomodel.coinmarket import  prices
from cryptodataaccess.config import configure_app
from cryptodataaccess.TransactionRepository import TransactionRepository
import pytest
from cryptodataaccess.helpers import do_connect


@pytest.fixture(scope='module')
def mock_log():
    with mock.patch("cryptodataaccess.helpers.log_error"
                    ) as _mock:
        _mock.return_value = True
        yield _mock


def test_eval_collection():
    config = configure_app()
    do_connect(config)
    actual_count = prices.objects()
    j = "prices"
    assert(len(eval(j).objects()),actual_count)


