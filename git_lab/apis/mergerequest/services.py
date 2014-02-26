# -*- coding: utf-8 -*-


class ReferService(object):
    u"""マージリクエスト参照サービス"""

    def __init__(self):
        from git_lab.apis.mergerequest.repositories import MergeRequestRepository
        self.repo = MergeRequestRepository()

    def show_merge_request(self, req_id):
        u"""指定IDのマージリクエストを表示します

        @param req_id : マージリクエストのID
        @type  req_id : int
        """
        assert isinstance(req_id, int)

        mr = self.repo.get_request(req_id)
        if mr is not None:
            merge_request = u"""
[ {state} ] #{iid} {title}
--------------------------------------------------------------------------------
merge request id  : {id}

author            : {author}
assignee          : {assignee}
opened at         : {opened_at}

upvotes/downbotes : +{up} / -{down}

[ merge to ] : {target} <----- [ merge from ] {source}
--------------------------------------------------------------------------------""".format(
                state=mr.get_state(),
                iid=mr.get_iid(),
                title=mr.get_title(),
                id=mr.get_id(),
                author=mr.get_author().get_name(),
                assignee=mr.get_assignee().get_name(),
                opened_at=mr.get_author().get_created_at(),
                up=mr.get_upvotes(),
                down=mr.get_downvotes(),
                target=mr.get_target_branch(),
                source=mr.get_source_branch(),
            )

            print merge_request

            notes = self.repo.get_notes(req_id)
            for note in notes:
                n = u"""
    {author} posted at {posted_at}
    ----------------------------------------------------------------------------
    {body}""".format(
                    author=note.get_author().get_name(),
                    posted_at=note.get_created_at(),
                    body=note.get_body()
                )

                print n

    def list_merge_request(self, page, count):
        u"""指定条件でマージリクエストの一覧を取得して表示します

        @param page : 表示するページ番号
        @type  page : int

        @param page : ページあたりに表示する件数
        @type  page : int
        """
        assert isinstance(page, int)
        assert isinstance(count, int)

        mrs = self.repo.get_requests(page, count)
        if len(mrs) != 0:
            header = u"""
 id       mid      state    author     title
+--------+--------+--------+----------+----------------------------------------+"""
            print header

        for mr in mrs:

            m = u" #{id: <7} #{mid: <7} {state: ^8} {author: ^10} {title: <40}".format(
                id=mr.get_iid(),
                mid=mr.get_id(),
                state=mr.get_state(),
                author=mr.get_author().get_name(),
                title=mr.get_title(),
            )

            print m
