# Proposta di Amedeo Sarpa

Metriche proposte per determinare *stime inaccurate* :


- coefficiente di correlazione dei ranghi di Spearman tra l'effort attuale e quello stimato.
- Alla fine dello sprint raccogliere feedback dal team, e far stimare nuovamente la storia post implementazione, vedendo
la differenza della nuova stima con quella iniziale.
- siccome si utilizza il range [1,13] della scala Fibonacci, determinare  per ciascuna categoria la media dell'effort delle user story già implementate. Una user story, che appartiene ad una certa categoria, è non stimata correttamente se l'effort finale è una standard deviation più alta/bassa rispetto alla media della rispettiva categoria.


Metriche per determinare le *cause* più comuni di stime inaccurate:
- Contare le occorrenze delle ragioni per cui la storia è stata sotto o sopra stimata. Considerare le più riccorenti
e proporre delle soluzioni a priori (da adattare sin dallo sprint planning) per ciascuna di queste categorie.
Si potrebbe anche classificare, in base a degli indicatori, le altre storie del backlog in modo da tenerne conto durante la fase di estimation.

Questi indicatori potrei prenderli usando come metrica il coefficiente di correlazione di Pearson, tra i feedback forniti dagli sviluppatori e i seguenti fattori :
- User story fa parte di un nuovo set di funzionalità da implementare(ex. ad esempio richiede il setup di un nuovo microservizio).
- La user story richiede l'uso di nuove tecnologie fin'ora non utilizzate (ex. utilizzare un nuovo protocollo di comunicazione).
- User story è una Spike Story.
