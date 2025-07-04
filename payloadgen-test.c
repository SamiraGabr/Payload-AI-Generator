// first lets identify our libraries ;)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void select_platform(char *platform) { // then the first interface which ask the user to select the paltform he want
    printf("Select the platform:\n");
    printf("1) Windows\n2) Linux\n3) macOS\n4) Web Application\n> ");
    int choice;
    scanf("%d", &choice);
    switch (choice)
    {
    case 1: strcpy(platform, "Windows"); break;
    case 2: strcpy(platform, "Linux");   break;
    case 3: strcpy(platform, "macOS");   break;
    case 4: strcpy(platform, "Web Application"); break;
    default: printf("Invalid platform.\n"); exit(1);
    }
}
void select_payload(char *payload_type) { // then if the user select OS as platform we have specific payloads for that choice
    const char *payload[] = {
    "Reverse Shell", "Bind Shell", "Execute Command", "Keylogger", "Downloader",
    "Privilege Escalation", "Credential Harvester", "Persistence Mechanism",
    "Port Scanner", "Command and Control", "File Exfiltration", "Anti-VM Detection"
    };
    printf("Select Payload type:\n");
    for (int i = 0; i< 12; i++) {
        printf("%d) %s\n", i+1, payload[i]);
    }
    printf("> ");
    int choice;
    scanf("%d", &choice);
    if (choice < 1 || choice > 12) {
        printf("Invalid Payload.\n");
        exit(1);
    }
     strcpy(payload_type, payload[choice - 1]); /*here we make the payloads[choice - 1] and nor choice because as we know arraies start from 0 and the user have list start from 1 so the if he select payload 1 he ot will get the payload no 0 from the array*/
}
void select_language(char *language) {
    const char *languages[] = { "Bash", "Python", "C" };
    printf("Select programming language for the payload:\n");
    for (int i = 0; i < 3; i++){
        printf("%d) %s\n", i+1, languages[i]);
    }
    printf("> ");
    int choice;
    scanf("%d", &choice);
    if (choice < 1 || choice > 3) {
        printf("Invalid choice.\n");
        exit(1);
    }
    strcpy(language, languages[choice - 1]); //same as line 39 and 40
}
void select_mode(char *mode) {
    const char *modes[] = {"walkthrough", "payloads"};
    printf("Do you want:\n");
    printf("1) Step-by-Step walkthrough\n2) 50 payloads\n");
    int choice;
    scanf("%d",&choice);
    if (choice < 1 || choice > 2) {
        printf("Invalid Choice.\n");
        exit(1);
    }
    strcpy(mode, modes[choice - 1]);
}
void select_web_vuln(char *vuln){
    const char *vulns[] = {
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
        "Web Cache Deception"
    };
    printf("Select web vulnerability to target:\n");
    for (int i = 0; i < 30; i++) {
        printf("%d) %s\n", i+1, vulns[i]);
    }
    printf("> ");
    int choice;
    scanf("%d", &choice);
    if (choice < 1 || choice > 30) {
        printf("Invalid Choice.\n");
        exit(1);
    }
    strcpy(vuln, vulns[choice - 1]);
}
void select_obfuscation(char *level){
    const char *levels[] = {"None", "Basic", "Advanced"};
    printf("Select obfuscation level:\n");
    for (int i = 0; i < 3 ; i++){
        printf("%d) %s\n", i+1, levels[i]);
    }
    printf("> ");
    int choice;
    scanf("%d", &choice);
    if (choice < 1 || choice > 3) {
        printf("Invalid Choice.\n");
        exit(1);
    }
    strcpy(level, levels[choice - 1]);
}
int main() {
    char paltform[64], payload[128], obfuscation[32], vuln[128], language[32], mode[32];
    select_platform(paltform);
    select_obfuscation(obfuscation);
    select_mode(mode);
    if (strcmp(paltform, "Web Application") == 0) {
        select_web_vuln(vuln);
        char command[1024];
        snprintf(command, sizeof(command), "python ai_helper.py --platform \"%s\" --webvuln \"%s\" --obfuscation \"%s\" --mode \"%s\"", paltform, vuln, obfuscation, mode); //here the (sizeof()) used to determine the size of memory we will use for that command to prevent buffer overflow
        system(command);
    } else {
        select_payload(payload);
        select_language(language);
        select_obfuscation(obfuscation);
        char command[1024];
        snprintf(command, sizeof(command),
         "python ai_helper.py --platform \"%s\" --payload \"%s\" --obfuscation \"%s\" --language \"%s\"",
        paltform, payload, obfuscation, language);
        system(command);
    }
    return 0;
}
