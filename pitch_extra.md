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

<style scoped>
table {
  font-size: 15px;
}
</style>

## There is nothing out there like SuperDuperDB

<center>

| | [SuperDuperDB](https://www.superduperdb.com/) | [MindsDB](https://mindsdb.com/) | [Databricks](https://www.databricks.com/) | [Snowflake](https://docs.snowflake.com/en/developer-guide/snowpark/index) | [AWS Sagemaker](https://aws.amazon.com/sagemaker/) | [Eto](https://eto.ai/) | [Brytlyt](https://brytlyt.io/) | [Continual](https://continual.ai/) | 
| - | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| AI models in database | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Open Source | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| Unified environment | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |❓| ✅ |
| Train AI models in database | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❓ | ❌ |
| Arbitrary AI models | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ |❓| ❌ |
| Vector Search | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| Flexible data types | ✅ | ❌ | ❌ | ❌ | ❌ | ❓ | ❌ | ❌ |
| Flexible AI Operators | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Python first | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ |

</center>

---

## Case study: Snowpark

[https://github.com/Snowflake-Labs/sfguide-citibike-ml-snowpark-python/blob/main/03_ML_Engineering.ipynb](https://github.com/Snowflake-Labs/sfguide-citibike-ml-snowpark-python/blob/main/03_ML_Engineering.ipynb)

---

![](images/architecture_detailed.png)

---

## Use case: anomaly detection for SAP-like companies

```python
>>> from transformers import *  # use Hugging-Face library (open-source)
>>> from my_codebase.models import VAE   # in-house code-base for anomaly detection
>>> import torch                       # torch standard library
>>> docs.create_model('bert', BertModel(BertConfig()), key='text')
>>> docs.create_imputation('anomaly',
...                        model={'input': 'text', 'model': VAE()}, 
...                        target={'input': 'text': 'model': torch.nn.Identity()},
...                        features={'text': 'bert'},
...                        loss={'anomaly-loss': torch.nn.BCELoss()})
# (lots of output) model trains aynschronously on server
>>> outliers = docs.find({'_outputs.text.anomaly': {'$leq': 0.001}})  # find outliers with database query
```

---

## Use-case: e-Commerce semantic text-search, similar product recommendation, reverse image search

```python
>>> products.insert_many(product_list)
>>> products.create_semantic_index(
...    'shop_index',
...    [{'name': 'text-searcher', 'object': text_model, 'key': 'query'},
...     {'name': 'product-indexer', 'object': product_model, 'key': 'product'},
...     {'name': 'street-image', 'object': image_model, 'key': 'image'}]
... )
# single line for semantic text-search
>>> docs.find({'brand': 'Adidas'}, like={'query': 'leopard print t-shirt'})
# single line for reverse image-search from web-url
>>> docs.find({'brand': 'Nike'}, like={'image': {'_content': {'url': '<image-url'}}})
```

---

## Use-case: open-AI API + CI-CD quality control for automatic programming

"Write a function called `f` which extracts the base URL from any URL"

```python
>>> unittest_collection.insert_many(programming_tasks)
>>> unittest_collection.create_model(
...     'codex',  
...     api='https://api.openai.com/v1/models/codex',
...     method='POST',
...     headers={'Authorization': 'Bearer <YOUR_API_KEY>',
...              'OpenAI-Organization': '<YOUR_ORG_ID>'},
... )
>>> for test_function, id_ in test_suite:
...     unittest_collection.create_model(id_, test_function, key='_outputs.desc.codex', features={'desc': 'codex'})     
>>> unittest_collection.insert_one({
...     '_id': ObjectId(my_id),
...     'desc': 'write a function in python called `f` which sorts documents in MongoDB using `aggregate`'
... })
# get the answer, quality controlled and checked
>>> unittest_collection.find_one({'_id': ObjectId(my_id)}, {'_outputs': 1})
{
  '_outputs': {'desc': 'codex': 'def f(query, docs):\n    docs.aggregate(\n...)'}
}
```

---

## Use-case: in-house chat-bots which answer questions about *your* data

Hot off the press! Open Source Chat-GPT like model [here](https://github.com/nebuly-ai/nebullvm/tree/main/apps/accelerate/chatllama).

```python
>>> docs.insert_many(textual_data)
>>> docs.create_imputation(
...     'gpt-llama',  
...     model={'object': LLaMa(), 'name': 'llama'},
...     target={'object': Tokenizer(), 'name': 'tokenizer'}
...     loss=torch.nn.CrossEntropy(),
... )
>>> docs.create_imputation(
...     'reward-model',  
...     model={'object': RewardModel(), 'name': 'reward', varieties=['model', 'loss']},
...     target={'object': Identity(), 'name': 'quality'}
...     loss=torch.nn.MSELoss(),
... )
>>> docs.create_maximizer(
...     'ppo-model',
...     model={'object': RewardModel(), 'name': 'ppo'},
...     loss='reward',
... )
```
