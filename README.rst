git-lab
=======
gitlabにアクセスするためのgitのサブコマンド

Requirements
------------
Python 2.7

Installation
------------
``$ pip install git-lab``

Configuration
-------------
git configに下記の設定項目を追加する

::

  # git config -l
  gitlab.host=http://host.of.gitlab
  gitlab.private-token=privatetoken
  gitlab.project=namespace/project


Usage
-----
詳しくはヘルプ

::

   $ git lab requests show {id}
   $ git lab requests list


Changes
-------

- 0.2
    - add feature of create merge request
- 0.1
    - initial release
    - show and list merge request(s)
