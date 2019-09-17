#!/bin/bash

set -euo pipefail

tox -- molecule --debug test --all
