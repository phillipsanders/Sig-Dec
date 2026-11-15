# checks/

One check per decision. A check says what to read and what counts as a pass, in words a person can verify
and an agent can run. A decision names its check in `verify:`.

A check reads the design file or the code. It never changes them. A failure goes to the decision's signers.

`verify: axe:<rule>` and `verify: lint:<rule>` point to a rule in an existing tool and need no file here.
