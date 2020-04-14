# python lecture

## 環境
1. このリポジトリをclone
2. ローカルで、cloneしたディレクトリに移動
3. `docker-compose up -d`
4. `./exec.sh src/main.py`して、`hello python!`と出力されればおk

./exec.shでpermission errorが出たら、`chmod u+x exec.sh install.sh test.sh`してください

## 実行
### pythonファイルの実行
`./exec.sh filePath [opt...]`

### テストの実行
`./test.sh list|dict|loop|map`