# Amedeo Sarpa Intern RETROSPECTIVE Sprint 9

## PROCESS MEASURES

### Macro statistics

- Number of stories committed vs done : 8/8
- Total points committed vs done : 27/27

### Definition of Done

- Unit Tests passing with a coverage of at least 90 %
- Code review completed
- Working code present on GitLab main branch
- Work deployed on cloud
- PO approvals
- Satisfy acceptance criteria
- All steps of the pipeline pass

### Detailed statistics

| Story                              | # Tasks | Points |
| ---------------------------------- | ------- | ------ |
| Create a consultant                | 9       | 8      |
| List of consultants                | 3       | 3      |
| Modify consultant information      | 3       | 2      |
| Consultant page for BM             | 2       | 2      |
| Consultant page for Consultant     | 1       | 2      |
| Delete a consultant                | 5       | 3      |
| See consultant's statistics widget | 2       | 2      |
| New design adaptation              | 7       | 5      |

## QUALITY MEASURES

- Unit Testing:

  - Nr of automated unit test cases : 67 Front End + 686 Back End
  - Coverage : 97.36%

- E2E testing:
  - Not yet done
- Code review
  - 8h

## ASSESSMENT

- What caused your errors in estimation (if any)?

  - `Create consultant` user sotries was underestimated, required a lot of effort in the backend, for the grpc connection, and even because the draft filed, added in the user object, created a lot of confusions.

- What lessons did you learn (both positive and negative) in this sprint?

  - Is important to be reactive to some absence of a team member, and take this in consideration during the palnning if known in advance

- Which improvement goals set in the previous retrospective were you able to achieve? <br>
  - We knew that one member was not working with us during the first sprint and we took it into account during the plannig
  - Seperate the work on git, creating not one big branch but severals (like one for the service and another for the controller)
  - we did not create to many user sotries for a single feedback received
- Which ones you were not able to achieve? Why?<br>
  - none
- Improvement goals for the next sprint <br>

  - Test manually what cannot be tested automatically as soon as possible, like the grpc connection

- One thing you are proud of as a Team!!<br>
  We very like the harmony with which we work and the way we communicate as we come from different countries.
