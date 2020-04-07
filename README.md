# Invictus Application

clone the repo locally and run setup.sh which will use docker compose (assumes docker and docker compose are available locally)
to build a rabbitmq docker for rabbit requirement and a services docker for the actual nameko services required

It will then docker exec the services docker to drop you into a shell in the docker

you can then run pytest to run the tests

or the main client is python3 client.py

it functions as follows

usage: client.py [-h] --cmd CMD --data DATA

optional arguments:
  -h, --help   show this help message and exit
  --cmd CMD    choose a service command: 'squares', 'compress' or 'decode' are
               valid values
  --data DATA  data for the command selected: for squares list of integers eg
               1,2,3, for compress list of words eg 'cat','dog','hamster', for
               decode the compressed word to decode

# Evaluation of the test

I found this to be a really well thought out test and it is well suited to testing engineering principles. 
It made me think of all the production requirements (not all of which are satisfied here). For example what is the best way to use
nameko in production? (I was thinking supervisord perhaps), how would I secure it etc. 

I would also need to secure rabbit in production (not done here) and so forth.

I also just put in some unit tests and in production I would have to extend this for more integration tests but I felt 
it needed some testing for my submission at the very least.

Challenges for me were I had never used nameko and had never even heard of it! It's actually a really nice piece of softeware! 

I have used flask and bottle for my python microservices

I spent a good day of research on nameko just reading up on it and I am glad to see it offers async (which I never used here)
as I am very pro async due to node / react work and have dablled in asyncio for python

I also had to spend some time on the container side of things and to be honest I never achieved exactly what I wanted
i.e. I wanted to do a better docker / host network implementation where pytest and my client could be local but I felt it
was prudent to rather get the solution out sooner rather than later. 

As it now runs you actually use the shell of the docker to execute the client and tests

I hope this does enough to demonstrate my ability and if this was a real world problem I would call this my mvp
and I'd iterate to make my desired improvements.

