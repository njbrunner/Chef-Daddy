import pytest
import json
from pymongo import MongoClient
from http import HTTPStatus
""" Tests for the Recipe routes, utilities, and model """

@pytest.fixture(name="valid_recipe")
def fixture_valid_recipe():
    return {
        "name": "test",
        "description": "this is a test description",
        "ingredients": [{
            "name": "test ingredient",
            "quantity": 1,
            "measurement": "lb"
        }]
    }

def teardown():
    mongo_client = MongoClient('mongodb://localhost:27017')
    mongo_client.drop_database('test')


def test_create_recipe_success(test_client, valid_recipe):
    response = test_client.post(
        "/recipe/",
        json=valid_recipe
    )

    assert response.status_code == HTTPStatus.CREATED
    response_json = json.loads(response.data)
    assert response_json['Message'].lower() == "successfully created recipe"
