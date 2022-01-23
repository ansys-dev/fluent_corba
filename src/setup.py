"""
Installation file for fluent corba
"""
import setuptools
from distutils.core import setup

setup(
    name='fluent_corba',
    packages=['fluent_corba'],
    version='0.2.0',
    description='Fluent Corba interface --> Wechat: @ansys_development',

    # Author details
    author='guangsheng.tian',
    author_email='tguangs@163.com',

    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows 10',
    ],
    python_requires='~=3.8',
    url='https://www.fangzhenxiuxiu.com/pro/1374',
    keywords='ANSYS Fluent CORBA omniorb omniORBpy',
    include_package_data=True,
    platforms="win-amd64",
)
