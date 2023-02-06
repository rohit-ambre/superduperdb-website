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

---

# Additional slides

---

## Example: with SuperDuperDB instantly deploy a full-stack of e-Commerce AI

![center w:950](images/cycle-linear-e-commerce.svg)

---

## Competition: MindsDB [:link:](https://mindsdb.com/) is the only apparent competitor in this space

### MindsDB's approach is nothing like SuperDuperDB and is not ready for fully fledged modern AI

<style scoped>
table {
  font-size: 16px;
}
</style>

| MindsDB                | SuperDuperDB                      |
| ---------------------- | --------------------------------- |
| Predefined models only | Bring any model                   |
| Relational             | Relational+Object                 |
| Inbuilt trainer        | Arbitrary training                |
| CPU only               | multi-GPU                         |
| SQL query              | Fully semantic search queries     |
| Small data             | Big data                          |
| Table data only        | Full content: images, text, video |

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


