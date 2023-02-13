# 🤖 pistoBot

> Create an AI that chats like you. 

[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1T4-Gk-mlAWJkX9RuRd3_EiS5JBP5UvyV?usp=sharing)
[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://pistocop.github.io/pistoBot-website/)

# 🥜 In a nutshell
1. Get your whatsapp and telegram data
2. Parse it using [this](https://github.com/pistocop/messaging-chat-parser)
3. Train one of the [available](https://github.com/pistocop/pistoBot/tree/master/pistoBot) models (gpt2 suggested)
4. Chat with the model

## 👀 Example of chat

An example of GPT-2 model trained on my whatsapp and telegram messages.<br>
See the [website](https://pistocop.github.io/pistoBot-website/) for more examples.

**Chat:**<br>
> :pencil2: come sei messo col pistobot?<br>
> :robot: ahaha male<br>
> :pencil2: chatta meglio di te? 😂 <br>
> :robot: si <br>
> :pencil2: non che ci volesse molto... <br>
> :robot: ma tu che dici <br>
> :pencil2: io dico che potevi impegnarti di più <br>

:pencil2: ⟶ message that I have wrote<br>
:robot: ⟶ message generated from the model<br>


# 👉 I want one
- Create and chat with your model using [this](https://colab.research.google.com/drive/1T4-Gk-mlAWJkX9RuRd3_EiS5JBP5UvyV?usp=sharing) colab notebook
- For more info visit the [project website](https://pistocop.github.io/pistoBot-website/)
---

# :warning: Disclaimer
This project is only a **personal playground** build during the week-ends of Covid-19 quarantine.<br>
Used mainly to:
- Use interesting packages (like [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple), tensorflow 2.0 etc.)
- Gain experience

Due to this nature, this repository has probably: 
- ML _naif approaches_ 
- For sure: not so good english text (sorry 😢)


---
## 📝 Note
- Thanks to Salvinator: Under Covid 19 quarantine I found [this](https://salvinator.github.io/) project, 
that had inspired me to start this repository.
- Why _pistoBot_ name?
    - :crystal_ball: The answer could be handed down only by voice


# Run Docker

1. Go to the telegram bot directory
> cd telegramBot

2. Make sure you have the model files `config.json` and `pytorch_model.bin` in the `model` directory

3. Docker build
> docker build -t zubot:latest .

4. Docker run
> docker run -e BOT_TOKEN='<bot-token>' --name zubot zubot:latest


send messages to your telegram bot and enjoy