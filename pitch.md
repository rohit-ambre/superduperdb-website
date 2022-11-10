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
  
---

<!-- _class: lead 
_backgroundColor: #4527a4;
-->

![bg center w:800](logos/white_on_purple.svg)

---

## Integrating AI and applying AI to data is a huge challenge

- Our experience with scores of large organizations bears this out
- Companies with 8 figure revenue waste 10s-100 of millions $ on doing this

---

## The AI lifecycle can be highly complex and interdependent

![center w:800](images/workflow.svg)

---

## Each building block is supported by different providers

![center w:650](images/mlops_logos.svg)

---

## No existing solution supports these steps in a unified way

---

## Traditional AI includes all knowledge *in* the model

![center w:500](images/mozart.svg)

This is contrary to human intelligence, which incorporates external knowledge, and uses fluid intelligence to make inferences based on this external knowledge

---

## However, the latest developments allow AI to "look up" information

![center w:500](images/mozart_reml.svg)

From the internet, from books, from user feedback ...

---

## This means new AI needs to interoperate closely with the data

- Looking up important insights from the data
- Reading new streaming data
- Updating data on the fly
- Pushing incoming data through the AI model

---

## No existing solution can handle these needs

---

# Introducing SuperDuperDB

---

## SuperDuperDB

### ...aims to revolutionize how companies and organizations work with and apply AI to their data

---

## SuperDuperDB

### ...is based on the fact that *true AI* unites deep learning and data insights

![center](images/equation.svg)

---

## SuperDuperDB

### ...will unite best in class database and deep learning software

![center w:600](images/connector.svg)

---

## SuperDuperDB

### ...will lead to deployments and development with never seen before simplicity

1 python command creates deployed multimodal semantic search

```python
collection.create_semantic_index(
    filter={'vertical': 'groceries'},
    model=my_model,    # user supplied PyTorch model
    keys=['query', 'product']
)
```

---

## SuperDuperDB

### ...will allow users to navigate data in a totally new way using the power of AI

Semantic indices available with `$like` operator

```python
results = collection.find({
    'vertical': 'groceries',
    'shop': 'cosco',
    '$like': {'document': example, 'n': 10}
})
```

---

## SuperDuperDB

### ...is infinitely modifiable

...and makes any learning problem with (sub)records as datapoints doable

```python
collection.create_model(
    filter={'type': 'legal'},
    model=second_model,
    loss=my_loss,
    metrics=my_metrics,
)
```

---

<style scoped>
span {
  font-size: 16px;
}
</style>

## SuperDuperDB listens to inserts and updates

### Model outputs are encoded in vanilla MongoDB

```
{'_id': ObjectId('6360d90ccc1a1937d5d8d428'),
 'information': {'image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x640 at 0x10B5CBBE0>,
                 'price': '£112.03',
                 'snippet': '',
                 'title': 'Sealey Suspension Arm Lever VS3815 Vehicle'}}
```

---

## Design decisions

### PyTorch is the most popular AI framework among experts

(Source: [horace.io](http://horace.io/pytorch-vs-tensorflow/))

| Rank | Percentage Papers | Framework  |
| ---- | ----------------- | ---------- |
| 1.   | 84%               | PyTorch    |
| 2.   | 16%               | Tensorflow |

---

## Design decisions

### MongoDB is the most popular document store in use today

(Source: [db-engines.com](https://db-engines.com/en/ranking/document+store))

| Rank | Database                  | Score |
| ---- | ------------------------- | ----- |
| 1.   | MongoDB                   | 486   |
| 2.   | Amazon DynamoDB           | 88    |
| 3.   | Databricks                | 58    |
| 4.   | Microsoft Azure Cosmos DB | 40    |

---

## Design decisions

### Experience building agile AI in Academia, Zalando, LF1 and Attraqt

PyTorch together with MongoDB allow for deep learning built ***with ease on a shoestring***.

Developers ***love*** these tools ***passionately***.

---

## The founder

### Duncan Blythe

- Graduated first in class Oxford Mathematics 2007
- MMathPhil, MSc, PhD
- 1,000s citations on published top AI research
- 10,000s of stars on GitHub open source
- Exited AlephSearch (bootstrapped) 2020 with team of 2 for mid 7-figure
- Gamut of skills: deep learning, software development, infrastructure, management, lean startup

---

## Progress

- Working prototype v0.1 in Python
- Installable via Python `pip`
- Initial traction via social media
- Response positive

---

## Business models

- Tiered managed cloud service
- On premises solution with technical support
- Model repository (like "App Store")
- Sub-brands:
  - **LegalTech/ NLP/ e-Commerce/ Biomedical/ Cybersecurity...**
- Consulting
- Certifications

---

## Market

### 2019

![w:600](images/venn-now.svg)

---

## Market

### 2022 

![w:600](images/venn-future-logo-1.svg)

---

## Market

### 2023 onwards

![w:600](images/venn-future-logo-2.svg)

---

## Market

### Databases

A huge market with unprecedented growth (source: [gartner.com](https://blogs.gartner.com/merv-adrian/2022/04/16/dbms-market-transformation-2021-the-big-picture/))

| Year | Market Size ($) |
| ---  | --------------- |
| 2022 | 80 Billion      |
| 2020 | 65 Billion      |
| 2017 | 39 Billion      |

---

## Market

### AI software

A burgeoning new market already with huge reach (source: [gartner.com](https://www.gartner.com/en/newsroom/press-releases/2021-11-22-gartner-forecasts-worldwide-artificial-intelligence-software-market-to-reach-62-billion-in-2022))

| Year | Market Size ($) |
| ---- | --------------- |
| 2022 | 63 Billion      |
| 2021 | 52 Billion      |

---

## Timeline

![center](images/timeline.svg)

---

<style scoped>
table {
  font-size: 20px;
}
</style>

## The Ask

**1 year, 1.2 million €**

| Item                 | Count | Cost unit (€) | Cost (€) |
| -------------------- | ----- | ------------- | -------- |
| Python developer     | 3     | 80,000        | 240,000  |
| Cloud engineer       | 2     | 90,000        | 180,000  |
| Research scientist   | 2     | 100,000       | 200,000  |
| Marketing            | 1     | 60,000        | 60,000   |
| Cloud Infrastructure | 1     | 100,000       | 100,000  |
| Management           | 1     | 100,000       | 100,000  |
| Miscellaneous        | 1     | 200,000       | 200,000  |