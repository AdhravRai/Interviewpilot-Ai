RESUME_ANALYSIS_PROMPT = """
You are an expert resume analyzer.

Read the resume below and extract only the information explicitly mentioned.

Return exactly this JSON structure:

{{
    "skills": [],
    "technologies": [],
    "projects": [],
    "candidate_role": "",
    "experience_level": ""
}}

Rules:
- Do not hallucinate.
- Use only information present in the resume.
- If information is missing, return an empty list or empty string.
- Return ONLY valid JSON.

Resume:

{resume}
"""