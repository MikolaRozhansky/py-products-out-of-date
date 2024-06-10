import pytest
from unittest import mock
from app.main import outdated_products
import datetime


# @pytest.fixture()
# def mocked_date():
#     with mock.patch("datetime.date.today()") as mocked_date:
#         return 100


@mock.patch("app.main.datetime")
def test_out(mocked_date) -> None:

    mocked_date.today.return_value = datetime.date(2022, 2, 10)

    print("Inside test", datetime.datetime.today())
    assert outdated_products(
        [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 160
            }
        ]
    ) == ['duck']


def test_out_new() -> None:
    mocked_date = mock.Mock(wraps=datetime.datetime)
    mocked_date.today.return_value = datetime.date(2022, 2, 10)

    with mock.patch("datetime.datetime", new=mocked_date):
        print("Inside test", datetime.datetime.today())
        assert outdated_products(
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ]
        ) == ['duck']