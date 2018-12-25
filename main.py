from pydub import AudioSegment

"""
There are two input files:
    tic.mp3
    tic(high_pitch).mp3

There are two output files:
    output(17).mp3
    output(51).mp3
# Note that the number in the parentheses indicates the measure to start 
  singing, so there will be two empty measures in the beginning to have 
  the singers prepared.
"""

tick = AudioSegment.from_mp3('tic.mp3')
high_pitch = AudioSegment.from_mp3('tic(high_pitch).mp3')

one_tick_duration = 1000 * 60 / 150
half_tick_duration = one_tick_duration / 2

error = 40

first_tick = high_pitch[error:error+one_tick_duration]
one_tick = tick[:one_tick_duration]
half_tick = tick[:half_tick_duration]

seven_over_eight = first_tick + one_tick * 2 + half_tick
four_four = first_tick + one_tick * 3

output = seven_over_eight * 2\
       + seven_over_eight * 18\
       + four_four * 8\
       + seven_over_eight * 8\
       + seven_over_eight * 18\
       + four_four * 8\
       + seven_over_eight * (112 - 76)
# starts from 49
output2 = seven_over_eight * 2\
       + seven_over_eight * 18\
       + four_four * 8\
       + seven_over_eight * (112 - 76)

output.export('output(17).mp3', format='mp3')
output2.export('output(51).mp3', format='mp3')
