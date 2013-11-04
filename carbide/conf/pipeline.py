# Django-Pipeline
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)

PIPELINE_CSS = {
    'carbide': {
        'source_filenames': (
            'less/*.less',
        ),
        'output_filename': 'css/carbide.css',
        'extra_context': {
            'media': 'screen,projection',
        },
        'variant': 'datauri',
    },
}

PIPELINE_JS = {
    'standard': {
        'source_filenames': [
            'js/jquery-2.0.3.min.js',
            'js/bootstrap.min.js',
            'js/angular.min.js',
        ],
        'output_filename': 'js/s.js',
    },
    'all': {
        'source_filenames': [
            'js/**/*.js',
        ],
        'output_filename': 'js/all.js',
    }
}

#PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.uglifyjs.UglifyJSCompressor'
#PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.cssmin.CSSMinCompressor'

PIPELINE_UGLIFYJS_ARGUMENTS = '--screw-ie8'

PIPELINE_ENABLED = True
