from marshmallow import Schema
from marshmallow.fields import Integer, String
from pytest import raises

from retail_calc_demo.app import AppConfigValidationError, create_app
from retail_calc_demo.constant import DISCOUNTS_SETTING_LABEL, \
    TAX_RATES_SETTING_LABEL
from .conftest import INVALID_DECIMAL_VALUE_MESSAGE, \
    INVALID_VALUE_MESSAGE, REQUIRED_FIELD_MISSING_MESSAGE


def test_app_creation(app):
    # Check application instance creation without errors.
    pass


def test_wrong_app_settings_validation():
    def check_settings_validation(settings, err_messages):
        with raises(AppConfigValidationError) as err:
            create_app(settings)

        assert err.value.messages == err_messages

    check_settings_validation(
        {},
        {
            DISCOUNTS_SETTING_LABEL: [REQUIRED_FIELD_MISSING_MESSAGE],
            TAX_RATES_SETTING_LABEL: [REQUIRED_FIELD_MISSING_MESSAGE],
        },
    )

    check_settings_validation(
        [],
        {
            '_schema': [Schema._default_error_messages['type']],
        },
    )

    check_settings_validation(
        {
            DISCOUNTS_SETTING_LABEL: {'one': '10%', -1: 120},
            TAX_RATES_SETTING_LABEL: {0.45: 'NA'},
        },
        {
            DISCOUNTS_SETTING_LABEL: {
                'one': {
                    'key': [Integer.default_error_messages['invalid']],
                    'value': [INVALID_DECIMAL_VALUE_MESSAGE],
                },
                -1: {
                    'key': [INVALID_VALUE_MESSAGE],
                    'value': [INVALID_VALUE_MESSAGE]
                }
            },
            TAX_RATES_SETTING_LABEL: {
                0.45: {
                    'key': [String.default_error_messages['invalid']],
                    'value': [INVALID_DECIMAL_VALUE_MESSAGE],
                },
            },
        },
    )
