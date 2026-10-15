# File: tests/test_cat_facts.py
from unittest.mock import Mock
from lib.cat_facts import CatFacts

def test_provides_a_cat_fact_from_the_api():
    requester_mock = Mock(name="requester")
    response_mock = Mock(name="response")

    # requester.get(...) returns our fake response
    requester_mock.get.return_value = response_mock

    # response.json() returns sample API data
    response_mock.json.return_value = {
        "fact": "Cats sleep for around 13 to 16 hours a day.",
        "length": 43
    }

    cat_facts = CatFacts(requester_mock)
    result = cat_facts.provide()

    assert result == "Cat fact: Cats sleep for around 13 to 16 hours a day."

def test_calls_the_cat_fact_api():
    requester_mock = Mock(name="requester")
    response_mock = Mock(name="response")
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"fact": "anything", "length": 8}

    CatFacts(requester_mock).provide()

    requester_mock.get.assert_called_with("https://catfact.ninja/fact")