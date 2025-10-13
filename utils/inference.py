import torch

def get_price_recommendation():
    # Load the dummy .pt model
    model = torch.load("rl_pricing.pt", map_location=torch.device("cpu"))
    model.eval()

    # Fake input data (e.g., market state, customer info)
    state = torch.tensor([[0.3, 0.6, 0.9]])  # dummy vector

    # Run inference
    with torch.no_grad():
        action = model(state).argmax().item()

    # Translate action into pricing tier
    return {
        "recommended_price_tier": action,
        "explanation": f"Action {action} chosen by RL model for given state input"
    }
