from skorecard.datasets import load_credit_card

try:
    data = load_credit_card(as_frame=True)
except Exception as e:
    print(f"Error loading credit card data: {e}")
    # Optionally load backup data or exit gracefully
    raise 