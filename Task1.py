import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import defaultdict

# Download required NLTK data (run once)
nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, num_sentences=3):
    """
    Summarizes the given text by extracting the most important sentences.

    Args:
        text (str): The input text to be summarized.
        num_sentences (int): Number of sentences in the summary.

    Returns:
        str: A concise summary of the input text.
    """
    # Validate input
    if not text or not isinstance(text, str):
        return "Invalid input text."

    # 1. Sentence tokenization
    sentences = sent_tokenize(text)

    if len(sentences) <= num_sentences:
        return text.strip()

    # 2. Word tokenization and stopword removal
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

    # 3. Calculate word frequencies
    word_frequencies = defaultdict(int)
    for word in filtered_words:
        word_frequencies[word] += 1

    if not word_frequencies:
        return "Cannot summarize: No meaningful words found."

    # 4. Normalize word frequencies
    max_freq = max(word_frequencies.values())
    for word in word_frequencies:
        word_frequencies[word] /= max_freq

    # 5. Score sentences based on word frequencies
    sentence_scores = defaultdict(float)
    for i, sentence in enumerate(sentences):
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                sentence_scores[i] += word_frequencies[word]

    # 6. Select top N sentences by score
    top_sentence_indices = sorted(
        sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    )

    # 7. Build summary
    summary = ' '.join([sentences[i] for i in top_sentence_indices])
    return summary.strip()


# --- Example Usage ---
if __name__ == "__main__":
    article = """
    Natural Language Processing (NLP) is a branch of artificial intelligence (AI) that enables computers to understand, interpret, and respond to human language. It bridges the gap between human communication and machine understanding by combining computational linguistics with machine learning and deep learning models. NLP has made significant strides in recent years, largely due to advancements in deep learning architectures like transformers.

    NLP techniques are used to analyze text and speech data, allowing machines to perform tasks such as language translation, sentiment analysis, text summarization, and chatbot interactions. Key NLP applications include virtual assistants like Siri and Alexa, email spam filters, and language translation tools such as Google Translate.

    Text summarization is a key task in Natural Language Processing that involves generating a concise and coherent summary from a longer text document while preserving its essential information. There are two primary approaches to summarization: extractive and abstractive. Extractive summarization works by identifying and selecting the most important sentences or phrases directly from the original text. In contrast, abstractive summarization generates entirely new sentences that convey the core meaning of the source material, often relying on advanced deep learning models to understand context and rephrase content effectively.

    Challenges in NLP include the inherent ambiguity of human language, variations in grammar and sentence structure, and the need for large volumes of high-quality data to train effective models. These challenges make it difficult for machines to fully grasp meaning, context, and intent. Despite these hurdles, continuous advancements in research and technology are steadily overcoming such limitations, resulting in increasingly sophisticated and accurate NLP systems. As progress continues, the future of NLP holds tremendous potential to revolutionize the way humans interact with machines and process information.
    
    """

    print("Original Article:\n")
    print(article.strip())

    print("\n" + "="*60 + "\n")

    # Generate and print summary
    summary = summarize_text(article, num_sentences=3)
    print("Summary:\n")
    print(summary)
