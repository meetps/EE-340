#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Fri Aug 28 17:23:24 2015
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import wx

class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Variables
        ##################################################
        self.variable_slider_0 = variable_slider_0 = -60000
        self.slide = slide = 0.05
        self.samp_rate = samp_rate = 40000

        ##################################################
        # Blocks
        ##################################################
        _variable_slider_0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._variable_slider_0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_variable_slider_0_sizer,
        	value=self.variable_slider_0,
        	callback=self.set_variable_slider_0,
        	label='variable_slider_0',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._variable_slider_0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_variable_slider_0_sizer,
        	value=self.variable_slider_0,
        	callback=self.set_variable_slider_0,
        	minimum=-100000,
        	maximum=100000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_variable_slider_0_sizer)
        _slide_sizer = wx.BoxSizer(wx.VERTICAL)
        self._slide_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_slide_sizer,
        	value=self.slide,
        	callback=self.set_slide,
        	label='slide',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._slide_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_slide_sizer,
        	value=self.slide,
        	callback=self.set_slide,
        	minimum=0.05,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_slide_sizer)
        self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "fftDe")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "scopeDe")
        self.Add(self.notebook_0)
        self.wxgui_fftsink2_0_1_0 = fftsink2.fft_sink_c(
        	self.notebook_0.GetPage(1).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=640000*2,
        	fft_size=1024,
        	fft_rate=15,
        	average=True,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        	win=window.hamming,
        )
        self.notebook_0.GetPage(1).Add(self.wxgui_fftsink2_0_1_0.win)
        self.wxgui_fftsink2_0_1 = fftsink2.fft_sink_f(
        	self.notebook_0.GetPage(0).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=40000,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.notebook_0.GetPage(0).Add(self.wxgui_fftsink2_0_1.win)
        self.rtlsdr_source_0_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0_0.set_sample_rate(640000*2)
        self.rtlsdr_source_0_0.set_center_freq(1140.002e6  + variable_slider_0, 0)
        self.rtlsdr_source_0_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0_0.set_gain(80, 0)
        self.rtlsdr_source_0_0.set_if_gain(30, 0)
        self.rtlsdr_source_0_0.set_bb_gain(30, 0)
        self.rtlsdr_source_0_0.set_antenna("", 0)
        self.rtlsdr_source_0_0.set_bandwidth(0, 0)
          
        self.low_pass_filter_0 = filter.fir_filter_fff(16*2, firdes.low_pass(
        	1, 640000*2, 20000, 4000, firdes.WIN_HAMMING, 6.76))
        self.iir_filter_xxx_0_0 = filter.iir_filter_ffd(([1,0]), ([1,slide]), True)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_arg_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.iir_filter_xxx_0_0, 0))
        self.connect((self.rtlsdr_source_0_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.iir_filter_xxx_0_0, 0), (self.wxgui_fftsink2_0_1, 0))
        self.connect((self.rtlsdr_source_0_0, 0), (self.wxgui_fftsink2_0_1_0, 0))
        self.connect((self.rtlsdr_source_0_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.blocks_complex_to_arg_0, 0))



    def get_variable_slider_0(self):
        return self.variable_slider_0

    def set_variable_slider_0(self, variable_slider_0):
        self.variable_slider_0 = variable_slider_0
        self._variable_slider_0_slider.set_value(self.variable_slider_0)
        self._variable_slider_0_text_box.set_value(self.variable_slider_0)
        self.rtlsdr_source_0_0.set_center_freq(1140.002e6  + self.variable_slider_0, 0)

    def get_slide(self):
        return self.slide

    def set_slide(self, slide):
        self.slide = slide
        self._slide_slider.set_value(self.slide)
        self._slide_text_box.set_value(self.slide)
        self.iir_filter_xxx_0_0.set_taps(([1,0]), ([1,self.slide]))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.Start(True)
    tb.Wait()
