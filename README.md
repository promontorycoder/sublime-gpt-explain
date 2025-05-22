# 🧠 GPT Explain for Sublime Text

**GPT Explain** is a right-click AI assistant for Sublime Text that lets you instantly generate natural language explanations for selected code using OpenAI’s GPT models.

It supports any programming language — Python, JavaScript, JSON, Go, C#, Bash, and more — and automatically tailors its response based on your file type.

---

## ✨ Features

- 🔍 Right-click to “Explain Code with GPT”
- 🧠 Language-aware prompts (auto-detects from syntax)
- 🪄 Uses GPT-4o via your OpenAI API key
- 💬 Shows explanations in a new Sublime tab
- ⚙️ Command palette support (optional)
- 🖥️ Also prints logs to the Sublime Console (for debug)

---

## 🚀 How to Install

### Manual Installation

1. Clone or download this repo:
   ```bash
   git clone https://github.com/promontorycoder/sublime-gpt-explain.git
   ```

2. Move or symlink the folder to your Sublime `Packages/` directory:
   ```
   ~/.config/sublime-text/Packages/GPTExplain/
   ```

3. Restart Sublime Text

---

## 🛠️ Setup

### 1. Create an OpenAI API Key

- Go to: [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
- Click “Create new secret key”
- Copy the key

### 2. Save your key in a Python file:

Create a file named `gpt_api_key.py` somewhere outside your plugin directory (e.g., in a secure `~/secrets/` folder):

```python
OPEN_AI_KEY = "sk-..."  # your actual API key here
```

Then make sure your plugin points to that file using this in `gpt_explain.py`:

```python
key_module_path = "/full/path/to/gpt_api_key.py"
```

> 🔐 This key should not be uploaded or shared. Keep it private!

---

## 🖱️ How to Use

### ✅ Option 1: Right-Click Menu

1. Select any block of code
2. Right-click → **🧠 Explain Code with GPT**

### ✅ Option 2: Command Palette

Press `Ctrl+Shift+P` → search: `GPT Explain: Explain Selected Code`

---

## 🔧 Configuration

By default, the plugin uses the `gpt-4o` model with temperature `0.3`.  
You can modify these in `explain_code.py` if needed.

---

## 🧠 Example Output

```text
🧠 Code Explanation:

This Python function checks if a user is logged in by validating a session token...
```

---

## 📄 License

MIT License  
© 2025 Jonathan Tucker
