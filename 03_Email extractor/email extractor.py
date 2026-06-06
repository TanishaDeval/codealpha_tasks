import re
path="Details.txt"
with open(path,mode="r",encoding="utf-8") as f:
    file_content=f.read()
emails=re.findall(r"[a-zA-Z0-9._%+-]+"r"@[a-zA-Z0-9.-]"
                          r""r"+\.[a-zA-Z]{2,}",file_content)
unique_emails=set(emails)
with open("emails.txt",mode="w",encoding="utf-8") as f:
        f.write("📂EXTRACTED EMAILS📂 \n\n")

        for email in unique_emails:
            f.write(email+"\n")

print("🔎Emails extracted and saved successfully!✅")