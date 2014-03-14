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


class EditService(object):
    u"""マージリクエスト編集サービス"""

    def __init__(self):
        from git_lab.apis.mergerequest.repositories import MergeRequestRepository
        from git_lab.apis.projects.repositories import ProjectsRepository

        self.request_repo = MergeRequestRepository()
        self.project_repo = ProjectsRepository()

    def create_request(self, destination, source, title):
        u"""マージリクエストを作成します
        @param destination : 宛先({namespace}/{project}:{branch})
        @type  destination : str

        @param source : 作成元ブランチ名
        @type  source : str | None

        @param title : タイトル
        @type  title : str | None
        """
        from git_lab.utils import get_current_branch

        dest_info = EditService.parse_dest_spec(destination.decode("utf-8") if destination is not None else None)
        target_project = self.project_repo.get_project(dest_info["dest_project"])
        target_project_id = target_project.get_id() if target_project is not None else None
        target_branch = dest_info["dest_branch"]

        source_branch = source.decode("utf-8") if source is not None else get_current_branch()
        title = title.decode("utf-8") if title is not None else source_branch

        print u"creating merge request [%s] %s ---> %s:%s" % (
            title, source_branch, target_project.get_name_with_namespace(), target_branch
        )

        if self.request_repo.create_requests(source_branch, target_project_id, target_branch, title):
            print "created"
        else:
            print "failed"

    @staticmethod
    def parse_dest_spec(dest):
        u"""宛先記述をパースする
        None -> このプロジェクトのmaster
        ":{branch}" -> このプロジェクトの{branch}
        "{namespace/project}:" -> {namespace/project}のmaster
        "{namespace/project}" -> {namespace/project}のmaster
        "{namespace/project}:{branch}" -> {namespace/project}の{branch}

        @type dest : str | None
        @rtype : dict
        """

        from git_lab.utils import get_project
        from string import replace

        if dest is None:
            return {
                "dest_project": get_project(),
                "dest_branch": "master"
            }

        elif ":" in dest:
            proj, br = dest.split(":", 2)

            project = replace(proj, u"/", u"%2F") if proj != "" else get_project()
            branch = br if br != "" else "master"

            return {
                "dest_project": project,
                "dest_branch": branch
            }

        elif ":" not in dest:
            return {
                "dest_project": replace(dest, u"/", u"%2F"),
                "dest_branch": "master"
            }

        else:
            project, branch = dest.split(":", 2)
            return {
                "dest_project": replace(project, u"/", u"%2F"),
                "dest_branch": branch
            }
