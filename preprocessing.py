import numpy as np
import os
import glob
import pickle
import music21 as m21
import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from music21 import converter, instrument, stream, note, chord


def notes_from_midi():
    #create a note objects off all notes, chords, and rests from midi files
    notes = []
    
    for file in glob.glob('midi_files/*.mid'):
        midi = converter.parse(file)
        
        #print(midi) -> To make sure it is creating a music stream object
        
        #notes to parse
        notes_to_parse = None
        
        try: #songs have multiple paino parts
            p_parts = instrument.partitionByInstrument(midi)
#             print(len(p_parts)) # just checking to see if the output is what I want
#             print(p_parts[1])
            notes_to_parse = p_parts[0].recurse()
        except: #when note is not a chord
            notes_to_parse = midi.flat.notes
            
        for element in notes_to_parse:
            if isinstance(element, note.Note):
                notes.append(str(element.pitch) + " " + str(element.quarterLength))
            elif isinstance(element, chord.Chord):
                notes.append('.'.join(str(n) for n in element.normalOrder) + str(element.quarterLength))
            elif isinstance(element, note.Rest):
                notes.append(str(element.name) + " " + str(element.quarterLength))
                
#run this when you are ready to save the notes make sure they are correct first.
#     with open('data/', 'wb') as filepath:
#         pickle.dump(notes, filepath)
        
    return notes

def prepare_notes(notes):
    '''
    prepare the notes to be the input and output used by the network
    
    notes = note object created after parsing the midi files using M21
    
    Output: The input and output sequences to the LSTM network
    
    '''
    notes = notes_from_midi()
    #setting the sequence length to 100
    sequence = 100 
    
    #creating all the unique notes for create the dictionary from
    pitches = sorted(set(note for note in notes))
    
    #creating the note to int dict to map pitches to integers
    note_dict = dict((note, number) for number, note in enumerate(pitches))
    
    lstm_input = []
    lstm_output = []
    
    #creating inputs and corresponding outputs
    for i in range(0, len(notes)- sequence, 1):
        inputs = notes[i : i + sequence]
        outputs = notes[i + sequence]
        lstm_input.append([note_dict[pitch] for pitch in inputs])
        lstm_output.append(note_dict[outputs])
    
    #creating all the objects to reshape network input to make compatable with lstm network
    shape_1 = lstm_input
    shape_2 = len(lstm_input)
    shape_3 = sequence 
    
    #reshaping lstm input for lstm
    lstm_input = np.reshape(shape_1, (shape_2, shape_3, 1))
    
    #normalize lstm input with  number of unique notes
    lstm_input = lstm_input / float(len(pitches))
    #one_hot_encoding lstm_ input
    lstm_output = to_categorical(lstm_output)
    
    return (lstm_input, lstm_output)
            