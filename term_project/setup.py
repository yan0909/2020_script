from distutils.core import setup
setup(name='term_project',
version='1.0',
py_package='pkg',
py_modules=['term_project'],
package_data={'pkg': ['spam.pyd']},
)