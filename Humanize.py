import json
import urllib.request
import urllib.error

SERVER_URL = "http://127.0.0.1:8080"


def humanize(text):
    prompt = f"""Rewrite the following text in natural, fluent English.
Preserve the original meaning and facts.
Do not add explanations or examples.
Return only the rewritten text.

Text:
{text}

Rewritten text:"""

    data = {
        "prompt": prompt,
        "temperature": 0.3,
        "top_p": 0.9,
        "n_predict": 150,
        "stop": ["\nText:", "\nRewritten text:"]
    }

    request = urllib.request.Request(
        f"{SERVER_URL}/completion",
        data=json.dumps(data).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(request, timeout=900) as response:
        result = json.loads(response.read().decode("utf-8"))

    return result["content"].strip()


def main():
    print("\n=== HUMANIZER AI ===")
    print("Enter text to rewrite, or type 'exit' to quit.\n")

    while True:
        text = input("Your text: ")

        if text.strip().lower() == "exit":
            print("Goodbye!")
            break

        if not text.strip():
            continue

        try:
            result = humanize(text)
            print("\nRewritten text:")
            print(result)
            print()

        except urllib.error.URLError as error:
            print(f"Cannot connect to llama-server: {error}")

        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()