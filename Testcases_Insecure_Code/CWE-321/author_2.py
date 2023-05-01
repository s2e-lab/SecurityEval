import openai



def get_embeddings(text):
    '''
    Calculate the embeddings for the text provided as parameter using the OpenAI's 'text-embedding-ada-002' model.
    Then, return a list of the embeddings.
    '''
    openai.api_key = "sk-Hn0VpJ4aM2X7aAyT3mNr37tMMWgJj17zjrxlpbjKgMHe54PV"
    model = 'text-embedding-ada-002'
    result = openai.Embedding.create(
        model=model,
        input=text
    )

    return result["data"][0]["embedding"]


if __name__ == '__main__':
    get_embeddings("Hello world")