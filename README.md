# mozart-composes-videogame
Generating an original video game soundtrack in the style of classical music

![Alt text](images/mario_piano.jpg?raw=true "MARIO/ PIANO")


-----------------------------------------------------------------------------------------------------------------------

## Abstract

Some people say it takes 10,000 hours to master an instrument, or become a professional. With that said, how long does it take a machine to acquire the same amount of knoowledge it takes a human 10,000 hours to learn ? Perhaps, a machine can learn all of that in a day. But, where a machine falls short is taking that knowlege and recreating something truly unique. As machines continue to improve (specifically in the area of NLP) we are inching closer and closer to the day when a machine can create original art, and in the case of this project, music. This project is exploring some of the possibilities and shortcomings in creating original music through AI.


-----------------------------------------------------------------------------------------------------------------------

## Background and Motivation

With a background in Economics and a passion for music this project is especially important to me as it blends my passion for Data, problem solving, and music. I believe that there are going to be huge opportunities in Music and AI within the next 3-5 years. What if the next multi-platinum selling musician/producer is actually an AI engineer with very little knowledge of music theory in general ? Whatever your thoughts on this topic we can't ignore the fact that this is a very real possibility and dare I say inevitable.

-----------------------------------------------------------------------------------------------------------------------
## The Data

The data I used to train my network consists of 50 different popular video game soundtracks. For example, some of the video games include Donkey Kong, Mega Man, Final Fantasy, and Mario. I combined those 50 video games music files with 20 different compositions featuring the three famous composers Bach, Mozart, and Mendelssohn. My ultimate goal was to blend fun video game music with the complexity of a classical composer and produce an original piece of music that captures both worlds. 



-----------------------------------------------------------------------------------------------------------------------

## Network Architecture


I chose an LSTM (Long Short Term Memory) architecture rather than a RNN to deal with the problem of vanishing gradients wrapped in a bi-directional layer. I utilized a bi-directional layer because when trying to predict a new note it's important to understand the context of how that notes relates to previous notes and the notes that follow. In some cases I implemented a Time Distributed layer as there is a time series element inherent in music. After comparing five different architectures to eachother I found that a deep network consisting of two Time Distributed layers and three bi-directional LSTMS turned out to have performed the best in terms of minimizing error. This is surpirsing because it learned better when comparing to an architecture that was more complex that consisted of two additional self-attention layers. This is surpising because from every paper I read the best sequence to sequence networks have some sort of attention layer. Perhaps, I chose the wrong type of attention for this problem. It is worth it to continue exploration of different architecures and types of attention, but would require a lot more time because as it is it takes an entire day each time I train the network.

*Below is a comparison of how the different architectures were able to learn over time*

![Alt text](images/model_learning.jpg?raw=true "Networks Learning")



-----------------------------------------------------------------------------------------------------------------------

## Results

All of the models seems to have similar shortcomings and successes. For the most part the network is able to produce music, and make sense of basic music structure. And, there are different moments of brilliance scattereed throughout each generated piece of music where the model actually created a melodic sequence and some type of theme. However, all the models where unable to sustain said melody or general theme for longer periods of time. It seems as though the network gets confused about where to go after each sequence and loses it's ability to maintain momentum and structure. These results are promising and gives hope to the possibilities, but also highlights the fact that creating art through AI is a very difficult task.  

-----------------------------------------------------------------------------------------------------------------------

## Next Steps

- Get more Data: Perhaps, more data would enable the network to generalize better. Perhaps, limit the data to a specific genre as well so that it doesn't get confused about how it interpets predictions.

-Transpose the songs: Perhaps, transposing each song to every key would enable the network to understand the note to note relationship better. However, this will explode the amount of data we have and increase compute time and the cost to train the model. 

-How about a Transformer ? I have heard some great unique pieces of music created by Transformers. Perhaps, this type of architecture is better suited for this problem. Plus, it will significantly decrease our need for compute resources because Transformers are able to process the Data in parallel rather than linearly. 



