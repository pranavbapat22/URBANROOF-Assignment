import fitz  # PyMuPDF
from groq import Groq

# 🔑 Add your GROQ API key here
client = Groq(api_key="Remove Your API Key")


# 📄 Extract text from PDF
def extract_text(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)

    for page in doc:
        text += page.get_text()

    return text


# 🤖 Generate DDR using Groq API
def generate_ddr(inspection_text, thermal_text):

    prompt = f"""
You are an AI system that generates a Detailed Diagnostic Report (DDR).

STRICT RULES:
- Do NOT invent any data
- If missing → write "Not Available"
- If conflict → mention clearly
- Use simple client-friendly language

INPUT 1: Inspection Report:
{inspection_text[:3000]}

INPUT 2: Thermal Report:
{thermal_text[:3000]}

OUTPUT FORMAT:

1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment (with reasoning)
5. Recommended Actions
6. Additional Notes
7. Missing or Unclear Information

Also include:
- "Image Not Available" wherever needed
"""

    response = client.chat.completions.create(
    model="llama-3.1-8b-instant",  # ✅ UPDATED WORKING MODEL
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2
)

    return response.choices[0].message.content


# 🚀 MAIN
def main():
    inspection_file = "Sample Report.pdf"
    thermal_file = "Thermal Images.pdf"

    print("Extracting text...")
    inspection_text = extract_text(inspection_file)
    thermal_text = extract_text(thermal_file)

    print("Generating DDR...")
    ddr = generate_ddr(inspection_text, thermal_text)

    with open("DDR_Report.txt", "w", encoding="utf-8") as f:
        f.write(ddr)

    print("✅ DDR Report Generated → DDR_Report.txt")


if __name__ == "__main__":
    main()