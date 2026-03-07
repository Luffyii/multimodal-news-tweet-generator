import pandas as pd
import matplotlib.pyplot as plt
from nltk.translate.bleu_score import sentence_bleu
from rouge_score import rouge_scorer
import evaluate

# Example dataset (replace with your tweets)
references = [
    "ISRO launches new satellite to improve rural connectivity",
    "India wins cricket world cup after thrilling final",
    "NASA discovers signs of water on Mars",
    "Government introduces new AI policy",
    "New electric vehicle launched in India"
]

generated = [
    "ISRO successfully launches satellite to boost rural internet",
    "India secures world cup victory after exciting final",
    "NASA finds possible water traces on Mars",
    "Government announces AI policy for technology growth",
    "India launches new electric vehicle model"
]

bleu_scores = []
rouge_l_scores = []
tweet_lengths = []

scorer = rouge_scorer.RougeScorer(['rouge1','rouge2','rougeL'], use_stemmer=True)
bertscore = evaluate.load("bertscore")

for ref, gen in zip(references, generated):

    bleu = sentence_bleu([ref.split()], gen.split())
    bleu_scores.append(bleu)

    rouge = scorer.score(ref, gen)
    rouge_l_scores.append(rouge["rougeL"].fmeasure)

    tweet_lengths.append(len(gen.split()))

bert = bertscore.compute(predictions=generated, references=references, lang="en")
bert_scores = bert["f1"]

# Save results table
df = pd.DataFrame({
    "BLEU": bleu_scores,
    "ROUGE-L": rouge_l_scores,
    "BERTScore": bert_scores,
    "Tweet_Length": tweet_lengths
})

df.to_csv("evaluation_results.csv", index=False)

print("\nAverage BLEU:", df["BLEU"].mean())
print("Average ROUGE-L:", df["ROUGE-L"].mean())
print("Average BERTScore:", df["BERTScore"].mean())

# ----------------------------
# GRAPH 1: Metric comparison
# ----------------------------

plt.bar(
    ["BLEU","ROUGE-L","BERTScore"],
    [df["BLEU"].mean(), df["ROUGE-L"].mean(), df["BERTScore"].mean()]
)

plt.title("Model Performance Metrics")
plt.ylabel("Score")
plt.savefig("metric_comparison.png")
plt.show()

# ----------------------------
# GRAPH 2: Tweet length distribution
# ----------------------------

plt.hist(tweet_lengths, bins=5)

plt.title("Tweet Length Distribution")
plt.xlabel("Number of Words")
plt.ylabel("Frequency")

plt.savefig("tweet_length_distribution.png")
plt.show()