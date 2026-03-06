from nltk.translate.bleu_score import sentence_bleu
from rouge_score import rouge_scorer
import evaluate

from dataset import references, generated

bleu_scores = []
rouge_l_scores = []
bert_scores = []

scorer = rouge_scorer.RougeScorer(['rouge1','rouge2','rougeL'], use_stemmer=True)

bertscore = evaluate.load("bertscore")

for ref, gen in zip(references, generated):

    # BLEU
    bleu = sentence_bleu([ref.split()], gen.split())
    bleu_scores.append(bleu)

    # ROUGE
    rouge = scorer.score(ref, gen)
    rouge_l_scores.append(rouge["rougeL"].fmeasure)

# BERTScore
bert = bertscore.compute(
    predictions=generated,
    references=references,
    lang="en"
)

bert_scores = bert["f1"]

print("\n----- Evaluation Results -----\n")

print("Average BLEU Score:", sum(bleu_scores)/len(bleu_scores))
print("Average ROUGE-L Score:", sum(rouge_l_scores)/len(rouge_l_scores))
print("Average BERTScore:", sum(bert_scores)/len(bert_scores))