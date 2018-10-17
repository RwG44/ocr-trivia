
def optimize(query):
    noise_words = [
        'khi nào', 'ai', 'ở đâu'
    ]
    for noise_word in noise_words:
        if noise_word in query:
            query.replace(noise_word, '')
    return query