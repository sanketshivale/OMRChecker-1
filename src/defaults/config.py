from dotmap import DotMap

CONFIG_DEFAULTS = DotMap(
    {
        "dimensions": {
            "display_height": 2480,
            "display_width": 1640,
            "processing_height": 820,
            "processing_width": 666,
        },
        "threshold_params": {
            "GAMMA_LOW": 0.7,
            "MIN_GAP": 30,
            "MIN_JUMP": 25,
            "CONFIDENT_JUMP_SURPLUS_FOR_DISPARITY": 25,
            "MIN_JUMP_SURPLUS_FOR_GLOBAL_FALLBACK": 5,
            "GLOBAL_THRESHOLD_MARGIN": 10,
            "JUMP_DELTA": 30,
            "PAGE_TYPE_FOR_THRESHOLD": "white",
            "GLOBAL_PAGE_THRESHOLD_WHITE": 200,
            "GLOBAL_PAGE_THRESHOLD_BLACK": 100,
        },
        "outputs": {
            "show_image_level": 0,
            "save_image_level": 0,
            "save_detections": True,
            "save_image_metrics": False,
            "filter_out_multimarked_files": False,
        },
    },
    _dynamic=False,
)
