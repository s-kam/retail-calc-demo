
async def test_calc_view(app_client):
    response = await app_client.get('/', params={'1': 2})
    assert response.status == 200
