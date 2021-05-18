# mozart-composes-videogame
Generating an original video game soundtrack in the style of classical music

![Alt text](images/mario_piano.jpg?raw=true "MARIO/ PIANO")


-----------------------------------------------------------------------------------------------------------------------

## Abstract

Some people say it takes 10,000 hours to master an instrument, or become a professional. With that said, how long does it take a machine to acquire the same amount of knoowledge it takes a human 10,000 hours to learn ? Perhaps, a machine can learn all of that in a day. But, where a machine falls short is taking that knowlege and recreating something truly unique. As machines continue to improve (specifically in the area of NLP) we are getting inchining closer and closer to the day when a machine can create original art, and in the case of this project, music. This project is exploring some of the possibilities and shortcomings in creatig original music through AI.


-----------------------------------------------------------------------------------------------------------------------

## Background and Motivation

With a background in Economics and a passion for music this project is especially important to me as it blends my passion for Data, problem solving and music. I believe that there are going to be huge opportunities in Music and AI within the next 3-5 years. What if the next multi-platinum selling musician/producer is actually an AI engineer with very little knowledge of music theory in general ? Whatever your thoughts on this topic we can't ignore the fact that this is a very real possibility.

-----------------------------------------------------------------------------------------------------------------------
## The Data

The data I used to train my network are 50 different popular video game soundtracks. For example, some of the video games include Donkey Kong, Mega Man, Final Fantasy, and Mario. I combined those 50 video games music files with 20 different compositions of three famous composers featuring Bach, Mozart, and Mendelssohn. My ultimate goal was to blend fun video game music with the complexity of a classical composer and produce an original piece of music that captures both worlds. 



-----------------------------------------------------------------------------------------------------------------------

## Network Architecture

Once we convert the midi data to a time series this becomes an NLP sequence to sequence problem.
I chose an LSTM (Long Short Term Memory) architecture rather than a RNN to deal with the problem of vanishing gradients wrapped in a bi-directional layer. I utilized a bi-directional layer because when trying to predict a new note it's important to understand the context of how that notes relates to it's previous notes and the notes that follow. In some cases I implemented a Time Distributed layer. After comparing five different architectures to eachother I found that a deep network consisting of two Time Distributed layers and three bi-directional LSTMS turned out to have performed the best in terms of minimizing error. This is surpirsing because it learned better when comparing to an architecture that was more complex that consists of two additional self-attention layers. This is surpising because from every paper I read the best sequence to sequence networks have some sort of attention layer. Perhaps, I chose the wrong type of attention for this type of model. It is worth it to continue exploration of different architecures and types of attention. 

*Below is a comparison of how the different architectures were able to learn over time*

![Alt text](images/model_learning.jpg?raw=true "Networks Learning")




















