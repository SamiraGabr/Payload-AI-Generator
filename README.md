# `AI-Assisted Payload Generator and Walkthrough`

## Overview

This project provides a command-line interface (CLI) tool that leverages AI models (Gemini or GPT-4) to generate various penetration testing payloads and walkthroughs. It's designed to assist security professionals and red team operators in quickly obtaining relevant and obfuscated payloads for different platforms and vulnerabilities.

The project consists of two main components:

  * A **C-based front-end** that handles user interaction, collects parameters like platform, AI model, payload type, language, and obfuscation level, and then constructs a command to execute the Python backend.
  * A **Python-based backend (`ai_helper.py`)** that communicates with the selected AI model (Gemini or OpenAI's GPT-4) to generate the requested payloads or vulnerability walkthroughs, and then saves the output to a file.

---
## Demo
---


## Features
---

  * **Platform Selection**: Generate payloads for Windows, Linux, macOS, or Web Applications.
  * **AI Model Choice**: Utilize either **Google's Gemini** or **OpenAI's GPT-4** for content generation.
  * **Payload Variety (OS)**: Supports a wide range of OS-specific payloads, including Reverse Shell, Keylogger, Privilege Escalation, and more.
  * **Web Vulnerability Exploitation**: Provides detailed walkthroughs or multiple payloads for various web vulnerabilities like SQL Injection, XSS, SSRF, and many others.
  * **Language Specificity**: Generate OS payloads in Bash, Python, or C.
  * **Obfuscation**: Request payloads with varying levels of obfuscation (None, Basic, Advanced) and WAF bypass techniques.
  * **Output Management**: Automatically saves generated content to a timestamped file within `OutPuts/OS` or `OutPuts/Web` directories, with an option for custom filenames.
  * **User-Friendly Interface**: Simple menu-driven interaction for selecting options.


## Project Structure
---

```
.
├── payloads-gen.c      # C source code for the command-line interface
├── ai_helper.py        # Python backend for AI interaction and payload generation
├── config.json         # Configuration file for API keys (create this manually)
├── requirements.txt    # Python dependencies
├── OutPuts/            # Directory for all generated outputs
│   ├── OS/             # Outputs for OS-specific payloads
│   └── Web/            # Outputs for Web Application vulnerabilities
├── venv/               # Python virtual environment (should be ignored by Git)
├── .gitignore          # Recommended: include 'venv/' and 'OutPuts/' here
└── README.md           # This file
```


## Getting Started
---


### Prerequisites

  * **C Compiler**: You need a C compiler (like GCC) to compile the C front-end.

    ```bash
    sudo apt install build-essential # For Debian/Ubuntu
    # Or for macOS with Homebrew:
    brew install gcc
    ```

  * **Python 3**: Ensure you have Python 3 installed.

    ```bash
    python3 --version
    ```

  * **API Keys**: Obtain API keys for your chosen AI model(s) and store them in a `config.json` file in the project root.

    **`config.json` example:**

    ```json
    {
      "Gemini_api_key": "YOUR_GEMINI_API_KEY",
      "OpenAI_api_key": "YOUR_OPENAI_API_KEY"
    }
    ```
    https://platform.openai.com/
    ![Screenshot1](https://github.com/user-attachments/assets/8bd87280-29c5-4288-9c66-fae331546967)

    https://ai.google.dev/gemini-api/
    ![Screenshot2](https://github.com/user-attachments/assets/fe288733-ddb2-46ce-bc97-36d0e89f215f)
    

### Installation
---


1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Samira-Gabr/Payload-AI-Generator.git
    cd Payload-AI-Generator
    ```
2.  **Compile the C front-end:**
    ```bash
    gcc payloads-gen.c -o ai_pentest_tool
    ```
    
### Virtual Environment Setup (Recommended)

It's highly recommended to use a virtual environment (`venv`) for Python projects to manage dependencies and avoid conflicts with other Python projects on your system.

1.  **Create a virtual environment:**
    Navigate to your project's root directory (where `ai_helper.py` and `requirements.txt` are located) and run:

    ```bash
    python3 -m venv venv
    ```

    This will create a new directory named `venv` in your project folder, containing the isolated Python environment.

2.  **Activate the virtual environment:**

      * **On Linux/macOS:**
        ```bash
        source venv/bin/activate
        ```
      * **On Windows (Command Prompt):**
        ```bash
        venv\Scripts\activate.bat
        ```
      * **On Windows (PowerShell):**
        ```powershell
        .\venv\Scripts\Activate.ps1
        ```

    You'll notice `(venv)` appearing at the beginning of your terminal prompt, indicating that the virtual environment is active.

3.  **Install Python Libraries:**
    With the virtual environment activated, install the necessary Python packages using `pip` and the provided `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

    *To deactivate the virtual environment when you're done working:*

    ```bash
    deactivate
    ```

## Usage
---


1.  **Run the compiled C executable:**

    ```bash
    ./ai_pentest_tool
    ```

    (Ensure your virtual environment is activated if you've installed Python dependencies within it.)

2.  **Follow the on-screen prompts** to select your desired options. The C program will guide you through the choices for platform, AI model, payload type/web vulnerability, language, obfuscation, and mode.

### Example Interactions

#### 1\. Generating a Reverse Shell for Linux

```
Select the platform:
1) Windows
2) Linux
3) macOS
4) Web Application
> 2
Select AI model please;>
1) Gemini
2) GPT-4 (OpenAI)
> 1
Select Payload type:
1) Reverse Shell
2) Bind Shell
...
12) Anti-VM Detection
> 1
Select programming language for the payload:
1) Bash
2) Python
3) C
> 1
Select obfuscation level:
1) None
2) Basic
3) Advanced
> 2
⏳ Waiting for response /
```

The output will be saved to a file like `OutPuts/OS/output_gemini_Linux_Reverse_Shell_Bash_Basic_YYYYMMDD_HHMMSS.txt`.

#### 2\. Getting a Web Vulnerability Walkthrough for SQL Injection

```
Select the platform:
1) Windows
2) Linux
3) macOS
4) Web Application
> 4
Select AI model please;>
1) Gemini
2) GPT-4 (OpenAI)
> 2
Select web vulnerability to target:
1) SQL Injection
2) Cross-Site Scripting (XSS)
...
31) Insecure Direct Object References (IDOR)
> 1
Select obfuscation level:
1) None
2) Basic
3) Advanced
> 1
Do you want:
1) Step-by-Step walkthrough
2) Payloads? Hit the number that you need >>
> 1
⏳ Waiting for response |
```

The output will be saved to a file like `OutPuts/Web/output_gpt_WebApp_SQL_Injection_None_YYYYMMDD_HHMMSS.txt`.

#### 3\. Generating Multiple Obfuscated XSS Payloads

```
Select the platform:
1) Windows
2) Linux
3) macOS
4) Web Application
> 4
Select AI model please;>
1) Gemini
2) GPT-4 (OpenAI)
> 1
Select web vulnerability to target:
1) SQL Injection
2) Cross-Site Scripting (XSS)
...
31) Insecure Direct Object References (IDOR)
> 2
Select obfuscation level:
1) None
2) Basic
3) Advanced
> 3
Do you want:
1) Step-by-Step walkthrough
2) Payloads? Hit the number that you need >>
> 5  # Requesting 5 payloads
⏳ Waiting for response -
```

The output will be saved to a file like `OutPuts/Web/output_gemini_WebApp_Cross-Site_Scripting_(XSS)_Advanced_YYYYMMDD_HHMMSS.txt` and will contain 5 original XSS payloads, 5 obfuscated versions, and 5 WAF bypass versions.

