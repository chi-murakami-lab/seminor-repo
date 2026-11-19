# 第6回 Docker + GPU

課題（2）は、研究室のデスクトップPCでDockerfileを完成させ、GPUコンテナで `train.py` を実行する個人演習です。実施要件、`train.py`、Dockerfileのテンプレートは講義資料を参照してください。[講義資料の課題（2）](https://appears-infringement-duncan-meters.trycloudflare.com/open.knowledge/view/68?offset=0#task-2)

## 提出物

自分の学生番号ブランチの `session06/学生番号/` に、次の4ファイルをそろえます。

- `Dockerfile` と `train.py`
- レポート `report.pdf` と研究ノート `notebook.md`

レポートには次のスクリーンショット3点を載せてください。

1. ビルド後、学生番号を含むイメージ名が `sudo docker images` の一覧に表示されている画面。
2. `train.py` の実行結果に `CUDA Available: True`、GPU名、`tqdm` の進捗100%、`Training test completed successfully` が表示されている画面。
3. 削除後、課題で作成したコンテナとイメージが `sudo docker ps -a` と `sudo docker images` の一覧にないことを確認した画面。

## 課題（2）の提出手順

以下は学生番号が `4017` の例です。コマンドとURLにある `4017` を自分の学生番号に置き換えてください。cloneやブランチ作成の基本操作は、第4回READMEを参照してください。[第4回READMEの提出手順](../session04/README.md#提出手順)

1. 研究室のデスクトップPCで、講義資料に沿って `task2_gpu` の中にリポジトリをcloneし、自分の学生番号ブランチに切り替えます。`session06/4017/` に `Dockerfile` と `train.py` を用意し、そのフォルダでビルド、GPU実行、環境整理を行います。撮影を終えたら、同じフォルダから以下を実行します。

   ```bash
   cd ../..
   git branch --show-current
   git add session06/4017/Dockerfile session06/4017/train.py
   git status
   git commit -m "第6回プログラム提出：4017"
   git push -u origin 4017
   ```

2. ノートPCのUbuntuで、提出用リポジトリを開きます。第4回・第5回でclone済みの場合は同じフォルダを使ってください。研究室PCからpushしたプログラムを先に取得します。

   ```bash
   cd ~/projects/seminor-repo
   git fetch origin
   git switch 4017
   git pull --ff-only origin 4017
   ls session06/4017
   ```

3. `Dockerfile` と `train.py` があることを確認し、同じフォルダに `report.pdf` と `notebook.md` を置きます。研究ノートから参照する画像があれば、相対パスに合わせて提出フォルダ内に置いてください。

   ```bash
   git add session06/4017/
   git status
   git commit -m "第6回レポート・研究ノート提出：4017"
   git push -u origin 4017
   ```

4. GitHubで4ファイルがそろっていることを確認し、提出フォルダのURLをSlackのゼミナールチャンネルに投稿します。2人目以降は、最初の提出メッセージのスレッドへ返信してください。

   ```text
   https://github.com/chi-murakami-lab/seminor-repo/tree/4017/session06/4017
   ```
