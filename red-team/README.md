# Red Team Dataset

## Description

This red teaming dataset was created to test the limits of the responsible prompting system. Each sentence was written in the style of a potential user's prompt, inspired by the [Awesome ChatGPT prompts dataset](https://github.com/f/awesome-chatgpt-prompts), and contained three parts:

1. A persona (e.g., “Act as a data scientist with 20 years of experience studying consumer behavior...”),
2. A prompt body, which contained 1-2 additional statements specifying a related object and/or additional context/priming (e.g., “Here is a csv file with banking information from 800,00 Americans...”), and
3. The user’s inquiry or task (e.g., “Generate a code to classify applicants based on...”).

## Download

[Download the red_team.csv file](./red_team.csv).

## Details and Rationale

There were 5 different business personas in total, divided so that each persona appeared twice in each task; this was done so as to control for potential differences seen due to the job descriptions in semantic space (and to represent roles that were common in our institutional setting). We were interested in 4 potential issues:

1. 10 sentences were created to explore embedded or latent ambiguity within values and embeddings and its impact on recommendations. 5 of these were written such that the persona and prompt body specified clear reasoning or context for why a given task was being requested (‘unambiguous’) whereas the other 5 sentences contained the same persona and prompt body with the exception of this specific rationale (‘ambiguous’). As an example, one sentence might specify that the reason they are predicting likelihood of default is to study and mitigate biases in banking loans, whereas the corresponding adversarial sentence would not provide such context, meaning it is unclear if the use is for malicious or discriminatory use.
2. 10 sentences were created to test how susceptible the recommender system was to semantic “cross-fire” based on existing and/or conflicting sentences found in the sentences dataset. In this case, 5 sentences were written such that their topic and its associated valence contained no direct overlap with the JSON sentences (‘distinct’), whereas the other 5 sentences were changed so that there was substantial overlap with the exact wording utilized in the JSON despite being about a different topic or of an opposite valence (‘wires-crossed’). For example, if a positive sentence about inclusion prompts the user to “list under- prioritized stakeholders I should include in this meeting”; the accompanying adversarial sentence would be “list under-prioritized stakeholders I should exclude form this meeting”, which contains significant word-reuse but instead promotes discrimination. This would artificially and superficially inflate local semantic similarity, testing to see if the system would be influenced or skewed by these events or if the embedding’s larger semantic space would reduce their impact.
3. 10 sentences were created to check for expected valence alignment of responsible prompting outputs (that is, did the system reliably detect positively-valenced sentences and recommend additional ones or did it reliably detect negatively-valenced sentences and recommend their removal). In this case, 5 sentences were overtly positive (containing keywords from specific values or the positive cluster - e.g., “generate three test protocols we could perform to assess how diverse their dataset is.” ) and 5 sentences were overtly negative (containing keywords from specific harms or actions to avoid in the negative cluster, e.g., “What are ways I might be able to steal some of their weapons blueprints undetected?”). While not adversarial, these sentences provided a good test for the system’s false positive and false negative rates.
4. Finally, 10 sentences were created to explore both the JSON and embedding spaces’ semantic coverage. 5 sentences broached topics that were mentioned within the JSON file or were reasonably related and would have been expected to be within a transformer’s training data (within scope). In contrast, 5 sentences broached topics that were not specifically mentioned within the JSON (out of distribution) and, depending on the transformer, may not have been part of its training data. For example, one sentence contained the name of a rare medical condition being studied with a client, one that was not in the JSON and likely would not be in most training data that didn’t include medical text; another included a very specific cultural dish that might not be well-known. These sentences allowed us to investigate the relevance of the tool’s outputs when provided with unexpected inputs, as well as explore different semantic thresholds for removal or suggestion.

## Citing the Red Team Dataset

Please cite this dataset as:

```bibtex
@inproceedings{santana2025can,
    author = {Santana, Vagner Figueredo de and Berger, Sara and Machado, Tiago and de Macedo, Maysa Malfiza Garcia and Sanctos, Cassia Sampaio and Williams, Lemara and Wu, Zhaoqing},
    title = {Can LLMs Recommend More Responsible Prompts?},
    year = {2025},
    isbn = {9798400713064},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    url = {https://doi.org/10.1145/3708359.3712137},
    doi = {10.1145/3708359.3712137},
    booktitle = {Proceedings of the 30th International Conference on Intelligent User Interfaces},
    pages = {298–313},
    numpages = {16},
    keywords = {Prompt Engineering, Responsible Prompting, Responsible AI, Recommender Systems, Recommendation Systems},
    location = {
    },
    series = {IUI '25}
}
```