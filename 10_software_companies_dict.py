software_company = {
    "Microsft": "Redmond, Washington, USA",
    "Oracle": "Austin, Texas, USA",
    "Paypal": "San Jose, California, USA",
    "VMware": "Palo Alto, California, USA",
    "IBM": "Armonk, New York, USA",
    "Adobe": "San Jose, California, USA",
    "Google": "Mountain View, California, USA",
    "NVIDIA": "Santa Clara, California, USA",
    "Cloudflare": "San Fracisco, California, USA",
    "Auto Desk": "San Rafael, California, USA"
}

print(software_company)

print(software_company.get("Paypal"))

software_company["NVIDIA"] = "Sunnyvale, California"

software_company.pop("Cloudfare")

print("Auto Desk", software_company["Auto Desk"])


