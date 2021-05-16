from functools import partial

from retail_calc_demo.constant import GET_PARAMS_ERROR_MESSAGE, \
    PRICE_GET_PARAM_LABEL, QUANTITY_GET_PARAM_LABEL, STATE_CODE_GET_PARAM_LABEL, \
    UNKNOWN_STATE_CODE_GET_PARAM_ERROR_MESSAGE
from .conftest import INVALID_DECIMAL_VALUE_MESSAGE, \
    INVALID_VALUE_MESSAGE, REQUIRED_FIELD_MISSING_MESSAGE


async def test_calc_view(app_client):
    get = partial(app_client.get, '/calc')

    # Check params validation.
    async def check_params(params, error_messages):
        response = await get(params=params)
        assert response.status == 400
        assert await response.json() == {
            'identity': GET_PARAMS_ERROR_MESSAGE,
            'data': error_messages,
        }

    await check_params(
        None,
        {
            PRICE_GET_PARAM_LABEL: [REQUIRED_FIELD_MISSING_MESSAGE],
            QUANTITY_GET_PARAM_LABEL: [REQUIRED_FIELD_MISSING_MESSAGE],
            STATE_CODE_GET_PARAM_LABEL: [REQUIRED_FIELD_MISSING_MESSAGE],
        }
    )

    await check_params(
        {
            PRICE_GET_PARAM_LABEL: 'one',
            QUANTITY_GET_PARAM_LABEL: -1,
            # Empty state code may be presented in config file.
            STATE_CODE_GET_PARAM_LABEL: '',
        },
        {
            PRICE_GET_PARAM_LABEL: [INVALID_DECIMAL_VALUE_MESSAGE],
            QUANTITY_GET_PARAM_LABEL: [INVALID_VALUE_MESSAGE],
        }
    )

    await check_params(
        {
            PRICE_GET_PARAM_LABEL: 1,
            QUANTITY_GET_PARAM_LABEL: 1,
            STATE_CODE_GET_PARAM_LABEL: '',
        },
        # Empty state code is not presented in config file.
        [
            UNKNOWN_STATE_CODE_GET_PARAM_ERROR_MESSAGE
        ],
    )

    # Check request with valid params.
    response = await get(
        params={
            PRICE_GET_PARAM_LABEL: 0.3,
            QUANTITY_GET_PARAM_LABEL: 10,
            STATE_CODE_GET_PARAM_LABEL: 'UT',
        }
    )
    assert response.status == 200
    assert await response.json() == {
        'subtotal_with_discount': 3.0,
        'total': 3.2055,
    }


async def test_state_codes_view(app_client):
    response = await app_client.get('/state_codes')
    assert response.status == 200
    assert sorted(await response.json()) == ['AL', 'CA', 'NV', 'TX', 'UT']
