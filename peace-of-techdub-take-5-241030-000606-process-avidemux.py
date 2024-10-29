#PY  <- Needed to identify #
#--automatically built--

adm = Avidemux()
if not adm.loadVideo("C:/Work/design.experiments/peace.of.techdub#2/assets/export/peace-of-techdub-take-5-241030-000606.mkv"):
    raise("Cannot load C:/Work/design.experiments/peace.of.techdub#2/assets/export/peace-of-techdub-take-5-241030-000606.mkv")
adm.clearSegments()
adm.addSegment(0, 34000, 46504000)
adm.markerA = 388000
adm.markerB = 46504000
adm.setHDRConfig(1, 1, 1, 1, 0)
adm.videoCodec("x264", "useAdvancedConfiguration=False", "general.params=AQ=20", "general.threads=99", "general.preset=medium", "general.tuning=", "general.profile=high", "general.fast_decode=False", "general.zero_latency=False"
, "general.fast_first_pass=True", "general.blueray_compatibility=False", "general.fake_interlaced=False", "level=-1", "vui.sar_height=1", "vui.sar_width=1", "vui.overscan=0", "vui.vidformat=5", "vui.fullrange=False"
, "vui.colorprim=2", "vui.transfer=2", "vui.colmatrix=2", "vui.chroma_loc=0", "MaxRefFrames=3", "MinIdr=25", "MaxIdr=250", "i_scenecut_threshold=40", "intra_refresh=False", "MaxBFrame=3", "i_bframe_adaptive=1"
, "i_bframe_bias=0", "i_bframe_pyramid=2", "b_deblocking_filter=True", "i_deblocking_filter_alphac0=0", "i_deblocking_filter_beta=0", "cabac=True", "interlaced=False", "constrained_intra=False", "tff=True"
, "fake_interlaced=False", "analyze.b_8x8=True", "analyze.b_i4x4=True", "analyze.b_i8x8=True", "analyze.b_p8x8=True", "analyze.b_p16x16=False", "analyze.b_b16x16=False", "analyze.weighted_pred=2", "analyze.weighted_bipred=True"
, "analyze.direct_mv_pred=1", "analyze.chroma_offset=0", "analyze.me_method=1", "analyze.me_range=16", "analyze.mv_range=-1", "analyze.mv_range_thread=-1", "analyze.subpel_refine=7", "analyze.chroma_me=True"
, "analyze.mixed_references=True", "analyze.trellis=1", "analyze.psy_rd=1.000000", "analyze.psy_trellis=0.000000", "analyze.fast_pskip=True", "analyze.dct_decimate=True", "analyze.noise_reduction=0", "analyze.psy=True"
, "analyze.intra_luma=11", "analyze.inter_luma=21", "ratecontrol.rc_method=0", "ratecontrol.qp_constant=0", "ratecontrol.qp_min=10", "ratecontrol.qp_max=51", "ratecontrol.qp_step=4", "ratecontrol.bitrate=0"
, "ratecontrol.rate_tolerance=1.000000", "ratecontrol.vbv_max_bitrate=0", "ratecontrol.vbv_buffer_size=0", "ratecontrol.vbv_buffer_init=1", "ratecontrol.ip_factor=1.400000", "ratecontrol.pb_factor=1.300000"
, "ratecontrol.aq_mode=1", "ratecontrol.aq_strength=1.000000", "ratecontrol.mb_tree=True", "ratecontrol.lookahead=40")
adm.addVideoFilter("contrast", "coef=1.180000", "offset=-6", "doLuma=True", "doChromaU=True", "doChromaV=True")
adm.addVideoFilter("colorBalance", "loLuma=-0.260000", "mdLuma=0.320000", "hiLuma=0.330000", "loAngle=42.000000", "mdAngle=252.000000", "hiAngle=139.000000", "loShift=0.000000", "mdShift=0.000000", "hiShift=0.000000", "loSaturation=-0.030000"
, "mdSaturation=-0.270000", "hiSaturation=-0.220000")
adm.addVideoFilter("zoom", "top=66", "bottom=26", "left=0", "right=0", "ar_select=0", "algo=1", "pad=0", "tolerance=0.010000")
adm.addVideoFilter("fitToSize", "width=1272", "height=1272", "algo=1", "roundup=0", "pad=0", "tolerance=0.000000")
adm.addVideoFilter("crop", "top=36", "bottom=38", "left=40", "right=34", "ar_select=7")
adm.audioClearTracks()
adm.setSourceTrackLanguage(0,"und")
adm.audioAddExternal("C:/Work/design.experiments/peace.of.techdub#2/assets/KANZ - Luminal Spaces (Original Mix) (1).wav")
adm.setSourceTrackLanguage(1,"und")
if adm.audioTotalTracksCount() <= 1:
    raise("Cannot add audio track 1, total tracks: " + str(adm.audioTotalTracksCount()))
adm.audioAddTrack(1)
adm.audioCodec(0, "LavAAC", "bitrate=128")
adm.audioSetDrc2(0, 1, 1, 0.001, 0.2, 1, 2, -12)
adm.audioSetEq(0, 0, 0, 0, 0, 880, 5000)
adm.audioSetChannelGains(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
adm.audioSetChannelDelays(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
adm.audioSetChannelRemap(0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8)
adm.audioSetShift(0, 0, 0)
adm.audioSetNormalize2(0, 1, 10, -10)
adm.setContainer("MP4", "muxerType=0", "optimize=1", "forceAspectRatio=False", "aspectRatio=1", "displayWidth=1280", "rotation=0", "clockfreq=0")
