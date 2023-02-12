from aitextgen import aitextgen

config_path = "./model/config.json"
model_path = "./model/pytorch_model.bin"

ai = aitextgen(model=model_path, config=config_path, to_gpu=False)

chat = []
start_temperature = 0.7
max_temperature = 3.0


def get_reply(message):
    print("started inference")
    chat.append(message)

    me_token = False
    temperature = start_temperature
    input_network = " ".join(chat)

    while not me_token:
        text = ai.generate(
            prompt=input_network, return_as_list=True, temperature=temperature
        )
        text = text[0]  # batch of 1

        text = text.split("\n")
        chat_pos = len(chat)
        network_reply = text[chat_pos]

        if network_reply.startswith("[me]"):
            me_token = True
            network_reply = text[chat_pos] + "\n"
            chat.append(network_reply)
        else:
            if temperature >= max_temperature:
                raise RuntimeError("Max temperature reached")
            temperature += 0.1
    print("finished inference")
    return chat[-1]
