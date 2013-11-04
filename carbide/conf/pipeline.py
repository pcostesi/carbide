# Django-Pipeline
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)

PIPELINE_CSS = {
    'standard': {
        'source_filenames': (
            #'css/*.css',
            'less/*.less',
        ),
        'output_filename': 'css/s.css',
        'extra_context': {
            'media': 'screen,projection',
        },
        'variant': 'datauri',
    },
}

PIPELINE_JS = {
    'standard': {
        'source_filenames': [
            # 'js/sample1.js',
            # 'js/sample2.js',
        ],
        'output_filename': 'js/s.js',
    }
}

PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.cssmin.CSSMinCompressor'

PIPELINE_UGLIFYJS_ARGUMENTS = '--screw-ie8 -c --comments'
