from fastapi import APIRouter, Response
from typing import Optional
from models.ResponseModel import ResponseModel
from common.res import response_data


class ServiceRouter:
    def __new__(cls):
        instance = super(ServiceRouter, cls).__new__(cls)
        instance.description = {}
        instance.summary = {}
        instance.router = APIRouter()
        instance.path = None
        instance.res = response_data
        instance.routerInit = True
        instance.methods = ["get", "post", "put", "delete"]
        return instance

    def __init__(self):
        self.description = {}
        self.summary = {}
        self.router = APIRouter()
        self.path = None
        self.res = response_data
        self.routerInit = True
        self.methods = ["get", "post", "put", "delete"]

    def set_path(self, path: str):
        """
        设置路由路径。
        :param path: 路由路径
        """
        self.path = path

    def set_desc(
        self,
        method: str = "get",
        summary: str = None,
        description: str = None,
    ):
        """
        设置指定方法的描述或摘要。
        :param method: HTTP 方法
        :param summary: 要设置的摘要
        :param description: 要设置的描述
        :param routerInit: 是否重新初始化路由
        """
        if summary is not None:
            current_summary = self.summary
            current_summary[method] = summary
            self.summary = current_summary

        if description is not None:
            current_description = self.description
            current_description[method] = description
            self.description = current_description

    def get(self):
        return Response(content="1")

    def post(self):
        return Response(content="1")

    def delete(self):
        return Response(content="1")

    def put(self):
        return Response(content="1")

    def setup_routes(self):
        for method in self.methods:
            if self.is_method_overridden(method):
                self.router.add_api_route(
                    path=self.path,
                    response_model=ResponseModel,
                    endpoint=getattr(self, method),
                    description=self.description.get(method),
                    summary=self.summary.get(method),
                    methods=[method.upper()],
                )

    def is_method_overridden(self, method_name: str) -> bool:
        current_method = getattr(self, method_name)
        parent_method = getattr(super(self.__class__, self), method_name, None)
        return current_method != parent_method
