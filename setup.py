import subprocess

from setuptools import setup, find_packages

version = "master"

filename = "master"

setup(name="pepper_behavior_sandbox",

      version=filename,

      description="",

      long_description="",

      author="Florian Lier and Nils Neumann",

      author_email="flier[at]techfak.uni-bielefeld.de and nneumann[at]techfak.uni-bielefeld.de",

      url="",

      download_url="",

      packages=find_packages(exclude=["*.tests",

                                      "*.tests.*",

                                      "tests.*",

                                      "tests"]),

      scripts=["tasks/itelligence_demo_2017.py","smach/pepper_smach_geniale_2017.py"],

      #package_data={'fsmtest': ['configuration/*']},

      #include_package_data=True,

      keywords=['Behavior'],

      license="LGPLv3",

      classifiers=['Development Status :: Beta',

                   'Environment :: Console',

                   'Environment :: Robotics',

                   'Intended Audience :: Developers',

                   'License :: OSI Approved :: GNU Library or ' +

                   'Lesser General Public License (LGPL)',

                   'Operating System :: OS Independent',

                   'Programming Language :: Python',

                   'Topic :: Text Processing :: Markup :: XML'],

      #install_requires=[],


      #tests_require=['logilab-common==0.63.0', 'pylint==1.4.4', 'setuptools-lint'],

      # Workaround for: http://bugs.python.org/issue856103

      zip_safe=False

      )

# Make scripts executable

subprocess.call(["chmod -R ugo+x tasks"], shell=True)