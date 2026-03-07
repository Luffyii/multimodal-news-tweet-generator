from rouge_score import rouge_scorer
from nltk.translate.bleu_score import sentence_bleu
import evaluate

reference = "ISRO launches new satellite to improve rural connectivity"
generated = "ISRO successfully launches satellite to improve internet access in rural India"

# BLEU score
bleu = sentence_bleu([reference.split()], generated.split())

# ROUGE
scorer = rouge_scorer.RougeScorer(['rouge1','rouge2','rougeL'], use_stemmer=True)
rouge = scorer.score(reference, generated)

# BERTScore
bertscore = evaluate.load("bertscore")
bert = bertscore.compute(
    predictions=[generated],
    references=[reference],
    lang="en"
)

print("BLEU Score:", bleu)
print("ROUGE Scores:", rouge)
print("BERTScore F1:", bert["f1"][0])