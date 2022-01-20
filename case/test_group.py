import jmespath
import pytest
from loguru import logger

from api.api_group import Grouping


class TestGrouping:
    def setup_class(self):
        self.group = Grouping()

    @pytest.mark.smoke
    @pytest.mark.parametrize("a,check", [(1, 200)], ids=["ONE"])
    def test_get_list(self, a, check):
        r = self.group.get_list(a)
        assert r.status_code == check

    @pytest.mark.parametrize("a,check", [("晓狗", 200), ("tay", 200), ("123", 200)], ids=["chin", "english", "int"])
    def test_add_group(self, a, check):
        r = self.group.add_group(a)
        assert r.status_code == check

    @pytest.mark.parametrize("a,check", [["[?name=='晓狗'].id", 200]])
    def test_add_company(self, a, check):
        r = self.group.get_list(1)
        id = jmespath.search(a, r.json())
        res = self.group.add_company(id)
        assert res.status_code == check

    #
    @pytest.mark.parametrize("a,check", [
        ("[?name=='晓狗'].id", 200),
        ("[?name=='123'].id", 200),
        ("[?name=='tay'].id", 200),
    ], ids=["汉字", "english", "int"])
    def test_del1_group(self, a, check):
        r = self.group.get_list(1)
        id = jmespath.search(a, r.json())
        res = self.group.del1_group(id)
        assert res.status_code == 123

    @pytest.mark.smoke
    def test_all_group(self):
        self.group.add_group("张晓狗")
        r = self.group.get_list(1)
        id = jmespath.search("[?name=='张晓狗'].id", r.json())
        logger.info(id)
        self.group.add_company(id)
        r = self.group.del1_group(id)
        assert r.json() == True




