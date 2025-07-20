# superlaw_ai/ai_modules.py

def create_prompt(action_type, extracted_text):
    extracted_text = extracted_text.strip()

    base_prompt = f"""
You are a senior Indian legal expert and professional legal document drafter.
Use the following CHARGESHEET to prepare the requested legal document professionally, with correct legal language, structure, and sections.

CHARGESHEET:
{extracted_text}

"""

    detailed_prompts = {
        "bail_application": f"""{base_prompt}
TASK: Draft a **Bail Application**.

Structure:
1. IN THE COURT OF...
2. Name of Applicant and Respondent
3. Case Details and FIR No.
4. Background and Facts
5. Grounds for Bail
6. Legal Arguments with IPC Sections
7. Prayer
8. Signature

Write in formal legal language. Add placeholder for court, date, and names if not present.
""",

        "court_petition": f"""{base_prompt}
TASK: Draft a **Court Petition**.

Structure:
1. Heading (e.g., IN THE COURT OF...)
2. Petitioner vs Respondent
3. Summary of the Case
4. Legal Grounds and Arguments
5. Prayer / Relief Sought
6. Signature and Date

Use proper Indian legal terminology.
""",

        "bail_approval": f"""{base_prompt}
TASK: Draft a **Bail Approval Letter** as issued by a judge.

Include:
- Court Heading
- Summary of Charges
- Justification for Granting Bail
- Legal Provisions Referenced
- Conditions (if any)
- Judge's Signature and Date
""",

        "bail_rejection": f"""{base_prompt}
TASK: Draft a **Bail Rejection Order**.

Include:
- Case Heading
- Summary of Facts
- Grounds for Rejection
- Applicable IPC Sections or Case Law
- Conclusion
- Judge’s Signature and Date
""",

        "final_judgment": f"""{base_prompt}
TASK: Draft a **Final Court Judgment**.

Include:
1. IN THE COURT OF...
2. Case Title and Number
3. Summary of Charges
4. Evidence Considered
5. Legal Analysis
6. Final Decision / Sentence
7. Date and Judge Signature

Maintain formal tone and structure.
""",

        "predict_outcome": f"""{base_prompt}
TASK: Predict the **probable legal outcome** of this case.

Include:
- Charges
- Legal Analysis
- IPC Sections Applied
- Strength of Evidence
- Conclusion (Conviction/Acquittal/Compromise etc.)
""",

        "similar_cases": f"""{base_prompt}
TASK: List 3–5 **similar Indian legal cases** (case law or judgments).

Include:
- Case Title
- Year
- Summary (1–2 lines)
- Citation (if known)

Focus on relevance to the facts and sections in the chargesheet.
"""
    }

    return detailed_prompts.get(action_type, f"{base_prompt}TASK: Provide a summary of the document.")
