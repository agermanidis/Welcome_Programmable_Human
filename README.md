<p align="center">
<br/>
<img src="http://i.imgur.com/1ACYBJH.gif" width="750px"></img>
<img src="http://i.imgur.com/uw860ie.jpg" width="750px"></img>
<br/>
<sub>Photo & video credit: Emi Spicer</sub></p>

This repository contains the source code for **Welcome, Programmable Human**, a performance piece I did at the [School for Poetic Computation](http://sfpc.io/) Spring 2015 final show (SFPC is an artist-run school in New York City that is like the 21st century version of the [Black Mountain College](http://www.blackmountaincollege.org/history) - consider [applying for the Fall 2015 term](https://docs.google.com/forms/d/1jWCoZSoTKwJeMA8yA1m_guUBi1OpsX01EU7OLztDRyU/viewform)).

## Description

**Welcome, Programmable Human** was an experimental performance in which all my actions, which included giving art critiques of student works, having conversations about today's news stories with visitors, and visualizing the stock market with my body, were generated by a computer program.

The Python modules included in this repository (starting from [`performance.py`](https://github.com/agermanidis/welcome_programmable_human/blob/master/performance.py)) were sending instructions telling me what to say and do to my phone, and then, through text-to-speech, to my earphones. The instructions generated were a function of a variety of online data sources scraped in real time; for instance, recent tweets containing the keyword "TFW" dictated what feelings I would express to the visitors.

For the duration of the performance, the source code of the program was projected on the wall, with line currently being evaluated highlighted, so as to enable complete [algorithmic transparency](http://www.techrepublic.com/article/data-driven-policy-and-commerce-requires-algorithmic-transparency/) of my behavior.

## Further Work

HAC (Human Action Code), the framework for generating human behavior that I started working on while I was at the school and that I'm using in this piece, is still heavily under development. Expect an alpha open source release sometime in July.

I'm planning to do more research and performances exploring the algorithmic construction of all kinds of human behavior this summer in New York City. If you're interested in a future of auto-generated social interactions, programmable theatre, computable social movements, and Turing-complete romance, [keep in touch](http://twitter.com/agermanidis).
