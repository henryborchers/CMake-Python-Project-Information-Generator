import os

from setuptools import setup
from setuptools import Command

from setuptools.command.build_py import build_py as _build_py


class Package_CMake(_build_py):
    # user_options= []
    description = 'Package Python into cmake project'
    # user_options = []

    def initialize_options(self):
        super().initialize_options()
        self.build_temp = None


    def run(self):
        self.mkpath(self.build_temp)
        cmake_targets_file = os.path.join(self.build_temp, "pythonTargets.cmake")
        with open(cmake_targets_file, "w") as f:
            # TODO: Write Metadata to a CMake variables

            f.write("set(PYTHON_PROJECT_NAME {})\n".format(self.distribution.metadata.name))
            f.write("set(PYTHON_PROJECT_VERSION {})\n".format(self.distribution.metadata.get_version()))
            f.write("\n")
            for pkg in self.distribution.install_requires:
                f.write("list(APPEND PYTHON_PROJECT_INSTALL_REQUIRES {})\n".format(pkg))

            # Write Package sources to PYTHON_SRC_FILES CMake variable
            f.write("\n")
            sources = self.get_source_files()
            for s in sources:
                f.write("list(APPEND PYTHON_PROJECT_SRC_FILES {})\n".format(s))
            # for v in self.distribution.metadata:
            #     print(v)
            print("running")

    def finalize_options(self):
        super().finalize_options()
        self.set_undefined_options('build', ('build_temp', 'build_temp'))


#


setup(
    name='dummy_pkg',
    version='0.1.2',
    packages=['dummy'],
    url='http://www.github.com',
    license='',
    install_requires=["pyside2"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    author='henry',
    cmdclass={"cmake_pkg": Package_CMake},
    # cmdclass={"foo": dummy.some_module.foo},
    author_email='',
    description=''
)
