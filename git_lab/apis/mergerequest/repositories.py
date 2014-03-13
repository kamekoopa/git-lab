# -*- coding: utf-8 -*-
from git_lab.apis.mergerequest.models import MergeRequest, Note


class MergeRequestRepository(object):

    def __init__(self, client=None, project=None):
        u"""
        @param client : GitLabクライアント
        @type  client : gitlab.Gitlab
        """
        from git_lab.utils import get_client, get_project

        self.client = client if client is not None else get_client()
        self.project = project if project is not None else get_project()

    def get_request(self, req_id):

        mr = self.client.getmergerequest(self.project, req_id)

        if mr is False:
            return None
        else:
            return MergeRequest(mr)

    def get_notes(self, req_id):
        u"""指定されたマージリクエストIDに紐づくノートの一覧を取得します

        @param req_id : マージリクエストID
        @type  req_id : int

        @return : ノートのリスト
        @rtype  : list of Note
        """

        notes = self.client.getmergerequestnotes(self.project, req_id)

        if notes is False:
            return []
        else:
            results = []
            for note in notes:
                results.append(Note(note))

            return results

    def get_requests(self, page=1, per_page=20):
        u"""
        @param page : ページ数
        @type  page : int

        @param per_page : ページ当たりの取得数
        @type  per_page : int

        @return : マージリクエストのリスト
        @rtype  : list of MergeRequest
        """

        mrs = self.client.getmergerequests(self.project, page=page, per_page=per_page)

        if mrs is False:
            return []
        else:
            result = []
            for mr in mrs:
                result.append(MergeRequest(mr))
            return result

    def create_requests(self, source_branch, target_project_id, target_branch, title):
        u"""
        @param source_branch : 送り元ブランチ
        @type  source_branch : str

        @param target_project_id : 送り先プロジェクト
        @type  target_project_id : str | None

        @param target_branch : 送り先ブランチ
        @type  target_branch : str

        @param title : タイトル
        @type  title : str

        @return : 成否
        @rtype : bool
        """

        return self.client.createmergerequest2(
            self.project,
            source_branch,
            target_project_id,
            target_branch,
            title
        )
