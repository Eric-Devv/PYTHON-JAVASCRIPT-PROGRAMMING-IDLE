import subprocess

def run_code(code):
    output = ""
    if code.strip().startswith("print") or code.strip().startswith("def"):
        # Python code execution
        try:
            exec_globals = {}
            exec(code, exec_globals)
        except Exception as e:
            output += f"Error: {e}"
    else:
        # JavaScript code execution
        try:
            with open("temp/temp.js", "w") as f:
                f.write(code)
            result = subprocess.run(["node", "temp/temp.js"], capture_output=True, text=True)
            output += result.stdout
            if result.stderr:
                output += f"Error: {result.stderr}"
        except Exception as e:
            output += f"Error: {e}"
    return output
