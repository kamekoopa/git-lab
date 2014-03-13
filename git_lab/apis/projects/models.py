# -*- coding: utf-8 -*-


class Owner(object):

    def __init__(self, owner):
        u"""
        @param owner : APIの戻り値のdict
        @type  owner : dict
        """
        self.owner = owner

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_created_at(self):
        return self.created_at

    def __getattr__(self, name):
        return self.owner[name] if name in self.owner else None


class Namespace(object):

    def __init__(self, namespace):
        u"""
        @param namespace : APIの戻り値のdict
        @type  namespace : dict
        """
        self.namespace = namespace

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_owner_id(self):
        return self.owner_id

    def get_path(self):
        return self.path

    def get_created_at(self):
        return self.created_at

    def get_updated_at(self):
        return self.updated_at

    def __getattr__(self, name):
        return self.namespace[name] if name in self.namespace else None


class Project(object):

    def __init__(self, project):
        u"""
        @param project : APIの戻り値のdict
        @type  project : dict
        """
        self.project = project

    def get_id(self):
        return self.id

    def get_description(self):
        return self.description

    def get_default_branch(self):
        return self.default_branch

    def is_public(self):
        return self.public

    def get_visibility_level(self):
        return self.visibility_level

    def get_ssh_url_to_repo(self):
        return self.ssh_url_to_repo

    def get_http_url_to_repo(self):
        return self.http_url_to_repo

    def get_web_url(self):
        return self.web_url

    def get_owner(self):
        return Owner(self.owner)

    def get_name(self):
        return self.name

    def get_name_with_namespace(self):
        return self.name_with_namespace

    def get_path(self):
        return self.path

    def get_path_with_namespace(self):
        return self.path_with_namespace

    def is_issues_enabled(self):
        return self.issues_enabled

    def is_merge_requests_enabled(self):
        return self.merge_requests_enabled

    def is_wall_enabled(self):
        return self.wall_enabled

    def is_wiki_enabled(self):
        return self.wiki_enabled

    def is_snippets_enabled(self):
        return self.snippets_enabled

    def get_last_activity_at(self):
        return self.last_activity_at

    def get_namespace(self):
        return Namespace(self.namespace)

    def __getattr__(self, name):
        return self.project[name] if name in self.project else None
