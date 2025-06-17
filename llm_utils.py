import subprocess

def query_ollama(prompt, model="phi3:mini"):
    process = subprocess.Popen(
        ["ollama", "run", model],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate(input=prompt.encode())
    return stdout.decode().strip()
