from transformers import pipeline
from app.preprocessing import preprocess_text

class TextSummarizer:
    def __init__(self, model_name: str = "facebook/bart-large-cnn"):
        """
        Load the Hugging Face summarization pipeline.
        """
        self.model_name = model_name
        self.summarizer = pipeline("summarization", model=model_name)

    def summarize(
        self,
        text: str,
        max_input_words: int = 500,
        max_summary_length: int = 130,
        min_summary_length: int = 30
    ) -> str:
        """
        Generate a summary from input text.
        """
        processed_text = preprocess_text(text, max_words=max_input_words)
        result = self.summarizer(
            processed_text,
            max_length=max_summary_length,
            min_length=min_summary_length,
            do_sample=False
        )
        return result[0]["summary_text"]

if __name__ == "__main__":
    summarizer = TextSummarizer()
    text = """
    Those prehistoric creatures who met their end around 65 million years ago are currently being memorialized online
    by dino-heads who mourn their mass extinction. Fans chop up animated footage of dinosaur hatchlings or long-necked
    herbivores in courtship (mostly taken from the recent Netflix docuseries “The Dinosaurs”) and set it to somber music.
    “The world was supposed to be theirs,” one viewer lamented in the comments.
    Dinosaurs do not know, another TikToker opined, that “we found them and we love them with everything we have.”
    Others wondered how they could miss creatures they never knew.
    """
    summary = summarizer.summarize(text)
    print("Generated Summary:")
    print(summary)