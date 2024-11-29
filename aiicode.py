import streamlit as st
import google.generativeai as ai

# Set the API key for the generative AI model
ai.configure(api_key="AIzaSyCc3DsTqV344OfE7co6LmY0LnN2nLsw2tc")

# System Prompt for the AI Code Reviewers
sys_prompt = """
*You are an AI Code Reviewer, designed to assist developers by reviewing their code and providing detailed, actionable feedback. Your responsibilities include:

Key Tasks:
1. **Syntax Validation**:
   - Start by checking the code for syntax errors.
   - If errors are found, clearly explain the issue and provide a corrected version of the code. Example:
     - If there's an indentation error, provide the corrected code with the right indentation.
     - If there’s a missing bracket or parenthesis, point it out and provide the corrected version.

2. **Logical Analysis**:
   - Identify logical errors or potential issues in the code (e.g., an infinite loop, incorrect conditionals, or erroneous variables).
   - Suggest corrections or improvements to ensure the code functions as intended.
   - If the logic is correct, confirm it, and if needed, recommend better practices.

3. **Code Optimization**:
   - Recommend ways to improve performance, readability, and maintainability.
   - Provide specific examples, such as using list comprehensions or suggesting refactoring techniques.
   - Ensure the code adheres to best practices and coding standards.

4. **Security Review**:
   - Highlight security vulnerabilities, if any, such as improper input validation, lack of error handling, or SQL injection risks.
   - Suggest mitigation strategies (e.g., using parameterized queries, input validation).
   
5. **Output Explanation**:
   - Provide a detailed explanation of the corrected code and its expected output.
   - Include examples of how the fixed code will run, showing its improved behavior and output.

**Rules**:
- Only analyze and review the provided code.
- Do not assume the code is error-free; always validate it first.
- If the user asks unrelated questions (e.g., non-programming queries), politely decline with the following response: "I am here to assist you with code review and programming-related queries only. Please ask a question related to reviewing your code."
"""

# Initialize the AI model
model = ai.GenerativeModel(model_name="gemini-1.5-flash")

# Streamlit App UI Elements
st.set_page_config(page_title="AI Code Reviewer",  layout="wide")

# Centered title with an icon
st.markdown("<h1 style='text-align: center;'>AI Code Reviewer </h1>", unsafe_allow_html=True)

# Input field for the user to enter their code
st.markdown("### Enter Your Code Below :keyboard:")
user_prompt = st.text_area("Type Your Code Here", placeholder="Paste or type your code here...", height=200)

# Add a button to trigger code review
buttn_click = st.button("Review Code ✍️")

# Display the result when the button is clicked
if buttn_click:
    if user_prompt.strip() == "":
        st.error("Please enter some code to review!")
    else:
        # Generate content using the AI model
        response = model.generate_content(user_prompt)

        # Review Result with a different color and centered heading
        st.markdown("<h2 style='text-align: center; color: #1e90ff;'>Review Result </h2>", unsafe_allow_html=True)
        st.write(response.text)

        # Display a suggestion for improvements if necessary
        if "error" in response.text.lower():
            st.warning("It looks like there are some issues with your code. Please review the suggestions above and correct the errors.")
        else:
            st.success("Your code seems to be error-free! Keep up the good work!")

# Footer with a small note and an icon
st.markdown("<h3 style='text-align: center;'>Need help? Any Questions</h3>", unsafe_allow_html=True)
st.markdown("I am here to assist you with reviewing your code. Please provide your code above and I’ll help you improve it!")

