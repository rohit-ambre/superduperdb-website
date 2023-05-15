---
marp: true
theme: css/style
paginate: true
fontSize: 10px
backgroundColor: #ffffff
backgroundImage: _url('https://marp.app/assets/hero-background.svg')
style: |

  a:link {
    color: #6610f2;
  }

  h1 {
    color: #4527a4;
  }
  h2 {
    padding-bottom: 10px;
    color: #4527a4;
  }
  section {
    font-size: 30px;
  }
  img[alt~="center"] {
    display: block;
    margin: 0 auto;
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0rem;
  }
  
---

<!---

<style scoped>
table {
  font-size: 20px;
}
</style>


## The Ask: 1 year, 1.2 million €

### The initial funding will go mainly towards development and research



| Item                 | Count | Cost unit (€) | Cost (€) |
| -------------------- | ----- | ------------- | -------- |
| Python developer     | 3     | 80,000        | 240,000  |
| Cloud engineer       | 2     | 90,000        | 180,000  |
| Research scientist   | 2     | 100,000       | 200,000  |
| Frontend             | 1     | 80,000        | 80,000   |
| Marketing            | 2     | 60,000        | 120,000  |
| Management           | 2     | 100,000       | 200,000  |
| Miscellaneous        | 1     | 200,000       | 200,000  |

-->

# Additional slides

---

## Example: with SuperDuperDB instantly deploy a full-stack of e-Commerce AI

![center w:950](images/cycle-linear-e-commerce.svg)

---

## Strategy: Open-core

- Hosting on GitHub with project page and full documentation
- Use standard scaling strategies on GitHub to gain viral adoption
- Basis on most popular components, leads to high adoption:
  - PyTorch (used by openAI)
  - MongoDB (most popular document store)
- Core functionality open-source
- Bells and whistles not included

---

## Strategy: Managed cloud hosted services

- Host fully managed and configurable SuperDuperDB deployments
  - AWS
  - GCloud
  - Azure
- Integration to existing hosted MongoD deployments possible

---

## Strategy: Managed onsite self-hosting

- Compiled binaries for easy self-hosting
- Support and consultation

---

## Strategy: Marketplace

- Marketplace of models and datasets
- Enable third-party sellers to revenue
- Enable friendly agreements with competition e.g. Hugging Face

---

## Strategy: Tune-ups and interfaces

- Open-core contains key-functionality
- Sell licenses for:
  - User interfaces
  - High-level work flows
  - Validation dashboards and management

---

## Strategy: Professional services 

- Tiered support
- Certifications
- Coaching and on-site consulting

---

## Strategy: Vertical expansion

- Bespoke models for key use-cases
- In-house team of data-scientists and SuperDuperDB specialists build models
- Integration to hosted or non-hosted SuperDuperDB deployment
- Per-request or per-model pricing possible

---

## Paradigmatic use-cases

- Reuters: news classification and aggregation with AI
- Crunchbase: company recommendation and understanding
- Zalando: full stack AI for semantic navigation and recommendation
- Wikipedia: tag extraction and summarization
- Deutsche Industrie Mittelstand: automated quality control using computer vision
- Cisco systems: anomaly prediction and early threat detection (edited)
- Biontech: drug candidate pre-screening and classification

---

## Recent developments in LLMs

- Alpaca
- LlaMa - leaked to the public (by Meta AI)
- Many incremental improvements based on recent research

---

<style scoped>
table {
  font-size: 15px;
}
</style>

## There is nothing out there like SuperDuperDB

<center>



| | [SuperDuperDB](https://www.superduperdb.com/) | [MindsDB](https://mindsdb.com/) | [PostGresML](https://postgresml.org/) | [DeepLake]() | [LanceDB](https://eto.ai/) | [Continual](https://continual.ai/) | [PineCone](https://www.pinecone.io/) | [Chroma](https://docs.trychroma.com/) |
| - | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| AI models in database | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Open Source | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ |
| Unified environment | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |❌| ❌ |
| Train AI models in database | ✅ | ✅ | ✅ | ❓ | ❌ | ❌ | ❌ | ❌ |
| Arbitrary AI models | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ |❌| ❌ |
| Vector Search | ✅ | ❌ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Flexible data types | ✅ | ❌ | ❌ | ✅ | ✅ | ❓ | ❌ | ❌ |
| Scalable compute | ✅ | ❌ | ❌ | ❌ | ❓ | ❌ | ✅ | ❌ |
| Python first | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Arbitrary datastore |✅  | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

</center>

---

![](images/architecture_detailed.png)

---

## Use case: vector search with OpenAI

```python
>>> from superduperdb.apis.openai import Embedding
>>> docs.insert_many([d for d in data])
>>> docs.create_model(Embedding('text-embedding-ada-002'), keys=['text'])
>>> docs.find(like={'text': 'Articles about biotech'}, semantic_index='gpt4/text')
```

---

## Use case: vector search with OpenAI

```python
>>> from sentence_transformers import pipeline
>>> docs.create_model(pipeline('multi-qa-distilbert-dot-v1'), keys=['text'])
>>> docs.find({'text': 'Articles about biotech'}, semantic_index='multi-qa-distilbert-dot-v1')
```

---

## Use case: personal assistant referencing private voice memos 

```python
>>> import torch
>>> from superduperdb.models.openai import RetrievalChatCompletion
>>> model, decoder, utils = torch.hub.load(repo_or_dir='snakers4/silero-models', model='silero_stt', language='en')
>>> docs.create_model(model, preprocess=utils[-1], postprocess=decoder, keys=['audio'])
>>> docs.create_model(pipeline('multi-qa-distilbert-dot-v1'), keys=['audio'], features={'audio': 'silero_stt'})
>>> docs.create_model(RetrievalChatCompletion('gpt-4'), features={'audio': 'multi-qa-distilbert-dot-v1'})
>>> docs.predict_one('gpt-4', 'Is there a reference here to the roadmap from September?')
```

---

## Use case: anomaly detection for SAP-like companies

```python
>>> from transformers import *  # use Hugging-Face library (open-source)
>>> from my_codebase.models import VAE   # in-house code-base for anomaly detection
>>> import torch                       # torch standard library
>>> docs.create_model('bert', BertModel(BertConfig()), key='text')
>>> docs.create_learning_task('anomaly',
...                           model={'input': 'text', 'model': VAE()}, 
...                           target={'input': 'text', 'model': torch.nn.Identity()},
...                           features={'text': 'bert'},
...                           loss={'anomaly-loss': torch.nn.BCELoss()})
# (lots of output) model trains aynschronously on server
>>> outliers = docs.find({'_outputs.text.anomaly': {'$leq': 0.001}})  # find outliers with database query
```

---

## Use-case: e-Commerce semantic text-search, similar product recommendation, reverse image search

```python
>>> products.insert_many(product_list)
>>> products.create_learning_task(
...    'shop_index',
...    [{'name': 'text-searcher', 'object': text_model, 'key': 'query'},
...     {'name': 'product-indexer', 'object': product_model, 'key': 'product'},
...     {'name': 'street-image', 'object': image_model, 'key': 'image'}]
... )
>>> docs.find({'brand': 'Adidas'}, like={'query': 'leopard print t-shirt'})
>>> docs.find({'brand': 'Nike'}, like={'image': {'_content': {'url': '<image-url'}}})
```

