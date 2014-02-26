# -*- coding: utf-8 -*-


class NoConfigurationException(Exception):
    pass


class Fetcher(object):
    u"""git configから設定を取得するAPI"""

    def get(self, section_name, name):
        u"""
        @param section_name : 設定のセクション名
        @type  section_name : str

        @param name : 設定名
        @type  name : str

        @return : 設定値。見つからなければNone
        @rtype  : str | None
        """

        raise NotImplementedError()


class FetcherImpl(Fetcher):
    u"""実装"""

    def __init__(self):
        super(FetcherImpl, self).__init__()

    def get(self, section_name, name):
        from subprocess import check_output
        from subprocess import CalledProcessError

        try:
            out = check_output(["git", "config", "%s.%s" % (section_name, name)])
        except CalledProcessError:
            out = None

        return out


class Section(object):
    u"""git configのセクション階層"""

    def __init__(self, section_name, fetcher):
        u"""
        @param section_name : このセクションのセクション名
        @type  section_name : str

        @param fetcher : 設定を取得するためのオブジェクト
        @type  fetcher : Fetcher
        """

        self.section_name = section_name
        self.fetcher = fetcher

    def __getattr__(self, name):
        u"""
        @param name : 設定名
        @type  name : str

        @return : 設定値。見つからなければNone
        @rtype  : unicode | None
        """

        value = self.fetcher.get(self.section_name, name)
        if value is not None:
            return value.decode("utf-8").strip()
        else:
            return None


class Config(object):
    u"""git configのルート階層"""

    def __init__(self, fetcher=FetcherImpl()):
        u"""
        @param fetcher : 設定を取得するためのオブジェクト
        @type  fetcher : Fetcher
        """
        self.fetcher = fetcher

    def __getattr__(self, name):
        return Section(name, self.fetcher)

    def get(self, key):
        u"""フルキー名で取得します
        @param key : フルキー名(e.g user.name)
        @type  key : str

        @return : 設定値。なければNone
        @rtype  : unicode | None
        """
        keys = key.split(".", 2)
        return self.__getattr__(keys[0]).__getattr__(keys[1])

config = Config()


def get_or_else(key, default, cfg=config):
    u"""gitの設定から設定値を取得します

    @param key : フルキー名
    @type  key : str

    @param default : 設定値がなかった場合のデフォルト値
    @type  default : unicode

    @return : 設定値、無ければデフォルト値
    @rtype  : unicode
    """

    value = cfg.get(key)
    if value is None:
        return default
    else:
        return value


def get_or_rise(key, cfg=config):
    u"""gitの設定から設定値を取得します。取得出来なかった場合は例外をスローします

    @param key : フルキー名
    @type  key : str

    @return : 設定値、無ければデフォルト値
    @rtype  : unicode

    @raises NoConfigurationException : 設定値が存在しなかった場合
    """

    value = cfg.get(key)
    if value is None:
        raise NoConfigurationException("%s is not defined in the config of git" % key)
    else:
        return value