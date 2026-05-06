import re
with open("index.html", "r", encoding="utf-8") as f: content = f.read()

print("TryHackMe:", "TryHackMe Progress" in content)
print("HackTheBox:", "HackTheBox" in content)
print("Active Research:", "Active Research" in content)

print("SIH 2025:", "SIH 2025" in content)
print("Deloitte:", "Deloitte" in content)

print("ATTENDANCE-SYSTEM link:", "github.com/SAMIHZS/ATTENDANCE-SYSTEM" in content)
print("FUTURE_CS_01 link:", "github.com/SAMIHZS/FUTURE_CS_01" in content)
print("FILE ORGANIZER link:", "CYBERSECURITY-PROJECTS/tree/main/FILE" in content)

resumes = re.findall(r'href="[^"]*Resume[^"]*pdf"', content, re.IGNORECASE)
print("Resume links:", resumes)
