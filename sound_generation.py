import numpy, math, pygame
from pygame import mixer, sndarray, K_ESCAPE, QUIT, KEYDOWN, K_SPACE


_freq = 22050  # Hz
_bits = 16  # 16 _bits means you want to use numpy.int16 when building sounds
_buf_size = 2 ** 10  # set to zero if audio is delayed, but risk buffering


def init():
    # 16-bit signed, stereo
    mixer.pre_init(frequency=_freq, size=-_bits, channels=2, buffer=_buf_size)
    # channels=2 means stereo, it's not related to mixer.Channel(i)
    mixer.init()  # must be before pygame.init https://stackoverflow.com/a/34324343
    pygame.init()
    

def hz_from_key(pitch_key):
    # translate MIDI key to Hz frequency
    # https://en.wikipedia.org/wiki/Pitch_(music)#Labeling_pitches
    return 2 ** ((pitch_key - 69) / 12) * 440
     
def build_sound(pitch_key, duration):
    # pitch_key is MIDI pitch, an integer 0-127, eg A4 (440Hz) is 69
    # duration is in seconds, int or float
    pitch_hz = hz_from_key(pitch_key)
    amplitude = 2 ** (_bits - 1) - 1  # 16 _bits, signed
    omega = 2 * math.pi * pitch_hz
    n_samples = int(round(duration * _freq))
    samples = [amplitude * math.sin(omega * j / _freq) for j in range(n_samples)]
    arr = numpy.array(list(zip(samples, samples)))  # stereo needs width of 2
    sound = sndarray.make_sound(numpy.int16(arr))
    return sound

def main():
    init()
    screen = pygame.display.set_mode((500, 500))
    sound = build_sound(69, 1)  # 69 is A4
    channel = mixer.Channel(0) # don't use mixer.find_channel()
    clock = pygame.time.Clock()
    while 1:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            if event.type == KEYDOWN and event.key == K_SPACE:
                if channel and channel.get_busy():  # sound not over
                    # sound.get_num_channels() lists active chans, not busy ones
                    channel.stop()
                else:
                    channel.play(sound)  # background thread plays this
            
        # display color to match channel state
        if channel and channel.get_busy(): 
            screen.fill((255, 0, 0))
        else:
            screen.fill((0, 0, 255))
        pygame.display.flip()
    
        
if __name__ == '__main__':
#     init()
#     assert math.fabs(hz_from_key(69) - 440) < 0.01
#     assert math.fabs(hz_from_key(49) - 138.59) < 0.01
#     assert math.fabs(build_sound(111, 3.00).get_length() - 3.00) < 0.01
    main()

# Resources:
# https://github.com/cosmologicon/pyjam/wiki/pygame-notes-and-tricks#pygamemixer
# https://github.com/atizo/pygame/blob/master/examples/sound_array_demos.py
# generating 8-bit sounds (JS) https://github.com/ttencate/jfxr 

# Avoiding memory leaks:
# don't do `channel = Sound.play()` because it always returns a different one.
# don't do `channel = mixer.find_channel()` either: it makes a new channel too!

# To know if sound is done playing, use `channel.get_busy()`.
# Do not use `sound.get_num_channels()`: it returns active channels, not busy ones.
