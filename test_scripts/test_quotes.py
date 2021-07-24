import random
from src.helpers.environment_vars import Environment as env
from src.helpers.utils import get_data, get_json_data
from src.data.payloads import payloads


class TestQuotesAPI:
    """
    Test class to implement test suite for the getQuotes API: tests following params:
    - author
    - tags
    - page number
    - quote counts
    """

    def test_quotes_happy_path_smoke(self):
        response = get_data(env.URL, payloads["params_generic"])
        assert response.status_code == 200, 'Request failed'
        assert get_json_data(response, "page") == 1, 'Page results returned do not belong to page 1'

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

        response = get_data(env.URL, payloads["params_generic"])
        assert response.status_code == 200
        assert get_json_data(response, "page") == 1, 'Page results returned do not belong to page 1'

    def test_quotes_valid_paging(self):
        response = get_data(env.URL, payloads["params_generic"])
        total_pages = get_json_data(response, "totalPages")  # Assumption: The total pages count will keep changing.
        random_int = random.randint(1, total_pages)
        updated_params = {"page": random_int}
        response = get_data(env.URL, updated_params)
        assert get_json_data(response, "page") == random_int, 'Pagination is broken'

    def test_quotes_result_counts_per_page(self):
        response = get_data(env.URL, payloads["params_generic"])
        assert get_json_data(response, "count") == len(get_json_data(response, "results")) == 20, \
            'Quote count is not equal to 20'

    def test_quotes_or_tags(self):
        response = get_data(env.URL, payloads["params_tags_or"])
        assert get_json_data(response, "totalCount") == 1348, 'Count not equal to the expected result of quotes, 13'

    def test_quotes_invalid_tags(self):
        response = get_data(env.URL, payloads["invalid_tags"])
        assert get_json_data(response, "totalCount") == 0, 'Results are being returned for an invalid tag'

    def test_quotes_and_tags(self):
        response = get_data(env.URL, payloads["and_tags"])
        assert get_json_data(response, "totalCount") == 4, 'Count not equal to the expected result of quotes, 4'

    def test_quotes_or_and_tags(self):
        response = get_data(env.URL, payloads["and_or_tags"])
        assert get_json_data(response, "totalCount") == 5, 'Count not equal to the expected result of quotes, 5'

    def test_quotes_tags_pages(self):
        response = get_data(env.URL, payloads["tags_pages"])
        assert get_json_data(response, "page") == 3, 'Page number does not match'
        assert get_json_data(response, "totalCount") == 1348, 'The total count does not match'

    def test_quotes_valid_author(self):
        response = get_data(env.URL, payloads["valid_author"])
        assert get_json_data(response, "totalCount") == 30, 'Count for author tested does not match'

    def test_quotes_invalid_author(self):
        response = get_data(env.URL, payloads["invalid_author"])
        assert get_json_data(response, "totalCount") == 0, 'Quotes exist for invalid author'

    def test_quotes_author_tags(self):
        response = get_data(env.URL, payloads["authors_tags"])
        assert get_json_data(response, "totalCount") == 75, 'Count does not match for author and tag'

    def test_quotes_pages_author(self):
        response = get_data(env.URL, payloads["pages_author"])
        assert get_json_data(response, "page") == 3, 'Page 3 of author not selected'








