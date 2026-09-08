---
author: '@pocarles'
date: '2026-09-07T10:38:22.000Z'
links:
- https://learn.chatgpt.com/docs/config-file/config-reference
primary_topic: dev-tools
proposed_tags: []
tags:
- ai-agents
- dev-tools
- productivity
- prompt-engineering
title: Prompt pour auto-optimiser sa configuration Codex selon son historique d'usage
tweet_id: '2096910944165146678'
url: https://x.com/pocarles/status/2096910944165146678
---

# Prompt pour auto-optimiser sa configuration Codex selon son historique d'usage

> Post de **@pocarles** — [voir sur X](https://x.com/pocarles/status/2096910944165146678)

## Résumé

Le post propose un prompt réutilisable qui demande à Codex d'analyser vos sessions précédentes et vos habitudes de travail, puis de croiser cela avec la documentation de référence des options de configuration pour suggérer des changements personnalisés. La page liée est la référence exhaustive des clés de config.toml (agents, approvals, features, hooks, network proxy, etc.) que Codex peut exploiter pour formuler ces recommandations. L'idée est de laisser le modèle auto-diagnostiquer les réglages sous-exploités et d'appliquer ensuite les suggestions jugées pertinentes.

## Idées clés

- Un prompt méta qui fait analyser par l'IA son propre historique d'usage pour proposer des optimisations de configuration personnalisées.
- Combiner l'analyse comportementale (sessions passées) avec une doc de référence structurée permet des recommandations contextualisées plutôt que génériques.
- La config.toml de Codex expose énormément de leviers fins (approval_policy granulaire, hooks lifecycle, multi-agent, network proxy, permissions) souvent ignorés par défaut.
- Demander systématiquement le bénéfice concret de chaque changement suggéré avant de l'appliquer évite d'adopter des options inutiles ou risquées.
- Ce pattern de prompt (analyser usage + doc de config + proposer améliorations) est généralisable à d'autres outils dev configurables.

## Citations

> Analyze the way I work with @computerhistory and my previous sessions, then check this link

## Texte du post

Vous avez enfin basculé sur Codex et touchez du doigt ce qu'est sans doute l'AGI pour beaucoup d'entre nous avec Astra.

Voici un prompt très simple qui va vous faire franchir un nouveau cap de productivité.

Vous pouvez le copier - coller tel quel :
___

Analyze the way I work with @computerhistory and my previous sessions, then check this link:
https://t.co/xqEfNw21y4

Based on the features available in Codex configuration, tell me what changes we should apply and what would be, in a few words for each change suggested, the benefits for me?
___

Lisez ses propositions et dites-lui d'appliquer celles qui vous semblent utiles.

## Archive du contenu lié

### https://learn.chatgpt.com/docs/config-file/config-reference

Use this page as a searchable reference for Codex configuration files. For conceptual guidance and examples, start with Config basics and Advanced Config.

## `config.toml`

User-level configuration lives in `~/.codex/config.toml`. You can also add project-scoped overrides in `.codex/config.toml` files. Codex loads project-scoped config files only when you trust the project.

Project-scoped config can't override machine-local provider, auth,
host-owned app request metadata, notification, configuration profile selection,
or telemetry routing keys. Codex ignores `openai_base_url`,
`chatgpt_base_url`, `apps_mcp_product_sku`, `model_provider`,
`model_providers`, `notify`, `profile`, `profiles`,
`experimental_realtime_ws_base_url`, and `otel` when they appear in a
project-local `.codex/config.toml`; put provider, notification, and telemetry
keys in user-level config instead. Config profile files live next to
`config.toml` as `$CODEX_HOME/profile-name.config.toml`; select one with
`--profile profile-name`.

For sandbox and approval keys (`approval_policy`, `sandbox_mode`, and `sandbox_workspace_write.*`), pair this reference with Sandbox and approvals, Protected paths in writable roots, and Network access. For beta permission profiles, see Permissions.

| Key | Type / Values | Details | 
|---|---|---|
| `agents` | `table` | Multi-agent settings and custom role declarations. Scalar setting names are reserved and can't be used as custom role names. | 
| `agents.<name>.config_file` | `string (path)` | Path to a TOML config layer for that role; relative paths resolve from the config file that declares the role. | 
| `agents.<name>.description` | `string` | Role guidance shown to Codex when choosing and spawning that agent type. | 
| `agents.default_subagent_model` | `string` | Default model for spawned agents. An explicit spawn model takes precedence. | 
| `agents.default_subagent_reasoning_effort` | `string` | Default reasoning effort for spawned agents. An explicit spawn effort takes precedence. | 
| `agents.enabled` | `boolean` | Enable or disable multi-agent tools (default: true). | 
| `agents.interrupt_message` | `boolean` | Record a model-visible message when an agent turn is interrupted (default: true). | 
| `agents.max_concurrent_threads_per_session` | `number` | Maximum number of spawned-agent threads that can be open concurrently, excluding the primary thread. When unset, Codex chooses the default. | 
| `agents.max_threads` | `number` | Legacy alias for `agents.max_concurrent_threads_per_session` . | 
| `allow_login_shell` | `boolean` | Allow shell-based tools to use login-shell semantics. Defaults to `true` ; when`false` ,`login = true` requests are rejected and omitted`login` defaults to non-login shells. | 
| `analytics.enabled` | `boolean` | Enable or disable analytics for this machine/profile. When unset, the client default applies. | 
| `approval_policy` | `untrusted \| on-request \| never \| { granular = { sandbox_approval = bool, rules = bool, mcp_elicitations = bool, request_permissions = bool, skill_approval = bool } }` | Controls when Codex pauses for approval before executing commands. You can also use `approval_policy = { granular = { ... } }` to allow or auto-reject specific prompt categories while keeping other prompts interactive.`on-failure` is deprecated; use`on-request` for interactive runs or`never` for non-interactive runs. | 
| `approval_policy.granular.mcp_elicitations` | `boolean` | When `true` , MCP elicitation prompts are allowed to surface instead of being auto-rejected. | 
| `approval_policy.granular.request_permissions` | `boolean` | When `true` , prompts from the`request_permissions` tool are allowed to surface. | 
| `approval_policy.granular.rules` | `boolean` | When `true` , approvals triggered by execpolicy`prompt` rules are allowed to surface. | 
| `approval_policy.granular.sandbox_approval` | `boolean` | When `true` , sandbox escalation approval prompts are allowed to surface. | 
| `approval_policy.granular.skill_approval` | `boolean` | When `true` , skill-script approval prompts are allowed to surface. | 
| `approvals_reviewer` | `user \| auto_review` | Who reviews eligible approval prompts under `on-request` or granular approval policies. Defaults to`user` ;`auto_review` uses the reviewer subagent. This setting doesn't change sandboxing or review actions already allowed inside the sandbox. | 
| `apps._default.approvals_reviewer` | `user \| auto_review` | Default reviewer for app tool approval prompts unless overridden per app. When omitted, apps inherit the top-level `approvals_reviewer` value. | 
| `apps._default.default_tools_approval_mode` | `auto \| prompt \| writes \| approve` | Default approval behavior for app tools without per-app or per-tool overrides. | 
| `apps._default.destructive_enabled` | `boolean` | Default allow/deny for app tools with `destructive_hint = true` . | 
| `apps._default.enabled` | `boolean` | Default app enabled state for all apps unless overridden per app. | 
| `apps._default.open_world_enabled` | `boolean` | Default allow/deny for app tools with `open_world_hint = true` . | 
| `apps.<id>.approvals_reviewer` | `user \| auto_review` | Reviewer for this app's tool approval prompts. Overrides `apps._default.approvals_reviewer` . | 
| `apps.<id>.default_tools_approval_mode` | `auto \| prompt \| writes \| approve` | Default approval behavior for tools in this app unless a per-tool override exists. | 
| `apps.<id>.default_tools_enabled` | `boolean` | Default enabled state for tools in this app unless a per-tool override exists. | 
| `apps.<id>.destructive_enabled` | `boolean` | Allow or block tools in this app that advertise `destructive_hint = true` . | 
| `apps.<id>.enabled` | `boolean` | Enable or disable a specific app/connector by id (default: true). | 
| `apps.<id>.open_world_enabled` | `boolean` | Allow or block tools in this app that advertise `open_world_hint = true` . | 
| `apps.<id>.tools.<tool>.approval_mode` | `auto \| prompt \| writes \| approve` | Per-tool approval behavior override for a single app tool. | 
| `apps.<id>.tools.<tool>.enabled` | `boolean` | Per-tool enabled override for an app tool (for example `repos/list` ). | 
| `auto_review.policy` | `string` | Local Markdown policy instructions for automatic review. Managed `guardian_policy_config` takes precedence. Blank values are ignored. | 
| `background_terminal_max_timeout` | `number` | Maximum poll window in milliseconds for empty `write_stdin` polls (background terminal polling). Default:`300000` (5 minutes). Replaces the older`background_terminal_timeout` key. | 
| `browser_use.allow_history_access` | `boolean` | Set to `false` to restrict browser-history access. Managed requirements can enforce this restriction. | 
| `browser_use.default_origin_policy` | `table` | Fallback browser-origin restrictions. Supports `access` ,`uploads` ,`downloads` , and`full_cdp_access` , each set to`allow` or`deny` . | 
| `browser_use.origins.<origin>` | `table` | Per-origin browser restrictions with the same fields as `browser_use.default_origin_policy` . Include an HTTP or HTTPS scheme and optional port; omit paths, queries, and fragments. Local values cannot relax managed denies. | 
| `chatgpt_base_url` | `string` | Override the base URL used during the ChatGPT login flow. | 
| `check_for_update_on_startup` | `boolean` | Check for Codex updates on startup (set to false only when updates are centrally managed). | 
| `cli_auth_credentials_store` | `file \| keyring \| auto` | Control where the CLI stores cached credentials (file-based auth.json vs OS keychain). | 
| `compact_prompt` | `string` | Inline override for the history compaction prompt. | 
| `computer_use.default_app_access` | `allow \| deny` | Fallback native-app access policy for Computer Use. App-specific entries can supply a policy; local configuration cannot relax managed restrictions. | 
| `computer_use.macos.bundle_ids` | `map<string, allow \| deny>` | Native macOS app access keyed by bundle identifier. | 
| `computer_use.windows.always_allowed_app_ids` | `array<string>` | Windows app identifiers that Computer Use can open without prompting. Apps not in the list require approval; remove saved entries from the ChatGPT desktop app's Computer Use settings. | 
| `computer_use.windows.aumids` | `map<string, allow \| deny>` | Packaged Windows app access keyed by Application User Model ID (AUMID). | 
| `computer_use.windows.exes` | `array<table>` | Windows executable access rules. Each rule requires `publisher_name` ,`product_name` , and`access` (`allow` or`deny` );`binary_name` is optional. | 
| `default_permissions` | `string` | Name of the default permissions profile to apply to sandboxed tool calls. Built-ins are `:read-only` ,`:workspace` , and`:danger-full-access` ; custom profile names require matching`[permissions.<name>]` tables. Don't combine with`sandbox_mode` or`[sandbox_workspace_write]` . | 
| `desktop.custom_file_handlers.<id>` | `table` | User-level only. Defines an additional **Open in** target for the ChatGPT desktop app. See Add custom file handlers for examples and handler ID constraints. | 
| `desktop.custom_file_handlers.<id>.args` | `array<string>` | Arguments inserted between the command and file input (default: `[]` ). | 
| `desktop.custom_file_handlers.<id>.command` | `string` | Executable path or command name to detect and launch. Required. | 
| `desktop.custom_file_handlers.<id>.icon` | `string` | Bundled asset path, Base64-encoded `data:image/...` URL, file URI, or absolute local path for the handler icon. Required; unsupported sources use the default VS Code icon. | 
| `desktop.custom_file_handlers.<id>.input` | `path \| json_argument \| json_stdin` | How the app sends file input to the handler (default: `path` ). | 
| `desktop.custom_file_handlers.<id>.label` | `string` | Display name shown in **Open in** menus. Required. | 
| `desktop.custom_file_handlers.<id>.supports_ssh` | `boolean` | Offer the handler for files in SSH workspaces (default: `false` ). | 
| `developer_instructions` | `string` | Additional developer instructions injected into the session (optional). | 
| `disable_paste_burst` | `boolean` | Disable burst-paste detection in the TUI. | 
| `experimental_compact_prompt_file` | `string (path)` | Load the compaction prompt override from a file (experimental). | 
| `experimental_use_unified_exec_tool` | `boolean` | Legacy name for enabling unified exec; prefer `[features].unified_exec` or`codex --enable unified_exec` . | 
| `features.apps` | `boolean` | Enable app (connector) integrations (stable; on by default). App and connector traffic is not controlled by the sandboxed-command network proxy or its domain allowlist. | 
| `features.code_mode.direct_only_tool_namespaces` | `array<string>` | Tool namespaces code mode can use only through direct tool calls. | 
| `features.code_mode.enabled` | `boolean` | Enable code mode feature configuration. This feature is under development and off by default. | 
| `features.code_mode.excluded_tool_namespaces` | `array<string>` | Tool namespaces code mode excludes from nested code-mode tool guidance and executor exposure. | 
| `features.context_management.experimental_mode` | `boolean` | Enable experimental context management (off by default). Rather than repeatedly compressing context into a single summary, it uses notes and searchable history to preserve accumulated details. Requires ChatGPT sign-in on Plus, Pro, or Pro Lite. | 
| `features.enable_request_compression` | `boolean` | Compress streaming request bodies with zstd when supported (stable; on by default). | 
| `features.fast_mode` | `boolean` | Enable model-catalog service tier selection in the TUI, including Fast-tier commands when the active model advertises them (stable; on by default). | 
| `features.goals` | `boolean` | Enable persisted goals and automatic continuation (stable; on by default). | 
| `features.hooks` | `boolean` | Enable lifecycle hooks loaded from `hooks.json` or inline`[hooks]` config.`features.codex_hooks` is a deprecated alias. | 
| `features.memories` | `boolean` | Enable Memories (off by default). | 
| `features.multi_agent` | `boolean` | Enable multi-agent collaboration tools (`spawn_agent` ,`send_input` ,`resume_agent` ,`wait_agent` , and`close_agent` ) (stable; on by default). | 
| `features.network_proxy` | `boolean \| table` | Start the network proxy for sandboxed commands (experimental; off by default). Required to enforce permission-profile domain rules unless enabled administrator-managed `experimental_network` requirements start the proxy. Use a table when setting feature-level policy options such as`domains` . Does not filter web search, apps, MCP, or other hosted tools. | 
| `features.network_proxy.allow_local_binding` | `boolean` | Allow broader local/private-network access. Defaults to `false` ; exact local IP literal or`localhost` allow rules can still permit specific local targets. | 
| `features.network_proxy.allow_upstream_proxy` | `boolean` | Allow chaining through an upstream proxy from the environment. Defaults to `true` . | 
| `features.network_proxy.dangerously_allow_all_unix_sockets` | `boolean` | Permit arbitrary Unix socket destinations instead of allowlist-only access. Defaults to `false` ; use only in tightly controlled environments. | 
| `features.network_proxy.dangerously_allow_non_loopback_proxy` | `boolean` | Permit non-loopback listener addresses. Defaults to `false` ; enabling it can expose proxy listeners beyond localhost. | 
| `features.network_proxy.domains` | `map<string, allow \| deny>` | Domain policy for sandboxed networking. Unset by default, which means no external destinations are allowed until you add `allow` rules. Supports exact hosts,`*.example.com` for subdomains only,`**.example.com` for apex plus subdomains, and global`*` allow rules; prefer scoped rules because`*` broadly opens public outbound access. Add`deny` rules for blocked destinations;`deny` wins on conflicts. | 
| `features.network_proxy.enable_socks5` | `boolean` | Expose SOCKS5 support. Defaults to `true` . | 
| `features.network_proxy.enable_socks5_udp` | `boolean` | Allow UDP over SOCKS5. Defaults to `true` . | 
| `features.network_proxy.enabled` | `boolean` | Start the sandboxed-command network proxy when command network access is enabled. Defaults to `false` ; permission-profile domain rules are not enforced while the proxy is off. | 
| `features.network_proxy.proxy_url` | `string` | HTTP listener URL for sandboxed networking. Defaults to `"http://127.0.0.1:3128"` . | 
| `features.network_proxy.socks_url` | `string` | SOCKS5 listener URL. Defaults to `"http://127.0.0.1:8081"` . | 
| `features.network_proxy.unix_sockets` | `map<string, allow \| deny>` | Unix socket policy for sandboxed networking. Unset by default; add `allow` entries for permitted sockets. | 
| `features.personality` | `boolean` | Enable personality selection controls (stable; on by default). | 
| `features.prevent_idle_sleep` | `boolean` | Prevent the machine from sleeping while a turn is actively running (experimental; off by default). | 
| `features.remote_plugin` | `boolean` | Enable the remote plugin catalog (stable; on by default). | 
| `features.rollout_budget.enabled` | `boolean` | Enable rollout budget tracking. This feature is under development and off by default. When enabled, `features.rollout_budget.limit_tokens` is required. | 
| `features.rollout_budget.limit_tokens` | `integer` | Positive token limit for rollout budget tracking. Required when rollout budget is enabled. | 
| `features.rollout_budget.prefill_token_weight` | `number` | Finite non-negative multiplier for prefill tokens in rollout budget accounting. Defaults to `1.0` . | 
| `features.rollout_budget.reminder_interval_tokens` | `integer` | Positive token interval between rollout budget reminders. Defaults to 10% of `limit_tokens` , with a minimum of 1 token. | 
| `features.rollout_budget.sampling_token_weight` | `number` | Finite non-negative multiplier for sampled tokens in rollout budget accounting. Defaults to `1.0` . | 
| `features.shell_snapshot` | `boolean` | Snapshot shell environment to speed up repeated commands (stable; on by default). | 
| `features.shell_tool` | `boolean` | Enable the default `shell` tool for running commands (stable; on by default). | 
| `features.skill_mcp_dependency_install` | `boolean` | Allow prompting and installing missing MCP dependencies for skills (stable; on by default). | 
| `features.unified_exec` | `boolean` | Use the unified PTY-backed exec tool (stable; enabled by default except on Windows). | 
| `features.web_search` | `boolean` | Deprecated legacy toggle; prefer the top-level `web_search` setting. | 
| `features.web_search_cached` | `boolean` | Deprecated legacy toggle. When `web_search` is unset, true maps to`web_search = "cached"` . | 
| `features.web_search_request` | `boolean` | Deprecated legacy toggle. When `web_search` is unset, true maps to`web_search = "live"` . | 
| `feedback.enabled` | `boolean` | Enable feedback submission via `/feedback` across local clients (default: true). | 
| `file_opener` | `vscode \| vscode-insiders \| windsurf \| cursor \| none` | URI scheme used to open citations from Codex output (default: `vscode` ). | 
| `forced_chatgpt_workspace_id` | `string (uuid)` | Limit ChatGPT logins to a specific workspace identifier. | 
| `forced_login_method` | `chatgpt \| api` | Restrict Codex to a specific authentication method. | 
| `hide_agent_reasoning` | `boolean` | Suppress reasoning events in both the TUI and `codex exec` output. | 
| `history.max_bytes` | `number` | If set, caps the history file size in bytes by dropping oldest entries. | 
| `history.persistence` | `save-all \| none` | Control whether Codex saves session transcripts to history.jsonl. | 
| `hooks` | `table` | Lifecycle hooks configured inline in `config.toml` . Uses the same event schema as`hooks.json` ; see the Hooks guide for examples and supported events. | 
| `hooks.<Event>` | `array<table>` | Matcher groups for hook events such as `PreToolUse` ,`PermissionRequest` ,`PostToolUse` ,`PreCompact` ,`PostCompact` ,`SessionStart` ,`SessionEnd` ,`SubagentStart` ,`SubagentStop` ,`UserPromptSubmit` ,`Stop` , or`Interrupt` . | 
| `hooks.<Event>[].hooks` | `array<table>` | Hook handlers for a matcher group. Command and MCP tool hooks are supported while prompt and agent hook handlers are parsed but skipped. | 
| `hooks.<Event>[].hooks[].additionalContextLimit` | `integer` | Approximate per-handler token threshold for saving oversized `additionalContext` to disk and showing the model a shorter preview. Defaults to`2500` ;`0` passes the full context directly to the model. See Large hook output. | 
| `hooks.<Event>[].hooks[].async` | `boolean` | Run a command hook in the background without delaying the triggering operation. Defaults to `false` ;`SessionEnd` always runs synchronously. See Run hooks in the background. | 
| `hooks.<Event>[].hooks[].commandWindows` | `string` | Windows-only command override for command hooks. The TOML alias `command_windows` is also accepted. | 
| `instructions` | `string` | Reserved for future use; prefer `model_instructions_file` or`AGENTS.md` . | 
| `log_dir` | `string (path)` | Directory where Codex writes log files; defaults to `$CODEX_HOME/log` . Setting this explicitly also enables the opt-in plaintext TUI log,`codex-tui.log` , in that directory. | 
| `mcp_oauth_callback_port` | `integer` | Optional global fixed port for the local HTTP callback server used during MCP OAuth login. A server-specific `oauth.callback_port` takes precedence. When neither is set, Codex binds to an ephemeral port chosen by the OS. | 
| `mcp_oauth_callback_url` | `string` | Optional base callback URL for MCP OAuth login, such as a devbox ingress URL. Newly added pre-registered clients use this URL unchanged when the authorization server supports issuer identification; existing c
