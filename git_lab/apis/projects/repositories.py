# -*- coding: utf-8 -*-
from git_lab.apis.projects.models import Project


class ProjectsRepository(object):

    def __init__(self, client=None, project=None):
        u"""
        @param client : GitLabクライアント
        @type  client : gitlab.Gitlab
        """
        from git_lab.utils import get_client, get_project

        self.client = client if client is not None else get_client()
        self.project = project if project is not None else get_project()

    def get_project(self, project_id=None):
        u"""プロジェクトIDでプロジェクト情報を取得する。

        @param project_id : 取得するプロジェクトのID、指定しない場合configに設定されているID
        @type  project_id : str | None
        """

        id_ = project_id if project_id is not None else self.project
        p = self.client.getproject(id_)

        if p is False:
            return None
        else:
            return Project(p)
