# 第6回 Docker + GPU

課題（2）は、デスクトップPCでDockerfileを完成させ、追加ライブラリを含むGPU実行環境を構築します。完成したDockerfileの記述内容、GPU実行結果（GPU名・tqdmの進捗バー・完了表示）、コンテナとイメージの削除後の確認をまとめたレポート（PDF）と研究ノート（Markdown）を提出します。実施要件と撮影する画面は、[講義資料の課題（2）](https://appears-infringement-duncan-meters.trycloudflare.com/open.knowledge/view/68?offset=0#task-2)で確認してください。

デスクトップPCで作成したレポート・研究ノート・参照画像を、外付けSSDなどで自分のノートPCへコピーし、提出操作はノートPCのUbuntuで行ってください。

## 課題（2）の提出手順

第4回で使ったリポジトリと学生番号ブランチを使います。cloneやブランチ作成が必要な場合は、[第4回READMEの提出手順](../session04/README.md#提出手順)を見ながら各自で進めてください。

以下は学生番号が `4017` の例です。コマンドとURLにある `4017` を自分の学生番号に置き換えてください。

1. ノートPCのUbuntuで、第4回にcloneしたフォルダに移動し、自分のブランチを確認します。別の場所にcloneした場合は、実際のフォルダへ移動してください。

   ```bash
   cd ~/projects/seminor-repo
   git switch 4017
   git branch --show-current
   mkdir -p session06/4017
   ```

2. 作成した `session06/4017/` に、レポート `report.pdf` と研究ノート `notebook.md` を配置します。研究ノートが画像を相対パスで参照している場合は、その画像も同じ提出フォルダ内に配置してください。
3. 提出ファイルを登録し、`git status` で登録内容を確認してから、コミットしてpushします。

   ```bash
   git add session06/4017/
   git status
   git commit -m "第6回課題提出"
   git push -u origin 4017
   ```

4. GitHubで自分の提出フォルダを開き、PDFと研究ノートが表示されることを確認します。フォルダのURLをSlackのゼミナールチャンネルに投稿してください。2人目以降は、最初の提出メッセージのスレッドへ返信します。

   ```text
   https://github.com/chi-murakami-lab/seminor-repo/tree/4017/session06/4017
   ```
