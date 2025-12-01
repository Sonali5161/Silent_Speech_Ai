def predict_text(frames):
    # Simulated lip reading output
    common_words = ["hello my name is sonali i need help"
    ""]
    return common_words[len(frames) % len(common_words)]
 