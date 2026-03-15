# Teacher-AID: AI-Powered Classroom Insight Engine

## Overview

Teacher-AID is an AI-powered classroom analytics system designed to help teachers understand **how students are reasoning about problems**, not just whether answers are correct.

The system analyzes student submissions, identifies **misconceptions and reasoning patterns**, and generates **actionable teaching insights** at both the **individual student level** and the **entire class level**.

Instead of grading alone, Teacher-AID acts as an **AI teaching assistant** that surfaces learning patterns, highlights common errors, and suggests targeted reteaching strategies.

---

# Core Idea

Traditional educational systems track:

* Correct vs incorrect answers
* Scores
* Completion rates

Teacher-AID goes deeper by identifying:

* *why* a student made an error
* *what concept* they misunderstood
* *which misconceptions are spreading in a class*

The system continuously builds a **learning memory** of the classroom and uses it to generate insights for teachers.

---

# Key Features

## 1. AI Submission Analysis

When a student submits an answer, the system:

1. Evaluates correctness
2. Classifies the **bug category** or reasoning error
3. Extracts the **misconception** behind the mistake
4. Generates **evidence and reasoning patterns**

Example insight:

```
Misconception: Python range() includes the stop value
Concept: loops
Bug Category: misunderstanding_range_bounds
```

This allows the system to track patterns across multiple students.

---

## 2. Student Learning Memory

Teacher-AID maintains a **persistent memory of student misconceptions**.

For each student, the system tracks:

* recurring misconceptions
* reasoning patterns
* evidence examples
* confidence trends
* timestamps of occurrences

This allows teachers to see **how a student's understanding evolves over time**.

---

## 3. Classroom Learning Memory

The system also aggregates errors across the entire class.

This enables:

* identifying **class-wide misconceptions**
* detecting **emerging vs persistent issues**
* measuring **how many students are affected**

Example insight:

```
Top misconception:
"Python range() excludes the stop value"

Students affected: 5
Trend: persistent
```

---

## 4. AI Teacher Insights

The system generates **teacher-friendly summaries** of what is happening in the classroom.

Example:

```
The class is struggling with understanding that Python's range() function excludes the stop value.
This is leading to off-by-one errors in loops.

A short reteaching segment with visual tracing examples is recommended.
```

These summaries help teachers quickly decide **what to reteach and when**.

---

## 5. Suggested Interventions

For individual students, the system suggests targeted interventions.

Example:

```
Suggested Intervention:
Give this student a short tracing exercise on Python range() boundaries.
```

These suggestions are generated automatically based on detected misconceptions.

---

## 6. Classroom Event Detection

The system generates **AI alerts** when patterns emerge.

Examples:

* A misconception becomes class-wide
* A student repeatedly struggles with a concept
* A concept trend becomes persistent

Example event:

```
Event Type: class_insight
Message:
"Misunderstanding of Python range() boundaries is emerging as a class-wide issue."
```

---

# Dashboard Capabilities

The frontend dashboard visualizes classroom insights.

## Class Overview

Displays:

* top misconceptions
* concept difficulty trends
* students affected
* teacher summaries
* suggested reteaching topics

Possible visualizations:

* misconception frequency charts
* concept heatmaps
* class alerts

---

## Student Progression View

Displays:

* recurring misconceptions
* reasoning patterns
* intervention suggestions
* teacher summary
* evidence examples

This allows teachers to quickly understand **where a student is struggling**.

---

## AI Alert Feed

Shows detected events such as:

* emerging misconceptions
* recurring student errors
* class learning signals

---

# Architecture

## Backend

Built with:

* **FastAPI**
* **LLM reasoning engine (DeepSeek)**
* **Vector memory system (Moorcheh)**

Responsibilities:

* classify student reasoning
* store misconception memory
* generate teacher insights
* detect learning events

---

## AI Components

### LLM Classification

An LLM analyzes student reasoning to extract:

* bug category
* misconception
* reasoning pattern
* supporting evidence

---

### Vector Memory (Moorcheh)

Embeddings are stored to allow:

* similarity search
* long-term learning memory
* pattern retrieval

This allows the system to recall prior classroom events.

---

# Example API Endpoints

## Class Insights

```
GET /insights/class/{classroom_id}
```

Returns:

* top misconceptions
* reteach suggestions
* teacher summary

---

## Student Insights

```
GET /insights/student/{student_id}
```

Returns:

* recurring misconceptions
* suggested interventions
* teacher summary

---

## Class Events

```
GET /events/class/{classroom_id}
```

Returns detected learning events.

---

## Student Events

```
GET /events/student/{student_id}
```

Returns events related to a specific student.

---

## Classroom Memory

```
GET /memory/class/{classroom_id}
```

Returns aggregated misconception memory.

---

## Student Memory

```
GET /memory/student/{student_id}
```

Returns a student's misconception history.

---

# Demo Dataset

The repository includes a **compact demo dataset** representing a Grade 10 programming class.

Dataset characteristics:

* 12 students
* ~200 submissions
* multiple programming concepts
* correct and incorrect answers

Concepts covered:

* loops
* conditionals
* variables
* lists

The dataset allows the system to demonstrate:

* class-wide misconceptions
* student progression
* AI-generated teacher insights

---

# Example Insight

```
Classroom Insight

Concept: loops
Misconception: range() includes the stop value
Trend: persistent
Students affected: 4

Recommendation:
Demonstrate loop tracing using a visual number line.
```

---

# Future Improvements

Planned enhancements include:

* timeline analysis of misconceptions
* automated curriculum alignment
* adaptive question generation
* longitudinal student learning profiles

---

# Why This Matters

Teachers often lack visibility into **how students are thinking**.

Teacher-AID helps bridge this gap by providing:

* explainable AI feedback
* actionable classroom insights
* student reasoning analysis

The goal is to help teachers **teach more effectively using AI-powered learning analytics**.

---

# License

This project was developed for an AI education hackathon demonstration and research prototype.
