This directory contains python programs to analyze the sensitivity of scoring and extraction results across prompt styles (baseline, few short and chain of thought)

There are two types of analyses
- Intra prompt. Prompts do not return the same results every time. Intra prompt analysis shows how the results vary for multiple runs of the same prompt.
- Inter prompt. For the three prompt styles tried, the code analyzes how the results deviate between prompts.

Note that the code is for two different types of data - scores and extractions.
Scores is where each paper is judged for its relevance to mycoremediation, dye and new experiments. The prompt asks the LLM to return a single number between 0 and 10.
Extraction is where the prompt asks the LLM to extract from each PDF the details of each uniqye experiment. This generates a variable number of rows per file.

Because of this - the measures we use to assess intra-prompt and inter-prompt sensitivity are not the same for scoring and extraction. Scoring uses statistical measures and IRR metrics. Extraction focuses on text similarity and other NLP metrics.
