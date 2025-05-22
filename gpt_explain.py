import sublime
import sublime_plugin
import subprocess
import os
import tempfile
import sys
import imp

# Load API key from external file
try:
    key_module_path = "/Path to your copy of/gpt_api_key.py"
    gpt_api_key = imp.load_source("gpt_api_key", key_module_path)
    OPEN_API_KEY = gpt_api_key.OPEN_AI_KEY
except Exception as e:
    OPEN_API_KEY = None

# Path to your code explanation script
SCRIPT_PATH = "/Path to your copy of/explain_code.py"

class GptExplainCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selections = self.view.sel()
        code = ""
        output = ""

        # Collect selected code from all selections
        for region in selections:
            if not region.empty():
                code += self.view.substr(region) + "\n"

        if not code.strip():
            sublime.message_dialog("Please select some code first.")
            return

        # Write selected code to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as tmp:
            tmp.write(code)
            tmp_path = tmp.name

        try:
            env = os.environ.copy()
            if not OPEN_API_KEY:
                sublime.message_dialog("API key could not be loaded from gpt_api_key.py")
                return

            env["OPENAI_API_KEY"] = OPEN_API_KEY
            print("🔑 API Key Sent:", OPEN_API_KEY[:8] + "...")

            # Attempt to extract language from syntax scope
            scope = self.view.scope_name(0).split(" ")[0]
            lang_hint = ""

            if "python" in scope:
                lang_hint = "Python"
            elif "javascript" in scope:
                lang_hint = "JavaScript"
            elif "html" in scope:
                lang_hint = "HTML"
            elif "css" in scope:
                lang_hint = "CSS"
            elif "bash" in scope or "shell" in scope:
                lang_hint = "Bash"
            elif "json" in scope:
                lang_hint = "JSON"
            elif "xml" in scope:
                lang_hint = "XML"
            elif "sql" in scope:
                lang_hint = "SQL"
            # Add more as needed...

            env["GPT_LANG_HINT"] = lang_hint
            
            # Run subprocess and capture all output
            proc = subprocess.Popen(
                ["python3", SCRIPT_PATH],
                stdin=open(tmp_path, "r"),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=env
            )

            out, err = proc.communicate()
            raw_out = out.decode("utf-8").strip()
            raw_err = err.decode("utf-8").strip()

            print("📤 STDOUT (raw):\n{}".format(raw_out))
            print("📛 STDERR (raw):\n{}".format(raw_err))
            print("📦 Return Code:", proc.returncode)

            # Always show all raw info inside Sublime for now
            output = (
                "📦 Return Code: {}\n\n"
                "📤 STDOUT:\n{}\n\n"
                "📛 STDERR:\n{}".format(proc.returncode, raw_out or "[EMPTY]", raw_err or "[EMPTY]")
            )

        except Exception as e:
            sublime.message_dialog("Exception:\n{}".format(str(e)))
            return
        finally:
            os.unlink(tmp_path)

            try:
                new_view = self.view.window().new_file()
                new_view.set_name("Code Explanation")
                new_view.set_scratch(True)

                if not output.strip():
                    output = "⚠️ Output was empty. Check console for debug logs."

                new_view.run_command("append", {"characters": output})
            except Exception as e:
                print("💥 Error creating tab:", e)
                sublime.message_dialog("💥 Failed to show explanation in new tab.\n{}".format(str(e)))



