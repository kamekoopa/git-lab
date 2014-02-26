# -*- coding: utf-8 -*-
from gitlab import Gitlab


class GitlabClient(Gitlab):
    u"""元のクライアントが対応してないAPIに対応する用"""

    def __init__(self, host, token=u"", verify_ssl=True):
        super(GitlabClient, self).__init__(host, token, verify_ssl)

    def getmergerequestnotes(self, project_id, mergerequest_id):
        import requests
        import json

        url_str = '{0}/{1}/merge_requests/{2}/notes'.format(
            self.projects_url,
            project_id,
            mergerequest_id
        )

        request = requests.get(url_str, headers=self.headers, verify=self.verify_ssl)
        if request.status_code == 200:
            return json.loads(request.content.decode("utf-8"))
        else:
            return False


def get_client():
    u"""デフォルトのGitLabクライアントを取得する
    @rtype : GitlabClient
    """
    from config import get_or_rise

    return GitlabClient(
        get_or_rise("gitlab.host"),
        get_or_rise("gitlab.private-token")
    )


def get_project():
    u"""gitのconfigに設定されているプロジェクト名をAPIに利用できる形式で取得する"""
    from config import get_or_rise
    from string import replace

    project = get_or_rise("gitlab.project")

    return replace(project, u"/", u"%2F")
