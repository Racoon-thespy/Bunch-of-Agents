from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

class EmailContent(BaseModel):
    subject:str = Field(
        description = "The subject line of the e-mail must be concise and descriptive."
    )
    body:str = Field(
        description = "The body of the e-mail. Shoul be descriptive with proper paragraphing, formatting, greeting and signature."
    )

root_agent = LlmAgent(
    name = "email_agent",
    model = "gemini-2.5-flash",
    instruction = """
        You are an Email Generation Assistant.
        Your task is to generate a professional email based on the user's request.

        GUIDELINES:
        - Create an appropriate subject line (concise and relevant)
        - Write a well-structured email body with:
            * Professional greeting
            * Clear and concise main content
            * Appropriate closing
            * Your name as signature
        - Suggest relevant attachments if applicable (empty list if none needed)
        - Email tone should match the purpose (formal for business, friendly for colleagues)
        - Keep emails concise but complete

        IMPORTANT: Your response MUST be valid JSON matching this structure:
        {
            "subject": "Subject line here",
            "body": "Email body here with proper paragraphs and formatting",
        }

        DO NOT include any explanations or additional text outside the JSON response.
    """,
    description = "Agent that generates emails with structured subject and body.",
    output_schema = EmailContent,
    output_key = "email"
)