# DALL-E 3 requires version 1.0.0 or later of the openai-python library.
import os
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI
import json

# You will need to set these environment variables or edit the following values.
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "https://ai-#########.cognitiveservices.azure.com/")
api_version = os.getenv("OPENAI_API_VERSION", "2024-04-01-preview")
deployment = os.getenv("DEPLOYMENT_NAME", "dall-e-3")

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    azure_ad_token_provider=token_provider
)

result = client.images.generate(
    model=deployment,
    prompt="""i want a cleanner image.
i want a image put the letters SAIA with the label "small ai applications".
need to have microcontrollers and cameras.
The image need to pass the feeling for security, for video survaliance.
pls use a style for web applications """,
    n=1,
    style="natural",
    quality="standard"
)

image_url = json.loads(result.model_dump_json())['data'][0]['url']
print(image_url)