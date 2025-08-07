# Agents, Runner, aur models import kar rahe hain
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel 
# Environment variables load karne ke liye
from dotenv import load_dotenv
import os

# .env file se environment variables load karo
load_dotenv()

# Gemini API key hasil karo
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini client banaya ja raha hai
client = AsyncOpenAI(
    api_key=GEMINI_API_KEY, 
    base_url="https://generativelanguage.googleapis.com/v1beta"
)

# Model ki settings define kar rahe hainr\
modell = OpenAIChatCompletionsModel(
    openai_client = client,
    model="gemini-2.5-flash"
)

# Simple Agent banaya ja raha hai, yeh user ki madad karega
Simple_Agent = Agent(
    name="Simple Agent",
    instructions="You are a helpful and friendly assistant. Answer questions clearly and concisely.",
    model=modell
)

# Yeh loop user se bar bar prompt leta hai jab tak user 'exit' nahi likhta
while True:
    # User se prompt lo
    prompt = input("Enter your prompt (ya 'exit' likhein to band karein): ")
    # Agar user 'exit' likhe to program band kar do
    if prompt.lower() == 'exit':
        print("Program band ho gaya.")
        break
    # Agent se jawab hasil karo
    result = Runner.run_sync(Simple_Agent, prompt)
    # Jawab print karo
    print(result.final_output)



