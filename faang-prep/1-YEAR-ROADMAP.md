# 1-YEAR FAANG PREPARATION ROADMAP

**Goal:** Full-Stack + ML Engineer ready for FAANG interviews

---

## OVERVIEW

**Total Duration:** 52 weeks (1 year)

- **Phase 1:** Foundations (Weeks 1-8) - Python + Core DS&A Patterns
- **Phase 2:** Apply + Build Projects (Weeks 9-20) - Event Scraper, Data Pipeline, ML Model
- **Phase 3:** ML Deep Dive (Weeks 21-36) - ML fundamentals + Advanced projects
- **Phase 4:** Interview Prep Sprint (Weeks 37-52) - Intensive practice + Mock interviews

**Total Problems by End:** ~200-250 quality problems
**Total Projects:** 3-4 production-ready projects with ML components

---

## PHASE 1: FOUNDATIONS (Weeks 1-8)

### Weeks 1-2: Python Fluency + Basic Patterns

**Patterns to Master:**

- Hash Maps (O(1) lookups, frequency counting)
- Two Pointers (sorted arrays, palindromes)
- Sliding Window (subarrays, substrings)
- Array/String manipulation

**Daily Time:**

- Weekdays: 1-1.5 hours (1 problem + pattern notes)
- Weekends: 3-4 hours (3 problems + review)

**Total Problems:** 15 problems (deeply understood)

**Key Deliverables:**

- Can write Python without AI assistance
- Understand when to use hash map vs array vs set
- Master list comprehensions, dictionary methods, string slicing

---

### Weeks 3-4: Intermediate Patterns

**New Patterns:**

- Stack/Queue problems
- Fast & Slow Pointers (linked lists, cycle detection)
- Sorting variations
- Binary Search

**Same Structure:** 1 problem weekdays, 3 on weekends

**Total Problems:** 15 problems

**Week 4 Milestone:**

- Review all 30 problems from Weeks 1-4
- Redo 5 random problems from memory without looking at solutions
- Update pattern documentation

---

### Weeks 5-6: Trees Deep Dive

**What You'll Learn:**

- Binary Trees, Binary Search Trees
- Tree Traversals: DFS (Preorder, Inorder, Postorder)
- BFS (Level-order traversal)
- Recursion patterns for trees
- When to use DFS vs BFS

**Structure:**

- Weekdays: 1 tree problem (30-45 min)
- Weekends: 2 tree problems + review (3-4 hours)

**Total Problems:** 12-15 tree problems

**Projects:**

- Implement your own Binary Tree class
- Build a tree visualizer (optional but helpful)

---

### Weeks 7-8: Graphs Deep Dive

**What You'll Learn:**

- Graph representations (adjacency list, adjacency matrix)
- DFS on graphs (connected components, path finding)
- BFS on graphs (shortest path)
- Topological sort
- Union Find basics

**Structure:** Same as trees

**Total Problems:** 12-15 graph problems

**Week 8 Major Milestone:**

- Complete review of all 60-70 problems
- Redo 10 random problems timed
- Can explain all major patterns confidently
- Assessment: Mock interview with peer or platform

---

## PHASE 2: APPLY + BUILD (Weeks 9-20, ~3 months)

### Strategy Shift:

- **Problem-solving:** 3 problems/week (1-1.5 hours total) - MAINTENANCE MODE
- **Building:** Rest of time on real projects

---

### Weeks 9-12: PROJECT 1 - Event Scraper

**Goal:** Build a production-ready web scraper with API and database

**Tech Stack:**

- Python (web scraping: BeautifulSoup, Selenium, Scrapy)
- PostgreSQL (data storage)
- Flask (REST API)
- Docker (containerization)

**Weekly Breakdown:**

- Week 9: Setup + Basic scraper (scrape event data from 1-2 websites)
- Week 10: Database design + storage layer
- Week 11: Flask API + CRUD operations
- Week 12: Error handling, logging, deployment

**Deliverables:**

- GitHub repo with clean code
- README with setup instructions
- Deployed API (Heroku/Railway/similar)
- Can scrape, store, and serve event data via API

**Continue:** 3 problems/week (mix of patterns from Phase 1)

---

### Weeks 13-16: PROJECT 2 - Stock Data Pipeline

**Goal:** Build ETL pipeline for stock market data

**Tech Stack:**

- Data ingestion (APIs: Alpha Vantage, Yahoo Finance)
- Pandas (data transformation)
- PostgreSQL/TimescaleDB (time-series storage)
- Airflow or Prefect (orchestration)
- Data validation (Great Expectations)

**Weekly Breakdown:**

- Week 13: Data ingestion - API integration, handle rate limits
- Week 14: Data transformation - clean, normalize, feature engineering
- Week 15: Storage + validation - schema design, data quality checks
- Week 16: Orchestration - scheduled jobs, monitoring, alerts

**Deliverables:**

- Automated pipeline running daily
- Historical data for 50+ stocks
- Data quality dashboards
- Documentation of pipeline architecture

**Continue:** 3 problems/week (start introducing medium difficulty)

---

### Weeks 17-20: PROJECT 3 - Stock Analytics ML Model (MVP)

**Goal:** Build basic ML model for stock prediction/analysis

**Tech Stack:**

- Scikit-learn (ML models)
- Pandas (feature engineering)
- Matplotlib/Plotly (visualization)
- Jupyter notebooks (experimentation)

**Weekly Breakdown:**

- Week 17: EDA + feature engineering (technical indicators, lagged features)
- Week 18: Model training - linear regression, random forest, basic evaluation
- Week 19: Model evaluation - cross-validation, metrics, backtesting
- Week 20: Documentation + presentation - what worked, what didn't, insights

**Deliverables:**

- Jupyter notebooks with full analysis
- Basic prediction model with evaluation metrics
- Insights document on what features matter
- GitHub repo with clean, documented code

**Continue:** 3 problems/week

**Phase 2 Checkpoint:**

- 3 portfolio projects live
- ~36-45 additional problems solved (total: ~100-115)
- Strong Python + data engineering skills
- Basic ML experience

---

## PHASE 3: ML DEEP DIVE + ADVANCED BUILDING (Weeks 21-36, ~4 months)

### Weeks 21-24: ML Fundamentals Theory + Practice

**Learning:**

- Supervised Learning: Linear/Logistic Regression, Decision Trees, Random Forests, Gradient Boosting
- Unsupervised Learning: K-Means, PCA, t-SNE
- Model evaluation: Confusion matrix, ROC curves, precision/recall
- Cross-validation, hyperparameter tuning
- Bias-variance tradeoff

**Resources:**

- Andrew Ng's ML course (Coursera) - 1 hour/day
- Hands-On Machine Learning (book) - practical exercises

**Practice:**

- Kaggle competitions (beginner level)
- Improve your stock model with new techniques

**Problem-solving:** 2-3 problems/week (now including some harder problems)

---

### Weeks 25-28: Advanced ML + Feature Engineering

**Learning:**

- Time series specific: ARIMA, Prophet, LSTM basics
- Feature engineering techniques
- Handling imbalanced data
- Ensemble methods

**Project:** Upgrade Stock Analytics Model

- Advanced features
- Multiple model comparison
- Better evaluation metrics
- Simple web interface (Streamlit or Flask)

**Problem-solving:** 2-3 problems/week

---

### Weeks 29-32: Deep Learning Basics

**Learning:**

- Neural network fundamentals
- PyTorch or TensorFlow basics
- CNNs (if interested in image data)
- RNNs/LSTMs for sequences
- Transfer learning

**Resources:**

- Fast.ai course OR
- Deep Learning Specialization (Coursera)

**Practice:**

- Apply to stock prediction (LSTM for time series)
- Small side projects (image classification, text sentiment)

**Problem-solving:** 2-3 problems/week

---

### Weeks 33-36: MLOps + Production ML

**Learning:**

- Model deployment (Flask API, FastAPI)
- Model versioning (MLflow, DVC)
- Monitoring (data drift, model performance)
- A/B testing concepts
- CI/CD for ML

**Project:** Production ML Platform

- Deploy your stock model as API
- Add monitoring dashboard
- Implement model retraining pipeline
- Documentation for "production" use

**Problem-solving:** 2-3 problems/week (focus on medium-hard)

**Phase 3 Checkpoint:**

- Solid ML fundamentals + practical experience
- Production-ready ML project
- ~50-60 additional problems (total: ~150-175)
- Ready for ML system design discussions

---

## PHASE 4: INTERVIEW PREP SPRINT (Weeks 37-52, ~4 months)

### Weeks 37-40: Algorithm Intensive

**Focus:** Sharpen problem-solving skills to peak level

**Structure:**

- 5-7 problems per week
- Mix of all patterns from Phase 1
- Focus on medium difficulty
- Time yourself (45 min per problem max)
- Redo old problems from Phase 1 (timed)

**System Design:**

- Study 2-3 hours/week
- System Design Interview book
- YouTube: System Design Interview channel
- Focus on: scalability, databases, caching, load balancing

**Total New Problems:** 20-28
**Total Review:** 15-20 old problems

---

### Weeks 41-44: Mock Interviews + Medium/Hard Problems

**Structure:**

- 4-5 NEW problems per week (medium-hard difficulty)
- 2 mock interviews per week:
  - Pramp, Interviewing.io, or peers
  - 1 coding interview
  - 1 system design or ML system design
- Review and analyze every mock interview

**Behavioral Prep:**

- STAR method for all projects
- Prepare stories: leadership, conflict, failure, success
- Practice explaining technical decisions

**Company Research:**

- Target 5-10 companies
- Study their interview patterns (Blind, Glassdoor)
- Understand their tech stacks

**Total New Problems:** 16-20

---

### Weeks 45-48: Company-Specific Prep

**Structure:**

- Focus on target companies' common problems
- 3-4 hard problems per week
- Daily mock interviews (alternate coding/system design)
- Polish your projects for discussion:
  - Can explain every technical decision
  - Know the tradeoffs
  - Understand what you'd improve

**System Design Deep Dive:**

- Design: Twitter, Instagram, YouTube, Netflix
- ML Systems: Recommendation engine, Search ranking, Fraud detection
- Practice whiteboarding (use Excalidraw)

**Final Projects Polish:**

- Update READMEs
- Add architecture diagrams
- Deploy everything (make sure it's live)
- Create 5-min demo videos

**Total New Problems:** 12-16

---

### Weeks 49-52: FINAL PUSH

**Structure:**

- 2-3 hard problems per week
- Full mock interviews (2-3 per week)
- One complete "mock day" per week:
  - Phone screen (1 hour)
  - Technical round 1 (45 min)
  - Technical round 2 (45 min)
  - System design (1 hour)
  - Behavioral (30 min)

**Mental Prep:**

- Sleep schedule
- Stress management
- Confidence building (review your wins)

**Application Strategy:**

- Apply to target companies
- Leverage referrals
- Practice recruiter calls

**Total New Problems:** 8-12

**Phase 4 Checkpoint:**

- ~80-100 additional problems in Phase 4
- **TOTAL: 230-275 problems across all phases**
- Can solve medium problems comfortably
- Can discuss hard problems even if not perfect
- Strong system design skills
- 3-4 impressive projects
- **READY FOR FAANG**

---

## ANTI-GUILT SYSTEM (CRITICAL FOR YOUR SUCCESS)

### Rule 1: Flex Time Built In

- Every week has weekend buffer time
- Missing a weekday? Use Saturday/Sunday catch-up slot
- Did all weekdays? Weekend = bonus practice or rest

### Rule 2: Never Compound Work

- Miss Day 3? Skip it, do Day 4 next
- Missed content goes to review cycle later
- NO guilt, NO catching up multiple days

### Rule 3: Emergency 15-Min Mode

- Life crazy? Do 15-min version:
  - Read 1 solution, understand the pattern, add to notes
  - Keeps streak alive, maintains momentum
  - Better than zero

### Rule 4: Monthly Reviews (Every 4 weeks)

- Sunday of Week 4, 8, 12, 16, etc.
- Redo 10 random old problems
- Update pattern documentation
- Assess what's working, what's not

### Rule 5: Progress Tracking

- GitHub green squares (commit daily)
- Spreadsheet of problems solved
- Project milestones visible
- Celebrate wins (every 25 problems, every project shipped)

---

## SUCCESS METRICS BY PHASE

**End of Phase 1 (Week 8):**

- [ ] 60-70 problems solved
- [ ] Can write Python fluently without AI
- [ ] Know all basic patterns
- [ ] Pass a mock easy-medium interview

**End of Phase 2 (Week 20):**

- [ ] 100-115 total problems
- [ ] 3 live projects on GitHub
- [ ] Comfortable with data pipelines
- [ ] Basic ML model deployed

**End of Phase 3 (Week 36):**

- [ ] 150-175 total problems
- [ ] Strong ML fundamentals
- [ ] Production ML project
- [ ] Can discuss ML system design

**End of Phase 4 (Week 52):**

- [ ] 230-275 total problems
- [ ] Comfortable with medium, can attempt hard
- [ ] Strong system design skills
- [ ] Interview-ready confidence
- [ ] **PASS FAANG INTERVIEWS**

---

## RESOURCES

### Problem-Solving:

- LeetCode Premium (worth it for company-specific problems)
- NeetCode 150 (great pattern list)
- AlgoExpert (if you prefer structured courses)

### System Design:

- "System Design Interview" by Alex Xu (Vol 1 & 2)
- "Designing Data-Intensive Applications" by Martin Kleppmann
- YouTube: Gaurav Sen, System Design Interview

### ML:

- Andrew Ng's ML Course (Coursera)
- "Hands-On Machine Learning" by Aurélien Géron
- Fast.ai (practical deep learning)
- "Designing Machine Learning Systems" by Chip Huyen

### Mock Interviews:

- Pramp (free)
- Interviewing.io
- Peers (find study buddies on Discord/Blind)

---

## COMMITMENT

This roadmap requires:

- **Weekdays:** 1-2 hours/day (varies by phase)
- **Weekends:** 3-4 hours/day
- **Total:** ~15-20 hours/week average
- **Consistency:** 52 weeks, with flexibility built in

**You can do this.** The plan accounts for your patterns (guilt-avoidance, forgetting strategies, life getting busy). Trust the system, show up consistently, and you'll be FAANG-ready in 12 months.

**START DATE:** **\*\***\_\_\_**\*\***
**TARGET INTERVIEW DATE:** **\*\***\_\_\_**\*\***

**LET'S GO! 🚀**
