This agent analyzes a MoEngage Help Center article and returns structured, actionable suggestions for improvement based on:

✅ Readability (especially for non-technical marketers)
🧭 Structure and Flow
📚 Completeness of Information and Examples
✍️ Adherence to Simplified Style Guidelines (Microsoft Style Guide principles)


🧱 Design Choices & Approach

Readability
Used the readability Python library to calculate Flesch-Kincaid and Gunning Fog scores.
Supplemented raw scores with LLM-generated qualitative interpretation.
Structure & Flow
LLM prompt specifically asks for evaluation of:
Use of headings/lists
Logical progression
Paragraph and formatting clarity
Completeness
LLM checks for:
Presence of real-world use cases
Clear definitions and onboarding context
Sufficient examples for execution
Style Guidelines (Simplified Microsoft Style Guide)
Emphasis on:
Active voice
Clarity and conciseness
Action-oriented language
These are enforced via prompt engineering and qualitative LLM critique, rather than rigid rule-based enforcement.
⚠️ Challenges and Improvements

Challenges
HTML Variability: Some articles may not use a consistent DOM structure.
Token Limitations: Articles over 8,000 characters must be truncated; some context may be lost.
Style Interpretation: Applying style guide principles through an LLM can be inconsistent unless prompt engineering is precise.
If Given More Time
Add streamlit UI for non-technical use.
Implement automated version comparison (diff-style feedback on article edits).
Expand to support batch URL processing.
