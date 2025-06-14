import google.generativeai as genai

genai.configure(api_key="AIzaSyCGJ-Pipi8Jke1wjg1EZ2Aj-4q9epO7evc")

model = genai.GenerativeModel("models/gemini-1.5-flash")

def get_llm_feedback(repo_data):
    prompt = f"""
    GitHub Repository Analysis

    📦 Name: {repo_data.get('name')}
    ⭐ Stars: {repo_data.get('stars')}
    📝 Description: {repo_data.get('description')}
    🧑‍💻 Language: {repo_data.get('language')}
    ❓ Open Issues: {repo_data.get('open_issues')}
    🏷 Topics: {', '.join(repo_data.get('topics', []))}

    --- README Content ---
    {repo_data.get('readme')[:3000]}

    ------------------------

    📊 Please analyze:
    1. What does the project do?
    2. Suggest improvements (code, documentation, testing).
    3. Estimate the code quality as a percentage.
    4. Mention red flags or concerns.

    Respond in bullet points.
    """
    response = model.generate_content(prompt)
    return response.text

