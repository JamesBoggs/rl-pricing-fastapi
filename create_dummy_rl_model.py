# Save this to create_dummy_rl_model.py and run it
import torch.nn as nn
import torch

class DummyRLModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(3, 3)  # 3 inputs → 3 price tiers

    def forward(self, x):
        return self.linear(x)

model = DummyRLModel()
torch.save(model, "rl_pricing.pt")
