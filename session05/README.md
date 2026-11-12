# 第5回 Dockerによる開発環境構築

課題（1）は、自分のノートPCでDocker基礎演習を行い、指定の実行画面4点をまとめたレポート（PDF）と研究ノート（Markdown）を提出します。撮影する画面と演習手順は、[第5回講義資料の課題（1）](https://appears-infringement-duncan-meters.trycloudflare.com/open.knowledge/view/68?offset=0#task-1)で確認してください。

## 課題（1）の提出手順

第4回で使ったリポジトリと学生番号ブランチを使います。cloneやブランチ作成が必要な場合は、[第4回READMEの提出手順](../session04/README.md#提出手順)を見ながら各自で進めてください。

以下は学生番号が `4017` の例です。コマンドとURLにある `4017` を自分の学生番号に置き換えてください。

1. ノートPCのUbuntuで、第4回にcloneしたフォルダに移動し、自分のブランチを確認します。別の場所にcloneした場合は、実際のフォルダへ移動してください。

   ```bash
   cd ~/projects/seminor-repo
   git switch 4017
   git branch --show-current
   mkdir -p session05/4017
   ```

2. 作成した `session05/4017/` に、レポート `report.pdf` と研究ノート `notebook.md` を配置します。研究ノートが画像を相対パスで参照している場合は、その画像も同じ提出フォルダ内に配置してください。
3. 提出ファイルを登録し、`git status` で登録内容を確認してから、コミットしてpushします。

   ```bash
   git add session05/4017/
   git status
   git commit -m "第5回課題提出"
   git push -u origin 4017
   ```

4. GitHubで自分の提出フォルダを開き、PDFと研究ノートが表示されることを確認します。フォルダのURLをSlackのゼミナールチャンネルに投稿してください。2人目以降は、最初の提出メッセージのスレッドへ返信します。

   ```text
   https://github.com/chi-murakami-lab/seminor-repo/tree/4017/session05/4017
   ```
