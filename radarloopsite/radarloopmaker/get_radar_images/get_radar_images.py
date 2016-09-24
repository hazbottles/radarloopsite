# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 10:40:09 2016

@author: harry
"""
from datetime import datetime as dt
from ftplib import FTP
from io import BytesIO
import re
import urllib.request
from PIL import Image
import os

import yaml

from .images2gif.images2gif import writeGif

# constants
STR_TIMESTAMP = 'str_timestamp'
FTP_SITE = 'ftp.bom.gov.au'
FTP_DIRNAME = '/anon/gen/radar/'
FTP_URL = ''.join(['ftp://', FTP_SITE, FTP_DIRNAME])

LEGEND_FILENAME = 'IDR.legend.0.png'

# FTP_TRANSPARENCIES_DIRNAME = '/anon/gen/radar_transparencies/'
# FTP_TRANSPARENCIES_URL = ''.join(['ftp://', FTP_SITE, FTP_TRANSPARENCIES_DIRNAME])
TRANSPARENCIES_URL = 'http://ws.cdn.bom.gov.au/products/radar_transparencies/'

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def str_to_datetime(str_timestamp):
    """
    Converts a string timesamp in the form 'yyyymmddhhmi' (as used in the
    radar filenaming convention, and converts it to a datetime.datetime object
    """
    if len(str_timestamp) != 12:
        error_msg = (
            "string timestamp {str_timestamp} must be 12 digits long".format(
                str_timestamp=str_timestamp)
        )
        raise ValueError(error_msg)

    year = int(str_timestamp[:4])
    month = int(str_timestamp[4:6])
    day = int(str_timestamp[6:8])
    hour = int(str_timestamp[8:10])
    minute = int(str_timestamp[10:12])

    return dt(year, month, day, hour=hour, minute=minute)
assert str_to_datetime('201609172305') == dt(2016, 9, 17, 23, 5)


def get_filename_pattern(radar_id):
    """
    Returns a re.complile pattern to match the radar filenaming convention

    Args:
        radar_id (str): ID code of the radar ID

    Returns:
        A re.compile pattern of the form:
        '{radar_id}[.]T[.](?P<str_timestamp>\d\d\d\d\d\d\d\d\d\d\d\d)[.]png'.
        str_timestamp is the group name for the string timestamp in the
        radar filenmaing convention.

    Notes:
        Radar filename convention is of the form: '{radar_id}.T.201609172305.png'

    """
    # timstamp convention is: yyyymmddhhmi
    # timestamp_pattern is: '(?P<str_timestamp>\d\d\d\d\d\d\d\d\d\d\d\d)'
    timestamp_pattern = '(?P<str_timestamp>\d\d\d\d\d\d\d\d\d\d\d\d)'
    # overall pattern '{radar_id}[.]T[.](?P<str_timestamp>\d\d\d\d\d\d\d\d\d\d\d\d)[.]png'
    pattern = re.compile('[.]'.join([radar_id, 'T', timestamp_pattern, 'png']))
    return pattern
    assert get_filename_pattern('IDR021') == re.compile(
        'IDR021[.]T[.](?P<str_timestamp>\d\d\d\d\d\d\d\d\d\d\d\d)[.]png'
    )


class SourceError(Exception):
    def __init__(self, source):
        self.source = source
    def __str__(self):
        return "'{source}' is not a valid source".format(source=self.source)

class RadarImages:
    """
    Container for multiple RadarImage classes
    """
    def __init__(self, *, radar_id, source, location):
        self.radar_id = radar_id
        self.source = source
        self.location = location
        # a list of RadarImage instances
        self.radar_images = []

    def add(self, *, filename, img_time, source, location):
        self.radar_images.append(
            RadarImage(
                radar_id=self.radar_id, source=self.source, location=self.location,
                filename=filename, img_time=img_time
            )
        )
        # always keep self sorted
        self.sort_by_time()

    def __contains__(self, radar_image):
        return radar_image in self.radar_images

    def get_images(self):
        """ returns a list of the img files, sorted from most to least recent """
        self.sort_by_time()
        return [radar_img.get_image() for radar_img in self.radar_images]

    def get_times(self):
        """ returns a list of datetime.datetime """
        times = [radar_img.img_time for radar_img in self.radar_images]
        return sorted(times, reverse=True)

    def prune_to_latest(self, *, latest):
        self.sort_by_time()
        self.radar_images = self.radar_images[:latest]

    def sort_by_time(self):
        self.radar_images = sorted(self.radar_images, key=lambda x: x.get_time(), reverse=True)

    def get_transparencies(self, transparencies=None):
        if transparencies is None:
            transparencies = ["background", "topography", "range", "locations"]
        trans_imgs = []
        for transparency in transparencies:
            name = '.'.join([self.radar_id, transparency, 'png'])
            address = ''.join([TRANSPARENCIES_URL, name])
            with urllib.request.urlopen(address) as response:
                img = BytesIO(response.read())
            trans_imgs.append(img)
        return trans_imgs


class RadarImage():
    """
    Holds info about a radar image
    """
    def __init__(self, *, radar_id, source, location, filename, img_time):
        self.radar_id = radar_id
        self.source = source
        self.location = location
        self.filename = filename
        if isinstance(img_time, dt):
            self.img_time = img_time
        else:
            raise TypeError('`img_time` must be a datetime object not {}'.format(type(img_time)))

    def get_image(self):
        if self.source == 'ftp':
            address = ''.join([self.location, self.filename])
            with urllib.request.urlopen(address) as response:
                img = BytesIO(response.read())
        else:
            raise SourceError(self.source)
        return img

    def get_time(self):
        return self.img_time

def get_available_images_info(*, radar_id, source):
    """
    Returns:
        A RadarImages object with all available radar images for the specified
        radar_id, from the specified source
    """
    if source == 'ftp':
        with FTP(FTP_SITE) as ftp:
            ftp.login()
            ftp.cwd(FTP_DIRNAME)
            img_names = ftp.nlst()  # a list of img_names

    else:
        raise SourceError(source)


    # overall pattern:
    pattern = get_filename_pattern(radar_id)
    radar_images = RadarImages(radar_id=radar_id, source=source, location=FTP_URL)
    for img_name in img_names:
        match = pattern.match(img_name)
        if match is not None:
            dt_timestamp = str_to_datetime(match.group(STR_TIMESTAMP))
            radar_images.add(
            filename=match.group(), img_time=dt_timestamp, source=source, location=FTP_URL
            )
    return radar_images

def get_latest_images(*, radar_id, source, latest):
    radar_images = get_available_images_info(radar_id=radar_id, source=source)
    radar_images.prune_to_latest(latest=latest)
    return radar_images.get_images(), radar_images.get_transparencies()


def make_full_images(image_files, transparency_files):
    base_address = TRANSPARENCIES_URL + LEGEND_FILENAME

    with urllib.request.urlopen(base_address) as response:
        base_file = BytesIO(response.read())

    complete_images = [
        _make_full_image(base_file, transparency_files + [image_file]) for image_file in image_files
    ]
    return complete_images

def _make_full_image(base_file, image_files):

    base_img = Image.open(base_file).convert("RGBA")

    for image_file in image_files:
        img = Image.open(image_file).convert("RGBA")
        base_img.paste(img, (0,0), img)

    return base_img

def get_radar_details():
    """
    Returns a dict of the radar details
    """
    config_filepath = os.path.join(SCRIPT_DIR, 'radar_config.yml')
    with open(config_filepath, 'r') as fd:
        radar_config = yaml.safe_load(fd)
    return radar_config


def get_latest_gif(filename, radar_id, source='ftp', latest=24):
    """
    Returns a bytes object gif loop.
    """
    # get the image files
    image_files, trans_files = get_latest_images(radar_id=radar_id, source=source, latest=latest)
    # create the .pngs
    full_images = list(reversed(make_full_images(image_files, trans_files)))

    # make the gif loop
    duration = len(full_images) * [0.2]
    duration[-1] = 3
    writeGif(filename, full_images, duration=duration)

