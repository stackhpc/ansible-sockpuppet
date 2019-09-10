#!/bin/bash

set -euo pipefail

tox -- molecule test --all
