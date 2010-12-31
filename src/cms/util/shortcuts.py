import os

project_dirname = os.path.expanduser('~')
asset_dirname = 'assets'

def project_path(dirname):
    """ Gets a path relative to the project's root directory. """

    return '{0}{1}{2}'.format(
        project_dirname, os.sep, dirname
    )

def asset_path(dirname):
    """ Gets a path under the project's assets directory. """

    return project_path('{0}{1}{2}'.format(
        asset_dirname, os.sep, dirname
    ))

