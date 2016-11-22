from __future__ import division
from featurex.stimuli import Stim, CollectionStimMixin
from featurex.stimuli.image import ImageStim
from featurex.extractors import ExtractorResult, merge_results
from moviepy.video.io.VideoFileClip import VideoFileClip
import pandas as pd


class VideoFrameStim(ImageStim):

    ''' A single frame of video. '''

    def __init__(self, video, frame_num, duration=None, filename=None, data=None):
        self.video = video
        self.data = self.video.frames[frame_num]
        self.frame_num = frame_num
        spf = 1. / video.fps
        duration = spf if duration is None else duration
        onset = frame_num * spf
        super(VideoFrameStim, self).__init__(filename, onset, duration, data)


class VideoStim(Stim, CollectionStimMixin):

    ''' A video. '''

    def __init__(self, filename, onset=None):

        self.clip = VideoFileClip(filename)
        self.fps = self.clip.fps
        self.width = self.clip.w
        self.height = self.clip.h

        self.frames = [f for f in self.clip.iter_frames()]
        self.n_frames = len(self.frames)
        duration = self.n_frames * 1. / self.fps

        super(VideoStim, self).__init__(filename, onset, duration)

    def __iter__(self):
        """ Frame iteration. """
        for i, f in enumerate(self.frames):
            yield VideoFrameStim(self, i, data=f)



class DerivedVideoStim(VideoStim):
    """
    VideoStim containing keyframes (for API calls). Each keyframe is associated
    with a duration reflecting the length of its "scene."
    """
    def __init__(self, filename, elements, frame_index=None, history=None):
        super(DerivedVideoStim, self).__init__(filename)
        self.elements = elements
        self.frame_index = frame_index
        self.history = history
        
    def __iter__(self):
        for elem in self.elements:
            yield elem

