# References and credits

Signed Decisions is a concept by Phillip Sanders. No single part of it is new. This file lists the work it
stands on and the people who shaped it.

Citations are given as they appear in the project's working documents. Entries marked *to verify* have not
yet been checked against the published source; check them before you cite them.

## The work it supports

- **Cassie Groos**, "Probabilistic isn't a dirty word…" (Medium, 27 August 2026). The CRD, or Component
  Requirements Document, is her work: one file per component, co-authored by product managers, designers
  and developers and maintained by the agents that work from it. It follows a component through its life,
  from requirements to design, implementation and usage. Its numbered statements (F, S, B, C, A, I) are
  atomic and tested; `[open]` marks a hunch that design must close, and `[review]` marks what a person
  checks. It keeps what was ruled out, and logs design and implementation decisions as dated one-liners
  with the reason. Its guiding principle is "one origin per fact".

  Signed Decisions takes two things directly from that article: the bar for logging a decision ("could
  someone plausibly propose the opposite?") and the principle that a fact is stated once, where it
  originates. In her system, rules that are true of every component live in the build skill and the agent
  rules. Signed Decisions is a proposal for that cross-component layer only: a signed, ranked, reviewed
  home for those rules, which a CRD can cite. Nothing here describes or reproduces her files, and she has
  not reviewed this project.

## Decision records and design rationale

- Kunz, W. and Rittel, H. (1970). *Issues as Elements of Information Systems* (IBIS). Record the argument,
  not only the result.
- Rittel, H. and Webber, M. (1973). "Dilemmas in a General Theory of Planning." *Policy Sciences*. Wicked
  problems.
- Nygard, M. (2011). "Documenting Architecture Decisions."
  https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions — short numbered records,
  superseded instead of edited.
- Zdun, U., Capilla, R., Tran, H. and Zimmermann, O. (2013). "Sustainable Architectural Design Decisions."
  *IEEE Software*. The Y-statement: "In the context of …, facing …, we decided …, to achieve …,
  accepting …".
- MADR, Markdown Architectural Decision Records. https://adr.github.io/madr/ — front matter for status,
  date and decision-makers.
- Grudin, J. (1996). In Moran, T. and Carroll, J. (eds.), *Design Rationale: Concepts, Techniques, and
  Use*. Capture fails when the writer pays and someone else benefits later.
- Buchgeher, G. et al. (2023). A study of more than 900 GitHub projects that adopted decision records;
  about half wrote fewer than five. *Title to verify.*

## Requirement levels

- Bradner, S. (1997). RFC 2119, "Key words for use in RFCs to Indicate Requirement Levels."
  https://www.rfc-editor.org/rfc/rfc2119
- Leiba, B. (2017). RFC 8174, "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words."
  https://www.rfc-editor.org/rfc/rfc8174
- GitHub Primer: rules linked to a decision record, with Check / Prefer / Authority strictness.
  *Link to verify.*

## How models use instructions

- Liu, N. et al. (2023). "Lost in the Middle: How Language Models Use Long Contexts."
  https://arxiv.org/abs/2307.03172
- Gloaguen et al. (2026). A study evaluating AGENTS.md-style context files (ETH Zurich): no general gain
  in task success, and over 20% higher cost. *Title and link to verify.*
- A 2025 study of 2,303 agent README files: context files grow line by line, like configuration.
  *Authors and title to verify.*

## Design systems and AI

- Kavcic, R. (2026). An audit of 50 design token files, and the "two reds" illustration: a brand red and a
  danger red with values and no meaning. She presents it as an illustration, not a benchmark.
  *Link to verify.*
- Deloumeau-Prigent, K. (2026). *State of AI in Design Systems*: 21 systems, 6 platforms, 165 techniques.
  *Link to verify.*
- Curtis, N. (2016). On variables ("what options exist?") and tokens ("what choice do I make?").
  *Link to verify.*
- D'Amato, D. and Baldwin, N.: writing on token architecture and colour systems. *Links to verify.*
- Fusilier, D. and Bent, S. (Spotify): conversation on design system practice.
- Named in the working documents for specific techniques: Atlassian (agent files, context cost), Astryx
  (rank by consequence, deterministic checks), Shopify Polaris (delivery telemetry), Supernova (AI context
  management), Mantine and Cloudscape (compiled context). *Links to verify.*

## Standards the format leans on

- Design Tokens Community Group. *Design Tokens Format Module 2025.10* (first stable version, 28 October
  2025). https://www.designtokens.org/ — `$description`, `$deprecated` and `$extensions`.
- Model Context Protocol specification: resources and their annotations (`audience`, `priority`,
  `lastModified`). https://modelcontextprotocol.io/specification/2025-11-25/server/resources
- W3C. *Web Content Accessibility Guidelines (WCAG) 2.2*. https://www.w3.org/TR/WCAG22/
- W3C. Accessibility Conformance Testing (ACT) rules. https://www.w3.org/WAI/standards-guidelines/act/
- Deque. axe-core, the accessibility rules engine. https://github.com/dequelabs/axe-core
- GitHub. CODEOWNERS, used here as the signing mechanism.

## Mistake-proofing and responsibility

- Shingo, S. (1986). *Zero Quality Control: Source Inspection and the Poka-yoke System*. The best rule is
  one the system makes impossible to break; promotion into tokens, CRDs and lint follows it.
- Elish, M. C. (2019). "Moral Crumple Zones: Cautionary Tales in Human-Robot Interaction."
  *Engaging Science, Technology, and Society*.
- Dekker, S. (2007). *Just Culture: Balancing Safety and Accountability*. A signature means "ask me why",
  never "blame me when".

## Thanks

- **Ismail Hamila**, for his continued support of this work and for the questions that made it sharper.
- **Thiga**, for the time and resources to develop the concept and run the experiment.
- **Cassie Groos**, whose CRD made this idea smaller and more useful.
