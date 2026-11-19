# 研究ノート

## 基本情報

- 氏名：上野朱香
- 学籍番号：4018
- 日付：2026.11.19
- 記録開始：11：30
- 記録終了：12：00
- 作業時間：30分

---

## 本日の目標

- NVIDIA Container Toolkitを利用し、Dockerコンテナ内部からホストPCのGPUを認識できるように設定し、PyTorchによる計算を行う。

---

## 実施内容

### 09:00 - 10:30

内容：NVIDIA Container Toolkitをインストールし、PythonファイルとDockerfileを作成したうえで、GPU付きでDockerイメージを作成し、実行する。

得られた結果：自作したPythonファイルとDockerfileをもとに、GPUを使用したDockerイメージを作成、実行することができた。

問題点：ターミナル上でdockerイメージを作成しようとした際に、途中でビルドが止まってしまう問題が発生した。

---

### 10:30 - 12:00

内容：上記の演習をもとに、Dockerfileを完成させ、GPU実行環境を構築して、簡易的なニューラルネットワークの学習テストを実行する。

得られた結果：自作したDockerfileによりGPU実行環境を構築することができた。

問題点：特になし

---

## GitHub作業履歴

### Commit

- 特になし

### Pull Request

- 特になし

---

## 調査・学習内容

- 特になし

---

## 発生した問題

### 問題1

現象：`sudo docker build -t mygpu .`を実行しようとした際に、途中でビルドが止まってしまう。

再現条件：

原因（推測可）：

対応：`sudo apt-get update && sudo apt-get install -y docker-buildx-plugin`コマンドを用いて、buildkitをインストールする。

結果：`sudo DOCKER_BUILDKIT=1 docker build --progress=plain -t mygpu .`により、ビルド状況が可視化され、ビルドが進むことを確認した。

---

## 打ち合わせ記録

特になし

---

## 気付き・考察

特になし

---

## 明日の予定

優先度高
1.paizaラーニングでPythonを学ぶ

---

## 指導教員への質問

特になし

---

## 自己評価

達成度：100%

理由：NVIDIA Container Toolkitを利用して、Dockerコンテナ内部からホストPCのGPUを認識できるように設定し、PyTorchによる計算を実現できたため。

今後の改善点：特になし

---