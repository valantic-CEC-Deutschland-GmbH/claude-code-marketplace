import OpenAI from "openai";

const client = new OpenAI(); // uses OPENAI_API_KEY env var

async function main() {
  // Read hook input from stdin
  let input = "";
  for await (const chunk of process.stdin) {
    input += chunk;
  }
  const hookInput = JSON.parse(input);

  const { tool_name, tool_input } = hookInput;

  // Tools that are always safe - Claude's internal task/plan management
  const ALWAYS_SAFE_TOOLS = [
    "TaskUpdate",
    "TaskCreate",
    "TaskList",
    "TaskGet",
    "TodoWrite",
    "TodoRead",
  ];

  if (ALWAYS_SAFE_TOOLS.includes(tool_name)) {
    console.log(
      JSON.stringify({
        hookSpecificOutput: {
          hookEventName: "PreToolUse",
          permissionDecision: "allow",
          permissionDecisionReason: `Internal tool '${tool_name}' is always safe.`,
        },
      })
    );
    return;
  }

  const toolInputStr = JSON.stringify(tool_input, null, 2);

  // Ask GPT-4.1-nano to evaluate
  const response = await client.chat.completions.create({
    model: "gpt-4.1-nano",
    max_tokens: 256,
    response_format: { type: "json_object" },
    messages: [
      {
        role: "user",
        content: `Evaluate this Claude Code tool usage request for safety and relevance.

IMPORTANT CONTEXT: This is running on the user's own local development machine. There is no sensitive data locally. Be permissive with:
- Reading files, directories, or code (always safe)
- Searching/grepping through code (always safe)
- Running build tools, linters, test suites, package managers (always safe)
- Git operations (always safe)
- Exploring the filesystem or project structure (always safe)
- Writing or editing files in the user's projects (always safe)

Only flag operations that are clearly destructive or dangerous, such as:
- Deleting important system files
- Sending data to unknown external services
- Running commands that could damage the system (rm -rf /, etc.)
- Exposing credentials to external endpoints

Tool: ${tool_name}
Input: ${toolInputStr}

Respond with JSON only: {"safe": boolean, "relevant": boolean, "concern": "string or null"}`,
      },
    ],
  });

  const text = response.choices[0]?.message?.content || "";

  // Extract JSON from the response, handling potential markdown code blocks
  let jsonText = text;
  const jsonMatch = text.match(/```(?:json)?\s*([\s\S]*?)```/);
  if (jsonMatch) {
    jsonText = jsonMatch[1].trim();
  }

  const evaluation = JSON.parse(jsonText);

  if (evaluation.safe && evaluation.relevant) {
    console.log(
      JSON.stringify({
        hookSpecificOutput: {
          hookEventName: "PreToolUse",
          permissionDecision: "allow",
          permissionDecisionReason: "GPT-4.1-nano approved this tool use.",
        },
      })
    );
  } else {
    console.log(
      JSON.stringify({
        hookSpecificOutput: {
          hookEventName: "PreToolUse",
          permissionDecision: "ask",
          permissionDecisionReason: `GPT-4.1-nano flagged: ${evaluation.concern || "Unsafe or irrelevant"}`,
        },
      })
    );
  }
}

main().catch((err) => {
  console.error(err);
  // On error, fall back to asking the user
  console.log(
    JSON.stringify({
      hookSpecificOutput: {
        hookEventName: "PreToolUse",
        permissionDecision: "ask",
        permissionDecisionReason: "Hook evaluation failed, asking user.",
      },
    })
  );
});
