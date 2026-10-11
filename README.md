# invoicekit — an Agent Trap test repository

**This repository is deliberately malicious-looking. It exists to demonstrate
[Agent Trap](https://github.com/p3Xxer/agent-trap).**

`setup.py` contains "build telemetry" that, during `pip install`, reads
`~/.aws/credentials` and the `OPENAI_API_KEY` / `ANTHROPIC_API_KEY` environment
variables and posts them to a remote server.

It is harmless outside a sandbox: the destination is
`collector.agenttrap.invalid`, and `.invalid` names can never exist on the real
internet (RFC 6761), so the request always fails and nothing leaves your
machine. Inside the Agent Trap sandbox every name resolves to the trap, so the
leak of the *fake* secrets planted there is caught and the exact lines are
reported.

Paste `https://github.com/p3Xxer/malicious-repo-agent-trap` into the
Agent Trap web page, or run `agenttrap scan` on a clone, to see it flagged
HIJACKED. Do not install it anywhere you would not install untrusted code.

## The library itself

A tiny invoice helper:

    pip install -e .
    pytest
