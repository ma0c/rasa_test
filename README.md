# Test RASA NLU

First install rasa and spacy

```bash
python -m venv rasa_env
pip install rasa
pip install spacy
```

Configure your config file in [config.yml](config.yml)

```yaml
language: "en"

pipeline: "pretrained_embeddings_spacy"
```

Then configure the spacy package to work with english

```bash
python -m spacy download en
```

Then run the trainer

```bash
rasa train nlu
```

And you can check the model

```bash
rasa shell nlu
```
