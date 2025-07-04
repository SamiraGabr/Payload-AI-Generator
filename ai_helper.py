from google import genai
from datetime import datetime
import argparse
import openai
import os
import sys
import json
import google.generativeai as genai
import threading
import time
from google import genai

# these part just for animation ;)
def spinner(msg = "⏳ Waiting for response"):
    chars = "|/-\\"
    i = 0 
    while not spinner_done:
        print(f"\r{msg} {chars[i % len(chars)]}", end='', flush=True)
        time.sleep(0.1)
        i += 1

def load_config():
    try:
        with open("config.json") as f:
            return json.load(f)
    except Exception as e:
        print("Error loading config.json:", e)
        sys.exit(1)

def build_prompt(args):
    injection_vulns = [
        "SQL Injection", "Cross-Site Scripting (XSS)", "Cross-Site Request Forgery (CSRF)", 
        "Clickjacking", "DOM-Based Vulnerabilities", "Cross-Origin Resource Sharing (CORS)", 
        "XML External Entity (XXE) Injection", "Server-Side Request Forgery (SSRF)", 
        "HTTP Request Smuggling", "OS Command Injection", "Server-Side Template Injection", 
        "Path Traversal", "Access Control Vulnerabilities", "Authentication Issues", 
        "WebSockets", "Web Cache Poisoning", "Insecure Deserialization", 
        "Information Disclosure", "Business Logic Vulnerabilities", 
        "HTTP Host Header Attacks", "OAuth Authentication", "File Upload Vulnerabilities", 
        "JWT Exploitation", "Prototype Pollution", "GraphQL API Vulnerabilities", 
        "Race Conditions", "NoSQL Injection", "API Testing", "Web LLM Attacks", 
        "Web Cache Deception", "Insecure Direct Object References (IDOR)"
    ]

    if args.webvuln:
        if args.mode == "payloads":
            return f"""You are an offensive security expert. Generate exactly {args.count} unique payloads to exploit the {args.webvuln} vulnerability.

Then for each payload, generate:
1. An obfuscated version using {args.obfuscation} techniques. Example formats: URL-encoding (%27%20OR%201%3D1), hex, base64, case transformation, etc. Indicate the obfuscation technique used next to each payload.
2. A WAF bypass version using advanced WAF evasion methods. Use realistic bypass strategies from this list (but not limited to it): encoding, HTTP parameter pollution, case manipulation, IP fragmentation, JSON/XML injection, 404 tricking, DNS redirection, rate throttling, or behavioral splitting. Indicate the bypass technique used next to each payload.

Output format (strictly):
1. A numbered list (1–{args.count}) of original payloads.
2. A numbered list (1–{args.count}) of obfuscated versions with technique used.
3. A numbered list (1–{args.count}) of WAF bypass versions with technique used.
4. Add inline comments between each list and Tiltle.
No explanations. No extra text. Just clean formatted lists."""
        
        else: #which mean walkthrough 
            return f"""You are a web penetration tester. Provide a detailed step-by-step exploitation guide for the vulnerability: {args.webvuln}. 
Include examples, tools, payloads, common WAF bypass techniques, and a summary."""
        
    else: #which here i refer to any type of vuln related to os linux, mac, windows
        return f"""You are an expert offensive security developer. Generate a {args.payload.lower()} payload targeting {args.platform}, written in {args.language}.

For this payload, produce the following:
1. The raw payload code.
2. An obfuscated version using {args.obfuscation} techniques.
3. A WAF bypass version using advanced bypass techniques (like encoding, HPP, 404 hiding, etc.)
4. Add inline comments to all code.
5. End with a short 2–3 sentence summary explaining the payload functionality, obfuscation technique used, and how WAF is bypassed.

Ensure output is practical, accurate, and focused for red team operations."""
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform", required=True)
    parser.add_argument("--payload", required=False)
    parser.add_argument("--obfuscation", required=False)
    parser.add_argument("--webvuln", required=False)
    parser.add_argument("--language", required=False)
    parser.add_argument("--mode", required=False)
    parser.add_argument("--count", type=int, required=False, default=50)
    parser.add_argument("--model", choices=["gemini","gpt"], default="gemini")

    args = parser.parse_args()
    
    config = load_config()
    prompt = build_prompt(args)

    global spinner_done
    spinner_done = False
    t = threading.Thread(target=spinner)
    t.start()

    try:
        if args.model == "gemini":
            client        = genai.Client(api_key=config["Gemini_api_key"])
            response      = client.models.generate_content(
                model     = "gemini-2.5-flash",
                contents  = prompt,
            )
            result        = response.text.strip()
        else:
            openai.api_key= config["OpenAI_api_key"]
            response      = openai.ChatCompletion.create(
                model     = "gpt-4",
                messages  = [{"role" : "user", "content" : prompt}]
            )
            result        = response['choices'][0]['message']['content'].strip()
        
        spinner_done = True
        t.join()
    except Exception as e:
        spinner_done = True
        t.join()
        print("\n❌ API error:", e)
        sys.exit(1)
    
    print("\n=== GENERATED PAYLOAD / WALKTHROUGH ===\n")
    print(result)

    custom_name = input("\n📁 Do you want to name the output file yourself? (y/n): ").strip().lower()

    if args.webvuln:
        output_base_dir = "Web"
    else:
        output_base_dir = "OS"

    output_parent_dir = "OutPuts"
    output_dir        = os.path.join(output_parent_dir, output_base_dir)
    os.makedirs(output_dir, exist_ok=True)

    if custom_name    == 'y':
        user_filename = input("Enter desired filename (without extention): ").strip()
        filename      = f"{user_filename}.txt"
    else: # if the user didn't enter anything or enter anything else y ... remember !! here i should change and edit y to be array of all possible choices user can hit Like yes, Y, Yes, YES
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if args.webvuln: #web vuln
            filename = f"output_{args.model}_WebApp_{args.webvuln}_{args.obfuscation}_{timestamp}.txt"
        else: #OS vuln
            filename = f"output_{args.model}_{args.platform}_{args.payload}_{args.language}_{args.obfuscation}_{timestamp}.txt"

    filename = filename.replace(" ", "_").replace("/", "-").replace("(", "").replace(")", "")

    filename = os.path.join(output_dir, filename)

    try: 
        with open(filename, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"\n✅ Output saved to: {filename}")
    except Exception as e:
        print("❌ Failed to save output to file:", e)

if __name__ == "__main__":
    main()
