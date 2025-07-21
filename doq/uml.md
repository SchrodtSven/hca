```mermaid
zenuml
    title Annotators
    @Actor Alice
    @Actor Bob
    @Entity Cypherpunk
    @Database David
    Alice->Bob: Hi Bob
    Bob->Alice: Hi Alice
    Bob->David: Show Tables
    David->Claude: sanitize data
    Claude->David: it is here
```
 