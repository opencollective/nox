# Copyright 2016 Jon Wayne Parrott
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def session_lint(session):
    session.install('flake8', 'flake8-import-order')
    session.run(
        'flake8',
        '--max-complexity=10',
        '--import-order-style=google',
        'main.py')


def session_py27(session):
    session.interpreter = 'python2.7'
    session.install('requirements-test.txt')
    session.install('.')
    session.run('py.test')


def session_py35(session):
    session.interpreter = 'python3.5'
    session.install('requirements-test.txt')
    session.install('.')
    session.run('py.test')