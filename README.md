AI DDR Report Generator

This project is an AI-based system that generates a Detailed Diagnostic Report (DDR) from inspection and thermal reports.

Workflow:
1. Extract text from PDF reports using PyMuPDF
2. Process data using LLM via Groq API
3. Generate structured DDR output

Features:
- Combines multiple data sources
- Handles missing data (Not Available)
- Avoids hallucination
- Generates client-friendly structured reports

Limitations:
- Image extraction not implemented
- Output depends on input quality

Future Improvements:
- Image extraction and mapping
- Web-based UI
- Advanced root cause analysis
