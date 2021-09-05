# coding: utf-8

"""
    Read-only API стриминга

    Получение ссылок на файловые ресурсы для стиминга  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import streaming_api
from streaming_api.api.file_location_api import FileLocationApi  # noqa: E501
from streaming_api.rest import ApiException


class TestFileLocationApi(unittest.TestCase):
    """FileLocationApi unit test stubs"""

    def setUp(self):
        self.api = FileLocationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_file_location_api_v1_add_file_location_post(self):
        """Test case for add_file_location_api_v1_add_file_location_post

        Добавление информации о местонахождении файла  # noqa: E501
        """
        pass

    def test_get_streaming_url_streaming_api_api_v1_get_streaming_url_post(self):
        """Test case for get_streaming_url_streaming_api_api_v1_get_streaming_url_post

        Добавление информации о местонахождении файла  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
