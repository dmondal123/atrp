from langchain_anthropic import ChatAnthropic
from validation.credentials import set_credentials

# Set credentials
ChatAnthropic.api_key = set_credentials()

# Initialize the Claude model (replace model name with the latest available if needed)
model = ChatAnthropic(model_name="claude-3-5-sonnet-20240620", max_tokens=8192)
