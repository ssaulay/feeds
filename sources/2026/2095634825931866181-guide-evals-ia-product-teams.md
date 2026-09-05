---
author: '@ttorres'
date: '2026-09-03T22:07:32.000Z'
links:
- https://www.producttalk.org/ai-evals/
primary_topic: product
proposed_tags: []
tags:
- ai-agents
- product
- llm
title: Guide pratique des AI evals pour les équipes produit
tweet_id: '2095634825931866181'
url: https://x.com/ttorres/status/2095634825931866181
---

# Guide pratique des AI evals pour les équipes produit

> Post de **@ttorres** — [voir sur X](https://x.com/ttorres/status/2095634825931866181)

## Résumé

Teresa Torres explique ce que sont les AI evals et pourquoi les équipes produit (pas seulement les ingénieurs) doivent apprendre à les construire. Contrairement aux tests unitaires classiques, les LLM sont probabilistes et produisent des sorties sémantiques difficiles à juger en noir et blanc, ce qui nécessite de définir explicitement ce à quoi ressemble une 'bonne réponse'. Le guide détaille une méthode en deux étapes : analyser les erreurs de l'IA sur des cas réels, puis choisir le bon type d'eval (golden dataset, code assertion, LLM-as-a-judge, ou feedback client) pour mesurer la fréquence de ces erreurs.

## Idées clés

- Les LLM sont probabilistes : contrairement au code traditionnel, la même entrée peut produire des sorties différentes, donc un test unique ne suffit pas — il faut mesurer un taux de réussite.
- Définir ce qu'est une 'bonne réponse' est un travail sémantique complexe qui ne peut pas être sous-traité à un vendor d'outils d'eval : la correction dépend du contexte produit.
- L'analyse d'erreur (error analysis) est la première étape : lire en détail les traces de sorties LLM, catégoriser les types d'erreurs, puis choisir lesquelles méritent un eval.
- Pour les workflows personnels, une analyse légère sur peu d'exemples suffit ; pour les produits customer-facing, il faut analyser des centaines de traces réelles.
- Il existe 4 types d'evals : golden dataset (bon pour tâches simples à réponse unique), code assertion (rapide et déterministe), LLM-as-a-judge (pour qualité sémantique, mais coûteux), et feedback client.
- Pour un LLM-as-a-judge efficace : donner une tâche plus simple que l'originale, exiger une réponse binaire, aligner le juge sur son propre jugement humain, et accepter qu'il fera aussi des erreurs.

## Citations

> Correctness is context dependent. Don't let a vendor define correctness for your product. This is the product team's job.

> With a unit test, we expect it to always get it right. With an eval, we are measuring how often it gets it right.

> For the ones that you wish would go away, these are great candidates for evals.

## Texte du post

AI evals have been the "it" skill for product teams for over a year. I've even called evals a new discovery habit.

But I still meet product teams who only have a vague idea of what evals are. And it's not their fault. Most of the writing on this topic is intended for engineers or just isn't specific enough.

I recently created an in-depth eval guide to explain what evals are and why product teams can and should create them. I did my best to make it practical, hands-on, and easy to follow.

AI evals (short for evaluations) are methods for measuring whether an AI product or workflow is performing well. Evals give teams confidence that their AI applications are doing what they expect them to do. They help teams maintain quality and catch issues before they reach users.

Similar to other discovery habits like interviewing and assumption testing, evals can act as a feedback loop to ensure we are on the right track.

If you want to learn more about this new discovery habit, explore my new guide: https://t.co/B1dgs7uEyU

## Archive du contenu lié

### https://www.producttalk.org/ai-evals/

# AI Evals: A Hands-On Guide for Product Teams

Share this article | Listen to this article ($)

AI evals have been the "it" skill for product teams for over a year. I've even called evals a new discovery habit.

But I still meet product teams who only have a vague idea of what evals are. And it's not their fault. Most of the writing on this topic is intended for engineers or just isn't specific enough.

My goal today is to explain what evals are and why product teams can and should create them. I'm going to make this practical, hands-on, and easy to follow.

AI evals (short for evaluations) are methods for measuring whether an AI product or workflow is performing well. Evals give teams confidence that their AI applications are doing what they expect them to do. They help teams maintain quality and catch issues before they reach users.

Similar to other discovery habits like interviewing and assumption testing, evals can act as a feedback loop to ensure we are on the right track.

## Why Product Teams Need to Learn to Build Evals

If you are using AI to help you write PRDs, synthesize what you learned from customer feedback or customer interviews, analyze behavioral analytics, make sense of meeting notes, or really anything else related to doing your day-to-day job, you can benefit from evals.

If you want to know if your AI-generated PRD includes everything you asked for, evals can help you measure this. If you want to know if any of the customer quotes the AI used are fabricated, evals can tell you this. If you want to make sure the data analysis started with the right questions and didn't deviate as it ran complex calculations, evals can monitor this.

When I used ChatGPT to help me write synopses of all of the Lovable interviews that I conducted for this blog post, I wondered how I could trust that the AI got each participant's story right. I built confidence in the summaries by building in some evals—a fact-checker and a hallucination guard. I'll walk you through how both worked in a bit.

If you are building customer-facing AI products or services and have asked yourself, "How do I know if this is consistently good across all of our customers and all target use cases?" you can benefit from evals.

I ran into this with my very first AI product. I ran several interview transcripts through my nascent Interview Coach and the results looked pretty good. But I started to wonder, "How do I know if this is good enough to roll out to all of my students?"

The only way to know if our AI products and workflows are any good is with evals.

## Evals Help Us Define and Measure What Good Looks Like

With traditional software, we write a requirements document, the engineers implement it, and we use automated testing to make sure it passes our acceptance criteria. When it does, we know it works the way we intended.

But when an LLM is involved, it can be harder to know if the software works. There are two reasons for this. First, given the same input, the LLM might give a different answer. And second, we tend to give LLMs semantic tasks that might have more than one right answer—or even better or worse answers.

The former makes it hard to use our traditional testing methods. With traditional software, what the software does is pre-determined. We can look at the code and know exactly what we'll get every time. With LLMs, it's not that simple. LLMs are probabilistic. That means their output can vary, even given the same input.

### Code Will Always Give the Same Answer, LLMs Will Not

Here's a simple way to think about it: If I write a function that takes two numbers and returns the sum, I can write unit tests for a range of cases. If the PRD requires that it works for integers (whole numbers), floats (numbers with decimals), negative numbers, and a mix of integers and floats, then I can write unit tests that span all of these cases.

- To test if the function handles integers well, I can write a test that calls the function with 2 and 3, and checks to make sure that it correctly returns 5.
- To test if the function handles floats, I can send it 3.2 and 4.1, and check to make sure it returns 7.3.
- To test negative numbers, I can send it -1 and -3, and check to see if it returns -4.
- To test a mix of integers and floats, I can send it 2 and 3.1, and check to make sure it returns 5.1.

I can write these tests once and run them every time I change the code. If all the tests pass, then I can be confident that my code works as expected.

But if instead I create an LLM service to do the same thing, this strategy doesn't work. The first time I send it 2 and 3, it might return 5. But the second time it might return 4. Testing it once isn't adequate. It might work once and then break the next time.

Evals allow us to measure the rate at which the LLM returns a correct response. This is different from a unit test. With a unit test, we expect it to always get it right. With an eval, we are measuring how often it gets it right.

### The Unique Challenge of Semantic Output

Before we can measure how often the LLM got the right answer, we need to define what a right answer looks like.

When we are talking about simple addition, defining the right answer is easy. 2 + 3 = 5 is correct. 2 + 3 = 4 is not correct.

But we tend to turn to LLMs for semantic tasks—that's their strength. And oftentimes, semantic tasks are harder to judge. It's rare that we can categorically say this is right and this is wrong. Instead, we might say this is better and this is worse. There's a lot of gray.

If you ask an LLM to write a joke, how would you determine if the response was right or wrong? Your primary criteria might be, "Did it make you laugh?" But you also might ask, "Is it clever?" Or, "Is it appropriate for my kids?"

Before you could evaluate the response, you have to first define what a right answer looks like. And more often than not, a right answer doesn't always have clear boundaries. One joke might be funnier than another joke. Another might be more clever. And so on.

You'll see with evals, one of our jobs will be to get clarity on what a right answer looks like, even when our intuition says it's blurry.

When I had ChatGPT help me summarize real stories from my Lovable interviews, I defined correctness as follows:

- The story follows the participant's narrative.
- All key moments are included.
- No quotes are made up or inaccurate.

For my Interview Coach, I also defined correctness on multiple dimensions:

- Did the agent sort each interview question into the right section for feedback?
- Did it avoid suggesting a leading question or a general question?
- Was each coaching tip appropriate given what the interviewer asked?
- Did it score each attribute correctly?
- Was the agent's tone appropriate?

For each, I had to take the time to define what good looked like and then I had to figure out a way to measure that. We'll walk through how to do exactly that in a minute.

### Don't Outsource What Good Looks Like

But first, I want to highlight that we typically can't outsource this work. Some of the big eval tool providers offer built-in evals to help you get started. For example, they might evaluate your agent on conciseness or helpfulness. They've baked in their own definitions of correct for each of these.

But it's pretty easy to see how one definition doesn't work across all environments. If I'm a student trying to learn about astrophysics, I might need verbose, detailed responses designed to teach. But if I'm an astrophysics professor asking a similar question, I don't need all the teaching detail.

Correctness is context dependent. Don't let a vendor define correctness for your product. This is the product team's job.

So how do we define a right or wrong answer?

## Step 1: Look at What the LLM is Doing

When we work with an LLM in a chat interface, we are constantly evaluating the model. We ask for something, we get a response, and then we revise our ask based on how well the response met our need.

But when we are building a workflow or product, the goal is for the LLM to do the right thing when we aren't watching. To get here, we have to look at a range of inputs and then evaluate how the LLM responds to those inputs. This process is often referred to as error analysis—where we manually evaluate what types of mistakes the LLM makes.

How much error analysis we do can vary based on how important it is for the LLM to get the output right every time. For personal workflows where a bad response only impacts us, we might do some lightweight error analysis. But for production products where a bad response affects a real customer, we should do more error analysis.

### Error Analysis for Personal Workflows

When I was writing my Lovable blog post, I had 17 transcripts that I wanted to convert into vignettes. I could have written each vignette one at a time. Instead, I wrote a prompt instructing ChatGPT how to write each one. My prompt included my desired structure for each story, the tone and writing style, and the desired length.

When the prompt was ready, I gave ChatGPT the first transcript and asked it to write the story. But I didn't just trust the output. I took the time to read the full transcript. I conducted the interview, but I wanted to remind myself what was said. I then identified what key moments I would have included in the story and checked them against what ChatGPT included. I checked each quote to make sure it came from the transcript verbatim. This took time.

But it also allowed me to see what types of mistakes ChatGPT made. I noticed two distinct errors:

1. It would get some of the specific details wrong—it would hallucinate the person's job title or make up a detail about the product that wasn't included in the transcript.
2. It would hallucinate quotes. It would take two different statements that the participant said and merge them into a new meaning that was not in the transcript.

This was enough for me to identify that I needed two evals: a fact-checker and a hallucination guard.

Was this process slow? Yes. But did it save me time in the long run? Yes. I could have manually reviewed all 17 stories myself. Instead, I reviewed one in-depth, identified the types of errors the LLM made, and then used those errors to identify which evals I needed.

For the next 16 transcripts, I then ran my evals to catch the LLM's mistakes. The evals allowed me to trust the output. We'll look at how I defined these evals in the next section.

Now, if I was turning this into a production product, I would probably want to look at more than one transcript. But for my personal workflow, this was plenty.

### Error Analysis for Customer-Facing Products

For my Interview Coach, I originally tested it with my own customer interview transcripts. The Coach did a good job. But my interview transcripts were in exactly the format and style that the Coach expected.

To really test the Coach, I needed to test it on student interviews. I decided to release my Interview Coach in beta to my April 2025 cohort, even though I wasn't sure it was ready. I needed traces to evaluate.

A trace is a detailed record of an AI interaction. It includes the user input, system prompts, tool calls, intermediate steps, and final LLM responses. In multi-turn conversations, it typically includes all of the back and forth between the user and the LLM.

For the Interview Coach, a trace is the system prompts, the interview transcript, and the Interview Coach's feedback on that transcript.

To mitigate the risk of putting something in front of students before it was ready, I told my students that the Coach wasn't perfect, but that I would be reviewing all of its responses. If it made a mistake, I would email them and let them know.

Reviewing each submission was how I did my error analysis. Every time the Interview Coach made a mistake, I would log it. I then categorized these errors and these became my candidates for evals.

Because this was a production product, I looked at hundreds of cases. I wanted to get a rich understanding of what mistakes occurred over a broad set of customer inputs. I still do these reviews today, even though my Interview Coach has been live for over a year.

As you do your error analysis, it can be tempting to try to fix everything all at once. But I recommend splitting this into phases. Annotate first, categorize errors, and then decide what's worth addressing. Otherwise, you run the risk of spending time fixing less important errors before you've even uncovered the more glaring ones.

And if you are working on a customer-facing product, use your discovery habits to figure out which errors matter most to your customers. Those are the ones that need evals.

### Now It's Your Turn

Take a moment to put what you learned into practice. Pick a personal workflow that you use in your day-to-day job. How might you judge correctness? What errors do you see in the responses?

As you use the workflow, don't just gloss over LLM mistakes. Instead, make note of them. Try to identify the most common categories. Some will be more important than others. Consider what types of mistakes you can live with and which ones you wish would go away.

For the ones that you wish would go away, these are great candidates for evals.

## Step 2: Identify the Best Way to Count How Often the Error Occurs

Now that we've identified the errors that we care most about, it's time to define some evals. Remember, an eval is a metric. It helps us count how often a specific error occurs in our LLM output.

There are four common types of evals.

1. Golden Dataset - A set of known inputs used to test the LLM
2. Code Assertion - A programmatic rule that helps us evaluate quality
3. LLM-as-a-Judge - A second model judges the output
4. Customer Feedback - The customer tells us if the response was good enough

### Golden Dataset Evals Are a Common Starting Point (But Are Limited)

When teams are new to evals, they typically start with golden dataset evals. To create a dataset eval, you simply define a set of inputs that you expect to represent what you might see in production and you define the ideal outputs. The ideal outputs are your definition of correctness. When you hear product managers talking about evals as working in spreadsheets, they are typically referring to golden dataset evals.

They can be a great way to help you develop a rubric for what good looks like. Error analysis helps us see what "bad" looks like by identifying errors. If we fix those errors and add them to our golden dataset, we can start to curate what "good" looks like.

But they only work well for tasks where you can define one correct output. If there are many correct outputs, then it's hard to define all variations of correctness. Similarly, if the inputs and outputs are quite large (like interview transcripts and opportunity solution trees), then it's simply not feasible to create golden dataset evals.

As a general rule of thumb, golden dataset evals are good when the inputs and outputs are small and there is one correct answer. They are good for classification tasks (e.g. is this a business outcome or a product outcome?), factual answers (e.g. who was the first US President?), routing tasks (e.g. which skill best applies?), and so on. They tend not to work well for measuring complex output or when working with complex inputs.

But you can often break complex tasks into smaller tasks and then use golden dataset evals to measure performance on those smaller tasks.

For example, in my AI-generated opportunity solution tree service, the agent has to decide if similar, but differently worded opportunities (from different source opportunities) are actually the same general opportunity. I can create a golden dataset eval to test this ability by defining sets of interview opportunities as inputs and defining the ideal output as a judgment on whether they are similar enough to generalize or not.

There are two challenges to keep in mind when creating golden dataset evals: 1. It's hard to know what your production inputs will look like before you launch, and 2. It's incredibly tedious. It's not a one-time activity. You have to continuously improve your golden dataset to make sure that it continues to match what you expect to see.

I use golden dataset evals for targeted steps where the input and output are simple and I am confident I can curate a golden dataset that represents what I'll see in production.

### Code Assertions Are Typically Cheap and Fast

A code assertion (also called a code-based assertion) is a type of AI eval where you use traditional deterministic code to evaluate the quality of an LLM response. Like unit tests, they are virtually free and the code works as intended every time.

The key to a good code assertion eval is you have to find a fixed structural approach to measuring the error in a way that doesn't require judgment.

For example, my hallucination guard eval for my Lovable stories blog post was a code assertion. For every quote that appeared in a ChatGPT story, I searched for the exact string in the original transcript. If there was a match, the code returned true, if there wasn't, it returned false.

With my Interview Coach, I came up with a list of red flag words that indicated the presence of a general question. This eval just did a string search for any of those words and returned true if it found one and false if it didn't.

For my AI-generated opportunity tree service, I have a code assertion eval that counts the nodes on the tree and evaluates how well they are distributed. I then set designated thresholds to define different error categories.

For every new error where I need an eval, I always try to find a way to measure it with deterministic code. It's fast and cheap. Only when an eval truly requires judgment do I turn to an LLM-as-a-Judge eval.

### LLM-as-a-Judge Evals Measure Semantic Qualities (But Can Be Expensive)

An LLM-as-a-Judge eval is where you use a second LLM to evaluate the output of your first LLM. Instead of relying solely on human judgment or code-based checks, you send your LLM's output to another LLM along with evaluation criteria, and ask it to score or judge the quality based on specific dimensions.

When I first heard about LLM-as-Judges, I immediately visualized turtles standing on turtles to infinity. If I can't trust the first LLM, how can I trust the second LLM? It turns out there are ways to make this work.

To make an LLM-as-a-Judge work well, we have to:

- Give the judge a much simpler task than what we gave the original model.
- Define our criteria such that our judge can return a binary response: true/false, yes/no.
- Align our judges with our own judgment.
- Understand that our judge will always make mistakes and account for that error when reporting our eval error rate.

We won't cover all of these steps in today's article. But I'll do a deeper dive on LLM-as-a-Judge evals soon.

For my Lovable stories blog post, I used an LLM-as-a-Judge to fact-check each claim in the ChatGPT-generated stories. The judge received one fact and a transcript and was told to respond with true if the fact was grounded in the transcript, false otherwise.

My Interview Coach has several LLM-as-a-Judge evals:

- My double-barreled-questions eval gets a question the interviewer asked and has to judge whether the question is asking for more than one thing at a time.
- My leading-question eval also gets a question, but it gets different judging criteria. It evaluates if the question assumes something about the participant or indicates a preferred response.
- My already-answered eval gets a question the Coach suggested and the transcript and has to evaluate if that question has already been answered in the transcript.

LLM-as-Judges can be incredibly helpful when we need to evaluate semantic quality. But they are expensive and it takes work to get them right.

### Custome
