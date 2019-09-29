import os
import codecs
import wave
import math

CATALOGUE_NAME = 'catalogue.csv'
FIELD_SEPARATOR = '\t'


def list_wav(folder_name):
    output_filename = folder_name + os.path.sep + CATALOGUE_NAME
    with codecs.open(output_filename, 'w', 'utf-8') as fout:
        for folder_village in os.listdir(folder_name):
            folder_village_path = os.path.join(folder_name, folder_village)
            if os.path.isdir(folder_village_path):
                list_wav_for_village(folder_village_path, folder_village, fout)
            else:
                print(folder_village_path)
    print('written to %s' % output_filename)


def list_wav_for_village(folder_village_path, village_name, fout):
    for folder_date in os.listdir(folder_village_path):
        list_wav_for_date(os.path.join(folder_village_path, folder_date), village_name, folder_date, fout)


def list_wav_for_date(folder_date_path, village_name, folder_date, fout):
    for folder_device in os.listdir(folder_date_path):
        list_wav_for_device(os.path.join(folder_date_path, folder_device),
                            village_name, folder_date, folder_device, fout)


def is_wav(filename):
    return filename.lower().endswith('.wav')


def list_wav_for_device(folder_device_path, village_name, folder_date, folder_device, fout):
    if not os.path.isdir(folder_device_path):
        return
    for filename in os.listdir(folder_device_path):
        if is_wav(filename):
            full_filename = os.path.join(folder_device_path, filename)
            fout.write(create_line(village_name, folder_date, folder_device, filename, full_filename) + '\r\n')


def create_line(village_name, folder_date, folder_device, filename, full_filename):
    return village_name +\
           FIELD_SEPARATOR +\
           format_date(folder_date) +\
           FIELD_SEPARATOR +\
           format_name(folder_device, filename) +\
           FIELD_SEPARATOR +\
           get_duration(full_filename)


def format_date(folder_date):
    return folder_date[6:8] + '.' + folder_date[4:6] + '.' + folder_date[0:4]


def format_name(folder_device, filename):
    return folder_device + '\\' + filename


def process_duration(duration):
    hours = math.floor(duration / 3600)
    duration -= 3600 * hours
    minutes = math.floor(duration / 60)
    duration -= 60 * minutes
    return hours, minutes, duration


def get_duration(full_filename):
    try:
        f = wave.open(full_filename, 'r')
        n_frames = f.getnframes()
        frame_rate = f.getframerate()
        duration = n_frames / frame_rate
        hours, minutes, seconds = process_duration(duration)
        hours_str = pad_zero(str(hours))
        minutes_str = pad_zero(str(minutes))
        seconds_str = pad_zero(str(round(seconds)))
        return hours_str + ':' + minutes_str + ':' + seconds_str
    except Exception as e:
        print(full_filename, e)
        return "??"


def pad_zero(str_to_pad):
    if len(str_to_pad) == 1:
        str_to_pad = '0' + str_to_pad
    return str_to_pad


list_wav("c:/Users/user/Expeds/Exped2019_Khabarovsk/Sound")
