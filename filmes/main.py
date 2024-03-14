import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

api_key = 'fa2d9c699f4dc38ee1b4af00d4bb0ecc'
analyzer = SentimentIntensityAnalyzer()

def suggest_movies():
    phrase = input("How it's going today?: ")
    emotion = analyzer.polarity_scores(phrase)['compound']

    if emotion <= -0.5:
        genre = "18"  # Drama
    elif emotion < 0:
        genre = "35"  # Comédia
    elif emotion < 0.5:
        genre = "10749"  # Romance
    else:
        genre = "27"  # Horror

    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&sort_by=popularity.desc&with_genres={genre}&vote_count.gte=4"  
    response = requests.get(url).json()

    if response['results']:
        titles = [result['title'] for result in response['results'][:3]]
        print("Recomendo os seguintes filmes para você:")
        for title in titles:
            print(f"-{title}")
    else:
      print("Não encontrei nenhuma sugestão de filme para você.")
    # TODO: Use the genre information to suggest movies (make an API request, for example)

# Call the function to start the process
def chatbot():
    print("Ola! Sou um chat de sugestão de filmes. Como posso te ajudar hoje?: ")

    while True:
        try:
            response = input().lower()
            if 'filme' in response:
                suggest_movies()
            elif'tchau' in response or 'adeus' in response:
                print("Adeus! Vejo você na próxima vez.")
                break
            else:
                print("Desculpe, não entendi o que quis dizer. ")
        except KeyboardInterrupt:
            break
        
chatbot()         
