# -*- coding: utf-8 -*-
import sys
import os
from distutils.core import setup
from setuptools import find_packages

#########
# settings
#########

project_var_name = "botadi"
sversion = "0.1"
versionPython = "%s.%s" % (sys.version_info.major, sys.version_info.minor)
path = "Lib/site-packages/" + project_var_name
readme = 'README.rst'
history = "HISTORY.rst"
requirements = None

KEYWORDS = project_var_name + ', first name, last name'
DESCRIPTION = """Material for presentations. The documentation generation is using pyquickhelper."""


CLASSIFIERS = [
    'Programming Language :: Python :: 3',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering',
    'Topic :: Education',
    'License :: OSI Approved :: MIT License',
    'Development Status :: 5 - Production/Stable'
]

#######
# data
#######

packages = find_packages('src', exclude='src')
package_dir = {k: "src/" + k.replace(".", "/") for k in packages}
package_data = {project_var_name + ".mokadi.grammars": ["*.g4", "*.tokens"],
                project_var_name + ".mokadi.data": ["*.wav", "*.ico"]}


############
# functions
############


def is_local():
    if "moviepy-setup" in sys.argv:
        return True
    file = os.path.abspath(__file__).replace("\\", "/").lower()
    if "/temp/" in file and "pip-" in file:
        return False
    from pyquickhelper.pycode.setup_helper import available_commands_list
    return available_commands_list(sys.argv)


def ask_help():
    return "--help" in sys.argv or "--help-commands" in sys.argv


def verbose():
    print("---------------------------------")
    print("package_dir =", package_dir)
    print("packages    =", packages)
    print("package_data=", package_data)
    print("current     =", os.path.abspath(os.getcwd()))
    print("---------------------------------")

##########
# version
##########


if is_local() and not ask_help():
    def write_version():
        from pyquickhelper.pycode import write_version_for_setup
        return write_version_for_setup(__file__)

    write_version()

    versiontxt = os.path.join(os.path.dirname(__file__), "version.txt")
    if os.path.exists(versiontxt):
        with open(versiontxt, "r") as f:
            lines = f.readlines()
        subversion = "." + lines[0].strip("\r\n ")
        if subversion == ".0":
            raise Exception("Git version is wrong: '{0}'.".format(subversion))
    else:
        raise FileNotFoundError(versiontxt)
else:
    # when the module is installed, no commit number is displayed
    subversion = ""

if "upload" in sys.argv and not subversion and not ask_help():
    # avoid uploading with a wrong subversion number
    raise Exception(
        "Git version is empty, cannot upload, is_local()={0}".format(is_local()))

##############
# common part
##############

if os.path.exists(readme):
    with open(readme, "r", encoding='utf-8-sig') as f:
        long_description = f.read()
else:
    long_description = ""
if os.path.exists(history):
    with open(history, "r", encoding='utf-8-sig') as f:
        long_description += f.read()

if "--verbose" in sys.argv:
    verbose()

if is_local():
    import pyquickhelper
    from pyquickhelper.pycode import process_standard_options_for_setup
    logging_function = pyquickhelper.get_fLOG()
    logging_function(OutputPrint=True)
    if "unittests" in sys.argv and sys.platform.startswith("win"):
        # There is some issues on Windows.
        from PIL import Image as PIL_Image
        assert PIL_Image is not None
    r = process_standard_options_for_setup(
        sys.argv, __file__, project_var_name, layout=["html"],
        unittest_modules=["pyquickhelper", "jyquickhelper"],
        additional_notebook_path=["pyquickhelper",
                                  "jyquickhelper", "pymmails", "csharpy"],
        additional_local_path=["pyquickhelper",
                               "jyquickhelper", "pymmails", "csharpy"],
        requirements=["pyquickhelper", "jyquickhelper", "pymmails", "csharpy"],
        add_htmlhelp=sys.platform.startswith("win"),
        coverage_options=dict(omit=["*exclude*.py"]),
        fLOG=logging_function, covtoken=(
            "216b00d8-6a02-4643-9ecc-c74ce42be58c", "'_UT_37_std' in outfile"),
        nbformats=('ipynb', 'html', 'python', 'rst',
                   'slides', 'present', 'github'),
        github_owner='sdpython')
    if not r and "update_grammars" in sys.argv:
        # expecting python setup.py update_grammars file
        ind = sys.argv.index("update_grammars")
        if len(sys.argv) <= ind:
            raise Exception(
                "Expecting a grammar file: python setup.py update_grammars MokadiGrammar.g4")
        grammar = sys.argv[ind + 1]
        if not os.path.exists(grammar):
            cdir = os.path.abspath(os.path.dirname(__file__))
            g2 = os.path.join(cdir, "src", "botadi",
                              "mokadi", "grammars", grammar)
            if not os.path.exists(g2):
                raise FileNotFoundError("{0}\n{1}".format(grammar, g2))
            grammar = g2
        try:
            from pyensae.languages import build_grammar
        except ImportError:
            sys.path.append(os.path.join(
                os.path.dirname(__file__), "..", "pyensae", "src"))
            from pyensae.languages import build_grammar
        build_grammar(grammar, fLOG=logging_function)
        r = True
    if not r and not ({"bdist_msi", "sdist",
                       "bdist_wheel", "publish", "publish_doc", "register",
                       "upload_docs", "bdist_wininst", "build_ext"} & set(sys.argv)):
        raise Exception("unable to interpret command line: " + str(sys.argv))
else:
    r = False

if ask_help():
    from pyquickhelper.pycode import process_standard_options_for_setup_help
    process_standard_options_for_setup_help(sys.argv)

if not r:
    if len(sys.argv) in (1, 2) and sys.argv[-1] in ("--help-commands",):
        from pyquickhelper.pycode import process_standard_options_for_setup_help
        process_standard_options_for_setup_help(sys.argv)
    from pyquickhelper.pycode import clean_readme
    long_description = clean_readme(long_description)
    setup(
        name=project_var_name,
        version='%s%s' % (sversion, subversion),
        author='Xavier Dupré',
        author_email='xavier.dupre@gmail.com',
        license="MIT",
        url="http://www.xavierdupre.fr/app/botadi/helpsphinx/index.html",
        download_url="https://github.com/sdpython/botadi",
        description=DESCRIPTION,
        long_description=long_description,
        keywords=KEYWORDS,
        classifiers=CLASSIFIERS,
        packages=packages,
        package_dir=package_dir,
        package_data=package_data,
        setup_requires=["pyquickhelper"],
        install_requires=['pyquickhelper', 'jyquickhelper', 'pymmails'],
    )
