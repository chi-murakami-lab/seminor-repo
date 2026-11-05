# 第4回：GPUの利用

[講義資料：2026版_第4回＿GPUの利用](https://appears-infringement-duncan-meters.trycloudflare.com/open.knowledge/view/67)

## 課題

GPU環境を用いた動作確認を行い、記録・考察・参考文献を記載したレポート（PDF）と研究ノート（Markdown）を作成して提出する。

### 1. 環境情報の確認

- Ubuntu上で`nvidia-smi`を実行し、「Driver Version」「CUDA Version」「GPU名」が表示された画面をレポートに記載する。
- 仮想環境`zemi_04`を有効化した状態で`pip show torch`を実行し、torchのバージョンが表示された画面をレポートに記載する。

### 2. 計算速度の比較とSSDマウントの確認

- `GPU_benchmark.py`を実行し、GPU（`cuda`）とCPU（`cpu`）で同じサイズのランダムテンソル（例：10000×10000行列）を生成し、行列積などの演算の処理時間を計測・比較する。
- 外付けSSDのマウントを確認するコマンド（例：`df -h /mnt/d`）を実行する。ドライブ文字は接続したSSDに合わせる。
- SSDのマウント確認結果と、プログラムが出力した処理時間を、両方とも1つの画面に収めて撮影し、レポートに記載する。

### 3. 考察の記述

- CPUとGPUの計算速度の違いを、並列計算の仕組みと実行結果を踏まえて考察する。深層学習の学習・推論でGPUを使用する理由を説明する。
- 行列サイズを変えた検証（例：5000×5000、20000×20000行列）を行い、比較した考察を書いた場合は加点とする。
- 書籍等の参考文献を必ず1つ以上引用・記載する。Webサイトのみは不可。大学図書館の蔵書や『Pythonでつくる対話システム』『PyTorchで始める深層学習』などを参考にする。

## 提出するファイル

- `report.pdf`：動作確認の記録・指定されたスクリーンショット・考察・参考文献を記載したレポート。
- `notebook.md`：実施した操作・コマンド・実行結果・気付いたことを記録した研究ノート。

保存先は`session04/自分の学生番号/`とする。以下は学生番号4017の例である。

```text
session04/4017/
├── report.pdf
└── notebook.md
```

画像を研究ノートから参照する場合は、自分の学生番号フォルダ内に`images`フォルダを作って画像も提出し、`![実行結果](images/result.png)`のような相対パスで記載する。

## 提出手順

以下のコマンドはUbuntuのターミナルで実行する。**4017は自分の学生番号4桁に置き換える。先頭が0の場合は0も含める。**

第3回で行ったGitの名前・メールアドレスの設定、GitHubへのSSH鍵登録を済ませ、chi-murakami-labへの招待を承諾しておく。

### 1. リポジトリを取得する

まだこのリポジトリを取得していない場合：

```bash
mkdir -p ~/projects
cd ~/projects
git clone git@github.com:chi-murakami-lab/seminor-repo.git
cd seminor-repo
```

すでに`~/projects/seminor-repo`へ取得済みの場合は、cloneを繰り返さず、次で移動する。別の場所へ取得した人は、そのフォルダに移動する。

```bash
cd ~/projects/seminor-repo
```

### 2. 自分の学生番号ブランチに切り替える

このリポジトリに自分の学生番号ブランチをまだ作成していない場合：

```bash
git fetch origin
git switch main
git pull --ff-only origin main
git switch -c 4017
```

最後に`Switched to a new branch '4017'`と表示される。

すでにこのリポジトリに自分の学生番号ブランチを作成済みの場合は、上の4行の代わりに次を実行する。

```bash
git fetch origin
git switch 4017
git pull --ff-only origin 4017
```

現在のブランチを確認する。

```bash
git branch --show-current
```

自分の学生番号が表示されればよい。

```text
4017
```

### 3. 提出物を保存する

```bash
mkdir -p session04/4017
explorer.exe .
```

Windowsのエクスプローラーでリポジトリのフォルダが開く。`session04`→自分の学生番号の順に開き、作成した`report.pdf`と`notebook.md`をコピーする。

エクスプローラー上部の「表示」→「表示」→「ファイル名拡張子」をオンにし、名前を確認する。`report.pdf.pdf`や`notebook.md.txt`にしないこと。

Ubuntuに戻って確認する。

```bash
ls session04/4017
```

画像フォルダを追加していない場合の表示例：

```text
notebook.md  report.pdf
```

### 4. commitする

```bash
git add session04/4017/
git status
```

`Changes to be committed`に、自分の学生番号フォルダ内の提出ファイルだけが表示されていることを確認する。初回提出時の例：

```text
Changes to be committed:
  new file:   session04/4017/notebook.md
  new file:   session04/4017/report.pdf
```

表示の文言はGitの言語設定によって異なる。仮想環境`zemi_04`や他人のフォルダは追加しない。

```bash
git commit -m "第4回課題提出：4017"
```

### 5. GitHubへpushする

```bash
git push -u origin 4017
```

SSH鍵のパスフレーズを求められたら、第3回で設定したSSH鍵のパスフレーズを入力する。入力中の文字は表示されない。

新しいブランチのpushに成功した場合、出力に次の表示が含まれる。

```text
[new branch]      4017 -> 4017
```

### 6. GitHubで確認し、Slackへ提出する

次のURLの4017を自分の学生番号に置き換えて開く。

```text
https://github.com/chi-murakami-lab/seminor-repo/tree/4017/session04/4017
```

PDFとMarkdownをそれぞれ開き、内容と画像が表示されることを確認する。Slackのゼミナールチャンネルに次の形式で投稿する。2人目以降は、最初の提出メッセージのスレッドへ返信する。

```text
第4回課題を提出します。
学生番号：4017
氏名：○○ ○○
提出先：https://github.com/chi-murakami-lab/seminor-repo/tree/4017/session04/4017
```

SlackへのURL投稿で提出完了とする。Pull Requestの作成は不要。

## 提出後に修正する場合

提出に使用したUbuntuのリポジトリで実行する。

```bash
cd ~/projects/seminor-repo
git switch 4017
git pull --ff-only origin 4017
```

その後、同じ学生番号フォルダ内の提出物を修正し、次を実行する。

```bash
git add session04/4017/
git status
git commit -m "第4回課題修正：4017"
git push
```

GitHubで修正後の内容を確認し、Slackの自分の提出メッセージに返信して修正したことを知らせる。
