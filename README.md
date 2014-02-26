# git-lab
gitlabにアクセスするためのgitのサブコマンド


## 設定
git configに下記の設定項目を追加する

```
# git config -l
gitlab.host=http://host.of.gitlab
gitlab.private-token=privatetoken
gitlab.project=namespace/project
```

## 使い方
詳しくはヘルプ

`git lab requests show {id}`
`git lab requests list`

