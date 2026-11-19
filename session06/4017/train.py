import torch
import torch.nn as nn
from tqdm import tqdm

# 1. GPU動作確認
print("=== GPU Check ===")
print("CUDA Available:", torch.cuda.is_available())

if torch.cuda.is_available():
   print("Device Name   :", torch.cuda.get_device_name(0))
   device = torch.device("cuda")
else:
   print("CUDA is not available. Running on CPU.")
   device = torch.device("cpu")

# 2. 簡易モデルの学習テスト
print("\n=== PyTorch Training Test ===")
model = nn.Sequential(
   nn.Linear(10, 32),
   nn.ReLU(),
   nn.Linear(32, 2)
).to(device)

x = torch.randn(64, 10, device=device)

for epoch in tqdm(range(5), desc="Training"):
   output = model(x)

print(f"Output Tensor Device: {output.device}")
print("Training test completed successfully")
