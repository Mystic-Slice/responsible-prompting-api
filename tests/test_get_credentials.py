import os

def test_get_credentials():
    required_vars = ["HF_TOKEN", "HF_URL"]
    for var in required_vars:
        if var not in os.environ:
            raise ValueError(f"Missing environment variable: {var}")
        # else:
        #     missing_hf_token_message = "Please add your HuggingFace token to .env file."
        #     assert os.environ["HF_TOKEN"] != "<include-token-here>", missing_hf_token_message
        #     check_hf_url_message = "Please check if the HuggingFace url is correct."
        #     assert os.environ["HF_URL"] == "https://api-inference.huggingface.co/pipeline/feature-extraction/", check_hf_url_message
 