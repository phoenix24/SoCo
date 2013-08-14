#!/usr/bin/env python

import sys

from soco import SoCo
from soco import SonosDiscovery

if __name__ == '__main__':

    speaker_spec = sys.argv[1]
    cmd = sys.argv[2].lower()
    arg = sys.argv[3] if len(sys.argv) > 3 else None

    if speaker_spec == "all":
        sonos = SonosDiscovery()
        if (cmd == 'list_ips'):
            print '\n'.join(sonos.get_speaker_ips())
        else:
            print "Valid commands (with 'all'): list_ips"
    else:
        sonos = SoCo(speaker_spec)
        if (cmd == 'partymode'):
            print sonos.partymode()

        elif (cmd == 'info'):
            all_info = sonos.get_speaker_info()
            for item in all_info:
                print "%s: %s" % (item, all_info[item])

        elif (cmd == 'play'):
            print sonos.play()

        elif (cmd == 'pause'):
            print sonos.pause()

        elif (cmd == 'stop'):
            print sonos.stop()

        elif (cmd == 'next'):
            print sonos.next()

        elif (cmd == 'song'):
            sonos.play_uri(arg)
            print sonos.play()

        elif (cmd == 'previous'):
            print sonos.previous()

        elif (cmd == 'current'):
            track = sonos.get_current_track_info()
            print 'Current track: ' + track['artist'] + ' - ' + track['title'] \
                   + '. From album ' + track['album'] \
                   + '. This is track number ' + track['playlist_position'] + ' in the playlist. It is ' + track['duration'] + ' minutes long.'

        elif (cmd == 'volume'):
            print sonos.volume(int(arg))

        elif (cmd == 'discover'):
            sonos_devices = SonosDiscovery()

            for ip in sonos_devices.get_speaker_ips():
                device = SoCo(ip)
                zone_name = device.get_speaker_info()['zone_name']
                print "IP of %s is %s" % (zone_name, ip)

        else:
            print "Valid commands (with IP): info, play, pause, stop, next, previous, current, and partymode"

