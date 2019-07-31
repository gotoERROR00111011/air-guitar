import time
import rtmidi

class midi:
    def __init__(self):
        self.melody = [
            [60, 62, 64, 65, 67, 69, 71], 
            [72, 74, 76, 77, 79, 81, 83], 
            [84, 86, 88, 89, 91, 93, 95]
        ]

        self.midiout = rtmidi.MidiOut()
        available_ports = self.midiout.get_ports()
        if available_ports:
            self.midiout.open_port(0)
        else:
            self.midiout.open_virtual_port("My virtual output")

    def to_note(self, distanceX, distanceY):
        #if distanceX < 0 or distanceX > 100 or distanceY < 0 or distanceY > 100:
        #    return -1

        if distanceX < 0:
            distanceX = 0
        elif distanceX > 300:
            distanceX = 300

        if distanceY < 0:
            distanceY = 0
        elif distanceY > 300:
            distanceY = 300

        minX = 0
        maxX = 300
        minY = 0
        maxY = 300
        min_octave = 0
        max_octave = 2.999
        min_note = 0
        max_note = 6.999

        # X축 옥타브 높낮이 영역
        OldValueX = distanceX
        OldMinX = minX
        OldMaxX = maxX
        NewMinX = min_octave
        NewMaxX = max_octave
        octave = (((OldValueX - OldMinX) * (NewMaxX - NewMinX)) / (OldMaxX - OldMinX)) + NewMinX

        # Y축 음 높낮이 영역
        OldValueY = distanceY
        OldMinY = minY
        OldMaxY = maxY
        NewMinY = min_note
        NewMaxY = max_note
        note = (((OldValueY - OldMinY) * (NewMaxY - NewMinY)) / (OldMaxY - OldMinY)) + NewMinY

        return self.melody[int(octave)][int(note)]

    def sound(self, soe, melody):
        if soe == 0:
            return

        note_on = [0x90, melody, 112]
        #note_off = [0x80, melody, 0]
        self.midiout.send_message(note_on)