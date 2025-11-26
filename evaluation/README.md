# Results

We evaluated six different LLMs: 
Deepseek, Gemini 2.5 pro, GPT-4 Omni, LLama-3.3-70B, Mixtral 8x22B and OpenAI o3. First, we present the similarity scores to analyze how each LLM performs across mapping tasks. Then, we show the F-score values for each evaluation setting (expert-based, raw, and post-processed). For adapting similarity measures to F1-score graphics, a threshold of 0.8 is used.

## Scenario 1
<figure style="text-align: left;">
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0px;">
    <img src="scenario1_clean/1A/1A.png" alt="Similarity Scenario 1A" style="width:24%;">
    <img src="scenario1_clean/1B/1B.png" alt="Similarity Scenario 1B" style="width:24%;">
    <img src="scenario1_clean/1C/1C.png" alt="Similarity Scenario 1C" style="width:24%;">
    <img src="scenario1_clean/1D/1D.png" alt="Similarity Scenario 1D" style="width:24%;">
    <img src="scenario1_clean/1E/1E.png" alt="Similarity Scenario 1E" style="width:24%;">
    <img src="scenario1_clean/1F/1F.png" alt="Similarity Scenario 1F" style="width:24%;">
    <img src="scenario1_clean/1G/1G.png" alt="Similarity Scenario 1G" style="width:24%;">
    <img src="scenario1_clean/1H/1H.png" alt="Similarity Scenario 1H" style="width:24%;">
    </div>
    <p><em>
        Similarity score across the eight configurations (A-D top, E-H bottom) with respect to the gold standard in the Scenario 1. It is only shown the post-processed case, as there are no significant differences between them and the raw ones.
    </em></p>
</figure>

<figure style="text-align: left;">
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 0px;">
    <img src="scenario1_manual/measure_f.png" alt="Expert F-score Scenario 1" style="width:32%;">
    <img src="scenario1_no_clean/f1_1_noclean.png" alt="Raw F-score Scenario 1" style="width:32%;">
    <img src="scenario1_clean/f1_1_clean.png" alt="Post-processed F-score Scenario 1" style="width:32%;">
    </div>
    <p><em>
        Comparison of the F-score between the three different evaluations in the Scenario 1, expert-based (left), raw (center), and post-processed (right).
    </em></p>
</figure>

## Scenario 2

<figure style="text-align: left;">
    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 0px;">
    <img src="scenario2_no_clean/mean_column_sim.png" alt="Similarity Scenario 2 Raw" style="width:49%;">
    <img src="scenario2_clean/mean_column_sim.png" alt="Similarity Scenario 2 Post-processed" style="width:49%;">
    </div>
    <p><em>
        Similarity between raw (left) and post-processed (right) configurations with respect to the gold standard in Scenario 2.
    </em></p>
</figure>

<figure style="text-align: left;">
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 0px;">
    <img src="scenario2_manual/measure_f.png" alt="Expert F-score Scenario 2" style="width:32%;">
    <img src="scenario2_no_clean/mean_column_f_80.png" alt="Raw F-score Scenario 2" style="width:32%;">
    <img src="scenario2_clean/mean_column_f_80.png" alt="Post-processed F-score Scenario 2" style="width:32%;">
    </div>
    <p><em>
        Comparison of the F-score between the three different evaluations in the Scenario 2, expert-based (left), raw (center), and post-processed (right).
    </em></p>
</figure>

## Scenario 3

<figure style="text-align: left;">
    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 0px;">
    <img src="scenario3_no_clean/mean_column_sim.png" alt="Similarity Scenario 3 Raw" style="width:49%;">
    <img src="scenario3_clean/mean_column_sim.png" alt="Similarity Scenario 3 Post-processed" style="width:49%;">
    </div>
    <p><em>
        Similarity between raw (left) and post-processed (right) configurations with respect to the gold standard in Scenario 3.
    </em></p>
</figure>

<figure style="text-align: left;">
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 0px;">
    <img src="scenario3_manual/measure_f.png" alt="Expert F-score Scenario 3" style="width:32%;">
    <img src="scenario3_no_clean/f1_3_noclean.png" alt="Raw F-score Scenario 3" style="width:32%;">
    <img src="scenario3_clean/f1_3_clean.png" alt="Post-processed F-score Scenario 3" style="width:32%;">
    </div>
    <p><em>
        Comparison of the F-score between the three different evaluations in the Scenario 3, expert-based (left), raw (center), and post-processed (right).
    </em></p>
</figure>