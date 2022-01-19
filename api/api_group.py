from api.base_api import BaseApi


class Grouping(BaseApi):
    def get_list(self, num):
        data = {
            "method": "get",
            "url": "http://123.56.138.96:3012/api/ainews-user/company-group/user-custom-group",
            "headers": self.header,
            "params": {'page': num, 'per_page': '10', 'start_time': '2021-12-30', 'end_time': '2022-01-13'}
        }
        return self.send(data)

    # todo 快讯
    def new_more(self):
        data = {
            "method": "post",
            "url": "http://123.56.138.96:3012/api/ainews-espy/api/opinion/flash-news",
            "json": {"start_time": "2022-01-04T16:51:49", "end_time": "2022-01-11T16:51:49", "page": 1, "pagesize": 20},
            "headers": self.header
        }
        return self.send(data)

    # todo 添加分组
    def add_group(self, name):
        data = {"method": "post",
                "url": "http://123.56.138.96:3012/api/ainews-user/company-group/create",
                "json": {"name": name},
                "headers": self.header
                }
        return self.send(data)

    # todo 添加公司
    def add_company(self, id):
        data = {"method": "post",
                "url": "http://123.56.138.96:3012/api/ainews-user/company-group/company-create",
                "json": {"company_code": "000001", "group_id": id},
                "headers": self.header
                }
        return self.send(data)

    # todo 删除分组
    def del1_group(self, id):
        data = {"method": "get",
                "url": "http://123.56.138.96:3012/api/ainews-user/company-group/delete",
                "params": {'id': id},
                "headers": self.header
                }
        return self.send(data)

    # todo 舆情第一个标题

    def liebiao(self):
        data = {"method": "post",
                "url": "http://123.56.138.96:3012/api/ainews-espy/api/company/article",
                "params": {"cp_code": ["undefined"], "id": "biaoti_id"},
                "headers": self.header
                }
        self.send(data)
