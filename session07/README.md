# 第7回：Dockerを用いた環境構築

[講義資料：2026版_第7回（URLを記載）]()

## 課題

Dockerを用いてUbuntu＋GPU環境を構築し、SLP（Simultaneously-collected multimodal Lying Pose）データセットをコンテナ内から参照できる状態にする。構築した環境ファイルおよび動作確認の記録を研究ノート（Markdown）にまとめて提出する。

### 1. 作業ディレクトリとコードの準備

- 研究室リポジトリ内に自分の学生番号フォルダを作成し、`SLP-Dataset-and-Code` を配置する。
- サブモジュール扱いにならないよう、`SLP-Dataset-and-Code` 内の `.git` フォルダを削除する。

### 2. `Dockerfile` と `.gitignore` の作成

- Ubuntu 22.04 と CUDA をベースとした `Dockerfile` を作成する（使用するGPUに応じてCUDAバージョンを選択する）。
- データセットや学習済みモデル（重みファイル）が誤ってGitHubへプッシュされないよう、`.gitignore` を設定する。

### 3. 外付けSSDのマウントとコンテナの起動確認

- 外付けSSDに保管されたSLPデータセットをWSL2（Ubuntu）から認識させる。
- Dockerイメージをビルドし、作業ディレクトリとSLPデータセットをマウントしてコンテナを起動する。
- コンテナ内でUbuntu・Pythonのバージョン、GPU認識（`torch.cuda.is_available()`）、およびデータセットのマウント（`ls /workspace/SLP-Dataset-and-Code/SLP`）を確認し、実行結果（またはスクリーンショット）を研究ノートに記録する。

## 作業手順

以下のコマンドは、作業用PCのWSL2（Ubuntu）ターミナルで実行する。**`4017` は自分の学生番号4桁に置き換える。**

### 1. リポジトリの取得とブランチの切り替え

まだリポジトリを取得していない場合：

```bash
mkdir -p ~/projects
cd ~/projects
git clone git@github.com:chi-murakami-lab/seminor-repo.git
cd seminor-repo
```

すでに取得済みの場合は、リポジトリのフォルダへ移動する。

```bash
cd ~/projects/seminor-repo
```

自分の学生番号ブランチに切り替える（未作成の場合は `git switch -c 4017` で作成する）。

```bash
git fetch origin
git switch 4017
git pull --ff-only origin 4017
```

現在のブランチを確認し、自分の学生番号が表示されることを確認する。

```bash
git branch --show-current
```

作業ディレクトリを作成して移動する。

```bash
mkdir -p session07/4017
cd session07/4017
```

### 2. 参考リポジトリのコード配置

`SLP-Dataset-and-Code` をクローンする。

```bash
git clone https://github.com/ostadabbas/SLP-Dataset-and-Code.git
```

研究室リポジトリのサブモジュール扱いにならないよう、クローンしたフォルダ内の `.git` ディレクトリを削除する。

```bash
rm -rf SLP-Dataset-and-Code/.git
```

### 3. Ubuntuベースの `Dockerfile` の作成

`session07/4017/Dockerfile` を新規作成する（例：`nano Dockerfile`）。

#### 標準環境（CUDA 11.8）の場合

```dockerfile
# 1. ベースイメージにGPU対応の Ubuntu 22.04 を指定
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

# 対話プロンプトの抑制とタイムゾーン設定
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo

# 2. Ubuntuのパッケージ更新と Python3 / pip / 必要ツールのインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-dev \
    git \
    wget \
    curl \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# python コマンドで python3 が起動するようにシンボリックリンクを作成
RUN ln -sf /usr/bin/python3 /usr/bin/python

# pip自体のアップグレード
RUN pip3 install --no-cache-dir --upgrade \
    pip \
    setuptools \
    wheel

# 3. 作業ディレクトリの設定
WORKDIR /workspace

# 4. PyTorch（CUDA 11.8対応版）および SLPコードに必要なPythonパッケージのインストール
RUN pip3 install --no-cache-dir \
    torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

RUN pip3 install --no-cache-dir \
    numpy==1.23.5 \
    scipy \
    matplotlib \
    opencv-python-headless \
    scikit-image \
    yacs \
    tensorboardX \
    tqdm \
    Pillow \
    configargparse \
    dominate \
    jsonpatch \
    plotly

# コンテナ起動時のデフォルトシェル
CMD ["/bin/bash"]
```

#### RTX 5060 Ti など新しいGPUでPyTorchの互換性問題が発生する場合（CUDA 12.8）

```dockerfile
FROM nvidia/cuda:12.8.1-cudnn-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-dev \
    git \
    wget \
    curl \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

RUN ln -sf /usr/bin/python3 /usr/bin/python

RUN pip3 install --no-cache-dir --upgrade \
    pip setuptools wheel

WORKDIR /workspace

RUN pip3 install --no-cache-dir \
    torch torchvision torchaudio \
    --index-url https://download.pytorch.org/whl/cu128

RUN pip3 install --no-cache-dir \
    numpy==1.23.5 \
    scipy \
    matplotlib \
    opencv-python-headless \
    scikit-image \
    yacs \
    tensorboardX \
    tqdm \
    Pillow \
    configargparse \
    dominate \
    jsonpatch \
    plotly

CMD ["/bin/bash"]
```

### 4. `.gitignore` の作成・修正

巨大なデータセットや学習済みモデルを誤ってGitHubへプッシュしないよう、`session07/4017/.gitignore` を作成（または修正）して以下を記述する（隠しファイルは `ls -a` で確認できる）。

```text
# データセット・ログ・重みファイル
data/
dataset/
SLP/
output/
log/
*.pth
*.tar
*.zip

# Pythonキャッシュ
__pycache__/
*.py[cod]
```

### 5. 外付けSSDからのデータセット利用準備

容量が大きいSLPデータセットは外付けSSDに保管し、利用時のみDockerコンテナにマウントする。

1. **Windows側でドライブ文字とフォルダ構成を確認する**
   外付けSSDを接続し、エクスプローラーでドライブ文字（例：`D:` や `H:`）と、`SLP` フォルダ内の構成を確認する。

```text
D:\SLP\                        # （マウント後のコンテナ内パス：/workspace/SLP-Dataset-and-Code/SLP/）
├── danaLab/                   # 実験室環境（102名分）
│   ├── 00001/
│   │   ├── RGB/               # RGB画像（uncover, cover1, cover2）
│   │   ├── depth/             # 深度画像
│   │   ├── IR/                # 赤外線画像
│   │   ├── PM/                # 体圧分布データ
│   │   └── joints_gt_RGB.mat  # 関節座標の正解ラベル
│   └── ...
└── simLab/                    # 病院環境（7名分）
```

2. **WSL2（Ubuntu）から外付けSSDをマウントする**
   まず `ls /mnt/d` が成功するか確認する。表示されない場合は手動でマウントする（ドライブ文字が `H:` の場合は `d` を `h`、`D:` を `H:` に置き換える）。

```bash
sudo mkdir -p /mnt/d
sudo mount -t drvfs D: /mnt/d
```

3. **マウントを確認する**
   `ls /mnt/d` を実行し、`SLP` フォルダが表示されれば成功。

### 6. Dockerイメージのビルドとコンテナの起動

`session07/4017/` 内でDockerイメージをビルドする。他の学生とイメージ名が衝突しないよう、タグに自分の学生番号を付ける。

```bash
docker build -t slp-session07:4017 .
```

※ `Dockerfile` を修正して再ビルドする場合は `--no-cache` を付ける。

```bash
docker build --no-cache -t slp-session07:4017 .
```

カレントディレクトリを `/workspace` に、外付けSSD内の `SLP` フォルダを `/workspace/SLP-Dataset-and-Code/SLP` にマウントしてコンテナを起動する（ドライブ文字 `/mnt/d` は接続したSSDに合わせる）。

- **GPU搭載PCの場合：**

```bash
docker run --gpus all -it --rm --shm-size=8g \
  -v $(pwd):/workspace \
  -v /mnt/d/SLP:/workspace/SLP-Dataset-and-Code/SLP \
  slp-session07:4017
```

- **CPU環境（GPU非搭載PC）の場合：**（`--gpus all` を外す）

```bash
docker run -it --rm --shm-size=8g \
  -v $(pwd):/workspace \
  -v /mnt/d/SLP:/workspace/SLP-Dataset-and-Code/SLP \
  slp-session07:4017
```

コンテナ起動後、環境とデータセットのマウントを確認する。

```bash
# Ubuntu・PythonのバージョンとGPU認識の確認
cat /etc/os-release | grep PRETTY_NAME
python --version
python -c "import torch; print('CUDA available:', torch.cuda.is_available())"

# データセットのマウント確認（danaLab, simLab が表示されれば成功）
ls /workspace/SLP-Dataset-and-Code/SLP
```

確認が完了したら `exit` でコンテナを終了する。

## 提出するファイル

保存先は `session07/自分の学生番号/` とする。以下は学生番号 `4017` の例である。

```text
session07/4017/
├── Dockerfile               # Ubuntuベースの環境構築ファイル
├── .gitignore               # データセットや重みファイルの除外設定
├── notebook.md              # 環境構築の手順・コマンド・動作確認結果・気付いたことを記録した研究ノート
└── SLP-Dataset-and-Code/    # 使用したPythonコード群（※.gitやデータセット・重みファイルは含めない）
```

画像を研究ノートから参照する場合は、自分の学生番号フォルダ内に `images` フォルダを作って画像も提出し、`![実行結果](images/result.png)` のような相対パスで記載する。

## 提出手順

以下のコマンドは、Ubuntuのターミナルでリポジトリのルートディレクトリ（`~/projects/seminor-repo`）に移動して実行する。**`4017` は自分の学生番号4桁に置き換える。**

### 1. ブランチと変更ファイルを確認する

```bash
cd ~/projects/seminor-repo
git branch --show-current
git status
```

自分の学生番号ブランチにいること、およびデータセット（`SLP/`）や巨大なファイルが含まれていないことを必ず確認する。

### 2. commitする

```bash
git add session07/4017/
git status
```

`Changes to be committed` に、自分の学生番号フォルダ内の提出ファイルだけが表示されていることを確認する。

```bash
git commit -m "第7回課題提出：4017"
```

### 3. GitHubへpushする

```bash
git push -u origin 4017
```

### 4. GitHubで確認し、Slackへ提出する

次のURLの `4017` を自分の学生番号に置き換えて開く。

```text
https://github.com/chi-murakami-lab/seminor-repo/tree/4017/session07/4017
```

各ファイルや画像が正しく表示されることを確認し、Slackのゼミナールチャンネルに次の形式で投稿する。2人目以降は、最初の提出メッセージのスレッドへ返信する。

```text
第7回課題を提出します。
学生番号：4017
氏名：○○ ○○
提出先：https://github.com/chi-murakami-lab/seminor-repo/tree/4017/session07/4017
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
git add session07/4017/
git status
git commit -m "第7回課題修正：4017"
git push
```

GitHubで修正後の内容を確認し、Slackの自分の提出メッセージに返信して修正したことを知らせる。
