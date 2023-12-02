from fastapi import FastAPI
import subprocess
import json

app = FastAPI()


@app.get("/class/{classname}/{group}")
def handle_request(classname: str, group: int) -> dict:
    # Build the command to execute your Python script
    command = ["py", "__main__.py", classname, str(group)]

    # Run the command and capture the output
    result = subprocess.run(command, capture_output=True, text=True)

    # Check for errors
    if result.returncode != 0:
        return {"error": "Failed to execute script", "details": result.stderr}

    # Parse the JSON output
    try:
        data = json.loads(result.stdout)

        return data
    except json.JSONDecodeError:
        print(result.stdout)
        return {"error": "Invalid JSON output"}
