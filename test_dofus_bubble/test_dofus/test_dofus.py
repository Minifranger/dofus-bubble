import json
import logging
import os
import unittest

from dofus_bubble.dofus.lambdas import LambdasDofus

logging.basicConfig(level=logging.INFO)


class TestDofus(unittest.TestCase):
    __event__ = {'headers': {'origin': 'http://localhost:3000'}, 'body': None, 'pathParameters': None,
                 'queryStringParameters': None}
    __context__ = None
    __mock__ = os.path.dirname(os.getcwd()) + '\mock\dofus\{mock}.json'

    def _test_response(self, result):
        body = json.loads(result.get('body'))
        self.assertIsInstance(result, dict)
        self.assertEqual(result.get('statusCode'), 200)
        [self.assertIsInstance(i, dict) for i in body]
        self.assertEqual(body, list({v['_id']: v for v in body}.values()))

    def test_scan_items_craft(self):
        result = LambdasDofus().scan_items_craft(self.__event__, self.__context__)
        self.assertIsInstance(result.get('body'), str)
        self._test_response(result)

    def test_scan_consumables_price(self):
        result = LambdasDofus().scan_consumables_price(self.__event__, self.__context__)
        self.assertIsInstance(result.get('body'), str)
        self._test_response(result)

    def test_scan_equipments_price(self):
        result = LambdasDofus().scan_equipments_price(self.__event__, self.__context__)
        self.assertIsInstance(result.get('body'), str)
        self._test_response(result)

    def test_scan_idols_price(self):
        result = LambdasDofus().scan_idols_price(self.__event__, self.__context__)
        self.assertIsInstance(result.get('body'), str)
        self._test_response(result)

    def test_scan_resources_price(self):
        result = LambdasDofus().scan_resources_price(self.__event__, self.__context__)
        self.assertIsInstance(result.get('body'), str)
        self._test_response(result)

    def test_scan_weapons_price(self):
        result = LambdasDofus().scan_weapons_price(self.__event__, self.__context__)
        self.assertIsInstance(result.get('body'), str)
        self._test_response(result)

    def test_scan_familiers_price(self):
        result = LambdasDofus().scan_familiers_price(self.__event__, self.__context__)
        self.assertIsInstance(result.get('body'), str)
        self._test_response(result)

    def test_scan_profession_craft(self):
        with open(self.__mock__.format(mock='scan_profession_craft'), "r") as mock:
            self.__event__['pathParameters'] = json.loads(mock.read()).get('pathParameters')
        result = LambdasDofus()._scan_profession_craft(self.__event__, self.__context__)


        # seen = []
        # for b in result:
        #     if b.get('_id') in seen:
        #         print(b.get('name'))
        #     else:
        #         seen.append(b.get('_id'))
        # print(len(result) - len(seen))

        self.assertIsInstance(result.get('body'), str)
        self._test_response(result)
