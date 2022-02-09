from cs50 import get_string


def main():
    # Get text from user
    text = get_string("Text: ")

    # Count number of letters in text
    letters = letterCount(text)

    # Count number of words in text
    words = wordCount(text)

    # Count number of sentences in text
    sentences = sentenceCount(text)

    # Apply Coleman-Liau Index formula
    gradeLevel = CLIndex(letters, words, sentences)

    # Print result within ranges
    if gradeLevel > 15:
        print("Grade 16+")
    elif gradeLevel < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {gradeLevel}")


def letterCount(text):
    """Count number of letters in a string, skipping spaces and punctuation"""

    # Tally a letter for each character, ignoring spaces and punctuation marks
    letters = 0
    for c in text:
        if c.isalpha() == True:
            letters += 1
    return letters


def wordCount(text):
    """Count number of words in a string"""

    # Every time a space is encountered, tally a word
    words = 0
    for c in text:
        if c == " ":
            words += 1
    # Account for last word not ending in a space
    words += 1
    return words


def sentenceCount(text):
    """Count number of sentences in a string"""

    # Tally a sentence, every time a ".", "!", or "?" is encountered
    sentences = 0
    for c in text:
        if c in [".", "!", "?"]:
            sentences += 1
    return sentences


def CLIndex(letters, words, sentences):
    """Applies Coleman-Liau Index formula using letter, word, and sentence count"""

    L = (letters / words) * 100
    S = (sentences / words) * 100
    gradeLevel = round(0.0588 * L - 0.296 * S - 15.8)
    return gradeLevel


if __name__ == "__main__":
    main()