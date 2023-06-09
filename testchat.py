import os
import openai
import valspeaklex as lex

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt="I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\".\n\nQ: What is human life expectancy in the United States?\nA: Human life expectancy in the United States is 78 years.\n\nQ: Who was president of the United States in 1955?\nA: Dwight D. Eisenhower was president of the United States in 1955.\n\nQ: Which party did he belong to?\nA: He belonged to the Republican Party.\n\nQ: What is the square root of banana?\nA: Unknown\n\nQ: How does a telescope work?\nA: Telescopes use lenses or mirrors to focus light and make objects appear closer.\n\nQ: Where were the 1992 Olympics held?\nA: The 1992 Olympics were held in Barcelona, Spain.\n\nQ: How many squigs are in a bonk?\nA: Unknown\n\nQ: Where is the Valley of Kings?\nA:",


prompts = ["Q: What is human life expectancy in the United States?\nA:","Q: Who was president of the United States in 1955?\nA:","Q: Which party did he belong to?\nA:", "Q: What is the square root of banana?\nA:",  "Q: How does a telescope work?\nA:", "Q: Where were the 1992 Olympics held?\nA:", "Q: How many squigs are in a bonk?\nA:", "Q: What is human life expectancy in the United States?\nA:"]

for p in prompts:
  print(p)

  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=p,
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"]
  )
  #print(lex.checkReplace(response["choices"][0]["text"]))
  print(response["choices"][0]["text"])


