"""T38 Movie recommendation using last movie watched.
"""


# Use spaCy to find similarities between last movie and available movies.
import spacy
nlp = spacy.load('en_core_web_md')

# Variables to store highest similarity value and next film.
similarity_value = 0
next_movie = None

# Synopsis of last movie watched.
last_movie = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,
 the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace.
  Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."""

last_movie_token = nlp(last_movie)

# Load in movie data.
file = open("movies.txt", "r")
movies = file.readlines()

# Loop through movie list and compare similarity with last movie watched.
for movie in movies:
    movie_split = movie.strip('\n').split(':')
    similarity = nlp(movie_split[1]).similarity(last_movie_token)

    # Check if movie similarity is higher than stored value.
    if similarity > similarity_value:
        similarity_value = similarity
        next_movie = movie_split

file.close()

# Display next movie recommendation using movie with highest similarity value.
print(f"\nNext movie recommendation is: {next_movie[0]}\nSynopsis : {next_movie[1]}")
