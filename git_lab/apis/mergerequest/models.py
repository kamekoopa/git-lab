# -*- coding: utf-8 -*-


class User(object):

    def __init__(self, user):
        u"""
        @param user : APIの戻り値のdict
        @type  user : dict
        """
        self.user = user

    def get_id(self):
        return self.id

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email()

    def get_name(self):
        return self.name

    def get_state(self):
        return self.state

    def get_created_at(self):
        return self.created_at

    def __getattr__(self, name):
        return self.user[name] if name in self.user else None


class MergeRequest(object):

    def __init__(self, mr):
        u"""
        @param mr : APIの戻り値のdict
        @type  mr : dict
        """
        self.mr = mr

    def get_id(self):
        return self.id

    def get_iid(self):
        return self.iid

    def get_target_branch(self):
        return self.target_branch

    def get_source_branch(self):
        return self.source_branch

    def get_project_id(self):
        return self.project_id

    def get_title(self):
        return self.title

    def get_state(self):
        return self.state

    def get_upvotes(self):
        return self.upvotes

    def get_downvotes(self):
        return self.downvotes

    def get_author(self):
        return User(self.author)

    def get_assignee(self):
        return User(self.assignee)

    def __getattr__(self, name):
        return self.mr[name] if name in self.mr else None


class Note(object):
    def __init__(self, note):
        u"""
        @param note : APIの戻り値のdict
        @type  note : dict
        """
        self.note = note

    def get_id(self):
        return self.id

    def get_body(self):
        return self.body

    def get_attachment(self):
        return self.attachment

    def get_author(self):
        return User(self.author)

    def get_created_at(self):
        return self.created_at

    def __getattr__(self, name):
        return self.note[name] if name in self.note else None
