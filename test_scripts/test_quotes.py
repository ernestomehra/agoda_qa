import requests
import random
from src.helpers.environment_vars import Environment as env
from src.helpers.utils import get_data
from src.data.payloads import payloads


class TestQuotesAPI:

    def test_quotes_happy_path_smoke(self):
        response = get_data(env.URL, payloads["params_generic"])
        assert response.status_code == 200, 'Request failed'
        assert response.json()["page"] == 1, 'Page results returned do not belong to page 1'

    def test_quotes_correct_headers_returned(self):
        response = get_data(env.URL, payloads["params_generic"])
        expected_keys = ['Server', 'Connection', 'X-Powered-By', 'Access-Control-Allow-Origin', 'Content-Type',
                         'Content-Length', 'Etag', 'Date', 'Via']
        result = []
        for key in response.headers.keys():
            if key in expected_keys:
                result.append(key)
        assert result == expected_keys, 'Returned headers do not match the expected headers.'

    def test_quotes_invalid_payload(self):
        # Error handling is not implemented, so for a blank page, it returns first page results so we will
        # validate that.
        params = {"page": False}
        response = requests.get(env.URL, params=params)
        assert response.status_code == 200
        json_object = response.json()
        assert json_object["page"] == 1

    def test_quotes_valid_paging(self):
        params = {"page": 1}
        response = requests.get(env.URL, params=params)
        json_object = response.json()
        total_pages = json_object["totalPages"]
        random_int = random.randint(1, total_pages)
        updated_params = {"page": random_int}
        response = requests.get(env.URL, params=updated_params)
        json_object = response.json()
        assert json_object["page"] == random_int, 'Pagination is broken'

    def test_quotes_result_counts_per_page(self):
        params = {"page": 1}
        response = requests.get(env.URL, params=params)
        json_object = response.json()
        assert json_object["count"] == len(json_object["results"]) == 20, 'Quote count is not equal to 20'

    def test_quotes_invalid_paging(self):
        pass

    def test_quotes_valid_tags(self):
        pass

    def test_quotes_invalid_tags(self):
        pass

    def test_quotes_and_tags(self):
        pass

    def test_quotes_or_tags(self):
        pass

    def test_quotes_or_and_tags(self):
        pass

    def test_quotes_tags_pages(self):
        pass

    def test_quotes_valid_author(self):
        pass

    def test_quotes_invalid_author(self):
        pass

    def test_quotes_author_tags(self):
        pass

    def test_quotes_author_and_tags(self):
        pass

    def test_quotes_author_or_tags(self):
        pass

    def test_quotes_pages_author(self):
        pass








