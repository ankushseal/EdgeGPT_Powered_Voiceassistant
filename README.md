**README**

## Voice Assistant with Whisper, EdgeGPT, and Polly

This repository contains a Python script for creating a voice-activated chatbot using Whisper for speech recognition, EdgeGPT for natural language processing, and Amazon Polly for text-to-speech conversion.

### Prerequisites

Before running the script, ensure you have the following dependencies installed:

- `Python 3.x`
- `A Microsoft Account with access to https://bing.com/chat (Optional, depending on your region)`
- `whisper`
- `boto3`
- `pydub`
- `speech_recognition`
- `EdgeGPT (install as required)`

### Authentication
!!! POSSIBLY NOT REQUIRED ANYMORE !!!

In some regions, Microsoft has made the chat feature available to everyone, so you might be able to skip this step. You can check this with a browser (with user-agent set to reflect Edge), by trying to start a chat without logging in.

It was also found that it might depend on your IP address. For example, if you try to access the chat features from an IP that is known to belong to a datacenter range (vServers, root servers, VPN, common proxies, ...), you might be required to log in while being able to access the features just fine from your home IP address.

If you receive the following error, you can try providing a cookie and see if it works then:

Exception: Authentication failed. You have not been accepted into the beta.

Collect cookies
Get a browser that looks like Microsoft Edge.
a) (Easy) Install the latest version of Microsoft Edge
b) (Advanced) Alternatively, you can use any browser and set the user-agent to look like you're using Edge (e.g., Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.51). You can do this easily with an extension like "User-Agent Switcher and Manager" for Chrome and Firefox.
Open bing.com/chat
If you see a chat feature, you are good to continue...
Install the cookie editor extension for Chrome or Firefox
Go to bing.com
Open the extension
Click "Export" on the bottom right, then "Export as JSON" (This saves your cookies to clipboard)
Paste your cookies into a file bing_cookies_alternative.json.
NOTE: The cookies file name MUST follow the regex pattern bing_cookies_*.json, so that they could be recognized by internal cookie processing mechanisms

Reference : https://github.com/acheong08/EdgeGPT.git

You can install the dependencies via pip:

```bash
pip install whisper boto3 pydub SpeechRecognition EdgeGPT
```

### Configuration

Make sure to update the following information in the script:

- `config.json`: Provide your AWS credentials (AWS Access Key ID and AWS Secret Access Key).
- `bing_cookies_alternative.json` : Refer Authentication section

### Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/voice-chatbot.git
cd voice-chatbot
```

2. Update the `config.json` file with your AWS credentials.

3. Install EdgeGPT as required, and ensure it's accessible to the script.

4. Run the Python script `main.py`:

```bash
python main.py
```

### Description

This script creates a voice-activated chatbot that listens for a wake word ("Hi") and then listens for prompts from the user. It uses Whisper for speech recognition to transcribe user prompts, interacts with an EdgeGPT chatbot for generating responses, and utilizes Amazon Polly for converting text responses to speech.

### Input

- Voice input from the microphone.

### Output

- Text responses from the chatbot.
- Speech responses synthesized by Amazon Polly.

### Contributing

Contributions are welcome! If you have suggestions, feature requests, or bug fixes, please feel free to open an issue or create a pull request.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Acknowledgements

- [whisper](https://github.com/canelmas/whisper) - Python library for speech recognition.
- [boto3](https://github.com/boto/boto3) - AWS SDK for Python.
- [pydub](https://github.com/jiaaro/pydub) - Python library for audio processing.
- [SpeechRecognition](https://github.com/Uberi/speech_recognition) - Python library for speech recognition.
- EdgeGPT - Utilized for natural language processing (install as required).
