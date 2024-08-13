[![Build Status](https://app.travis-ci.com/IBM/responsible-prompting-api.svg?token=3QHapyMs1C2MgHcEzaRi&branch=main)](https://app.travis-ci.com/IBM/responsible-prompting-api)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# Responsible prompting API
Responsible Prompting is an LLM-agnostic tool that aims at dynamically supporting users in crafting prompts that reflect responsible intentions and help avoid undesired or negative outputs.

## Usage
This API is composed by a `Flask server` that hosts the `recommend` route, the `swagger` files and a responsible prompting `demo`.
You can run the server locally to execute requests and obtain responsible prompting recommendations according to `swagger` description.

### Instructions on how to run the server locally
This short tutorial assumes that you have:
- A machine with python 3.9 installed
- A Hugging Face access token: https://huggingface.co/docs/hub/en/security-tokens

### Steps to start the server
1. In your terminal, clone this repository and `cd` into `responsible-prompting-api` folder
2. Create a virtual environment with `python -m venv <name-of-your-venv>` 
3. Activate your virtual environment with `source <name-of-your-venv>/bin/activate`
4. Execute `pip install -r requirements.txt` to install project requirements
5. Generate a Hugging Face access token: https://huggingface.co/docs/hub/en/security-tokens
6. In the `.env` file, replace `<include-token-here>` with your hugging face access token: 
```
HF_TOKEN= <include-token-here>
```
5. Execute `python app.py`
6. Check if the message `* Serving Flask app 'app'` appears and you are good to go!
7. In your browser, access http://127.0.0.1:8080/ and you will see the message 'Ready!'

### Running the demo and accessing server routes

#### Steps to run the demo
1. If not, generate a Hugging Face access token: https://huggingface.co/docs/hub/en/security-tokens
2. In line 140 of [index.html](https://github.com/IBM/responsible-prompting-api/blob/main/static/demo/index.html), replace `<include-token-here>` with your hugging face access token: 
```
headers: {"Authorization": "Bearer <include-token-here>"}
```
3. Run the server (if it is not already running)
4. In your browser, access: http://127.0.0.1:8080/static/demo/index.html

### Check the API swagger
1. Run the server (if it is not already running)
2. In your browser, access: http://127.0.0.1:8080/swagger

In swagger, you can test the API and understand how to make requests.

### Get recommendations
1. Run the server (if it is not already running)
2. In your browser, access: http://127.0.0.1:8080/recommend and pass your parameters, here are request examples with 
the prompt: `Act as a data scientist with 8 years of experience. Provide suggestions of what to do to make the data science project more inclusive.`

#### Using curl

Just copy and paste this in your terminal (make sure you have curl installed): 

```
curl -X 'GET' \
  'http://127.0.0.1:8080/recommend?prompt=Act%20as%20a%20data%20scientist%20with%208%20years%20of%20experience.%20Provide%20suggestions%20of%20what%20to%20do%20to%20make%20the%20data%20science%20project%20more%20inclusive.' \
  -H 'accept: */*' \
  -H 'add_lower_threshold: 0.3' \
  -H 'add_upper_threshold: 0.5' \
  -H 'remove_lower_threshold: 0.3' \
  -H 'remove_upper_threshold: 0.5' \
  -H 'model_id: sentence-transformers/all-minilm-l6-v2'
```

#### Making a request directly in the browser

Just copy and paste this in your browser:
```
http://127.0.0.1:8080/recommend?prompt=Act as a data scientist with 8 years of experience. Provide suggestions of what to do to make the data science project more inclusive.
```

#### Example response
The response should look like this:

```json
{
  "add": [
    {
      "prompt": "What participatory methods might I use to gain a deeper understanding of the context and nuances of the data they are working with?",
      "similarity": 0.49432045646542666,
      "value": "participation"
    },
    {
      "prompt": "Be inclusive of individuals with non-traditional backgrounds and experiences in your response.",
      "similarity": 0.48868733465585423,
      "value": "inclusion and diversity"
    },
    {
      "prompt": "Can you suggest some techniques to handle missing data in this dataset?",
      "similarity": 0.47995963514385853,
      "value": "progress"
    },
    {
      "prompt": "How do I make this dataset compatible with our analysis tools?",
      "similarity": 0.47405629104549163,
      "value": "transformation"
    },
    {
      "prompt": "Consider the potential impact of the data, question, or instruction on individuals and society as a whole.",
      "similarity": 0.4739456017558868,
      "value": "awareness"
    }
  ],
  "remove": []
}
```

## File structure

This is the current structure of the repository files:
```
.
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── Dockerfile
├── LICENSE
├── MAINTAINERS.md
├── README.md
├── SECURITY.md
├── app.py
├── config.py
├── control
│   └── recommendation_handler.py
├── helpers
│   └── get_credentials.py
├── prompt-sentences-main
│   ├── README.md
│   ├── prompt_sentences-all-minilm-l6-v2.json
│   ├── prompt_sentences-bge-large-en-v1.5.json
│   ├── prompt_sentences-multilingual-e5-large.json
│   ├── prompt_sentences-slate-125m-english-rtrvr.json
│   ├── prompt_sentences-slate-30m-english-rtrvr.json
│   ├── prompt_sentences.json
│   ├── sentences_by_values-all-minilm-l6-v2.png
│   ├── sentences_by_values-bge-large-en-v1.5.png
│   ├── sentences_by_values-multilingual-e5-large.png
│   ├── sentences_by_values-slate-125m-english-rtrvr.png
│   └── sentences_by_values-slate-30m-english-rtrvr.png
├── requirements.txt
└── static
    ├── demo
    │   ├── index.html
    │   └── js
    │       └── jquery-3.7.1.min.js
    └── swagger.json
```
<!-- This repository contains some example best practices for open source repositories:

* [LICENSE](LICENSE)
* [README.md](README.md)
* [CONTRIBUTING.md](CONTRIBUTING.md)
* [MAINTAINERS.md](MAINTAINERS.md)
A Changelog allows you to track major changes and things that happen, https://github.com/github-changelog-generator/github-changelog-generator can help automate the process
* [CHANGELOG.md](CHANGELOG.md)

> These are optional

The following are OPTIONAL, but strongly suggested to have in your repository. 
* [dco.yml](.github/dco.yml) - This enables DCO bot for you, please take a look https://github.com/probot/dco for more details.
* [travis.yml](.travis.yml) - This is a example `.travis.yml`, please take a look https://docs.travis-ci.com/user/tutorial/ for more details.

These may be copied into a new or existing project to make it easier for developers not on a project team to collaborate.-->

<!-- A notes section is useful for anything that isn't covered in the Usage or Scope. Like what we have below. -->
## Notes

<!-- **NOTE: While this boilerplate project uses the Apache 2.0 license, when
establishing a new repo using this template, please use the
license that was approved for your project.**

**NOTE: This repository has been configured with the [DCO bot](https://github.com/probot/dco).
When you set up a new repository that uses the Apache license, you should
use the DCO to manage contributions. The DCO bot will help enforce that.
Please contact one of the IBM GH Org stewards.** -->

<!-- Questions can be useful but optional, this gives you a place to say, "This is how to contact this project maintainers or create PRs -->
If you have any questions or issues you can create a new [issue here][issues].

Pull requests are very welcome! Make sure your patches are well tested.
Ideally create a topic branch for every separate change you make. For
example:

1. Fork the repo
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Added some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## License

<!-- All source files must include a Copyright and License header. The SPDX license header is 
preferred because it can be easily scanned. -->

If you would like to see the detailed LICENSE click [here](LICENSE).

<!-- 
```text
#
# Copyright IBM Corp. 2023 - 2024
# SPDX-License-Identifier: Apache-2.0
#
``` -->
## Authors

- Author: Vagner Santana vsantana@ibm.com
- Author: Melina Alberio
- Author: Cássia Sanctos csamp@ibm.com
- Author: Tiago Machado Tiago.Machado@ibm.com

[issues]: https://github.com/IBM/repo-template/issues/new
