# Summon

Summon is a web application for testing hypotheses about how people interact with LLMs.

Does asking an LLM to challenge your assumptions lead to better recommendations? Does giving it a particular perspective help? Which prompting styles produce responses people actually prefer?

Summon gives you a way to explore those questions through real conversations and compare the outcomes.

## How it works

1. **Define a hypothesis.** Describe what you want to learn, then create experiments with different perspectives and prompting styles to test it.
2. **Have a conversation.** Summon starts the LLM with the assigned experiment, perspective, and style. Ask follow-up questions, request revisions, and keep going until you have a response you want to submit.
3. **Choose a response.** Submit one LLM response as the outcome of that conversation. You decide when it is ready.
4. **Compare outcomes.** Judge two anonymous responses at a time. Jev, an automated judge, also compares them, so you can see where human and automated preferences agree or differ.

The goal is to gather evidence about which approaches help people get better results from LLMs.

## Inside the app

- **Hypotheses** — design and edit your experiments.
- **Collect** — hold conversations and submit responses.
- **Analyze** — run comparisons and record your preferences.
- **Results** — explore what the comparisons show.
- **Data** — export your work or clean up collected data.

Enter your name to keep your batches and judgments associated with you. You can switch users when sharing a computer. Data is stored locally in readable files.

For technical details, see the [experiment protocol](spec.md) and [data layout](experiment-data/README.md).
