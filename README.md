# Text-to-Speech 

Text-to-Speech is a Python application that harnesses the capabilities of AI4BHARAT models to seamlessly convert written text into lifelike voice, enabling a wide range of applications including voice assistants, audiobooks, and accessibility features. With this project, you can effortlessly generate spoken content from text, enhancing user experiences and opening up possibilities for various voice-related applications.


## Features

- **State-of-the-Art Models:** Harness the power of AI4BHARAT's cutting-edge pre-trained models for precise and efficient text-to-speech conversion.

- **User-Friendly Python Script:** An easy-to-use Python script that simplifies the process of making API calls and acquiring text-to-speech transcriptions.

- **Audio Format Flexibility:** Support for a variety of audio formats, allowing you to choose the format that best suits your needs.

- **Customization Options:** Tailor API requests to adapt to specific use cases, offering flexibility and control over the generated voice output.

- **Comprehensive Documentation:** Detailed documentation that provides clear and thorough guidance, ensuring a quick and smooth start with the text-to-speech conversion process.

## Table of Contents
- [Python](#python)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Python  
### Installation

To get started with text-to-voice, follow these installation steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/text-to-voice.git
   cd text-to-voice
   ```

2. Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

To run the text-to-voice application and make a POST request via the terminal, follow these steps:

1. Open your terminal or command prompt.

2. Navigate to the project directory:

   ```bash
   cd path/to/text-to-voice
   ```

3. Start the Flask application by running the Python script:
    ```bash
   python python_script.py
   ```
   The app will start running with the host set to '127.0.0.1' and port set to 5000.

4. Open another terminal window or tab.

5. Use curl to make a POST request to your Flask API endpoint with the specified parameters:

   ```bash
   curl -X POST -F "service_id=your_service_id" -F "src_lang_code=your_language_code" -F "input_text=your_text" http://localhost:5000/tts
   ```
    Replace the following placeholders:
    - your_service_id with the appropriate service ID.
    - your_language_code with the desired language code.
    - your_text with the text you want to convert to speech.
6. Press Enter to make the POST request.

This will send a POST request to your Flask API via the terminal, including the specified parameters and audio file. Your Flask server should process the request and return the transcript.

If you encounter any issues, please ensure that your Flask server is running on http://localhost:5000, and that you've followed the steps correctly.

### Configuration

Before using text-to-voice, you need to configure the API credentials. Follow these steps:

1. Sign up or log in to your AI4BHARAT account.

2. Generate API credentials, such as an API key or token, from your AI4BHARAT dashboard.

3. Open the config.json file located in the project directory.

4. Replace the placeholder values in config.json with your API credentials:
   ```json
   {
       "api_key": "your_api_key_here",
       "api_url": "https://api.ai4bharat.org/asr/v0.2/recognize"
   }
   ```

   Replace `"your_api_key_here"` with your actual API key/token.

4. Save the `config.json` file.


### Contributing

We welcome contributions to improve text-to-voice. To contribute, follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature/your-feature
   ```

3. Make your changes, test thoroughly, and ensure proper documentation.

4. Commit your changes with clear and concise messages.

5. Push your changes to your fork:

   ```bash
   git push origin feature/your-feature
   ```

6. Create a pull request to the main repository's `master` branch, describing your changes and their purpose.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE. See the [LICENSE](LICENSE) file for details.